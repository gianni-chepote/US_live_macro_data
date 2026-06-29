# Week 2 Australia Stage 1

This is the student-facing Data Factory Floor Station 1 path for the Australia
macro extension.

The goal is not to jump straight to figures. The goal is to learn how to pull
official data, type it, map its time fields, and save one honest long table
before any merged panel is built.

## Station 1 Goal

Build a long table with these fields:

- `raw_date`
- `reference_date`
- `release_date`
- `observable_month_end`
- `source_table`
- `native_frequency`
- `value`

That output is:

```text
fins2026/week2/results/data/australia_macro_stage1_long.csv
```

## Run The Walkthrough

Live pull:

```powershell
.\.venv\Scripts\python.exe fins2026\week2\scripts\make_australia_stage1_walkthrough.py
```

Offline walkthrough:

```powershell
.\.venv\Scripts\python.exe fins2026\week2\scripts\make_australia_stage1_walkthrough.py --use-fixture
```

## What The Walkthrough Does

1. lists the official RBA source tables used in Week 2
2. shows the series contracts that matter before merging
3. downloads and parses the raw source tables, or loads the frozen fixture
4. builds the typed Stage 1 long table with the Week 2 timing fields
5. runs the Week 2 Stage 1 assertions
6. prints a small timing preview for representative series
7. saves the long table to CSV and Parquet

## The Week 2 Stage 1 Assertions

The walkthrough checks four things explicitly:

1. date fields are typed as datetimes
2. `value` is numeric
3. `reference_date` never exceeds `release_date`
4. there is no duplicate `(series_id, reference_date)` pair

It also checks that every required Australia series appears in the output.

## What Students Should Check

- Does a monthly series use `month_end` reference dating?
- Does a quarterly series use `quarter_end` reference dating?
- Is the `release_date` month-end later than the `reference_date` when publication lags exist?
- Is `observable_month_end` the classroom month-end when we treat the observation as available?
- Are we clipped to the frozen Week 2 common reference endpoint of `2025-12-31`?

## Week 2 Timing Simplification

Week 2 stores a classroom month-end release proxy, not the exact ABS or RBA
publication timestamp.

- `reference_date` is when the economic period happened
- `release_date` is the first classroom month-end when Week 2 treats the
  observation as available
- `observable_month_end` is the same month-end merge key used by the classroom
  information set

Do not move to Stage 2 figures until this long-table logic is clear.
