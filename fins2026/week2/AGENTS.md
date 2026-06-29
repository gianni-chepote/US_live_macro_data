# Weekly Overlay

This folder is `fins2026/week2`.

Week 2 is the plotting week plus a simple first Streamlit app. The public
teaching arc has four figure surfaces:

- `results/figures/beginner_plotting/` for the one-series beginner plotting ladder
- `results/figures/style_gallery/` for the broad FT-style gallery, including GDP and world-bank comparisons
- `results/figures/market_macro_story/` for the 10-year FRED market-and-macro narrative pack
- `results/figures/australia_macro_story/` for the Australia macro lecture extension

## Read First

- `README.md`
- `FIGURE_RUBRIC.md`
- `BEGINNER_PLOTTING.md`
- `FRED_STAGE1_DDF.md`
- `STAGE1_DDF.md`
- `NARRATIVE_BRIEF.md`
- `WORKSHOP.md`
- `DATA_GUIDE.md`
- `FIGURE_GALLERY.md`
- `APP_LAB.md`
- `APP_AUDIT.md`
- `app/README.md`
- `guidance/week-context.md`
- `guidance/data-context.md`
- `guidance/output-context.md`

## Working Rules

- Keep week-specific work inside this folder.
- Use `data/` for committed source inputs only.
- Use `results/data/` for generated or refreshed datasets.
- Keep canonical rerunnable scripts in `scripts/`.
- Teach plain Matplotlib before the FT-style upgrade when a student is new to plotting.
- Keep the beginner ladder narrow: one synthetic series, one price column, one chart.
- Week 2 figures must satisfy the four standards: caption, units, source, sample window.
- Prefer sentence titles, direct labels, and one emphasis colour.
- Keep one question per figure.
- Treat fit lines as visual aids only unless the user explicitly changes the task.
- Write the beginner synthetic CSV to `results/data/week2_beginner_synthetic_prices.csv`.
- Write the FRED Stage 1 walkthrough output to `results/data/fred_market_macro_stage1_long.csv`.
- The Australia macro extension is a Data Factory Floor Station 1 and Station 2 exercise, not a modelling week.
- Write Week 2 live-exercise data to `results/data/fred_market_macro.csv`.
- Write the Australia Stage 1 fixture to `data/australia_macro_stage1_long.csv` only when intentionally refreshing the frozen class fixture.
- Write generated Australia Stage 1 and Stage 2 outputs to `results/data/australia_macro_*.csv` and `results/data/australia_macro_*.parquet`.
- Write the beginner plotting outputs to `results/figures/beginner_plotting/`.
- Write the broad style gallery to `results/figures/style_gallery/`.
- Write the curated FRED narrative pack to `results/figures/market_macro_story/`.
- Write the curated Australia narrative pack to `results/figures/australia_macro_story/`.
- Keep the Week 2 app simple: one series, one sample window, one chart.
- Teach when to use levels, bp changes, pp changes, log growth, and returns.
- Keep the Week 2 FRED app and figure pack aligned to the same month-end 10-year teaching panel.
- The lecture-facing FRED scripts default to the frozen `2015-01-01` through `2025-12-31` sample.
- Use `--rolling-window` only when the user explicitly wants fresher U.S. data.
- The Week 2 app is separate and can keep its latest rolling 10-year panel.
- Week 2 stores classroom month-end release proxies, not exact agency publication timestamps.
- For Australia mixed-frequency work, always distinguish `reference_date`, `release_date`, and `observable_month_end` before merging series.
- Freeze the Australia common reference endpoint at `2025-12-31` unless the user explicitly changes the teaching contract.
- Freeze the Australia common fully observed classroom information set at `2026-03-31` unless the user explicitly changes the teaching contract.
- Do not silently forward-fill quarterly GDP, WPI, or CPI in the Australia reference panel.
- Use `scratch/` for disposable experiments, not the final path.
- Promote reusable week-local logic into `code/`.
- Move anything reused across weeks into `fintools/`.
- Regenerate `guidance/*.md` after week docs, scripts, data, or outputs change.

## Useful Commands

- `python fins2026/week2/scripts/make_beginner_synthetic_prices.py`
- `python fins2026/week2/scripts/make_beginner_simple_time_series.py`
- `python fins2026/week2/scripts/make_beginner_ft_time_series.py`
- `python fins2026/week2/scripts/make_fred_stage1_walkthrough.py`
- `python fins2026/week2/scripts/make_fred_stage1_walkthrough.py --rolling-window`
- `python fins2026/week2/scripts/make_australia_stage1_walkthrough.py`
- `python fins2026/week2/scripts/describe_data.py`
- `python fins2026/week2/scripts/run_week.py`
- `python tools/workflow.py build-week-context --target fins2026/week2`
- `streamlit run fins2026/week2/app/streamlit_app.py`
