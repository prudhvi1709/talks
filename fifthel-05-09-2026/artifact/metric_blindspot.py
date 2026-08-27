# /// script
# requires-python = ">=3.12"
# dependencies = []
# ///
"""Score an OCR page two ways: the standard metric, and the one the task needs.

Character error rate averages over every character on the page. When the task
depends on a handful of identifiers, those characters are a rounding error in
the denominator, so CER is arithmetically incapable of reporting their loss.
This prints both numbers alongside the bound that makes the blindness provable
rather than anecdotal.
"""

from __future__ import annotations

import argparse
import re
import sys
import unicodedata
from dataclasses import dataclass
from pathlib import Path

DEFAULT_PATTERN = r"Question No\.\s*(\d+)"


@dataclass(slots=True, frozen=True)
class Report:
    """Both scorings of a single page, plus the inputs needed to audit them."""

    truth_chars: int
    edits: int
    expected: tuple[str, ...]
    recovered: tuple[str, ...]

    @property
    def cer(self) -> float:
        return self.edits / self.truth_chars if self.truth_chars else 0.0

    @property
    def reads_as(self) -> float:
        return (1.0 - self.cer) * 100.0

    @property
    def identifier_chars(self) -> int:
        return sum(len(item) for item in self.expected)

    @property
    def recall(self) -> float:
        return len(self.recovered) / len(self.expected) if self.expected else 0.0

    @property
    def blindness_bound(self) -> float:
        """Most CER can move if every identifier goes from perfect to destroyed.

        A substitution costs one edit per character, so the identifier budget is
        the ceiling on how much CER can respond to them.
        """
        return self.identifier_chars / self.truth_chars if self.truth_chars else 0.0


def edit_distance(source: str, target: str) -> int:
    """Levenshtein distance, two rows so memory stays linear in the shorter side."""
    if len(source) < len(target):
        source, target = target, source
    if not target:
        return len(source)

    previous = list(range(len(target) + 1))
    for i, source_char in enumerate(source, start=1):
        current = [i]
        for j, target_char in enumerate(target, start=1):
            current.append(
                min(
                    previous[j] + 1,
                    current[j - 1] + 1,
                    previous[j - 1] + (source_char != target_char),
                )
            )
        previous = current
    return previous[-1]


def normalise(text: str) -> str:
    """NFC-compose and collapse whitespace so layout noise is not scored as error."""
    return re.sub(r"\s+", " ", unicodedata.normalize("NFC", text)).strip()


def find_identifiers(text: str, pattern: re.Pattern[str]) -> list[str]:
    return [m.group(1) if m.groups() else m.group(0) for m in pattern.finditer(text)]


def analyse(truth: str, ocr: str, *, pattern: re.Pattern[str]) -> Report:
    clean_truth, clean_ocr = normalise(truth), normalise(ocr)
    expected = find_identifiers(clean_truth, pattern)
    # Substring rather than positional match: the most generous possible reading
    # of "did this identifier survive anywhere on the page".
    recovered = [item for item in expected if item in clean_ocr]
    return Report(
        truth_chars=len(clean_truth),
        edits=edit_distance(clean_truth, clean_ocr),
        expected=tuple(expected),
        recovered=tuple(recovered),
    )


def render(report: Report, *, truth_path: Path, ocr_path: Path) -> str:
    lost = [item for item in report.expected if item not in report.recovered]
    bound = report.blindness_bound * 100
    lines = [
        f"truth  {truth_path}",
        f"ocr    {ocr_path}",
        "",
        "the metric everyone reports",
        f"  character error rate    {report.cer:.4f}",
        f"  reads as                {report.reads_as:.1f}% accurate",
        f"  edits                   {report.edits} over {report.truth_chars} characters",
        "",
        "the metric the task needs",
        f"  identifiers expected    {len(report.expected)}",
        f"  identifiers recovered   {len(report.recovered)}",
        f"  identifier recall       {report.recall * 100:.1f}%",
    ]
    if lost:
        lines.append(f"  lost                    {', '.join(lost)}")
    lines += [
        "",
        "why the first number could not have caught it",
        f"  identifiers are {report.identifier_chars} of {report.truth_chars} characters, "
        f"{bound:.2f}% of the page",
        f"  so CER can move at most {bound:.2f} points between every identifier being",
        "  perfect and every identifier being destroyed",
        f"  identifier recall moved {(1 - report.recall) * 100:.0f} points on this same page",
    ]
    return "\n".join(lines)


def main() -> int:
    here = Path(__file__).parent
    parser = argparse.ArgumentParser(
        description="Compare character error rate against identifier recall on one page.",
    )
    parser.add_argument("--truth", type=Path, default=here / "fixtures/page_truth.txt")
    parser.add_argument("--ocr", type=Path, default=here / "fixtures/page_ocr.txt")
    parser.add_argument(
        "--pattern",
        default=DEFAULT_PATTERN,
        help="regex matching the identifiers the task depends on; group 1 used if present",
    )
    args = parser.parse_args()

    try:
        truth = args.truth.read_text(encoding="utf-8")
        ocr = args.ocr.read_text(encoding="utf-8")
    except OSError as err:
        print(f"cannot read input: {err}", file=sys.stderr)
        return 2

    try:
        pattern = re.compile(args.pattern)
    except re.error as err:
        raise SystemExit(f"bad --pattern: {err}") from err

    report = analyse(truth, ocr, pattern=pattern)
    if not report.expected:
        print(f"no identifiers matched {args.pattern!r} in the truth file", file=sys.stderr)
        return 2

    print(render(report, truth_path=args.truth, ocr_path=args.ocr))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
