# Week 2: FT-Style Plotting, Narrative, And A First Streamlit App

Week 2 is the plotting week. The point is not one chart type and not one
dataset. The point is to learn how to build a visual story from data, choose
the right transformation, and export clean Word/A4-ready FT-style figures.
That starts with one beginner step: draw one simple time-series chart well.

This week now has two macro case-study tracks:

- a U.S. FRED market-and-macro pack for month-end resampling and transformation choice
- an Australia macro pack that extends the same visual storytelling lesson through the Digital Data Factory framing from Week 1

The Australia extension is deliberately limited to Data Factory Floor Station 1
and Station 2:

- Station 1: official-source extraction, typing, cadence mapping, endpoint freezing, and release-lag handling
- Station 2: communication-ready panels and figures, not modelling or forecasting

Generated files are written under:

```text
fins2026/week2/results/
```

They are ignored by git. Re-run the scripts whenever you want a fresh proof
pack.

## What You Will Build

1. `week2_beginner_synthetic_prices.csv` in `results/data/`
   This is the deterministic beginner dataset used for the first Week 2
   plotting ladder.
2. `week2_beginner_simple_time_series.png` and `.pdf` in `results/figures/beginner_plotting/`
   This is the plain Matplotlib version of the first Week 2 time-series story.
3. `week2_beginner_ft_time_series.png`, `.pdf`, and `.caption.md` in `results/figures/beginner_plotting/`
   This is the FT-style upgrade of the same one-series beginner chart.
4. `validation_figures_ft.docx` in `results/figures/style_gallery/`
   This is the broad Week 2 style gallery. It includes GDP comparison plots,
   world-bank charts, return distributions, small multiples, scatter plots,
   heatmaps, calendar heatmaps, yield-spread charts, and more.
5. `week2_market_macro_story_ft.docx` in `results/figures/market_macro_story/`
   This is the 10-year Week 2 market-and-macro narrative pack built from
   public FRED data.
6. `week2_australia_macro_story_ft.docx` in `results/figures/australia_macro_story/`
   This is the Australia macro lecture extension built from official RBA
   tables with a frozen December 2025 reference endpoint and a March 2026
   classroom information set.
7. `app/streamlit_app.py`
   This is the first deployable Streamlit app. It stays simple, but it uses the
   same month-end market-and-macro teaching panel as the Week 2 figures.

## Core Week 2 Ideas

- not all data should be plotted in levels
- rates often matter in basis-point changes
- unemployment often matters in percentage-point changes
- activity series often read better in log growth
- equities often need returns or cumulative returns
- daily and monthly data often need resampling and merging before plotting
- mixed-frequency macro series need explicit reference dates, observable dates,
  and common-endpoint rules before plotting
- every narrative starts with one plotted object, often one clean time-series
  line
- a clean weekly workflow should separate Station 1 data authenticity from
  Station 2 communication-ready features and visuals
- subplots, scatter plots, and ranking charts are part of the story, not an optional extra

Useful guides:

- `FIGURE_RUBRIC.md`
- `BEGINNER_PLOTTING.md`
- `FRED_STAGE1_DDF.md`
- `STAGE1_DDF.md`
- `DATA_GUIDE.md`
- `FIGURE_GALLERY.md`
- `NARRATIVE_BRIEF.md`
- `data/README.md`
- `prompts/australia_macro_prompt.md`
- `prompts/figure_correction_prompt.md`
- `prompts/ft_figure_prompt.md`
- `APP_LAB.md`
- `APP_AUDIT.md`
- `docs/apps/streamlit/student-quickstart.md`

## Run Everything

Use the repo interpreter from the repo root.

Windows:

```powershell
.\.venv\Scripts\python.exe fins2026\week2\scripts\make_all_week2_figures.py --skip-live --use-fixture
```

macOS/Linux:

```bash
./.venv/bin/python fins2026/week2/scripts/make_all_week2_figures.py --skip-live --use-fixture
```

Drop `--skip-live --use-fixture` when you want fresh FRED and Australia data.
Use `--skip-australia` if you want only the beginner ladder, style gallery,
and original Week 2 U.S. surfaces.

For the U.S. lecture pack, Week 2 now defaults to a frozen chapter-aligned
FRED sample of `2015-01-01` through `2025-12-31`. If you want a rolling
updated FRED panel instead, use `--rolling-window` on the FRED scripts or
`--rolling-fred-window` on `make_all_week2_figures.py`.

## Start With The Beginner Plotting Ladder

Run these three scripts in order:

Windows:

```powershell
.\.venv\Scripts\python.exe fins2026\week2\scripts\make_beginner_synthetic_prices.py
.\.venv\Scripts\python.exe fins2026\week2\scripts\make_beginner_simple_time_series.py
.\.venv\Scripts\python.exe fins2026\week2\scripts\make_beginner_ft_time_series.py
```

macOS/Linux:

```bash
./.venv/bin/python fins2026/week2/scripts/make_beginner_synthetic_prices.py
./.venv/bin/python fins2026/week2/scripts/make_beginner_simple_time_series.py
./.venv/bin/python fins2026/week2/scripts/make_beginner_ft_time_series.py
```

This ladder teaches the first crucial Week 2 skill:

1. create one tidy dataframe
2. plot one clear time-series line with plain Matplotlib
3. upgrade the same chart with the Week 2 FT-style helper

The beginner outputs are written to:

```text
fins2026/week2/results/data/week2_beginner_synthetic_prices.csv
fins2026/week2/results/figures/beginner_plotting/
```

## Build The Style Gallery

Windows:

```powershell
.\.venv\Scripts\python.exe fins2026\week2\scripts\make_ft_validation_figures.py
```

macOS/Linux:

```bash
./.venv/bin/python fins2026/week2/scripts/make_ft_validation_figures.py
```

Equivalent workflow helper:

```bash
python tools/workflow.py build-figure --style ft --docx --output fins2026/week2/results/figures/style_gallery
```

This is where the GDP and world-bank comparison plots live.

## Build The Market-And-Macro Story Pack

Walk through the student-facing FRED Stage 1 path first if you want the
long-table version of the U.S. exercise:

```bash
python fins2026/week2/scripts/make_fred_stage1_walkthrough.py
```

This default path freezes the sample to `2015-01-01` through `2025-12-31` so
lecture results stay reproducible.

Offline classroom walkthrough:

```bash
python fins2026/week2/scripts/make_fred_stage1_walkthrough.py --use-fixture
```

Rolling updated FRED window:

```bash
python fins2026/week2/scripts/make_fred_stage1_walkthrough.py --rolling-window
```

The FRED Stage 1 guide is:

```text
fins2026/week2/FRED_STAGE1_DDF.md
```

Online:

```bash
python fins2026/week2/scripts/pull_fred_market_data.py
python fins2026/week2/scripts/make_fred_market_figures.py
```

The default FRED pull freezes the lecture sample to `2015-01-01` through
`2025-12-31`.

Offline:

```bash
python fins2026/week2/scripts/pull_fred_market_data.py --use-fixture
python fins2026/week2/scripts/make_fred_market_figures.py
```

Rolling updated FRED window:

```bash
python fins2026/week2/scripts/pull_fred_market_data.py --rolling-window
python fins2026/week2/scripts/make_fred_market_figures.py
```

The cleaned live-exercise dataset is written to:

```text
fins2026/week2/results/data/fred_market_macro.csv
```

That file now defaults to the frozen lecture sample. Use `--rolling-window` if
you intentionally want the latest rolling 10 years instead.

The curated narrative pack is written to:

```text
fins2026/week2/results/figures/market_macro_story/
```

If one of the exported figures is weak, screenshot it and use
`prompts/figure_correction_prompt.md`. The goal is to fix the generating code,
captions, and context, not to hand-edit the exported image.

When you turn the five figures into prose, use:

```text
fins2026/week2/NARRATIVE_BRIEF.md
```

## Build The Australia Macro Story Pack

Walk through Station 1 first if you want the student-facing DDF path:

```bash
python fins2026/week2/scripts/make_australia_stage1_walkthrough.py
```

Offline classroom walkthrough:

```bash
python fins2026/week2/scripts/make_australia_stage1_walkthrough.py --use-fixture
```

The Station 1 guide is:

```text
fins2026/week2/STAGE1_DDF.md
```

Online:

```bash
python fins2026/week2/scripts/pull_australia_macro_data.py
python fins2026/week2/scripts/make_australia_macro_figures.py
```

Offline:

```bash
python fins2026/week2/scripts/pull_australia_macro_data.py --use-fixture
python fins2026/week2/scripts/make_australia_macro_figures.py
```

The committed Stage 1 fixture is:

```text
fins2026/week2/data/australia_macro_stage1_long.csv
```

The generated Stage 1 and Stage 2 outputs are written to:

```text
fins2026/week2/results/data/australia_macro_stage1_long.csv
fins2026/week2/results/data/australia_macro_monthly_native_panel.csv
fins2026/week2/results/data/australia_macro_quarterly_native_panel.csv
fins2026/week2/results/data/australia_macro_reference_panel.csv
fins2026/week2/results/data/australia_macro_observable_panel.csv
fins2026/week2/results/data/australia_macro_feature_panel.csv
```

The curated Australia narrative pack is written to:

```text
fins2026/week2/results/figures/australia_macro_story/
```

The Australia workflow uses these frozen classroom dates:

- common reference endpoint: `2025-12-31`
- common fully observed classroom information set: `2026-03-31`

That means the figures compare Australia through December 2025 rather than
pretending every series has the same latest release date.

## Run The Streamlit App

Run from the repo root:

```bash
streamlit run fins2026/week2/app/streamlit_app.py
```

The app starts in fixture mode so it works offline. Live mode uses a no-key
FRED graph CSV when internet access is available.

Week 2 keeps the app deliberately small:

- choose fixture or live public data
- resample daily market data to month-end
- merge that panel with monthly macro data
- choose one level, change, growth, or return series
- choose one sample window inside the shared 10-year panel
- plot one clean time-series chart
- inspect and download the displayed data

Week 2 does not yet add forecasting, backtests, stress scoring, or GDP
modelling. Those belong in Week 3.

Before deployment, run:

```bash
python tools/workflow.py check-app-submission --target fins2026/week2 --entrypoint fins2026/week2/app/streamlit_app.py
```

To rehearse a clean private deploy repo:

```bash
python tools/workflow.py prepare-app-repo --source fins2026/week2 --dest ../week2-month-end-market-macro --repo week2-month-end-market-macro --entrypoint fins2026/week2/app/streamlit_app.py
```

Then follow `docs/apps/streamlit/finish-deployment.md`.

## PyCharm

1. Open the cloned `fins-agent` folder as one PyCharm project.
2. Set the interpreter to the repo `.venv`.
3. Run the Week 2 scripts from the repo root working directory.
4. Start with `BEGINNER_PLOTTING.md` if you need the one-chart on-ramp before
   the larger figure packs.
5. Use the Week 2 prompts when you want AI help that stays inside this week's plotting scope.

## Read The Code

- `code/beginner_plotting.py` holds the reusable logic for the beginner
  synthetic dataset and the two one-series plotting exports
- `code/fred_stage1.py` holds the Week 2 FRED Stage 1 contracts and long-table helper
- `scripts/make_fred_stage1_walkthrough.py` is the student-facing FRED Stage 1 walkthrough
- `scripts/make_australia_stage1_walkthrough.py` is the student-facing
  Australia Station 1 walkthrough
- `scripts/make_beginner_synthetic_prices.py` creates the Week 2 beginner
  synthetic CSV
- `scripts/make_beginner_simple_time_series.py` builds the plain Matplotlib
  beginner chart
- `scripts/make_beginner_ft_time_series.py` builds the FT-style upgrade of the
  same beginner chart
- `scripts/make_ft_validation_figures.py` builds the full style gallery
- `scripts/make_single_word_figure.py` shows the smallest one-figure Word export pattern
- `scripts/describe_week2_data.py` explains the public datasets and plotting workflow
- `scripts/pull_australia_macro_data.py` builds the official-source Australia Stage 1 and Stage 2 panels
- `scripts/make_australia_macro_figures.py` builds the Australia macro lecture pack
- `scripts/pull_fred_market_data.py` pulls or rebuilds the Week 2 live exercise data
- `scripts/make_fred_market_figures.py` builds the 10-year market-and-macro narrative pack
- `scripts/make_all_week2_figures.py` runs the full Week 2 figure workflow
- `app/streamlit_app.py` is the Week 2 month-end plotting app
