# Prompt: Build Or Fix The Week 2 Australia Macro Pipeline

Use this prompt when you want Codex to help with the Australia macro extension
for Week 2.

## Prompt Template

```text
Load Week 2 context first:

1. fins2026/week2/AGENTS.md
2. fins2026/week2/README.md
3. fins2026/week2/FIGURE_RUBRIC.md
4. fins2026/week2/STAGE1_DDF.md
5. fins2026/week2/DATA_GUIDE.md
6. fins2026/week2/FIGURE_GALLERY.md
7. fins2026/week2/guidance/week-context.md
8. fins2026/week2/guidance/data-context.md
9. fins2026/week2/guidance/output-context.md

Task:
I am working on the Week 2 Australia macro extension.

Please treat this as a Data Factory Floor exercise:

- Station 1: source extraction, dates, cadence mapping, release-lag handling, endpoint freezing, and typed outputs
- Station 2: communication-ready merged panels and figures

Before you change any plotting code, check these things explicitly:

1. What is the reference date for each series?
2. What is the first classroom-observable month-end for each series?
3. Which series are monthly, quarterly, daily, or point-in-time quarterly?
4. Are we using the frozen common reference endpoint of 2025-12-31?
5. Are we using the classroom information set month-end of 2026-03-31 when needed?
6. Are any quarterly series being silently forward-filled in the reference panel?
7. Are the visible labels reader-facing and publication quality?

If the figure is wrong:

- fix the Python generator, the data alignment, and the caption/context
- do not hand-edit the exported PNG or PDF
- regenerate the outputs in results/data/ and results/figures/australia_macro_story/
- refresh guidance/ if the workflow or outputs changed materially

Current problem:
[describe the bug, weak figure, or data-alignment issue here]
```

Use the exact Week 2 timing fields when they exist:

- `reference_date`
- `release_date`
- `observable_month_end`

In the Week 2 repo, `release_date` is a classroom month-end release proxy, not
an exact ABS or RBA publication timestamp.

## When To Use It

- the Australia figure looks wrong or messy
- a scatter uses the wrong frequency pairing
- the endpoint comparison uses inconsistent dates
- an RBA series is being merged before it would have been observable
- a visible label leaks a raw code, unclear acronym, or bad unit
