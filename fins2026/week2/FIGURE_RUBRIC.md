# Week 2 Figure Rubric

Use this checklist before you call a Week 2 figure finished.

## The Four Standards

Every report-ready figure must have:

1. a self-contained caption
2. axis labels with units
3. a source line
4. an explicit sample window

If a figure loses its slide notes, it should still make sense.

## The Week 2 Judgment Rule

Every figure should answer one question.

Use this sequence:

1. state the question in one sentence
2. choose the evidence: series, transformation, and sample window
3. make the answer visible in the design

If one canvas is trying to answer two questions, split it.

## Design Rules

- Prefer sentence titles over topic titles.
- Prefer direct labels over detached legends when the chart has only a few series.
- Use one emphasis colour and keep the rest muted.
- Use event shading when an episode matters more than a single date marker.
- Keep reader-facing labels readable; hide raw codes and unexplained acronyms.

## Transformation Rules

- Use levels when the level is the question.
- Use basis-point changes for rates.
- Use percentage-point changes for labour-market rates.
- Use log growth for activity levels.
- Use returns for market performance.
- Use indexing when units differ.
- Use growth of `$1` on a log y-axis when the story is compounding.

Do not plot cumulative return on a log y-axis. Plot `(1 + r).cumprod()`, not
`(1 + r).cumprod() - 1`.

## Scatter-Plot Rule

An OLS fit line in Week 2 is a visual aid only.

- Do not treat the slope as causal.
- Do not discuss significance unless the task explicitly becomes econometrics.
- Do not extrapolate from the line.

## Output Rule

If an exported figure is weak, fix the generator, the caption, or the data
alignment. Do not hand-edit the PNG or PDF.
