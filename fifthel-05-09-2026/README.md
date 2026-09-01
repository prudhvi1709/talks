# Good Enough for What?

**The Fifth Elephant - TBD**

Three small models I had to judge this year, and the one question that decided all three - why public benchmarks aren't the same as your task's metric.

- **Slides:** [View Presentation](https://prudhvi1709.github.io/talks/fifthel-05-09-2026/index.html)
- **Video:** Not available yet
- **Transcript:** Not available yet
- **Try it live:** [interactive.html](https://prudhvi1709.github.io/talks/fifthel-05-09-2026/artifact/interactive.html) - runs the talk's core check (identifier recall vs. character-error-rate) on your own text, right in the browser.

Built with [Reveal.js](https://revealjs.com/) (vendored locally, so it runs fully offline).

## Run it

Any static file server works. For example:

```bash
python3 -m http.server 4200
# then open http://127.0.0.1:4200/
```

- **Fullscreen:** press `F` - **Next/Prev:** arrow keys - **Overview:** `Esc`

## Structure

```
index.html          the deck (Reveal.js)
abstract.md          the submitted session description
vendor/               Reveal.js core (offline)
assets/               images used in the deck
artifact/             the reproducible scripts and fixtures the deck's QR codes point to
  metric_blindspot.py   the case-three check, runnable with `uv run --script`
  interactive.html       browser port of the same check, for the audience to run live
```

See `artifact/README.md` for how to run the scripts directly.
