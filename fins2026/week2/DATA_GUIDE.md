# Week 2 Data Guide

Week 2 uses several data frequencies on purpose. The plotting lesson is not
just styling. It is also about choosing the right unit of analysis before you
draw the figure.

Across the week you will touch:

- synthetic daily price data in the beginner plotting ladder
- annual data in the GDP and world-bank comparisons
- monthly data in the macro panels
- daily data in the Treasury, VIX, and S&P 500 series
- mixed-frequency Australia macro data with explicit release-lag rules

Two Week 2 teaching contracts matter all week:

- `FIGURE_RUBRIC.md` for publication-quality figure judgment
- `NARRATIVE_BRIEF.md` for the five-figure, six-paragraph case-study structure

## Beginner Synthetic On-Ramp

Week 2 starts with one synthetic business-day price series so beginners can
learn the mechanics of plotting before they have to reason about mixed units,
resampling, or macro timing contracts.

The generated beginner CSV is:

```text
fins2026/week2/results/data/week2_beginner_synthetic_prices.csv
```

It has three columns:

- `date`
- `ticker`
- `price`

The teaching point is narrow on purpose:

- one tidy dataframe
- one simple line chart
- one FT-style upgrade of the same story

## Frozen Validation Datasets

The broad Week 2 style gallery uses the compact public datasets stored in
`fintools.datasets`. These work offline.

- `ff3_monthly`
- `ff25_size_value_monthly`
- `ff_industry_10_monthly`
- `fred_macro_monthly`
- `fred_rates_daily`
- `fred_financial_stress_daily`
- `fred_sp500_daily`
- `shiller_market_monthly`
- `world_bank_country_panel_annual`
- `world_bank_gdp_annual`

The world-bank datasets are the main Week 2 source for GDP comparison figures:

- GDP per capita dumbbell
- GDP share stacked bar
- population-income-GDP bubble plot
- GDP lollipop
- GDP slope chart

Use:

```python
from fintools.datasets import load_validation_dataset

dataset = load_validation_dataset("world_bank_gdp_annual")
print(dataset.data.head())
print(dataset.source)
```

## Live FRED Exercise

The Week 2 live exercise pulls a fresh no-key FRED graph CSV:

```text
https://fred.stlouisfed.org/graph/fredgraph.csv?id=DGS10,DGS2,DTB3,T10Y2Y,VIXCLS,UNRATE,INDPRO,PAYEMS,FEDFUNDS,SP500
```

Raw series:

- `DGS10`: 10-year Treasury constant maturity rate
- `DGS2`: 2-year Treasury constant maturity rate
- `DTB3`: 3-month Treasury bill rate
- `T10Y2Y`: 10-year minus 2-year Treasury spread
- `VIXCLS`: VIX
- `UNRATE`: unemployment rate
- `INDPRO`: industrial production index
- `PAYEMS`: nonfarm payroll employment
- `FEDFUNDS`: effective federal funds rate
- `SP500`: S&P 500 index level

The lecture-facing FRED scripts now default to a frozen chapter-aligned sample:

- start date: `2015-01-01`
- end date: `2025-12-31`

This keeps the Week 2 lecture figures reproducible.

Students who want fresher data can opt into a rolling updated panel with:

- `python fins2026/week2/scripts/pull_fred_market_data.py --rolling-window`
- `python fins2026/week2/scripts/make_fred_stage1_walkthrough.py --rolling-window`

The Week 2 app still keeps its own live merged panel on the latest 10 years.

The cleaned live-exercise CSV is written to:

```text
fins2026/week2/results/data/fred_market_macro.csv
```

The student-facing FRED Stage 1 walkthrough is:

```text
fins2026/week2/FRED_STAGE1_DDF.md
fins2026/week2/scripts/make_fred_stage1_walkthrough.py
```

The generated FRED Stage 1 long table is:

```text
fins2026/week2/results/data/fred_market_macro_stage1_long.csv
```

By default this is also clipped to the frozen `2015-01-01` through
`2025-12-31` lecture window.

Students can inspect the same structure offline with:

```bash
python fins2026/week2/scripts/make_fred_stage1_walkthrough.py --use-fixture
```

## Australia Macro Extension

The Australia track is the Week 2 continuation of the Digital Data Factory
approach from Week 1.

The student-facing Station 1 walkthrough is:

```text
fins2026/week2/STAGE1_DDF.md
```

The runnable walkthrough script is:

```text
fins2026/week2/scripts/make_australia_stage1_walkthrough.py
```

Stage 1 output:

- one typed long table with `reference_date`, `release_date`,
  `observable_month_end`, `native_frequency`, units, and source fields

Stage 2 outputs:

- a native monthly panel
- a native quarterly panel
- a reference-date panel for historical storytelling
- an observable-date panel for the classroom information set
- a communication-ready feature panel for the figure pack

The committed Stage 1 fixture is:

```text
fins2026/week2/data/australia_macro_stage1_long.csv
```

Students can inspect the same structure offline with:

```bash
python fins2026/week2/scripts/make_australia_stage1_walkthrough.py --use-fixture
```

The generated outputs are written to:

```text
fins2026/week2/results/data/australia_macro_stage1_long.csv
fins2026/week2/results/data/australia_macro_monthly_native_panel.csv
fins2026/week2/results/data/australia_macro_quarterly_native_panel.csv
fins2026/week2/results/data/australia_macro_reference_panel.csv
fins2026/week2/results/data/australia_macro_observable_panel.csv
fins2026/week2/results/data/australia_macro_feature_panel.csv
```

Official-source coverage:

- cash rate target
- 10Y government bond yield
- trade-weighted index
- headline CPI inflation
- trimmed mean inflation
- real GDP growth
- Wage Price Index growth
- unemployment rate
- participation rate
- employment-to-population ratio
- job vacancies and the vacancies-to-labour-force ratio
- commodity price index in A$

## Frozen Australia Timing Contract

The Australia pack does not use a vague "latest data" date.

- common reference endpoint: `2025-12-31`
- common fully observed classroom information set: `2026-03-31`

Why those dates matter:

- December 2025 labour-force data is observable in January 2026
- December 2025 quarterly CPI is observable in January 2026
- December 2025 Wage Price Index data is observable in February 2026
- December quarter 2025 GDP is observable in March 2026

This means students should distinguish:

- `reference_date`: when the economic period happened
- `release_date`: the first classroom month-end when that observation is treated as available
- `observable_month_end`: the same classroom month-end merge key used for the teaching panels

Week 2 uses a classroom month-end release proxy rather than exact agency
publication timestamps.

Week 2 uses the `reference_panel` for historical figures and the
`observable_panel` for the release-lag lesson. Do not silently forward-fill
quarterly GDP, WPI, or CPI across non-quarter months in the reference panel.

## Month-End Teaching Panel

The Week 2 app and the curated Week 2 narrative pack do not plot the raw mixed
frequency dataframe directly.

They:

1. resample daily market data to month-end
2. align monthly macro observations to month-end
3. merge the panel
4. build transformed series when levels are not the right plotting choice

This is the main transformation logic:

- levels: `DGS10`, `DGS2`, `DTB3`, `T10Y2Y`, `VIXCLS`, `UNRATE`, `INDPRO`, `PAYEMS`, `FEDFUNDS`, `SP500`
- basis-point changes: `DGS10_CHANGE_BP`, `DGS2_CHANGE_BP`, `DTB3_CHANGE_BP`, `T10Y2Y_CHANGE_BP`, `FEDFUNDS_CHANGE_BP`
- percentage-point changes: `UNRATE_CHANGE_PP`
- log growth: `INDPRO_LOG_GROWTH_PCT`, `PAYEMS_LOG_GROWTH_PCT`
- returns: `SP500_RETURN_PCT`, `SP500_LOG_RETURN_PCT`, `SP500_CUMULATIVE_RETURN_PCT`
- volatility change example: `VIX_CHANGE_PCT`

Week 2 wants students to learn when each transformation is useful:

- level charts answer level questions
- basis-point charts answer rate-move questions
- percentage-point charts answer labor-market move questions
- log-growth charts answer activity-growth questions
- return charts answer market-performance questions

The Australia feature panel adds the same idea with publication-style names:

- `Cash rate target change (bp)`
- `10Y government bond yield change (bp)`
- `Unemployment rate change (pp)`
- `Trade-weighted index log change (%)`
- `Commodity price index (A$) log change (%)`
- `Real GDP quarterly log growth (%)`

## Australia Relationship Frames

The Australia pack uses the data pipeline to teach three famous relationships
plus one Australia-specific external-sector pairing:

- Wage Phillips curve: unemployment rate versus year-ended WPI growth
- Okun's law: quarterly real GDP log growth versus the change in the quarterly
  average unemployment rate
- Beveridge curve: unemployment rate versus the vacancies-to-labour-force ratio
- commodity prices and the trade-weighted index: monthly log-change scatter

These are not just plotting exercises. They require explicit choices about
quarter-end pairing, point-in-time vacancy dates, and monthly versus quarterly
aggregation.

## Output Locations

The beginner plotting ladder is written to:

```text
fins2026/week2/results/figures/beginner_plotting/
```

The broad style gallery is written to:

```text
fins2026/week2/results/figures/style_gallery/
```

The curated 10-year market-and-macro narrative pack is written to:

```text
fins2026/week2/results/figures/market_macro_story/
```

The curated Australia macro lecture pack is written to:

```text
fins2026/week2/results/figures/australia_macro_story/
```

## Fixture Notes

- offline daily rates come from `fred_rates_daily`
- offline VIX comes from `fred_financial_stress_daily`
- offline monthly macro data comes from `fred_macro_monthly`
- offline S&P 500 data comes from `fred_sp500_daily`
- fixture and live modes both use the same direct FRED `SP500` series definition
