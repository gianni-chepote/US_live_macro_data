# Week 2 FRED Stage 1

This is the student-facing Data Factory Floor Station 1 path for the U.S.
market-and-macro exercise.

The goal is to read the mixed-frequency FRED download, type it, assign timing
fields, and save one honest long table before any merged month-end panel is
built.

## Stage 1 Goal

Build a long table with these fields:

- `raw_date`
- `reference_date`
- `release_date`
- `observable_month_end`
- `series_id`
- `native_frequency`
- `value`

That output is:

```text
fins2026/week2/results/data/fred_market_macro_stage1_long.csv
```

By default the walkthrough freezes the sample to `2015-01-01` through
`2025-12-31` so the lecture and textbook outputs stay reproducible.

## Run The Walkthrough

Live pull:

```powershell
.\.venv\Scripts\python.exe fins2026\week2\scripts\make_fred_stage1_walkthrough.py
```

Offline walkthrough:

```powershell
.\.venv\Scripts\python.exe fins2026\week2\scripts\make_fred_stage1_walkthrough.py --use-fixture
```

Rolling updated window:

```powershell
.\.venv\Scripts\python.exe fins2026\week2\scripts\make_fred_stage1_walkthrough.py --rolling-window
```

## What The Walkthrough Does

1. reads the public `fredgraph.csv` endpoint used in Week 2
2. shows the ten series contracts and their classroom lag assumptions
3. loads the raw wide table
4. builds the typed Stage 1 long table
5. runs the Week 2 Stage 1 assertions
6. prints a timing preview for daily and monthly series
7. saves the long table to CSV and Parquet

## The Week 2 Stage 1 Assertions

The walkthrough checks four things explicitly:

1. date fields are typed as datetimes
2. `value` is numeric
3. `reference_date` never exceeds `release_date`
4. there is no duplicate `(series_id, reference_date)` pair

It also checks that all ten required Week 2 FRED series appear in the output.

## Week 2 Timing Simplification

Week 2 does not store exact agency publication timestamps for the FRED monthly
series.

- `reference_date` is when the economic period happened
- `release_date` is the first classroom month-end when Week 2 treats the
  observation as available
- `observable_month_end` is the same month-end merge key used by the classroom
  information set

That is a deliberate teaching simplification for the Week 2 merged panel.

## What Students Should Check

- Are the daily series still daily before resampling?
- Are the monthly series stamped to month-end before merging?
- Are we distinguishing raw levels from the transformed plotting variables?
- Are the monthly macro series delayed relative to the daily market series?
- Are we intentionally using the frozen `2015-01-01` through `2025-12-31`
  lecture window, or did we explicitly switch to `--rolling-window`?
