# Week 2 Beginner Plotting

Start here if you are new to Python plotting.

Week 2 is about building narratives with data. That starts with one small
step: pick one series, put dates on the x-axis, put the variable on the
y-axis, and draw one clean line chart that says something clear.

This beginner path fits the Data Factory Floor framing:

- Station 1: create one tidy synthetic dataset with dates, one ticker, and one
  price column
- Station 2: turn that tidy table into a communication-ready chart

Keep this on-ramp narrow on purpose:

- one synthetic asset
- one `price` series
- one time-series chart
- one clean upgrade from plain Matplotlib to the Week 2 FT-style helper

## The Three Steps

1. Build the synthetic dataset.
2. Plot the same series with plain Matplotlib.
3. Rebuild the same story with `fintools.figures`.

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

## What Each Step Teaches

`make_beginner_synthetic_prices.py`

- creates a deterministic business-day CSV
- writes `date`, `ticker`, and `price`
- gives students a tidy dataframe before they touch plotting code

`make_beginner_simple_time_series.py`

- loads the CSV
- draws one plain Matplotlib line
- adds a title, x-axis label, y-axis label, and a compact sample note

`make_beginner_ft_time_series.py`

- loads the same CSV
- rebuilds the chart with `fintools.figures.time_series_plot`
- exports PNG, PDF, and a caption sidecar so students see the Week 2
  communication-ready path

## Output Paths

Generated dataset:

```text
fins2026/week2/results/data/week2_beginner_synthetic_prices.csv
```

Generated beginner figures:

```text
fins2026/week2/results/figures/beginner_plotting/
```

You should see:

- `week2_beginner_simple_time_series.png`
- `week2_beginner_simple_time_series.pdf`
- `week2_beginner_ft_time_series.png`
- `week2_beginner_ft_time_series.pdf`
- `week2_beginner_ft_time_series.caption.md`

## Teaching Point

Do not rush students into six-panel dashboards, regression lines, or mixed-unit
macro packs before they can explain one simple line chart clearly.

The Week 2 ladder is:

1. build the tidy series
2. draw one clean line
3. explain what the line says
4. only then move to transformations, comparisons, and richer figure packs
