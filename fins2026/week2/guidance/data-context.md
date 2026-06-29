# Data Context

## Committed Inputs

- Folder: `fins2026/week2/data`
- Files: 2

### `fins2026/week2/data/australia_macro_stage1_long.csv`
- Size: 588.9 KB
- Shape: 2855 rows x 17 columns
- Columns: `series_id` (str), `display_name` (str), `source_name` (str), `source_table` (str), `native_frequency` (str), `reference_date_rule` (str), `raw_date` (str), `reference_date` (str), ... and 9 more

### `fins2026/week2/data/README.md`
- Size: 2.5 KB
- Type: `.md`

## Generated Data

- Folder: `fins2026/week2/results/data`
- Status: generated locally and not committed by default


## Timing And Alignment Notes

- a U.S. FRED market-and-macro pack for month-end resampling and transformation choice.
- mixed-frequency macro series need explicit reference dates, observable dates, and common-endpoint rules before plotting.
- common reference endpoint: `2025-12-31`.
- common fully observed classroom information set: `2026-03-31`.
- resample daily market data to month-end.
- `app/streamlit_app.py` is the Week 2 month-end plotting app.
- mixed-frequency Australia macro data with explicit release-lag rules.
- one typed long table with `reference_date`, `release_date`, `observable_month_end`, `native_frequency`, units, and source fields.
