# Week 2 Workshop

Week 2 should feel like a plotting studio, not a single-case-script.

## Suggested Flow

1. Read `README.md`, `FIGURE_RUBRIC.md`, `BEGINNER_PLOTTING.md`, `FRED_STAGE1_DDF.md`, `STAGE1_DDF.md`, `DATA_GUIDE.md`, `FIGURE_GALLERY.md`, and `NARRATIVE_BRIEF.md`.
2. Run `python fins2026/week2/scripts/describe_week2_data.py`.
3. Build the synthetic beginner CSV with `scripts/make_beginner_synthetic_prices.py`.
4. Build the plain one-line chart with `scripts/make_beginner_simple_time_series.py`.
5. Build the FT-style upgrade with `scripts/make_beginner_ft_time_series.py`.
6. Make students explain the one-line story and check it against `FIGURE_RUBRIC.md` before they open the larger figure packs.
7. Run `scripts/make_fred_stage1_walkthrough.py` so students see the U.S. Stage 1 long-table logic before the production FRED figure path.
8. Run `scripts/make_australia_stage1_walkthrough.py` so students see the Australia Stage 1 long-table logic before the production Australia pull path.
9. Build the broad style gallery with `scripts/make_ft_validation_figures.py`.
10. Open the GDP and world-bank figures first so students see ranking charts, slope charts, dumbbells, and bubble plots.
11. Pull or rebuild the FRED sample with `scripts/pull_fred_market_data.py`. The default is the frozen `2015-01-01` through `2025-12-31` lecture window; use `--rolling-window` only when you explicitly want updated data.
12. Build the curated market-and-macro pack with `scripts/make_fred_market_figures.py`.
13. Pull or rebuild the Australia Stage 1 fixture with `scripts/pull_australia_macro_data.py`.
14. Open `results/data/australia_macro_stage1_long.csv`, `australia_macro_reference_panel.csv`, and `australia_macro_observable_panel.csv` before plotting anything so students see the Data Factory Floor hand-off.
15. Build the Australia lecture pack with `scripts/make_australia_macro_figures.py`.
16. Discuss the transformation choice in each figure:
   level, bp change, percentage-point change, log growth, or return.
17. Use the Australia pack to teach reference dates versus observable dates, month-end versus quarter-end stamping, and why vacancies do not belong in the December 2025 common-endpoint core comparison.
18. Use `NARRATIVE_BRIEF.md` when students turn the five figures into the six-paragraph macro story.
19. Launch the Week 2 app and confirm it uses the same month-end merged panel.
20. Rehearse the Week 2 deployment checklist for the simple Streamlit app.
21. Refresh `guidance/` after any meaningful week change.

## Existing Week-Specific Guides

- `FIGURE_RUBRIC.md`
- `BEGINNER_PLOTTING.md`
- `FRED_STAGE1_DDF.md`
- `STAGE1_DDF.md`
- `NARRATIVE_BRIEF.md`
- `APP_AUDIT.md`
- `APP_LAB.md`
- `FIGURE_GALLERY.md`
