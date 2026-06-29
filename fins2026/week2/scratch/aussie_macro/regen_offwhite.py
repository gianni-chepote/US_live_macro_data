"""Regenerate the aussie_macro FT figures with an off-white (FT cream) background.

Self-contained: no shared-library edits. It (1) forces ft_background=True on every
plot the Week 2 builder uses, and (2) saves with the cream facecolor, since the
shared save_figure otherwise hard-codes white.

Run from the repo root:
    ./.venv/bin/python "fins2026/week2/scratch/aussie_macro/regen_offwhite.py"
"""

from __future__ import annotations

import functools
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parents[4]  # repo root: fins2026/week2/scratch/aussie_macro/<this>
if str(REPO) not in sys.path:
    sys.path.insert(0, str(REPO))

import fintools.figures.export as fexport  # noqa: E402
from fintools.figures.theme import FT_BACKGROUND  # noqa: E402

# (1) save preserving the cream background (shared save_figure forces white)
def _save_cream(fig, path, *, dpi=300, transparent=False):
    out = Path(path)
    out.parent.mkdir(parents=True, exist_ok=True)
    fig.savefig(out, dpi=dpi, bbox_inches="tight", pad_inches=0.04,
                facecolor=FT_BACKGROUND, transparent=transparent,
                metadata={"Creator": "fintools.figures"})
    return out


fexport.save_figure = _save_cream

import fins2026.week2.scripts.make_australia_macro_figures as mafig  # noqa: E402

# (2a) force ft_background=True on every plot helper the script calls
for _name in ("dumbbell_plot", "scatter_plot", "small_multiples", "time_series_plot"):
    _orig = getattr(mafig, _name)
    setattr(mafig, _name, functools.partial(_orig, ft_background=True))

# (2b) force it on the manual figure_style used by the endpoint-comparison figure
_orig_fs = mafig.figure_style


def _fs(*args, **kwargs):
    kwargs["ft_background"] = True
    return _orig_fs(*args, **kwargs)


mafig.figure_style = _fs


def main() -> int:
    out = REPO / "fins2026/week2/scratch/aussie_macro/figures"
    docx = mafig.build_australia_macro_figures(output=out)
    print(f"Regenerated off-white ({FT_BACKGROUND}) figures -> {out}")
    print(f"Figure pack: {docx}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
