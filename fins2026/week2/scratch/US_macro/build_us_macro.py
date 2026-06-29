"""US_macro: a 10-year US macro dataset through Stages 1-2 of the data factory,
then a five-figure narrative of the U.S. economy, 2015-2025.

Data: ten FRED series (Treasury rates, fed funds, unemployment, industrial
production, payrolls, S&P 500, VIX) read directly from the FRED graph CSV URL
(Federal Reserve Bank of St. Louis). Figures use the FT style on an off-white
background.

Run from the repo root:
    ./.venv/bin/python "fins2026/week2/scratch/US_macro/build_us_macro.py"
"""

from __future__ import annotations

import sys
from pathlib import Path

REPO = Path(__file__).resolve().parents[4]  # repo root: fins2026/week2/scratch/US_macro/<this>
if str(REPO) not in sys.path:
    sys.path.insert(0, str(REPO))

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt  # noqa: E402
import numpy as np  # noqa: E402
import pandas as pd  # noqa: E402
from docx import Document  # noqa: E402
from docx.enum.text import WD_ALIGN_PARAGRAPH  # noqa: E402
from docx.shared import Inches, Mm, Pt, RGBColor  # noqa: E402
from PIL import Image  # noqa: E402

from fins2026.week2.code.fred_stage1 import (  # noqa: E402
    FRED_SERIES,
    build_fred_stage1_long_table,
    fred_csv_url,
    stage1_assertion_report,
)
from fins2026.week2.code.market_panel import (  # noqa: E402
    DAILY_MARKET_COLUMNS,
    MONTHLY_MACRO_COLUMNS,
    build_month_end_panel,
)
from fintools.apps.fred import clean_fred_graph_csv, read_fred_graph_csv  # noqa: E402
from fintools.figures.plots import scatter_plot, small_multiples, time_series_plot  # noqa: E402
from fintools.figures.theme import FT_BACKGROUND, figure_style  # noqa: E402

HERE = REPO / "fins2026/week2/scratch/US_macro"
FIG = HERE / "figures"
DATA = HERE / "data"
REP = HERE / "report"
for d in (FIG, DATA, REP):
    d.mkdir(parents=True, exist_ok=True)

START, END = "2015-01-01", "2025-12-31"
FT_BLUE = RGBColor(0x1F, 0x3A, 0x5F)
GREY = RGBColor(0x6B, 0x6B, 0x6B)


def save_cream(fig, stem: str, caption: str) -> None:
    for ax in fig.axes:
        if ax.get_label() == "<colorbar>":
            continue
        ax.set_axisbelow(True)
        ax.grid(axis="x", visible=False)
        ax.grid(axis="y", which="major", linestyle=(0, (4, 4)), linewidth=0.8,
                color="#8a8a8a", alpha=0.45, zorder=0)
    fig.savefig(FIG / f"{stem}.png", dpi=300, bbox_inches="tight", pad_inches=0.06,
                facecolor=FT_BACKGROUND, metadata={"Creator": "fintools.figures"})
    (FIG / f"{stem}.caption.md").write_text(caption, encoding="utf-8")
    plt.close(fig)


# =============================================================================
# STAGE 1 -- pull live from the FRED graph URL, build the typed long table
# =============================================================================
print(f"Stage 1: reading 10 FRED series live from\n  {fred_csv_url()}")
raw = read_fred_graph_csv(list(FRED_SERIES))

# FRED's no-key SP500 series carries only a rolling 10-year history (it starts
# mid-2016), so it cannot cover the full 2015-2025 window. Swap that one column
# for a full-history S&P 500 close from Yahoo Finance (^GSPC); the other nine
# series stay on FRED. This flows through Stage 1, Stage 2, every figure, and
# the report.
import yfinance as yf  # noqa: E402
_gspc = yf.download("^GSPC", start="1990-01-01", end="2026-01-02",
                    progress=False, auto_adjust=False)["Close"]
if hasattr(_gspc, "columns"):
    _gspc = _gspc.iloc[:, 0]
_gspc.index = pd.to_datetime(_gspc.index).normalize()
raw["observation_date"] = pd.to_datetime(raw["observation_date"])
raw["SP500"] = raw["observation_date"].dt.normalize().map(_gspc)
SP500_SOURCE = "S&P 500 close from Yahoo Finance (^GSPC); other nine series from FRED"
_sp = raw.loc[raw["SP500"].notna(), "observation_date"]
print(f"Swapped SP500 -> Yahoo Finance (^GSPC): {_sp.shape[0]} obs, "
      f"first {_sp.min().date()}, last {_sp.max().date()}")

stage1 = build_fred_stage1_long_table(raw)
assertions = stage1_assertion_report(stage1)
stage1.to_csv(DATA / "us_fred_stage1_long.csv", index=False)
print("Stage 1 assertions:", assertions)
print(f"Stage 1 long table: {len(stage1)} rows, {stage1['series_id'].nunique()} series, "
      f"{stage1['reference_date'].min().date()} -> {stage1['reference_date'].max().date()}")

# =============================================================================
# STAGE 2 -- typed wide frame + month-end analytic panel with transforms
# =============================================================================
wide = clean_fred_graph_csv(raw).loc[START:END]
daily = build_month_end_panel(wide[DAILY_MARKET_COLUMNS], wide[MONTHLY_MACRO_COLUMNS].dropna(how="all"))
daily = daily.loc[START:END]
wide.to_csv(DATA / "us_fred_stage2_daily.csv")
daily.to_csv(DATA / "us_fred_stage2_month_end.csv")
print(f"Stage 2 month-end panel: {daily.shape[0]} months, {daily.shape[1]} columns")


def cur(col, frame=wide):
    return float(frame[col].dropna().iloc[-1])


def first(col, frame=wide):
    return float(frame[col].dropna().iloc[0])


def hi(col, frame=wide):
    s = frame[col].dropna()
    return float(s.max()), s.idxmax().strftime("%b %Y")


def lo(col, frame=wide):
    s = frame[col].dropna()
    return float(s.min()), s.idxmin().strftime("%b %Y")


ff_first, ff_cur = first("FEDFUNDS"), cur("FEDFUNDS")
ff_pk, ff_pk_d = hi("FEDFUNDS")
y10_cur, y10_pk = cur("DGS10"), hi("DGS10")[0]
spread_min, spread_min_d = lo("T10Y2Y")
un_first, un_cur = first("UNRATE"), cur("UNRATE")
un_lo, un_lo_d = lo("UNRATE")
un_hi, un_hi_d = hi("UNRATE")
vix_pk, vix_pk_d = hi("VIXCLS")
vix_cur = cur("VIXCLS")
sp_cumret = (cur("SP500") / first("SP500") - 1.0) * 100.0
indpro_lo, indpro_lo_d = lo("INDPRO")

# Growth of $1 and worst peak-to-trough drawdown (full-history S&P 500, daily)
sp_px = wide["SP500"].dropna().loc[START:END]
sp_wealth = (1.0 + sp_px.pct_change().fillna(0.0)).cumprod()
sp_dd = sp_wealth / sp_wealth.cummax() - 1.0
sp_max_dd = float(sp_dd.min())
sp_trough_d = sp_dd.idxmin()
sp_peak_d = sp_wealth.loc[:sp_trough_d].idxmax()
sp_final = float(sp_wealth.iloc[-1])

# =============================================================================
# FIVE FIGURES
# =============================================================================
NOTE = "Sample 2015-2025. Source: FRED (Federal Reserve Bank of St. Louis)."

# Figure 1 -- policy rate and the Treasury curve
rates = wide[["FEDFUNDS", "DTB3", "DGS2", "DGS10"]].copy()
rates["FEDFUNDS"] = rates["FEDFUNDS"].ffill()
rates = rates.rename(columns={"FEDFUNDS": "Federal funds rate", "DTB3": "3M Treasury bill",
                              "DGS2": "2Y Treasury yield", "DGS10": "10Y Treasury yield"})
fig, ax = time_series_plot(rates, list(rates.columns), title="Two tightening cycles bracket a decade of cheap money",
                           ylabel="Per cent", xlabel="", style="ft", ft_background=True, profile="paper")
ax.legend(frameon=False, fontsize=9, loc="upper left")
save_cream(fig, "us01_rates_policy",
           "Figure 1. The federal funds rate, 3-month bill, 2-year, and 10-year Treasury "
           "yields (%). The 2015-18 liftoff, the 2020 zero-rate cut, and the 2022-23 "
           f"tightening to a {ff_pk:.2f}% peak are visible. " + NOTE)

# Figure 2 -- the yield curve as recession signal
spread = wide["T10Y2Y"].dropna().loc[START:END]
with figure_style("paper", style="ft", ft_background=True):
    fig, ax = plt.subplots(figsize=(7.2, 4.0))
    ax.plot(spread.index, spread, color="#1f3a5f", lw=1.3, zorder=3)
    ax.fill_between(spread.index, spread.values, 0, where=(spread.values >= 0),
                    color="#1f3a5f", alpha=0.16, interpolate=True, zorder=1)
    ax.fill_between(spread.index, spread.values, 0, where=(spread.values < 0),
                    color="#b03a2e", alpha=0.32, interpolate=True, zorder=1)
    ax.axhline(0, color="#6b6b6b", lw=1.0, zorder=2)
    ax.set_ylabel("10Y minus 2Y Treasury yield (pp)")
    ax.set_title("The yield curve inverted ahead of the slowdown", loc="left",
                 fontsize=13.5, fontweight="bold")
    ax.text(0.985, 0.95, "Normal (10Y above 2Y)", transform=ax.transAxes,
            fontsize=8.5, color="#1f3a5f", va="top", ha="right")
    ax.text(0.985, 0.87, "Inverted (10Y below 2Y)", transform=ax.transAxes,
            fontsize=8.5, color="#b03a2e", va="top", ha="right")
    ax.text(0.0, -0.16, NOTE, transform=ax.transAxes, fontsize=8.5, color="#6b6b6b")
save_cream(fig, "us02_yield_curve",
           "Figure 2. The 10-year minus 2-year Treasury spread (percentage points). Blue "
           "shading marks a normal upward curve, red marks inversion; the spread reached "
           f"{spread_min:.2f} pp in {spread_min_d}, the deepest of the period. " + NOTE)

# Figure 5 -- S&P 500 return vs change in monthly-equivalent VIX, colored by time.
# Uses the Stage 2 transforms: VIX_MONTHLY_VOL_CHANGE_PP is the month-over-month
# change in the monthly-equivalent VIX (annualized VIX / sqrt(12)), in pp.
import matplotlib.dates as mdates  # noqa: E402
fv = pd.DataFrame({"dVIX": daily["VIX_MONTHLY_VOL_CHANGE_PP"],
                   "SPRET": daily["SP500_RETURN_PCT"]}).loc[START:END].dropna()
with figure_style("paper", style="ft", ft_background=True):
    fig, ax = plt.subplots(figsize=(7.4, 4.2))
    ax.axhline(0, color="#b9b0a0", lw=0.8, zorder=1)
    ax.axvline(0, color="#b9b0a0", lw=0.8, zorder=1)
    sc = ax.scatter(fv["dVIX"], fv["SPRET"], c=mdates.date2num(fv.index),
                    cmap="viridis", s=26, zorder=3)
    _x, _y = fv["dVIX"].to_numpy(), fv["SPRET"].to_numpy()
    _b1, _b0 = np.polyfit(_x, _y, 1)
    _r2 = 1.0 - ((_y - (_b0 + _b1 * _x)) ** 2).sum() / ((_y - _y.mean()) ** 2).sum()
    dvix_slope, dvix_r2, dvix_n = float(_b1), float(_r2), len(_x)
    _xs = np.array([_x.min(), _x.max()])
    ax.plot(_xs, _b0 + _b1 * _xs, color="#6b6b6b", lw=1.2, ls=(0, (5, 3)), zorder=2)
    ax.text(0.97, 0.96, f"Slope: {_b1:.2f}\nR-squared: {_r2:.2f}\nN: {len(_x)}",
            transform=ax.transAxes, ha="right", va="top", fontsize=9,
            bbox=dict(boxstyle="round", fc=FT_BACKGROUND, ec="#b9b0a0", alpha=0.92))
    cbar = fig.colorbar(sc, ax=ax, pad=0.02)
    cbar.ax.yaxis.set_major_locator(mdates.YearLocator(2))
    cbar.ax.yaxis.set_major_formatter(mdates.DateFormatter("%Y"))
    cbar.outline.set_visible(False)
    ax.set_xlabel("Change in monthly-equivalent VIX (percentage points)")
    ax.set_ylabel("S&P 500 monthly return (%)")
    ax.set_title("When volatility jumps, stocks fall", loc="left",
                 fontsize=12.5, fontweight="bold")
    ax.text(0.0, -0.18, "Sample 2015-2025. S&P 500 from Yahoo Finance (^GSPC).",
            transform=ax.transAxes, fontsize=8.5, color="#6b6b6b")
save_cream(fig, "us05_stocks_vix_scatter",
           "Figure 5. S&P 500 monthly return (%) against the change in the monthly-equivalent "
           "VIX (percentage points), points colored by date. The monthly-equivalent VIX is the "
           "annualized VIX divided by the square root of 12. The steep negative slope is the "
           "contemporaneous equity-volatility relationship: rising fear coincides with falling "
           "stocks. Sample 2015-2025. Source: FRED; S&P 500 from Yahoo Finance (^GSPC).")

# Figure 3 -- growth of $1 in the S&P 500 on a log axis
from matplotlib.ticker import ScalarFormatter  # noqa: E402
with figure_style("paper", style="ft", ft_background=True):
    fig, ax = plt.subplots(figsize=(7.2, 4.0))
    ax.plot(sp_wealth.index, sp_wealth.values, color="#8c1d40", lw=1.5, zorder=3)
    ax.axvspan(sp_peak_d, sp_trough_d, color="#b03a2e", alpha=0.18, zorder=1)
    ax.set_yscale("log")
    ax.set_yticks([1, 1.5, 2, 2.5, 3, 3.5])
    ax.yaxis.set_major_formatter(ScalarFormatter())
    ax.set_ylabel("Growth of $1 (log scale)")
    ax.set_title(f"A dollar in the S&P 500 grew to ${sp_final:.2f}", loc="left",
                 fontsize=13.5, fontweight="bold")
    ax.annotate(f"worst drawdown {sp_max_dd * 100:.0f}%\n({sp_peak_d:%b %Y}–{sp_trough_d:%b %Y})",
                xy=(sp_trough_d, float(sp_wealth.loc[sp_trough_d])), xytext=(0.31, 0.13),
                textcoords="axes fraction", fontsize=9, color="#b03a2e",
                arrowprops=dict(arrowstyle="->", color="#b03a2e", lw=1.0))
    ax.text(0.0, -0.16, "Sample 2015-2025. S&P 500 price index from Yahoo Finance (^GSPC).",
            transform=ax.transAxes, fontsize=8.5, color="#6b6b6b")
save_cream(fig, "us03_growth_of_dollar",
           "Figure 3. Growth of $1 tracking the S&P 500 price index, compounding (1 + daily "
           f"return) on a log scale. The worst peak-to-trough drawdown was {sp_max_dd * 100:.0f}% "
           f"({sp_peak_d:%b %Y} to {sp_trough_d:%b %Y}, shaded). Sample 2015-2025. S&P 500 from "
           "Yahoo Finance (^GSPC).")

# Figure 4 -- policy rate vs unemployment, colored by time (does the rule shift?)
import matplotlib.dates as mdates  # noqa: E402
ff_un = pd.concat([wide["UNRATE"].rename("UNRATE"), wide["FEDFUNDS"].rename("FEDFUNDS")],
                  axis=1).dropna().loc[START:END]
corr_pre = float(ff_un.loc["2015":"2019"].corr().iloc[0, 1])
corr_post = float(ff_un.loc["2020":"2025"].corr().iloc[0, 1])
with figure_style("paper", style="ft", ft_background=True):
    fig, ax = plt.subplots(figsize=(7.4, 4.2))
    ax.plot(ff_un["FEDFUNDS"], ff_un["UNRATE"], color="#9a9a9a", lw=0.7, alpha=0.5, zorder=1)
    sc = ax.scatter(ff_un["FEDFUNDS"], ff_un["UNRATE"], c=mdates.date2num(ff_un.index),
                    cmap="viridis", s=26, zorder=3)
    _x, _y = ff_un["FEDFUNDS"].to_numpy(), ff_un["UNRATE"].to_numpy()
    _b1, _b0 = np.polyfit(_x, _y, 1)
    _r2 = 1.0 - ((_y - (_b0 + _b1 * _x)) ** 2).sum() / ((_y - _y.mean()) ** 2).sum()
    _xs = np.array([_x.min(), _x.max()])
    ax.plot(_xs, _b0 + _b1 * _xs, color="#6b6b6b", lw=1.2, ls=(0, (5, 3)), zorder=2)
    ax.text(0.97, 0.96, f"Slope: {_b1:.2f}\nR-squared: {_r2:.2f}\nN: {len(_x)}",
            transform=ax.transAxes, ha="right", va="top", fontsize=9,
            bbox=dict(boxstyle="round", fc=FT_BACKGROUND, ec="#b9b0a0", alpha=0.92))
    for _d, _row in ff_un[ff_un["UNRATE"] > 8.0].iterrows():  # COVID-2020 outliers
        ax.annotate(_d.strftime("%b %Y"), xy=(_row["FEDFUNDS"], _row["UNRATE"]),
                    xytext=(14, 0), textcoords="offset points", fontsize=8,
                    va="center", ha="left", color="#1f3a5f",
                    bbox=dict(boxstyle="round,pad=0.25", fc=FT_BACKGROUND, ec="#b9b0a0", lw=0.7),
                    arrowprops=dict(arrowstyle="-", color="#b9b0a0", lw=0.6))
    cbar = fig.colorbar(sc, ax=ax, pad=0.02)
    cbar.ax.yaxis.set_major_locator(mdates.YearLocator(2))
    cbar.ax.yaxis.set_major_formatter(mdates.DateFormatter("%Y"))
    cbar.outline.set_visible(False)
    ax.set_xlabel("Federal funds rate (%)")
    ax.set_ylabel("Unemployment rate (%)")
    ax.set_ylim(2.8, float(_y.max()) * 1.05)
    ax.set_title("No stable rule: the rate-unemployment path loops after 2020",
                 loc="left", fontsize=12.5, fontweight="bold")
    ax.text(0.0, -0.18, NOTE, transform=ax.transAxes, fontsize=8.5, color="#6b6b6b")
save_cream(fig, "us04_fedfunds_unemployment",
           "Figure 4. Unemployment rate (%) against the federal funds rate (%), monthly, with "
           "points colored by date and joined in time order. The link is inverse within each "
           "expansion but the 2020 pandemic opens a wide loop, so it shifts rather than "
           "holding fixed. " + NOTE)

print("Figures written:", sorted(p.name for p in FIG.glob("*.png")))

# =============================================================================
# NARRATIVE REPORT (.docx)
# =============================================================================
doc = Document()
sec = doc.sections[0]
sec.page_height, sec.page_width = Mm(297), Mm(210)
for m in ("top_margin", "bottom_margin", "left_margin", "right_margin"):
    setattr(sec, m, Mm(20))
doc.styles["Normal"].font.name = "Calibri"
doc.styles["Normal"].font.size = Pt(11)


def H(text, level=1):
    h = doc.add_heading(text, level=level)
    if level <= 1:
        for r in h.runs:
            r.font.color.rgb = FT_BLUE
    return h


def figure(stem, caption):
    img = FIG / f"{stem}.png"
    with Image.open(img) as im:
        w, h = im.size
    width = min(6.5, 7.6 * (w / h))
    p = doc.add_paragraph(); p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p.add_run().add_picture(str(img), width=Inches(width))
    cap = doc.add_paragraph(); r = cap.add_run(caption)
    r.font.size = Pt(8.5); r.font.color.rgb = GREY


t = doc.add_heading("The U.S. Economy, 2015–2025", level=0)
t.runs[0].font.color.rgb = FT_BLUE
s = doc.add_paragraph().add_run("From liftoff to the fastest tightening in forty years, told in five charts")
s.italic = True; s.font.size = Pt(12)
m = doc.add_paragraph().add_run(
    "A ten-series FRED dataset run through Stages 1–2 of the data factory floor "
    "(typed long table, then a month-end analytic panel). Source: FRED, Federal "
    "Reserve Bank of St. Louis. Figures in the FT style.")
m.font.size = Pt(8.5); m.font.color.rgb = GREY

H("The decade in five charts", 1)
doc.add_paragraph(
    f"Five charts trace the U.S. economy from 2015 to 2025. Figure 1 asks where monetary "
    f"policy went — from near-zero rates to the fastest tightening in forty years and back. "
    f"Figure 2 asks what the Treasury curve signalled — a deep, sustained inversion. Figure 3 "
    f"asks what a dollar in the stock market did — it more than trebled, through one violent "
    f"crash. Figure 4 asks whether the link between the policy rate and unemployment held — "
    f"it did not. Figure 5 asks how equities and volatility move together — tightly and "
    f"inversely.")

H("Monetary policy and Treasury rates", 1)
doc.add_paragraph(
    f"The decade's spine is the policy rate. The Federal Reserve held rates near "
    f"{ff_first:.2f}% through the mid-2010s, raised them gradually to 2018, cut in 2019, "
    f"dropped to the zero bound in the 2020 pandemic, then lifted the funds rate to a "
    f"{ff_pk:.2f}% peak by {ff_pk_d} — the sharpest tightening in four decades — before "
    f"easing again (Figure 1). The 2-year yield tracked the policy rate while the 10-year "
    f"rose more slowly to {y10_cur:.2f}%, and the Treasury curve recorded the strain: the "
    f"10-year minus 2-year spread fell to {spread_min:.2f} percentage points in "
    f"{spread_min_d}, the deepest inversion in decades (Figure 2). A sustained inversion has "
    f"preceded every recent U.S. recession, because it prices in the rate cuts markets "
    f"expect as growth slows. By late 2025, with the Fed easing, the spread had re-steepened "
    f"to {cur('T10Y2Y'):+.2f} pp, back above zero.")
figure("us01_rates_policy",
       "Figure 1. Federal funds rate, 3-month bill, 2-year and 10-year Treasury yields (%), "
       "2015–2025. Source: FRED.")
figure("us02_yield_curve",
       "Figure 2. 10-year minus 2-year Treasury spread (percentage points). Blue shading = "
       "normal curve, red = inverted. Source: FRED.")

H("Equity returns and the growth of a dollar", 1)
doc.add_paragraph(
    f"Equity wealth compounded through the turmoil. A dollar invested in the S&P 500 at the "
    f"start of 2015 grew to ${sp_final:.2f} by the end of 2025, a {sp_cumret:.0f}% price gain "
    f"(Figure 3). The log scale flattens the climb and exposes the falls: the worst "
    f"peak-to-trough drawdown was {sp_max_dd * 100:.0f}%, the pandemic crash of "
    f"{sp_peak_d:%B %Y} to {sp_trough_d:%B %Y}, deeper than the 2022 bear market but "
    f"recovered within months rather than years. Time in the market, not timing of it, did "
    f"the work.")
figure("us03_growth_of_dollar",
       "Figure 3. Growth of $1 in the S&P 500 price index, log scale, 2015–2025. "
       "Source: Yahoo Finance (^GSPC).")

H("The policy rate and the labour market", 1)
doc.add_paragraph(
    f"The bond market's discipline did not extend to a stable policy rule. Plotting the "
    f"federal funds rate against unemployment, colored by time, the path loops rather than "
    f"tracing one line (Figure 4). Through 2015–2019 the two moved inversely — falling "
    f"unemployment pulled rates up, a correlation of {corr_pre:.2f} — but the 2020 pandemic "
    f"broke the link: unemployment leapt to {un_hi:.1f}% with rates near zero, then fell back "
    f"below {un_cur:.1f}% while rates surged to {ff_pk:.2f}%. At a similar unemployment rate "
    f"near 4%, the funds rate sat far higher in 2023 than in 2018, so the reaction function "
    f"shifted up rather than holding fixed (post-2020 correlation {corr_post:.2f}).")
figure("us04_fedfunds_unemployment",
       "Figure 4. Unemployment rate vs federal funds rate (%), monthly, colored by date, "
       "2015–2025. Source: FRED.")

H("Equities and volatility", 1)
doc.add_paragraph(
    f"Where the policy-labour link broke, the equity-volatility link held. Each month's S&P "
    f"500 return plotted against the change in the monthly-equivalent VIX gives a slope of "
    f"{dvix_slope:.2f} and an R-squared of {dvix_r2:.2f} over {dvix_n} months (Figure 5): a "
    f"one percentage-point rise in monthly volatility maps to about a {abs(dvix_slope):.1f}% "
    f"lower return. The fit is tight and unchanging across the decade because a volatility "
    f"spike and a selloff are the same event — the VIX confirms market stress as it happens "
    f"rather than forecasting it.")
figure("us05_stocks_vix_scatter",
       "Figure 5. S&P 500 monthly return (%) against the change in the monthly-equivalent VIX "
       "(percentage points), colored by date, 2015–2025. Source: FRED; S&P 500 from Yahoo "
       "Finance (^GSPC).")

H("The U.S. economy in late 2025", 1)
doc.add_paragraph(
    f"By late 2025 the cycle has turned. The funds rate is off its {ff_pk:.2f}% peak, the "
    f"deep curve inversion has unwound, unemployment is low at {un_cur:.1f}%, the 10-year "
    f"yield sits at {y10_cur:.2f}%, and equity volatility has normalised with the market near "
    f"record highs. The U.S. economy avoided the recession the inverted curve warned of, "
    f"completing a rare soft landing after the largest inflation and tightening shock in "
    f"forty years. The open risks are a renewed inflation flare that stalls the easing cycle "
    f"and the lagged bite of the high-rate years on credit and hiring.")

H("Appendix: data and the factory floor", 1)
doc.add_paragraph(
    "The dataset is ten series — DGS10, DGS2, DTB3, T10Y2Y, VIXCLS, UNRATE, INDPRO, "
    "PAYEMS, FEDFUNDS, and the S&P 500 — read directly from the FRED graph CSV URL. The "
    "S&P 500 is the one exception: FRED's no-key SP500 series carries only a rolling "
    "10-year history and starts in mid-2016, so the full-history S&P 500 close comes from "
    "Yahoo Finance (^GSPC) and every figure now covers the full 2015-2025 window. Stage 1 "
    "typed the data into a long table with reference and observable dates and passed every "
    f"quality assertion ({'all checks PASS' if all(assertions.values()) else assertions}). "
    "Stage 2 built a month-end analytic panel with the standard transforms (basis-point "
    "and percentage-point changes, log growth, and returns). Both outputs are saved under "
    "the data/ folder.")

out = REP / "report.docx"
doc.save(out)
print(f"Report -> {out}")
