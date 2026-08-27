# Good Enough for What?

**Three small models I had to judge this year, and the one question that decided all three**

## Session description

I keep getting asked some version of the same question - is this smaller,
cheaper model good enough to replace the hosted one - and I've had to answer
it three times this year, and got it wrong on the first pass every time, not
because the model was bad but because I was reading the wrong number.
Tesseract, a free local OCR engine, looked almost as good as hosted frontier
OCR APIs on word accuracy, and I nearly shipped it, until I checked the one
thing the product actually needed: could it still read question numbers, the
string that links a question to its answer. It recovered 68% of them on
Hindi and 39% on English against 100% for every hosted model, and the
failure had a signature, `*896.` coming back as `+896.` - same benchmark,
same model, and the number everyone reports said close call while the number
that mattered said not close at all. The same mistake showed up twice more
this year, once in an open embedding model I ended up choosing over a hosted
one, and once in a small vision model I added to a video pipeline and then
had to rip back out, because the verifier built to catch its errors was
catching a rule, not a mistake. I'll walk through all three, then run a
two-minute script live on stage that reproduces the core failure - a page
scoring 96%+ "accurate" while every ID number on it is wrong - so you can
check whether your own metric has the same blind spot.

## Takeaways

1. How to pick the number that actually decides "good enough" before you run
   the benchmark, not after - because the default metric often isn't it, and
   a single pass/fail score lets the wrong model win.
2. What it looks like when a "small model checks the big model" setup goes
   wrong, including a safety net whose biggest catch turned out to be a
   story it was built to tell, not a thing it actually found.

## Audience

Engineers and technical folks who have to make this call and then defend it
to someone else - a manager, a client, a teammate who disagrees. No ML
research background needed; every method here is something you could run
this afternoon.

## Bio

I'm Prudhvi Krovvidi, a Data Scientist at Straive, working at the
intersection of Data Science, Generative AI, and AI-driven applications. I
enjoy turning data and emerging AI technologies into practical solutions,
with hands-on experience across LLMs, RAG, document intelligence, computer
vision, and analytics.

Outside of work, I enjoy riding, exploring new places, and experimenting
with new technologies. I'm naturally curious and enjoy learning by building,
breaking things, and figuring out how they work. I'm also passionate about
sharing what I learn and connecting with people from the wider data and
technology community.

LinkedIn: linkedin.com/in/prudhvi-krovvidi
Email: prudhvi.krovvidi@straive.com

## Draft slides (PDF/PPT, comments access)

[TODO: add link once the deck from `slide-plan.md` is built]

## 2-minute elevator pitch video

[TODO: add link once recorded]
