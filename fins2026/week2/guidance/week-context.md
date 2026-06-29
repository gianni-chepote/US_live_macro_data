# Week Context

## Week Identity
- Week folder: `fins2026/week2`
- Title: Week 2: FT-Style Plotting, Narrative, And A First Streamlit App
- README summary: Week 2 is the plotting week. The point is not one chart type and not one dataset. The point is to learn how to build a visual story from data, choose the right transformation, and export clean Word/A4-ready FT-style figures. That starts with one beginner step: draw one simple time-series chart well.

## Core Guides

- `fins2026/week2/README.md`: Week 2: FT-Style Plotting, Narrative, And A First Streamlit App. Week 2 is the plotting week. The point is not one chart type and not one dataset. The point is to learn how to build a visual story from data, choose the right transformation, and export clean Word/A4-ready FT-style figures. That starts with one beginner step: draw one simple time-series chart well.
- `fins2026/week2/WORKSHOP.md`: Week 2 Workshop. Week 2 should feel like a plotting studio, not a single-case-script.
- `fins2026/week2/DATA_GUIDE.md`: Week 2 Data Guide. Week 2 uses several data frequencies on purpose. The plotting lesson is not just styling. It is also about choosing the right unit of analysis before you draw the figure.
- `fins2026/week2/SUBMISSION_CHECKLIST.md`: Week 2 App Deployment Checklist. Use this checklist to rehearse a final project deployment. For the plain-English full workflow, see `docs/apps/streamlit/student-quickstart.md`.

## Additional Week Docs

- `fins2026/week2/APP_AUDIT.md`: Week 2 Streamlit App Audit. Audit date: 2026-04-27
- `fins2026/week2/APP_LAB.md`: Week 2 App Lab: First Streamlit Plotting App. This lab turns the Week 2 market-and-macro figure workflow into a first deployable Streamlit app.
- `fins2026/week2/BEGINNER_PLOTTING.md`: Week 2 Beginner Plotting. Start here if you are new to Python plotting.
- `fins2026/week2/FIGURE_GALLERY.md`: Week 2 Figure Gallery. Week 2 has four figure surfaces.
- `fins2026/week2/FIGURE_RUBRIC.md`: Week 2 Figure Rubric. Use this checklist before you call a Week 2 figure finished.
- `fins2026/week2/FRED_STAGE1_DDF.md`: Week 2 FRED Stage 1. This is the student-facing Data Factory Floor Station 1 path for the U.S. market-and-macro exercise.
- `fins2026/week2/NARRATIVE_BRIEF.md`: Week 2 Narrative Brief. Week 2 is not only a plotting week. It is a five-figure narrative week.
- `fins2026/week2/STAGE1_DDF.md`: Week 2 Australia Stage 1. This is the student-facing Data Factory Floor Station 1 path for the Australia macro extension.

## Prompt Files

- `fins2026/week2/prompts/assistant_starter.md`: Week 2 Assistant Starter Prompt. Load Week 2 context in this order before answering:
- `fins2026/week2/prompts/australia_macro_prompt.md`: Prompt: Build Or Fix The Week 2 Australia Macro Pipeline. Use this prompt when you want Codex to help with the Australia macro extension for Week 2.
- `fins2026/week2/prompts/figure_correction_prompt.md`: Prompt: Fix A Week 2 Figure From A Screenshot. Use this prompt when an exported Week 2 figure looks wrong, messy, mislabeled, or weak.
- `fins2026/week2/prompts/ft_figure_prompt.md`: Prompt: Create FT-Style Figures From My Dataframe. Use this prompt in PyCharm when you have a dataframe named `df`.
- `fins2026/week2/prompts/README.md`: Week 2 Prompts. Keep reusable prompts here when the week benefits from repeated AI-assisted figure, app, report, or data-analysis tasks.
- `fins2026/week2/prompts/streamlit_intro_prompt.md`: Week 2 Streamlit Intro Prompt. Use this prompt when you want help with the Week 2 Streamlit app without accidentally jumping to the fuller Week 3 dashboard.

## Current Scripts

- `fins2026/week2/scripts/describe_data.py`: Summarize the data sources used in Week 2.
- `fins2026/week2/scripts/describe_week2_data.py`: Describe the datasets used in the Week 2 figure and app lab.
- `fins2026/week2/scripts/make_all_week2_figures.py`: Run the complete Week 2 figure lab.
- `fins2026/week2/scripts/make_australia_macro_figures.py`: Create the Week 2 Australia macro figure pack.
- `fins2026/week2/scripts/make_australia_stage1_walkthrough.py`: Walk through Week 2 Australia Data Factory Floor Station 1.
- `fins2026/week2/scripts/make_beginner_ft_time_series.py`: Build the FT-style Week 2 beginner time-series chart.
- `fins2026/week2/scripts/make_beginner_simple_time_series.py`: Build the plain Matplotlib Week 2 beginner time-series chart.
- `fins2026/week2/scripts/make_beginner_synthetic_prices.py`: Create the Week 2 beginner synthetic price CSV.
- `fins2026/week2/scripts/make_fred_market_figures.py`: Create FT-style figures from the Week 2 FRED market-and-macro panel.
- `fins2026/week2/scripts/make_fred_stage1_walkthrough.py`: Walk through Week 2 FRED Data Factory Floor Station 1.
- `fins2026/week2/scripts/make_ft_validation_figures.py`: Build the Week 2 FT-style validation figure proof pack.
- `fins2026/week2/scripts/make_single_word_figure.py`: Build one Word-ready FT-style figure from a validation dataset.
- `fins2026/week2/scripts/pull_australia_macro_data.py`: Pull official Australian macro data for the Week 2 Australia figure pack.
- `fins2026/week2/scripts/pull_fred_market_data.py`: Pull live FRED market-and-macro data for the Week 2 figure exercise.
- `fins2026/week2/scripts/run_week.py`: Print the canonical Week 2 workflow and create output folders.

## Standard Working Rules

- `data/` is for committed source inputs.
- `results/data/` is for generated, downloaded, cleaned, or merged datasets.
- `scratch/` is for disposable experiments, not the final path.
- Promote reused week-local logic into `code/` and cross-week logic into `fintools/`.

## Timing And Alignment Notes

- a U.S. FRED market-and-macro pack for month-end resampling and transformation choice.
- mixed-frequency macro series need explicit reference dates, observable dates, and common-endpoint rules before plotting.
- common reference endpoint: `2025-12-31`.
- common fully observed classroom information set: `2026-03-31`.
- resample daily market data to month-end.
- `app/streamlit_app.py` is the Week 2 month-end plotting app.
- mixed-frequency Australia macro data with explicit release-lag rules.
- one typed long table with `reference_date`, `release_date`, `observable_month_end`, `native_frequency`, units, and source fields.

## Current Paths

- Source data: `fins2026/week2/data`
- Generated outputs: `fins2026/week2/results`
- Current context files: `fins2026/week2/guidance`
