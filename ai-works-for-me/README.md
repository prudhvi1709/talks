# AI Works For Me

A short (~6.5 min) keynote-style talk for **Straive Convergence**: how I pointed the same AI I build for clients at my own life, built a measurable feedback loop, and lost 6 kg in 31 days without losing muscle. The app is the evidence; the real point is the compounding-asset loop between client work and personal projects.

Built with [Reveal.js](https://revealjs.com/) (vendored locally, so it runs fully offline).

## Run it

Any static file server works. For example:

```bash
python3 -m http.server 4200
# then open http://127.0.0.1:4200/
```

- **Deck:** `index.html`
- **Fullscreen:** press `F` · **Next/Prev:** arrow keys · **Overview:** `Esc`

## Structure

```
index.html            the deck (Reveal.js)
vendor/               Reveal.js core (offline)
```

## The two real assets in the loop

- **In:** a frontend skill reused from Straive work to scaffold the app's UI.
- **Out:** reusable patterns and telemetry from the project feed future work.

## GitHub Pages

Because the deck is `index.html` with relative asset paths, this folder can be served directly (e.g. `https://<user>.github.io/talks/ai-works-for-me/`).
