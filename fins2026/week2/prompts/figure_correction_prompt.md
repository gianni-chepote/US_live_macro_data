# Prompt: Fix A Week 2 Figure From A Screenshot

Use this prompt when an exported Week 2 figure looks wrong, messy, mislabeled,
or weak.

## Attach The Screenshot First

Windows:

1. Open the figure on screen.
2. Press `Win+Shift+S`.
3. Drag over the bad part of the chart.
4. Click into the Codex chat box and press `Alt+V` to paste the snip.
5. If your host uses standard paste instead, use `Ctrl+V`.

macOS:

1. Press `Command+Control+Shift+4`.
2. Drag over the bad part of the chart to copy it to the clipboard.
3. Click into the Codex chat box and press `Command+V`.

## Prompt Template

```text
We are correcting a Week 2 figure.

Read first:
- AGENTS.md
- fins2026/week2/README.md
- fins2026/week2/FIGURE_GALLERY.md
- fins2026/week2/prompts/assistant_starter.md
- fins2026/week2/scripts/make_fred_market_figures.py

Figure folder:
fins2026/week2/results/figures/market_macro_story

Figure stem:
week2_market_macro_story_<name>

I am attaching a screenshot of the current output.

Please:
1. diagnose why the figure is weak or wrong
2. fix the generating Python code, not the exported PNG/PDF directly
3. update captions, notes, prompts, and Week 2 context if the lesson changes
4. regenerate the affected figure outputs
5. run the relevant tests
6. tell me exactly what changed

Correction notes:
- <put your specific comments here>
- <example: y-axis labels are generic and should name each variable>
- <example: the connected scatter is unreadable and should become a clearer chart type>
```

## Good Correction Notes

- name the exact figure stem and output folder
- attach one screenshot per figure when possible
- say what is wrong in plain English
- say what the chart should teach instead
- ask for code, docs, context, and regenerated outputs together

## What To Avoid

- "make it better" with no screenshot or no note
- asking Codex to edit the exported image by hand
- mixing five unrelated figures into one correction pass
