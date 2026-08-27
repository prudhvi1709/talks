# metric_blindspot

A page where character error rate reads 96.6% accurate and every identifier on
it is wrong.

```bash
uv run --script metric_blindspot.py
```

No dependencies, no network, no model. The fixtures are two text files you can
read: a synthetic bilingual legislative page and a plausible OCR of it, with
realistic Devanagari matra and conjunct errors in the prose and digit confusions
in the question numbers.

## The point

The output is not "look, CER was wrong here." It is the bound at the bottom:

```
identifiers are 20 of 2322 characters, 0.86% of the page
so CER can move at most 0.86 points between every identifier being
perfect and every identifier being destroyed
```

A substitution costs one edit per character, so the identifier budget is the
ceiling on how far CER can respond to identifier loss. On this page that ceiling
is under one point. No amount of tuning, no better OCR engine, and no stricter
CER threshold can make the standard metric sensitive to the failure the task
cannot tolerate. The metric is not noisy, it is measuring a different thing.

This generalises to any page where the task depends on a small set of tokens:
invoice numbers, case IDs, dosages, account numbers, part numbers. Compute
`identifier_chars / total_chars` on your own corpus and you have the bound
before you run anything.

## On your own data

```bash
uv run --script metric_blindspot.py \
  --truth path/to/truth.txt \
  --ocr path/to/ocr.txt \
  --pattern 'Invoice #(\d{6})'
```

Group 1 is used if the pattern has one, otherwise the whole match. Identifier
recall uses a substring test anywhere on the page, which is the most generous
reading of "did it survive" and therefore an upper bound on real performance.
