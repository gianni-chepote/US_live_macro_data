# Week 2 Assistant Starter Prompt

Load Week 2 context in this order before answering:

1. `AGENTS.md`
2. `README.md`
3. `FIGURE_RUBRIC.md`
4. `BEGINNER_PLOTTING.md`
5. `FRED_STAGE1_DDF.md`
6. `STAGE1_DDF.md`
7. `DATA_GUIDE.md`
8. `FIGURE_GALLERY.md`
9. `NARRATIVE_BRIEF.md`
10. `prompts/australia_macro_prompt.md`
11. `APP_LAB.md`
12. `APP_AUDIT.md`
13. `app/README.md`
14. `guidance/week-context.md`
15. `guidance/data-context.md`
16. `guidance/output-context.md`

Then follow these rules:

- treat `data/` as committed source inputs only
- write generated datasets to `results/data/`
- write the beginner synthetic CSV to `results/data/week2_beginner_synthetic_prices.csv`
- write the FRED Stage 1 walkthrough output to `results/data/fred_market_macro_stage1_long.csv`
- write the beginner plotting outputs to `results/figures/beginner_plotting/`
- write the broad style gallery to `results/figures/style_gallery/`
- write the curated FRED narrative pack to `results/figures/market_macro_story/`
- write the curated Australia narrative pack to `results/figures/australia_macro_story/`
- when correcting an exported figure, fix the Python generator and captions, not the exported image files by hand
- make every Week 2 figure satisfy the four standards: caption, units, source, sample window
- keep one question per figure
- prefer sentence titles and direct labels when the chart is small enough to support them
- treat fit lines as visual aids only unless the task explicitly becomes econometrics
- teach plain Matplotlib first when the student is new to plotting
- keep the Week 2 app simple: plot time-series data only
- teach resampling to month-end and merging explicitly when relevant
- teach when to use levels, bp changes, rate changes shown in %, log growth, and returns
- for growth-of-one-dollar charts, use a log y-axis and wealth path, not cumulative return
- default the lecture-facing FRED scripts to the frozen `2015-01-01` through `2025-12-31` sample
- use `--rolling-window` only when the user explicitly wants fresher U.S. data
- treat the Week 2 app as a separate rolling latest-10-year surface
- Week 2 stores classroom month-end release proxies rather than exact agency publication timestamps
- for Australia mixed-frequency work, check `reference_date`, `release_date`, and `observable_month_end` before merging
- for the Australia lecture pack, default to the frozen common reference endpoint `2025-12-31`
- for the Australia lecture pack, default to the classroom information-set month-end `2026-03-31`
- do not silently forward-fill quarterly GDP, WPI, or CPI in the Australia reference panel
- do not add forecasting, backtests, stress scores, or GDP modelling to Week 2
- refresh `guidance/*.md` after a meaningful Week 2 doc, script, app, or data change
