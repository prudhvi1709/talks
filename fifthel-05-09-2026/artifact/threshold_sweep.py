# /// script
# requires-python = ">=3.12"
# dependencies = []
# ///
"""Re-threshold a retained detection log against ground truth, without a GPU.

If a detection scan recorded every hit and its score, choosing the confidence
threshold afterwards is arithmetic. Most teams tune the threshold by hand, ship
it, and never sweep it, on the assumption that sweeping means re-running the
model. It does not, provided the scan kept the scores.

The sweep answers a question a single threshold cannot: whether any operating
point would have worked, or whether the scores are simply not comparable across
runs, in which case no global threshold exists and the defect is upstream.

Input JSON: {"detections": [{"seconds": int, "score": float}, ...]} per run,
plus ground-truth seconds per run.
"""

from __future__ import annotations

import argparse
import json
import sys
from dataclasses import dataclass
from pathlib import Path

THRESHOLDS = (0.15, 0.20, 0.25, 0.30, 0.35, 0.40, 0.50, 0.60)


@dataclass(slots=True, frozen=True)
class Run:
    name: str
    detections: tuple[tuple[int, float], ...]
    truth: int

    @property
    def peak(self) -> float:
        return max((score for _, score in self.detections), default=0.0)


def first_hit(run: Run, threshold: float, *, count: int, window: int) -> int | None:
    """Earliest time `count` detections at or above `threshold` fall inside `window`."""
    hits = [seconds for seconds, score in run.detections if score >= threshold]
    if len(hits) < count:
        return None
    if count == 1:
        return hits[0]
    for i in range(len(hits) - count + 1):
        if hits[i + count - 1] - hits[i] <= window:
            return hits[i + count - 1]
    return None


def clock(seconds: int | None) -> str:
    if seconds is None:
        return "never"
    return f"{seconds // 3600:02d}:{seconds % 3600 // 60:02d}:{seconds % 60:02d}"


def sweep(runs: list[Run], *, count: int, window: int) -> str:
    header = f"{'thr':>5} " + " ".join(f"{r.name:>21}" for r in runs)
    lines = [header]
    for threshold in THRESHOLDS:
        cells = []
        for run in runs:
            hit = first_hit(run, threshold, count=count, window=window)
            drift = "  n/a " if hit is None else f"{(hit - run.truth) / 60:+5.0f}m"
            cells.append(f"{clock(hit):>10} ({drift})")
        lines.append(f"{threshold:>5.2f} " + " ".join(f"{c:>21}" for c in cells))
    return "\n".join(lines)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("scans", type=Path, nargs="+", help="one JSON detection log per run")
    parser.add_argument(
        "--truth",
        action="append",
        required=True,
        metavar="NAME=SECONDS",
        help="ground truth per run, repeatable",
    )
    parser.add_argument("--count", type=int, default=1, help="detections required (persistence)")
    parser.add_argument("--window", type=int, default=30, help="seconds the count must fit inside")
    args = parser.parse_args()

    try:
        truth = {k: int(v) for k, v in (item.split("=", 1) for item in args.truth)}
    except ValueError as err:
        raise SystemExit(f"--truth must look like NAME=SECONDS: {err}") from err

    runs: list[Run] = []
    for path in args.scans:
        name = path.stem
        if name not in truth:
            print(f"no ground truth for {name}, skipping", file=sys.stderr)
            continue
        payload = json.loads(path.read_text(encoding="utf-8"))
        detections = tuple(
            sorted((int(d["seconds"]), float(d["score"])) for d in payload["detections"])
        )
        runs.append(Run(name=name, detections=detections, truth=truth[name]))

    if not runs:
        print("no runs matched the supplied ground truth", file=sys.stderr)
        return 2

    for run in runs:
        print(f"{run.name}: {len(run.detections)} detections, peak score {run.peak:.3f}")
    print()
    print(sweep(runs, count=args.count, window=args.window))

    peaks = [run.peak for run in runs]
    if peaks and max(peaks) - min(peaks) > 0.2:
        print(
            f"\npeak scores span {min(peaks):.3f} to {max(peaks):.3f} across runs. "
            "Scores are not comparable, so no single global threshold exists; "
            "look upstream at the prompt or the input distribution."
        )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
