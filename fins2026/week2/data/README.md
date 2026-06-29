# Week 2 Data

Week 2 now ships one committed week-local source fixture for the Australia
macro extension:

- `australia_macro_stage1_long.csv`
  This is the frozen Stage 1 long table built from official RBA statistical
  tables and clipped to the classroom reference endpoint of `2025-12-31`.

The public Week 2 workflow uses:

- a generated beginner synthetic price CSV for the first plotting ladder
- frozen validation datasets from `fintools.datasets`
- live or frozen FRED Treasury, VIX, macro, and S&P 500 data
- live or frozen official Australia macro data from the Week 2 RBA pipeline

The student-facing Australia Stage 1 walkthrough is:

```text
fins2026/week2/STAGE1_DDF.md
fins2026/week2/scripts/make_australia_stage1_walkthrough.py
```

The student-facing FRED Stage 1 walkthrough is:

```text
fins2026/week2/FRED_STAGE1_DDF.md
fins2026/week2/scripts/make_fred_stage1_walkthrough.py
```

The Week 2 beginner synthetic CSV is generated into:

```text
fins2026/week2/results/data/week2_beginner_synthetic_prices.csv
```

The cleaned Week 2 live-exercise CSV is generated into:

```text
fins2026/week2/results/data/fred_market_macro.csv
```

By default this is the frozen `2015-01-01` through `2025-12-31` lecture
sample. Use `--rolling-window` on `pull_fred_market_data.py` if you want the
latest rolling 10 years instead.

The Week 2 FRED Stage 1 long table is generated into:

```text
fins2026/week2/results/data/fred_market_macro_stage1_long.csv
```

That long table follows the same default frozen lecture window unless students
explicitly switch to `--rolling-window`.

The generated Australia Stage 1 and Stage 2 outputs are generated into:

```text
fins2026/week2/results/data/australia_macro_stage1_long.csv
fins2026/week2/results/data/australia_macro_monthly_native_panel.csv
fins2026/week2/results/data/australia_macro_quarterly_native_panel.csv
fins2026/week2/results/data/australia_macro_reference_panel.csv
fins2026/week2/results/data/australia_macro_observable_panel.csv
fins2026/week2/results/data/australia_macro_feature_panel.csv
```

The broad Week 2 style gallery is generated into:

```text
fins2026/week2/results/figures/style_gallery/
```

The beginner plotting ladder is generated into:

```text
fins2026/week2/results/figures/beginner_plotting/
```

The curated 10-year market-and-macro narrative pack is generated into:

```text
fins2026/week2/results/figures/market_macro_story/
```

The curated Australia macro lecture pack is generated into:

```text
fins2026/week2/results/figures/australia_macro_story/
```
