"""Crypto panel: data pipeline, metrics, and FT-style figures.

Sample: 2020-01-01 to 2026-06-09. Five coins: ADA, BTC, DOGE, ETH, LINK.
Risk-free rate = 0. Annualisation factor = 365.

Run from repo root:
    .venv/bin/python fins2026/week2/scratch/crypto_report/code/analysis.py
"""

from __future__ import annotations

from pathlib import Path

import matplotlib.pyplot as plt
import matplotlib.ticker as mticker
import numpy as np
import pandas as pd

from fintools.figures import (
    FT_COLORS,
    add_source_note,
    correlation_heatmap,
    cumulative_returns_plot,
    export_word_figure,
    indexed_time_series_plot,
    time_series_plot,
)
from fintools.figures.theme import figure_style

# ── paths ──────────────────────────────────────────────────────────────────
ROOT = Path("fins2026/week2/scratch/crypto_report")
DATA_DIR = ROOT / "data"
FIG_DIR = ROOT / "output" / "figures"

DATA_URL = (
    "https://openbondassetpricing.com/wp-content/uploads/2026/06/crypto_panel.csv"
)

COINS = ["ADA", "BTC", "DOGE", "ETH", "LINK"]
ANN = 365
STYLE = "ft"
FT_BG = True
SOURCE = "Source: Open Bond Asset Pricing. Daily close prices, Jan 2020–Jun 2026. RF = 0."


# ── 1. Load & clean ────────────────────────────────────────────────────────
print("Loading data from web...")
raw = pd.read_csv(DATA_URL, parse_dates=["date"])
raw = raw.sort_values(["ticker", "date"]).reset_index(drop=True)

prices = raw.pivot(index="date", columns="ticker", values="close")[COINS]
volumes = raw.pivot(index="date", columns="ticker", values="usd_volume")[COINS]

print(f"  {len(prices):,} trading days | {prices.shape[1]} coins")
print(f"  {prices.index.min().date()} to {prices.index.max().date()}")
print(f"  Missing close prices: {prices.isna().sum().sum()}")

prices.to_parquet(DATA_DIR / "crypto_prices.parquet")
volumes.to_parquet(DATA_DIR / "crypto_volumes.parquet")


# ── 2. Compute returns & metrics ───────────────────────────────────────────
rets = prices.pct_change().dropna()


def _max_drawdown(ret_series: pd.Series) -> float:
    wealth = (1 + ret_series).cumprod()
    return float((wealth / wealth.cummax() - 1).min() * 100)


ann_ret = rets.mean() * ANN * 100
ann_vol = rets.std() * np.sqrt(ANN) * 100
sharpe = (rets.mean() * ANN) / (rets.std() * np.sqrt(ANN))
total_ret = ((1 + rets).prod() - 1) * 100
max_dd = rets.apply(_max_drawdown)

summary = pd.DataFrame(
    {
        "Tot Ret (%)": total_ret,
        "Ann Ret (%)": ann_ret,
        "Ann Vol (%)": ann_vol,
        "Sharpe": sharpe,
        "Max DD (%)": max_dd,
    }
)
summary.index.name = "Coin"
summary.to_csv(DATA_DIR / "performance_summary.csv")

print("\nPerformance summary:")
print(summary.round(3).to_string())

corr_matrix = rets.corr()
corr_matrix.to_csv(DATA_DIR / "correlation_matrix.csv")

print("\nCorrelation matrix:")
print(corr_matrix.round(3).to_string())


# ── 3. Figures ─────────────────────────────────────────────────────────────
print("\nGenerating figures...")

# Fig 1: Indexed prices (base = 100 at first observation)
fig1, ax1 = indexed_time_series_plot(
    prices,
    y=COINS,
    base=100.0,
    title="Cryptocurrency prices, indexed to 100 at January 2020",
    ylabel="Index (Jan 2020 = 100)",
    style=STYLE,
    ft_background=FT_BG,
    direct_labels=True,
    shade_recessions=False,
)
add_source_note(fig1, SOURCE, style=STYLE)
export_word_figure(fig1, FIG_DIR, "fig_indexed_price", spec="full_width")
plt.close(fig1)
print("  fig_indexed_price.png")

# Fig 2: Cumulative returns
rets_pct = rets * 100
fig2, ax2 = cumulative_returns_plot(
    rets_pct,
    returns=COINS,
    returns_are_percent=True,
    title="Cumulative returns, 2020–2026",
    style=STYLE,
    ft_background=FT_BG,
    direct_labels=True,
)
add_source_note(fig2, SOURCE, style=STYLE)
export_word_figure(fig2, FIG_DIR, "fig_cumulative_returns", spec="full_width")
plt.close(fig2)
print("  fig_cumulative_returns.png")

# Fig 3: Rolling 90-day annualised volatility
rolling_vol = rets.rolling(90, min_periods=30).std() * np.sqrt(ANN) * 100
fig3, ax3 = time_series_plot(
    rolling_vol,
    y=COINS,
    title="Rolling 90-day annualised volatility, 2020–2026",
    ylabel="Volatility (%)",
    shade_recessions=False,
    style=STYLE,
    ft_background=FT_BG,
)
ax3.yaxis.set_major_formatter(mticker.PercentFormatter(xmax=100, decimals=0))
add_source_note(fig3, SOURCE, style=STYLE)
export_word_figure(fig3, FIG_DIR, "fig_rolling_vol", spec="full_width")
plt.close(fig3)
print("  fig_rolling_vol.png")

# Fig 4: Drawdowns (all coins)
drawdowns = pd.DataFrame(index=rets.index)
for coin in COINS:
    wealth = (1 + rets[coin]).cumprod()
    drawdowns[coin] = (wealth / wealth.cummax() - 1) * 100

fig4, ax4 = time_series_plot(
    drawdowns,
    y=COINS,
    title="Drawdowns, 2020–2026",
    ylabel="Drawdown (%)",
    shade_recessions=False,
    style=STYLE,
    ft_background=FT_BG,
)
ax4.yaxis.set_major_formatter(mticker.PercentFormatter(xmax=100, decimals=0))
add_source_note(fig4, SOURCE, style=STYLE)
export_word_figure(fig4, FIG_DIR, "fig_drawdowns", spec="full_width")
plt.close(fig4)
print("  fig_drawdowns.png")

# Fig 5: Pairwise return correlations
fig5, ax5 = correlation_heatmap(
    rets,
    title="Pairwise return correlations, 2020–2026",
    style=STYLE,
    ft_background=FT_BG,
)
add_source_note(fig5, SOURCE, style=STYLE)
export_word_figure(fig5, FIG_DIR, "fig_correlation", spec="full_width")
plt.close(fig5)
print("  fig_correlation.png")

# Fig 6: Annualised risk–return scatter (one point per coin)
_palette = [
    FT_COLORS["maroon"],
    FT_COLORS["blue"],
    FT_COLORS["teal"],
    FT_COLORS["gold"],
    FT_COLORS["green"],
]

with figure_style("paper", style=STYLE, ft_background=FT_BG):
    fig6, ax6 = plt.subplots(figsize=(6.27, 3.75))
    for i, coin in enumerate(COINS):
        x_val = ann_vol[coin]
        y_val = ann_ret[coin]
        ax6.scatter(x_val, y_val, color=_palette[i], s=90, zorder=4)
        ax6.annotate(
            coin,
            (x_val, y_val),
            textcoords="offset points",
            xytext=(6, 3),
            fontsize=9.5,
            color=_palette[i],
        )
    ax6.axhline(0, color=FT_COLORS["axis"], linewidth=0.8, linestyle="--", zorder=2)
    ax6.set_xlabel("Annualised volatility (%)")
    ax6.set_ylabel("Annualised return (%)")
    ax6.set_title("Annualised risk–return, 2020–2026", loc="left")
    ax6.xaxis.set_major_formatter(mticker.PercentFormatter(xmax=100, decimals=0))
    ax6.yaxis.set_major_formatter(mticker.PercentFormatter(xmax=100, decimals=0))
    add_source_note(fig6, SOURCE, style=STYLE)
    export_word_figure(fig6, FIG_DIR, "fig_risk_return", spec="full_width")
    plt.close(fig6)
print("  fig_risk_return.png")

print(f"\nAll figures saved to {FIG_DIR}")
print("Run build_report.py next.")
