<!-- 2026-01-07-18-40-34 -->

# CV of Ash Eunoia

Hello, this repository is where you can find my most up-to-date CV (curriculum vitae, or résumé in American English): **[Ash-Eunoia-CV.pdf](Ash-Eunoia-CV.pdf)**. Thanks for dropping by!

I'm a software developer in Cockermouth, Cumbria. My website and portfolio are at [kyberfex.com](https://kyberfex.com/).

## How it's made

The CV is written in Markdown, in [cv.md](cv.md). [build.py](build.py) turns it into an A4 PDF, styled by [cv.css](cv.css), and checks the result:

```sh
uv run build.py                 # build Ash-Eunoia-CV.pdf and check it
uv run build.py --links         # also check that every link answers
uv run build.py tailored.md     # build a copy tailored to one application, as tailored.pdf
```

The build fails if the PDF runs past two pages, or if its text doesn't match the Markdown's word for word and in the same order, which is how screening software reads a CV. The PDF is tagged for screen readers and has bookmarks for each section.

It prints with Playwright's Chromium, or Microsoft Edge where that's installed instead. On a machine with neither, run `uv run playwright install chromium` first.

The typeface is [Bricolage Grotesque](https://github.com/ateliertriay/bricolage), under the SIL Open Font License ([fonts/OFL.txt](fonts/OFL.txt)), as on kyberfex.com.

What the CV is for, who reads it and the principles it follows are in the [brief](docs/brief.md).
