# synthetic_ocr

Reproduces case one's finding end to end, with no client data: a synthetic
Hindi question paper, OCR'd by the real Tesseract binary, scored two ways.

```bash
uv run --script generate_and_evaluate.py
```

Requires the `tesseract` binary with the Hindi language pack, and a
Chromium-family browser (used only to render the page - PIL's own text
drawing does not shape Devanagari conjuncts/matras correctly, a browser's
text engine does):

```bash
# macOS
brew install tesseract tesseract-lang   # Google Chrome already covers rendering
# Linux
apt install tesseract-ocr tesseract-ocr-hin chromium
```

## What it actually shows

The **headline result is deterministic and reproducible** - it doesn't
depend on the random seed at all, because it's just the clean render scored
against real Tesseract output:

```
word accuracy            85.0%
question numbers expected  6
question numbers recovered 3
question-number recall     50.0%
```

Word accuracy looks fine. Half the question numbers are already gone -
`896` came back as `8596`, `900` as `000`, `901` as `90` - in a page with no
scan noise, no rotation, no blur at all. That gap, on its own, is the whole
point of case one: an aggregate metric can look healthy while the specific
thing the task depends on is already failing.

## The degraded-scan comparison - honest caveat

The script also pushes the clean render through a generic degradation model
(rotation, Gaussian blur, additive noise, JPEG recompression) meant to
approximate a genuine scan, then re-runs Tesseract. With the default seed
this drops question-number recall to 0% while word accuracy holds at 85.0% -
a clean, dramatic confirmation of the pattern.

**But it isn't a reliable monotonic effect.** Testing seeds `1`, `7`, `42`,
and `123` gave question-number recall after degradation of `83.3%`, `0.0%`,
`66.7%`, and `83.3%` respectively - sometimes worse than the clean render,
sometimes not. Word accuracy stayed flat at 85-87.5% in every case. This
generic noise model isn't targeted enough to reproduce the real corpus's
specific mechanism (a scan-quality effect that disproportionately hits thin,
low-redundancy glyphs like `*` and digits, which body text's redundancy
partially protects against). Don't cite the degraded-case number as if it
were as robust as the clean-render one - the clean-render gap is the
reproducible finding; the degradation step is illustrative, not proof.

If you want to tighten this, the honest next step is a degradation model
that specifically targets stroke-thin glyphs (erosion/dilation on small
connected components) rather than uniform noise - not a bigger blur radius.

## On your own data

```bash
uv run --script generate_and_evaluate.py --seed 42 --jpeg-quality 25
```

`--seed` controls the degradation's random noise pattern and rotation angle.
`--jpeg-quality` controls recompression severity (lower = more artifacted).
`--out-dir` controls where the rendered pages and OCR transcripts land
(defaults to `fixtures/` alongside this script).
