"""Build the Word report for the crypto panel analysis.

Reads metrics from data/ and figures from output/figures/.
Produces report/crypto_report.docx.

Run from repo root after analysis.py:
    .venv/bin/python fins2026/week2/scratch/crypto_report/code/build_report.py
"""

from __future__ import annotations

from pathlib import Path

import pandas as pd
from docx import Document
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.oxml.ns import qn
from docx.oxml import OxmlElement
from docx.shared import Inches, Pt, RGBColor

# ── paths ──────────────────────────────────────────────────────────────────
ROOT = Path("fins2026/week2/scratch/crypto_report")
DATA_DIR = ROOT / "data"
FIG_DIR = ROOT / "output" / "figures"
REPORT_PATH = ROOT / "report" / "crypto_report.docx"
REPORT_PATH.parent.mkdir(parents=True, exist_ok=True)

FIG_WIDTH = Inches(6.27)
SAMPLE = "January 2020 – June 2026"
COINS = ["ADA", "BTC", "DOGE", "ETH", "LINK"]

# ── load data ──────────────────────────────────────────────────────────────
summary = pd.read_csv(DATA_DIR / "performance_summary.csv", index_col="Coin")
corr = pd.read_csv(DATA_DIR / "correlation_matrix.csv", index_col="ticker")

# Round for display
s = summary.round(3)
c = corr.round(3)


# ── helpers ────────────────────────────────────────────────────────────────
def _add_fig(doc: Document, stem: str, caption: str) -> None:
    """Insert a PNG figure then a short italic caption paragraph."""
    path = FIG_DIR / f"{stem}.png"
    doc.add_picture(str(path), width=FIG_WIDTH)
    # add_picture inserts into the last paragraph — centre it
    doc.paragraphs[-1].alignment = WD_ALIGN_PARAGRAPH.CENTER
    cap = doc.add_paragraph()
    cap.alignment = WD_ALIGN_PARAGRAPH.CENTER
    run = cap.add_run(caption)
    run.italic = True
    run.font.size = Pt(9)
    run.font.color.rgb = RGBColor(0x4C, 0x4C, 0x4C)
    doc.add_paragraph()  # breathing room


def _add_perf_table(doc: Document, frame: pd.DataFrame) -> None:
    """Insert the performance summary table with short column headers."""
    headers = ["Coin", "Tot Ret (%)", "Ann Ret (%)", "Ann Vol (%)", "Sharpe", "Max DD (%)"]
    data_cols = ["Tot Ret (%)", "Ann Ret (%)", "Ann Vol (%)", "Sharpe", "Max DD (%)"]

    table = doc.add_table(rows=1 + len(frame), cols=len(headers))
    table.style = "Table Grid"

    # header row
    hdr_cells = table.rows[0].cells
    for j, h in enumerate(headers):
        hdr_cells[j].text = h
        hdr_cells[j].paragraphs[0].runs[0].bold = True
        hdr_cells[j].paragraphs[0].alignment = WD_ALIGN_PARAGRAPH.CENTER

    # data rows
    for i, (coin, row) in enumerate(frame.iterrows(), start=1):
        cells = table.rows[i].cells
        cells[0].text = str(coin)
        for j, col in enumerate(data_cols, start=1):
            val = row[col]
            cells[j].text = f"{val:.3f}"
            cells[j].paragraphs[0].alignment = WD_ALIGN_PARAGRAPH.RIGHT

    doc.add_paragraph()


def _add_corr_table(doc: Document, frame: pd.DataFrame) -> None:
    """Insert the correlation matrix table."""
    tickers = list(frame.columns)
    table = doc.add_table(rows=1 + len(tickers), cols=1 + len(tickers))
    table.style = "Table Grid"

    # header row
    table.rows[0].cells[0].text = ""
    for j, t in enumerate(tickers, start=1):
        table.rows[0].cells[j].text = t
        table.rows[0].cells[j].paragraphs[0].runs[0].bold = True
        table.rows[0].cells[j].paragraphs[0].alignment = WD_ALIGN_PARAGRAPH.CENTER

    for i, ticker in enumerate(tickers, start=1):
        table.rows[i].cells[0].text = ticker
        table.rows[i].cells[0].paragraphs[0].runs[0].bold = True
        for j, col in enumerate(tickers, start=1):
            val = frame.loc[ticker, col]
            table.rows[i].cells[j].text = f"{val:.3f}"
            table.rows[i].cells[j].paragraphs[0].alignment = WD_ALIGN_PARAGRAPH.RIGHT

    doc.add_paragraph()


# ── build document ─────────────────────────────────────────────────────────
doc = Document()

# -- page margins (2.54 cm each side)
for section in doc.sections:
    section.top_margin = Inches(1.0)
    section.bottom_margin = Inches(1.0)
    section.left_margin = Inches(1.0)
    section.right_margin = Inches(1.0)

# ── Title ──────────────────────────────────────────────────────────────────
title = doc.add_heading("Cryptocurrency Investment Performance", level=0)
title.alignment = WD_ALIGN_PARAGRAPH.LEFT

sub = doc.add_paragraph(f"Cross-Asset Analysis | {SAMPLE}")
sub.alignment = WD_ALIGN_PARAGRAPH.LEFT
sub.runs[0].font.size = Pt(12)
sub.runs[0].font.color.rgb = RGBColor(0x4C, 0x4C, 0x4C)
doc.add_paragraph()

# ── Executive Summary ──────────────────────────────────────────────────────
doc.add_heading("Executive Summary", level=1)

# Pull best Sharpe
best_sharpe_coin = s["Sharpe"].idxmax()
best_sharpe = s.loc[best_sharpe_coin, "Sharpe"]
best_total_coin = s["Tot Ret (%)"].idxmax()
best_total = s.loc[best_total_coin, "Tot Ret (%)"]
best_ann_ret_coin = s["Ann Ret (%)"].idxmax()

doc.add_paragraph(
    f"Ethereum delivers the best risk-adjusted return across the sample, with a Sharpe ratio "
    f"of {s.loc['ETH', 'Sharpe']:.3f} and annualised volatility of "
    f"{s.loc['ETH', 'Ann Vol (%)']:.1f}%. Bitcoin follows closely at "
    f"{s.loc['BTC', 'Sharpe']:.3f}. Dogecoin generates the highest raw return "
    f"({s.loc['DOGE', 'Tot Ret (%)']:,.0f}%) but at extreme volatility "
    f"({s.loc['DOGE', 'Ann Vol (%)']:.0f}% annualised). All five coins exhibit "
    f"drawdowns exceeding 75%, confirming the cyclical severity that characterises "
    f"crypto markets. Pairwise correlations cluster between 0.35 and 0.82, "
    f"with BTC–ETH the tightest pair (0.819), limiting diversification gains "
    f"within this asset class."
)

# ── 1. Data ────────────────────────────────────────────────────────────────
doc.add_heading("1. Data", level=1)
doc.add_paragraph(
    "The panel covers five cryptocurrencies — ADA (Cardano), BTC (Bitcoin), "
    "DOGE (Dogecoin), ETH (Ethereum), and LINK (Chainlink) — observed daily "
    f"from 1 January 2020 to 9 June 2026 (2,351 trading days per coin). "
    "Close prices are sourced from Open Bond Asset Pricing. The panel is "
    "balanced with no missing observations. We annualise returns and volatility "
    "using a 365-day factor, reflecting continuous crypto trading. The risk-free "
    "rate is set to zero throughout."
)

# ── 2. Price Dynamics ──────────────────────────────────────────────────────
doc.add_heading("2. Price Dynamics", level=1)
doc.add_paragraph(
    "Figure 1 indexes each coin to 100 at the start of the sample. "
    "Dogecoin reaches index levels above 4,000 at its 2021 peak before "
    "collapsing, while Bitcoin and Ethereum show more sustained appreciation. "
    "ADA and LINK track the broader market cycle closely but recover less "
    "strongly after the 2022 downturn."
)
_add_fig(doc, "fig_indexed_price",
         "Figure 1. Indexed close prices, January 2020 = 100. Five coins: ADA, BTC, DOGE, ETH, LINK.")

doc.add_paragraph(
    "Figure 2 shows cumulative simple returns. Dogecoin's trajectory dominates "
    "the chart in raw terms, though the path is volatile. Bitcoin and Ethereum "
    "deliver steadier compounding over the six-year window."
)
_add_fig(doc, "fig_cumulative_returns",
         "Figure 2. Cumulative simple returns, 2020–2026. Each series compounds daily close-to-close returns.")

# ── 3. Performance ────────────────────────────────────────────────────────
doc.add_heading("3. Performance", level=1)
doc.add_paragraph(
    "Table 1 presents annualised metrics for each coin. Dogecoin records the "
    f"highest total return ({s.loc['DOGE', 'Tot Ret (%)']:,.0f}%) but also "
    f"the highest annualised volatility ({s.loc['DOGE', 'Ann Vol (%)']:.0f}%) "
    f"and a Sharpe ratio of {s.loc['DOGE', 'Sharpe']:.3f}. Ethereum leads on "
    f"risk adjustment (Sharpe {s.loc['ETH', 'Sharpe']:.3f}), followed by Bitcoin "
    f"({s.loc['BTC', 'Sharpe']:.3f}). ADA and LINK offer similar annualised returns "
    f"(~74–78%) but with volatility exceeding 100%, yielding the weakest Sharpe "
    "ratios in the set."
)

doc.add_paragraph("Table 1. Annualised performance, 2020–2026. Values in %, 3 decimal places.")
_add_perf_table(doc, s)

# ── 4. Risk & Volatility ──────────────────────────────────────────────────
doc.add_heading("4. Risk and Volatility", level=1)
doc.add_paragraph(
    "Figure 3 plots the 90-day rolling annualised volatility for each coin. "
    "All five coins spike during the March 2020 liquidity shock and again in "
    "mid-2021 and late 2022. Dogecoin's volatility reaches peaks well above "
    "the panel average, consistent with its speculative character. "
    "Bitcoin and Ethereum maintain lower and more stable volatility regimes "
    "relative to the altcoins throughout the sample."
)
_add_fig(doc, "fig_rolling_vol",
         "Figure 3. Rolling 90-day annualised volatility (%). Window: 90 trading days, min 30.")

doc.add_paragraph(
    "Figure 4 shows drawdowns for each coin from their respective rolling peaks. "
    f"All coins suffer drawdowns beyond 75%: Bitcoin reaches a trough of "
    f"{s.loc['BTC', 'Max DD (%)']:.1f}% and Ethereum "
    f"{s.loc['ETH', 'Max DD (%)']:.1f}%. ADA and LINK fall further, exceeding "
    f"90%. The 2022 bear market produces the deepest and most prolonged drawdown "
    "across the panel."
)
_add_fig(doc, "fig_drawdowns",
         "Figure 4. Drawdowns from rolling peak (%). Computed from daily close prices.")

# ── 5. Correlations ───────────────────────────────────────────────────────
doc.add_heading("5. Correlations", level=1)
doc.add_paragraph(
    "Figure 5 and Table 2 show pairwise return correlations. The BTC–ETH pair "
    f"records the highest correlation (0.819), indicating the two largest coins "
    "move closely together. Dogecoin is the least correlated with the rest of "
    "the panel (correlations of 0.35–0.40), reflecting its distinctive "
    "sentiment-driven return profile. ADA, ETH, and LINK form a moderately "
    "correlated group (0.70–0.76). These correlations suggest limited "
    "diversification benefit from holding multiple coins simultaneously."
)
_add_fig(doc, "fig_correlation",
         "Figure 5. Pairwise daily return correlations, 2020–2026. Pearson coefficient.")

doc.add_paragraph("Table 2. Pairwise return correlation matrix. 3 decimal places.")
_add_corr_table(doc, c)

# ── 6. Risk–Return Profile ─────────────────────────────────────────────────
doc.add_heading("6. Risk–Return Profile", level=1)
doc.add_paragraph(
    "Figure 6 plots each coin's annualised return against its annualised "
    "volatility. Bitcoin occupies the most efficient position: moderate "
    "volatility (~60%) with the second-highest Sharpe ratio. Ethereum sits "
    "close to Bitcoin with slightly higher return and volatility. "
    "ADA, LINK, and particularly DOGE shift right along the volatility axis "
    "without commensurate improvement in return per unit of risk, confirming "
    "Bitcoin and Ethereum as the dominant risk-adjusted choices within this panel."
)
_add_fig(doc, "fig_risk_return",
         "Figure 6. Annualised risk–return, 2020–2026. Each point is one coin. RF = 0.")

# ── 7. Conclusion ─────────────────────────────────────────────────────────
doc.add_heading("7. Conclusion", level=1)
doc.add_paragraph(
    "Across the January 2020 to June 2026 sample, Ethereum and Bitcoin offer "
    "the strongest risk-adjusted returns among the five coins examined, with "
    f"Sharpe ratios of {s.loc['ETH', 'Sharpe']:.3f} and "
    f"{s.loc['BTC', 'Sharpe']:.3f} respectively. Dogecoin delivers the highest "
    "raw return but imposes volatility of 187% and a maximum drawdown of 92%, "
    "making it unsuitable as a core holding for most institutional mandates. "
    "High cross-coin correlations — particularly between Bitcoin and Ethereum — "
    "limit within-asset-class diversification. A portfolio weighting towards "
    "Bitcoin and Ethereum, with careful drawdown management, represents the most "
    "defensible allocation given the evidence in this panel."
)

# ── save ───────────────────────────────────────────────────────────────────
doc.save(REPORT_PATH)
print(f"Report saved: {REPORT_PATH}")
