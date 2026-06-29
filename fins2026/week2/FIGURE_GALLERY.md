# Week 2 Figure Gallery

Week 2 has four figure surfaces.

- `results/figures/beginner_plotting/`
  This is the one-series beginner plotting ladder built from synthetic price
  data.
- `results/figures/style_gallery/`
  This is the broad FT-style gallery built from frozen public validation data.
- `results/figures/market_macro_story/`
  This is the curated 10-year FRED market-and-macro narrative pack.
- `results/figures/australia_macro_story/`
  This is the Australia macro lecture extension built around a frozen
  December 2025 common endpoint and an explicit observability lesson.

If you were looking for the GDP comparison plots, they are in the style
gallery, not the live FRED pack.

## Beginner Plotting Surface

The beginner ladder is built by these scripts:

- `scripts/make_beginner_synthetic_prices.py`
- `scripts/make_beginner_simple_time_series.py`
- `scripts/make_beginner_ft_time_series.py`

| Figure | Plot type | Lesson |
| --- | --- | --- |
| Synthetic price CSV | tidy one-series dataframe | Plotting starts with one clean table: `date`, `ticker`, and `price`. |
| Simple beginner time series | plain Matplotlib line chart | Start with one line, readable dates, and explicit axis labels before adding more complexity. |
| FT-style beginner time series | one-line FT-style time series | Rebuild the same story with better export, caption context, and Week 2 figure conventions. |

## Style Gallery

The style gallery is built by `scripts/make_ft_validation_figures.py`. It is a
tour of reusable Week 2 plot styles.

### Time-Series And Compounding

| Figure | Dataset | Plot type | Lesson |
| --- | --- | --- | --- |
| Fama/French factor returns | `ff3_monthly` | multi-line time series | Dense financial series still need readable ticks, legends, and recession shading. |
| Fama/French growth of one dollar | `ff3_monthly` | cumulative return | Compounding often deserves its own chart, not just a return table. |
| Indexed macro activity | `fred_macro_monthly` | indexed time series | Indexing helps when units differ. |
| Treasury rates | `fred_rates_daily` | multi-line rate chart | Long daily samples need sparse ticks and clean layering. |
| Yield spread deviation | `fred_rates_daily` | deviation area | Threshold questions often deserve above/below-reference shading. |

### Distributions, Relationships, And Panels

| Figure | Dataset | Plot type | Lesson |
| --- | --- | --- | --- |
| Federal funds and unemployment | `fred_macro_monthly` | scatter with fit | Use a scatter when you want a relationship, not a path. |
| Market return distribution | `ff3_monthly` | histogram/KDE | Shape matters, not just the mean. |
| Industry correlations | `ff_industry_10_monthly` | heatmap | Correlation matrices are layout problems as much as data problems. |
| Industry small multiples | `ff_industry_10_monthly` | small multiples | Subplots help when one shared axis would obscure the comparison. |
| Value-quintile distributions | `ff25_size_value_monthly` | distribution comparison | Show how groups differ across the full distribution. |

### GDP And World-Bank Comparisons

| Figure | Dataset | Plot type | Lesson |
| --- | --- | --- | --- |
| GDP per capita change | `world_bank_country_panel_annual` | dumbbell | Good for two-period changes with direct labels. |
| GDP share | `world_bank_country_panel_annual` | proportional stacked bar | Useful only when the categories sum to a clear whole. |
| Population, income, and GDP | `world_bank_country_panel_annual` | bubble scatter | Third-variable size must answer a real question. |
| GDP lollipop | `world_bank_gdp_annual` | ranked lollipop | Ranking plots help focus on a few highlighted countries. |
| GDP slope chart | `world_bank_gdp_annual` | slope chart | Endpoint comparisons can be much clearer than long spaghetti charts. |

## Week 2 Market-And-Macro Story Pack

The curated FRED pack is built by `scripts/make_fred_market_figures.py`.

| Figure | Plot type | Lesson |
| --- | --- | --- |
| Treasury yields | multi-line time series | Start with yields when the question is the shape of the term structure. |
| Yield-curve inversions | deviation area | Highlight inversion episodes against zero. |
| Month-end level small multiples | subplots | Mixed-unit level series often need separate panels. |
| Transformation small multiples | subplots | Rate changes, unemployment changes, log growth, and returns belong in different units. |
| Indexed market and activity levels | indexed time series | Compare paths after resampling and merging. |
| Policy rate and unemployment | scatter with fit | Ask a relationship question instead of a path question. |
| Pandemic-to-tightening episode | two-panel time series | When a connected scatter becomes noisy, split the episode into matched time-series panels. |
| VIX shocks and equity returns | scatter with fit | Relate S&P 500 month-end returns to changes in monthly-equivalent VIX. |
| S&P 500 growth of one dollar | log wealth path | Compounding is easier to read on a log-scale wealth chart with dollar ticks. |

## Week 2 Australia Macro Story Pack

The Australia pack is built by `scripts/make_australia_macro_figures.py`.

| Figure | Plot type | Lesson |
| --- | --- | --- |
| Reference date versus observable month-end | lag dumbbell | Mixed-frequency macro work starts with observability, not with plotting. |
| Australia from 2000 to December 2025 | small multiples | Keep each macro series in the unit that answers the question cleanly. |
| December 2000 versus December 2025 | endpoint comparison grid | Use a common reference endpoint instead of a fake synchronized "latest" date. |
| Pandemic to tightening in Australia | matched time-series panels | Narrate the recent cycle with reference-date-aligned panels. |
| Labour tightness needs mixed frequencies | small multiples | Labour indicators do not all share the same cadence or reference-date logic. |
| Wage Phillips curve | scatter with fit | Quarterly wage growth needs a timing-aware unemployment pairing. |
| Okun's law | scatter with fit | GDP growth and unemployment change require explicit quarterly aggregation. |
| Beveridge curve | scatter with fit | Vacancies are a point-in-time quarterly measure, not a monthly flow. |
| Commodity prices and the TWI | scatter with fit | Add one Australia-specific external-sector relationship to the lecture. |
| Quarterly inflation measures over time | two-line time series | Keep the inflation history on a consistent quarterly footing and compare headline with trimmed-mean inflation over the full sample. |

## Output Paths

- beginner plotting ladder: `results/figures/beginner_plotting/`
- style gallery: `results/figures/style_gallery/`
- market-and-macro story pack: `results/figures/market_macro_story/`
- Australia macro story pack: `results/figures/australia_macro_story/`
