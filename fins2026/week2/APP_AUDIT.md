# Week 2 Streamlit App Audit

Audit date: 2026-04-27

Primary app entrypoint: `fins2026/week2/app/streamlit_app.py`

## Summary

The Week 2 app now matches the teaching goal more closely. It is still a first
deployable app, but it now reflects the Week 2 plotting lesson properly:
students can inspect levels, bp changes, pp changes, log growth, and returns
from the same month-end merged panel.

That is the right scope for Week 2. The richer dashboard logic belongs in
Week 3.

## What The App Should Do

- load fixture or live FRED data
- resample daily market data to month-end
- align monthly macro data to month-end
- merge the month-end panel before plotting
- expose one clear series selector
- expose one clear sample-period selector
- show a readable time-series chart
- explain why some plotted series are levels and others are changes or returns
- show whether the source is fixture, live cache, or fallback
- show the displayed data in a table
- allow CSV download of the displayed data

## What The App Should Not Do In Week 2

- no stress-score construction
- no yield-curve interpretation layer
- no forecasting
- no backtests
- no GDP modelling
- no large multi-tab product shell

## Audit Notes

- Cached fixture/live loading is still appropriate.
- The source-status line should distinguish fixture mode from live-cache mode.
- The app should remain readable in one sitting.
- The plotted-series notes should keep explaining the transformation choice in student language.
- The smoke test only needs to prove the page renders and the main controls appear.

## Improvement Backlog

Immediate:

- keep deployment working for the simple Week 2 app
- keep labels app-facing and readable
- keep the figure and app narratives aligned in `README.md` and `APP_LAB.md`

Next week:

- extend this app into the fuller Week 3 dashboard
- add interpretation layers and modelling only after the simple plotting path is stable
