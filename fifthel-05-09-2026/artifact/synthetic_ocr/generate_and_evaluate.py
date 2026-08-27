# /// script
# requires-python = ">=3.12"
# dependencies = ["Pillow>=10.0"]
# ///
"""Reproduce case one's finding end to end, with no client data.

Renders a synthetic Hindi question paper, degrades it the way a genuine scan
degrades a crisp digital render, runs the real Tesseract binary over it, and
reports the same two numbers slide 3 and slide 4 are built on: word accuracy
against question-number recovery. Nothing here is hand-crafted to fail - the
degradation model is generic (rotation, blur, noise, low contrast, JPEG
recompression), and if it doesn't reproduce the gap, that's a real result
worth knowing, not a bug to paper over.

Requires the tesseract binary with the Hindi language pack, and a Chromium-
family browser for text rendering (PIL's own text drawing does not shape
Devanagari conjuncts/matras correctly - a browser's text engine does):
  macOS:  brew install tesseract tesseract-lang
  Linux:  apt install tesseract-ocr tesseract-ocr-hin chromium
"""

from __future__ import annotations

import argparse
import io
import random
import re
import shutil
import subprocess
import unicodedata
from dataclasses import dataclass
from pathlib import Path
from tempfile import TemporaryDirectory

from PIL import Image, ImageFilter

# (question number, Hindi instruction text) - a plausible exam-paper page.
QUESTIONS: tuple[tuple[str, str], ...] = (
    ("896", "निम्नलिखित प्रश्नों के उत्तर दीजिए।"),
    ("897", "यह सही है या गलत बताइए।"),
    ("898", "इस अनुच्छेद को ध्यान से पढ़िए।"),
    ("899", "अपने उत्तर स्पष्ट रूप से लिखिए।"),
    ("900", "नीचे दिए गए शब्दों का प्रयोग कीजिए।"),
    ("901", "सही विकल्प चुनकर लिखिए।"),
)

BROWSER_CANDIDATES = (
    "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome",
    "/Applications/Chromium.app/Contents/MacOS/Chromium",
    "google-chrome",
    "chromium",
    "chromium-browser",
)

NUMBER_PATTERN = re.compile(r"\*(\d+)\.")


def find_browser() -> str:
    for candidate in BROWSER_CANDIDATES:
        if Path(candidate).exists() or shutil.which(candidate):
            return candidate
    raise SystemExit(
        "no Chromium-family browser found - install Google Chrome or "
        "Chromium, or point BROWSER_CANDIDATES at one you have"
    )


def page_html() -> str:
    rows = "\n".join(f"<p>*{n}. {text}</p>" for n, text in QUESTIONS)
    return f"""<!doctype html><html><head><meta charset="utf-8">
<style>
  body {{ background:#fafaf5; margin:0; padding:60px 70px; width:1480px; }}
  h1, p {{ font-family: "Devanagari MT", "Devanagari Sangam MN", "Noto Sans Devanagari", sans-serif; color:#141414; }}
  h1 {{ font-size:48px; margin:0 0 50px; }}
  p {{ font-size:36px; margin:0 0 42px; line-height:1.4; }}
</style></head><body>
<h1>हिंदी प्रश्न पत्र</h1>
{rows}
</body></html>"""


def render_clean_page(width: int = 1600, height: int = 900) -> tuple[Image.Image, str]:
    """A crisp, browser-rendered page - proper Devanagari shaping, the easy
    case talk-notes.md describes (a digital render, not a camera capture)."""
    truth = "\n".join(f"*{n}. {text}" for n, text in QUESTIONS)

    with TemporaryDirectory() as tmp:
        html_path = Path(tmp) / "page.html"
        shot_path = Path(tmp) / "shot.png"
        html_path.write_text(page_html(), encoding="utf-8")

        subprocess.run(
            [
                find_browser(),
                "--headless",
                "--disable-gpu",
                f"--screenshot={shot_path}",
                f"--window-size={width},{height}",
                "--force-device-scale-factor=2",
                f"file://{html_path}",
            ],
            capture_output=True,
            check=True,
        )
        img = Image.open(shot_path).convert("L")
        img.load()  # detach from the temp file before it's removed

    return img, truth


def degrade(img: Image.Image, *, seed: int, jpeg_quality: int) -> Image.Image:
    """Push a clean render toward a genuine scan: skew, blur, noise, faded contrast."""
    rng = random.Random(seed)

    degraded = img.rotate(
        rng.uniform(-1.4, 1.4), resample=Image.BICUBIC, fillcolor=250, expand=False
    )
    degraded = degraded.filter(ImageFilter.GaussianBlur(radius=rng.uniform(0.7, 1.2)))

    pixels = degraded.load()
    w, h = degraded.size
    for _ in range(int(w * h * 0.03)):
        x, y = rng.randrange(w), rng.randrange(h)
        pixels[x, y] = max(0, min(255, pixels[x, y] + rng.randint(-70, 70)))

    degraded = degraded.point(lambda p: int(55 + p * 0.72))

    buf = io.BytesIO()
    degraded.convert("RGB").save(buf, format="JPEG", quality=jpeg_quality)
    buf.seek(0)
    return Image.open(buf).convert("L")


def run_tesseract(image_path: Path) -> str:
    if shutil.which("tesseract") is None:
        raise SystemExit("tesseract not found on PATH - see the module docstring")
    result = subprocess.run(
        ["tesseract", str(image_path), "stdout", "-l", "hin"],
        capture_output=True,
        check=True,
    )
    return result.stdout.decode("utf-8", errors="replace")


def normalise(text: str) -> str:
    return unicodedata.normalize("NFC", text)


def word_accuracy(truth: str, ocr: str) -> float:
    """Fraction of truth words found anywhere in the OCR text.

    A simplified stand-in for WER, not the exact production metric - good
    enough to show the same shape of result, not a claim of methodological
    equivalence with the real pipeline.
    """
    truth_words = normalise(truth).split()
    ocr_text = normalise(ocr)
    if not truth_words:
        return 0.0
    hits = sum(1 for w in truth_words if w in ocr_text)
    return hits / len(truth_words)


def question_numbers(text: str) -> list[str]:
    return NUMBER_PATTERN.findall(normalise(text))


@dataclass(slots=True, frozen=True)
class Result:
    truth: str
    ocr: str

    @property
    def word_acc(self) -> float:
        return word_accuracy(self.truth, self.ocr)

    @property
    def expected_numbers(self) -> list[str]:
        return question_numbers(self.truth)

    @property
    def recovered_numbers(self) -> list[str]:
        """Substring test anywhere in the OCR text - the most generous
        possible reading of "did this number survive", matching
        metric_blindspot.py's identifier-recall methodology. The asterisk
        and period are not required: Tesseract frequently drops the
        asterisk even when the digits themselves are correct, and punishing
        that would conflate a symbol-recognition slip with a number slip.
        """
        ocr_text = normalise(self.ocr)
        return [n for n in self.expected_numbers if n in ocr_text]

    @property
    def number_recall(self) -> float:
        if not self.expected_numbers:
            return 0.0
        return len(self.recovered_numbers) / len(self.expected_numbers)


def render_report(result: Result) -> str:
    lost = [n for n in result.expected_numbers if n not in result.recovered_numbers]
    lines = [
        "the metric everyone reports",
        f"  word accuracy            {result.word_acc * 100:.1f}%",
        "",
        "the metric the task needs",
        f"  question numbers expected  {len(result.expected_numbers)}",
        f"  question numbers recovered {len(result.recovered_numbers)}",
        f"  question-number recall     {result.number_recall * 100:.1f}%",
    ]
    if lost:
        lines.append(f"  lost                       {', '.join(lost)}")
    lines += [
        "",
        "raw tesseract output",
        *(f"  {line}" for line in result.ocr.strip().splitlines() if line.strip()),
    ]
    return "\n".join(lines)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--out-dir", type=Path, default=Path(__file__).parent / "fixtures"
    )
    parser.add_argument("--seed", type=int, default=7)
    parser.add_argument(
        "--jpeg-quality",
        type=int,
        default=35,
        help="lower = more recompression artifact, closer to a repeatedly-copied scan",
    )
    args = parser.parse_args()
    args.out_dir.mkdir(parents=True, exist_ok=True)

    clean, truth = render_clean_page()
    clean_path = args.out_dir / "page_clean.png"
    clean.save(clean_path)
    (args.out_dir / "truth.txt").write_text(truth, encoding="utf-8")

    scanned = degrade(clean, seed=args.seed, jpeg_quality=args.jpeg_quality)
    scanned_path = args.out_dir / "page_scanned.jpg"
    scanned.save(scanned_path)

    clean_ocr = run_tesseract(clean_path)
    scanned_ocr = run_tesseract(scanned_path)

    (args.out_dir / "ocr_clean.txt").write_text(clean_ocr, encoding="utf-8")
    (args.out_dir / "ocr_scanned.txt").write_text(scanned_ocr, encoding="utf-8")

    clean_result = Result(truth=truth, ocr=clean_ocr)
    scanned_result = Result(truth=truth, ocr=scanned_ocr)

    print(f"fixtures written to {args.out_dir}\n")
    print("=== clean digital render (the easy case) ===")
    print(render_report(clean_result))
    print("\n=== genuine-scan degradation (the case that matters) ===")
    print(render_report(scanned_result))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
