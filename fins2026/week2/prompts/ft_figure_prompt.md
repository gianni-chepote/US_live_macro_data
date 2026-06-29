# Prompt: Create FT-Style Figures From My Dataframe

Use this prompt in PyCharm when you have a dataframe named `df`.

```text
I have a pandas dataframe called df. Please inspect the columns, data types,
sample period, missing values, likely units, and likely data frequency first.

Then propose a compact FT-style figure pack. Do not default to plotting every
series in levels. Explicitly decide whether each candidate figure should use:
- levels
- basis-point changes
- changes in rates shown with `%` in visible chart text
- percent changes
- log changes
- cumulative returns

Use the repo's fintools.figures helpers where possible, and build a compact
publication-quality suite with clear titles, units, sample periods, and caption
context.

Use:

create_figure_suite(
    df,
    style="ft",
    output="fins2026/week2/results/figures/style_gallery",
    docx=True,
    narrative=True,
)

If the automatic suite is weak, replace the weak charts with better custom
figures. Prefer subplot layouts, indexed plots, scatter plots, or ranking plots
when they tell the story better than another basic line chart. Keep titles
short, keep legends off the data, and use distinct colors for each forecast
model or comparison series. If several evaluation metrics matter, prefer a
small-multiples scorecard instead of one bar chart with lots of text pasted
next to the bars. In multi-panel layouts, leave enough gap between panels that
subplot titles never crash into adjacent tick labels. In stacked scorecards,
pad the titles and increase row spacing until lower-row titles sit clearly
below the upper-row x-axis labels. Reserve explicit bottom margin for source
notes so they never overlap the lowest tick labels. If different subplots show
different groups of lines, give each subplot its own legend or use globally
unique colors; never reuse colors across panels and then dump all names into
one combined legend. On single-series charts, usually drop the legend
altogether; if you keep one, it must use a proper display label and never a
raw code or dataframe column name. For threshold/event charts, prefer compact
threshold labels like `Return > |10%|` rather than vague prose.
For dense drawdown comparisons, use thinner lines and moderate alpha so all
series stay visible. On efficient-frontier charts, use clear offsets or
leader lines so labels for risk-free, equal-weight, minimum-variance, and
tangency portfolios never collide. If a portfolio-weight figure needs to show
the actual signed weights across many assets, prefer panel-per-portfolio
diverging bar charts over a heatmap. In multi-panel scorecards with the same
categories repeated, usually show the category labels only on the left panels
and suppress redundant labels on the right if they create clutter. End-value
labels on bars must stay clear of category labels and panel boundaries. For
dense category charts with many labels, reduce category-label and panel-title
font sizes before accepting crowding. If there are dozens of category labels on
one axis, bias toward visibly smaller text rather than leaving stacked or
overlapping glyphs.
```

For the Week 2 live FRED exercise, load the dataframe first:

```python
from pathlib import Path

import pandas as pd

df = pd.read_csv(
    Path("fins2026/week2/results/data/fred_market_macro.csv"),
    parse_dates=["date"],
)
```

For the Week 2 market-and-macro narrative pack, default to the frozen
`2015-01-01` through `2025-12-31` lecture sample and move onto month-end merged
views when that improves the comparison. Switch only if the user explicitly
wants a rolling updated FRED window.
