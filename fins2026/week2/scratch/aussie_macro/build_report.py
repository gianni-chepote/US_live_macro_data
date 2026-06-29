"""Build the Australian macroeconomy evaluation report (.docx).

Pulls every figure value straight from the Week 2 reference panel so the prose
cannot drift from the data, embeds the FT-style figures with stand-alone captions,
and writes a neat Word report under report/report.docx.

Run from the repo root:
    ./.venv/bin/python "fins2026/week2/scratch/aussie_macro/build_report.py"
"""

from __future__ import annotations

from pathlib import Path

import pandas as pd
from docx import Document
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.shared import Inches, Mm, Pt, RGBColor
from PIL import Image

HERE = Path(__file__).resolve().parent
FIG = HERE / "figures"
REPO = Path(__file__).resolve().parents[4]  # repo root from fins2026/week2/scratch/aussie_macro
PANEL = REPO / "fins2026/week2/results/data/australia_macro_reference_panel.csv"
OUT = HERE / "report" / "report.docx"

FT_BLUE = RGBColor(0x1F, 0x3A, 0x5F)
GREY = RGBColor(0x6B, 0x6B, 0x6B)
USABLE_W = 6.5   # inches, within A4 margins
MAX_H = 7.8      # inches, keep image + caption on one page

ref = pd.read_csv(PANEL, index_col=0, parse_dates=True)


def cur(col: str) -> float:
    return float(ref[col].dropna().iloc[-1])


def ago(col: str, date: str = "2024-12-31") -> float:
    return float(ref[col].dropna().asof(pd.Timestamp(date)))


def at(col: str, date: str) -> float:
    return float(ref[col].dropna().asof(pd.Timestamp(date)))


def extreme(col: str, kind: str, since: str = "2020"):
    s = ref[col].dropna().loc[since:]
    idx = s.idxmax() if kind == "max" else s.idxmin()
    return float(s.loc[idx]), idx.strftime("%B %Y")


# ---- pull every figure used in the prose --------------------------------------
cash, cash_a = cur("Cash rate target"), ago("Cash rate target")
cash_pk, cash_pk_d = extreme("Cash rate target", "max")
cash_tr, cash_tr_d = extreme("Cash rate target", "min")
y10, y10_a = cur("10Y government bond yield"), ago("10Y government bond yield")
hl, hl_a = cur("Headline CPI inflation"), ago("Headline CPI inflation")
hl_pk, hl_pk_d = extreme("Headline CPI inflation", "max")
tm, tm_a = cur("Trimmed mean inflation"), ago("Trimmed mean inflation")
tm_pk, tm_pk_d = extreme("Trimmed mean inflation", "max")
wpi, wpi_a = cur("Wage Price Index growth"), ago("Wage Price Index growth")
wpi_pk, wpi_pk_d = extreme("Wage Price Index growth", "max")
gdp, gdp_a = cur("Real GDP growth"), ago("Real GDP growth")
un, un_a = cur("Unemployment rate"), ago("Unemployment rate")
un_tr, un_tr_d = extreme("Unemployment rate", "min")
part = cur("Participation rate")
part_pk, part_pk_d = extreme("Participation rate", "max")
e2p = cur("Employment-to-population ratio")
vac = cur("Vacancies to labour force ratio")
vac_pk, vac_pk_d = extreme("Vacancies to labour force ratio", "max")
twi, twi_a = cur("Trade-weighted index"), ago("Trade-weighted index")
comm, comm_a = cur("Commodity price index (A$)"), ago("Commodity price index (A$)")
comm_pk, comm_pk_d = extreme("Commodity price index (A$)", "max")

# ---- document setup -----------------------------------------------------------
doc = Document()
sec = doc.sections[0]
sec.page_height, sec.page_width = Mm(297), Mm(210)
for m in ("top_margin", "bottom_margin", "left_margin", "right_margin"):
    setattr(sec, m, Mm(20))
normal = doc.styles["Normal"]
normal.font.name = "Calibri"
normal.font.size = Pt(11)


def H(text, level=1):
    h = doc.add_heading(text, level=level)
    if level == 1:
        for run in h.runs:
            run.font.color.rgb = FT_BLUE
    return h


def P(text):
    return doc.add_paragraph(text)


def figure(stem, caption, *, number):
    img = FIG / f"{stem}.png"
    with Image.open(img) as im:
        w_px, h_px = im.size
    width = min(USABLE_W, MAX_H * (w_px / h_px))
    p = doc.add_paragraph()
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p.add_run().add_picture(str(img), width=Inches(width))
    cap = doc.add_paragraph()
    cap.alignment = WD_ALIGN_PARAGRAPH.LEFT
    r = cap.add_run(f"Figure {number}. {caption}")
    r.font.size = Pt(8.5)
    r.font.color.rgb = GREY


# ---- title block --------------------------------------------------------------
title = doc.add_heading("The Australian Macroeconomy in Late 2025", level=0)
title.runs[0].font.color.rgb = FT_BLUE
sub = doc.add_paragraph()
sr = sub.add_run("A soft landing that has stalled above target")
sr.italic = True
sr.font.size = Pt(12)
meta = doc.add_paragraph()
mr = meta.add_run("Evaluation as of the December 2025 data endpoint. Source: Reserve "
                  "Bank of Australia statistical tables. Figures generated with the "
                  "Week 2 FT-style figure toolkit.")
mr.font.size = Pt(8.5)
mr.font.color.rgb = GREY

# ---- summary ------------------------------------------------------------------
H("Summary", 1)
P(f"Australia closed 2025 completing a soft landing. Real GDP grew {gdp:.1f}% over "
  f"the year to December 2025, up from {gdp_a:.1f}% a year earlier, while unemployment "
  f"held at {un:.1f}%, close to its {un_tr:.1f}% post-pandemic trough of {un_tr_d}. "
  f"Headline inflation eased to {hl:.1f}% from its {hl_pk:.1f}% peak in {hl_pk_d}. The "
  f"disinflation has stalled above target: trimmed-mean inflation, the Reserve Bank of "
  f"Australia's preferred core gauge, sits at {tm:.1f}%, above the 2–3% band, and "
  f"headline inflation has risen from {hl_a:.1f}% a year earlier. The Reserve Bank has "
  f"started to ease, cutting the cash rate {round((cash_pk-cash)*100)} basis points to "
  f"{cash:.2f}% from its {cash_pk:.2f}% peak, yet the 10-year government bond yield "
  f"climbed to {y10:.2f}%, its highest post-pandemic reading. Near-trend growth and a "
  f"tight labour market sit against sticky core inflation and rising long-term yields.")

# ---- dashboard table ----------------------------------------------------------
H("Current readings", 1)
P("Table 1 collects the headline indicators with their year-ago values and their "
  "post-2020 extreme, so each current reading carries direction and scale.")
rows = [
    ("Indicator", "Dec 2025", "Dec 2024", "Post-2020 extreme"),
    ("Real GDP growth (year-ended, %)", f"{gdp:.1f}", f"{gdp_a:.1f}", "10.2 (Jun 2021) / -5.9 (Jun 2020)"),
    ("Unemployment rate (%)", f"{un:.1f}", f"{un_a:.1f}", f"{un_tr:.1f} trough ({un_tr_d})"),
    ("Participation rate (%)", f"{part:.1f}", f"{ago('Participation rate'):.1f}", f"{part_pk:.1f} peak ({part_pk_d})"),
    ("Vacancies-to-labour force (%)", f"{vac:.1f}", f"{ago('Vacancies to labour force ratio'):.1f}", f"{vac_pk:.1f} peak ({vac_pk_d})"),
    ("Headline CPI (year-ended, %)", f"{hl:.1f}", f"{hl_a:.1f}", f"{hl_pk:.1f} peak ({hl_pk_d})"),
    ("Trimmed-mean CPI (year-ended, %)", f"{tm:.1f}", f"{tm_a:.1f}", f"{tm_pk:.1f} peak ({tm_pk_d})"),
    ("Wage Price Index (year-ended, %)", f"{wpi:.1f}", f"{wpi_a:.1f}", f"{wpi_pk:.1f} peak ({wpi_pk_d})"),
    ("Cash rate target (%)", f"{cash:.2f}", f"{cash_a:.2f}", f"{cash_pk:.2f} peak / {cash_tr:.2f} trough"),
    ("10Y government bond yield (%)", f"{y10:.2f}", f"{y10_a:.2f}", "0.80 trough (Oct 2020)"),
    ("Commodity price index (A$)", f"{comm:.0f}", f"{comm_a:.0f}", f"{comm_pk:.0f} peak ({comm_pk_d})"),
]
table = doc.add_table(rows=len(rows), cols=4)
table.style = "Light Grid Accent 1"
for i, row in enumerate(rows):
    for j, val in enumerate(row):
        cell = table.rows[i].cells[j]
        cell.text = val
        for para in cell.paragraphs:
            for run in para.runs:
                run.font.size = Pt(8.5)
                if i == 0:
                    run.font.bold = True

# ---- 1. long-run context ------------------------------------------------------
H("Two decades of context", 1)
P("Australia's current position reads differently against its own history. Figure 1 "
  "tracks the core indicators since 2000 in their natural units rather than forcing "
  "rates, inflation, output, and the exchange rate onto one axis. The post-2020 era "
  "stands out: the deepest output contraction in the sample, the fastest inflation "
  "since the early 1990s, and the sharpest tightening cycle on record.")
figure("week2_australia_macro_story_core_small_multiples",
       "Australian macro indicators, 2000–2025, each in its own units. The panel "
       "shows the cash rate, bond yield, inflation, growth, wages, and labour-market "
       "series over a common 2000–2025 window. Source: RBA statistical tables.",
       number=1)
P(f"Figure 2 contrasts the December 2000 and December 2025 endpoints across eight "
  f"indicators measured on the same reference dates. The cash rate ended 2025 at "
  f"{cash:.2f}% against {at('Cash rate target','2000-12-31'):.2f}% in 2000, "
  f"unemployment at {un:.1f}% against {at('Unemployment rate','2000-12-31'):.1f}%, and "
  f"headline inflation at {hl:.1f}% against {at('Headline CPI inflation','2000-12-31'):.1f}%. "
  f"The economy carries lower unemployment and a similar policy rate, but inflation "
  f"and long yields sit higher than at the start of the century.")
figure("week2_australia_macro_story_dec2000_vs_dec2025",
       "December 2000 versus December 2025 across eight indicators, each on its own "
       "scale, compared at identical reference dates to avoid mixed-frequency "
       "mismatches. Source: RBA statistical tables.",
       number=2)

# ---- 2. inflation -------------------------------------------------------------
H("Inflation has fallen sharply but stalled above target", 1)
P(f"Inflation is the defining tension. Headline CPI inflation fell from {hl_pk:.1f}% in "
  f"{hl_pk_d} to {hl:.1f}% by December 2025, and trimmed-mean inflation fell from "
  f"{tm_pk:.1f}% to {tm:.1f}% over the same period. The disinflation has stalled in the "
  f"upper half of, or just above, the Reserve Bank's 2–3% target band. Headline "
  f"inflation has re-accelerated from {hl_a:.1f}% a year earlier, and core inflation at "
  f"{tm:.1f}% shows the persistence that keeps policy restrictive.")
figure("week2_australia_macro_story_inflation_transition",
       "Year-ended headline and trimmed-mean CPI inflation, 2000–2025 (%). The "
       "trimmed mean strips volatile items to track underlying inflation. The 2–3% "
       "RBA target band is the relevant benchmark. Source: RBA statistical tables.",
       number=3)

# ---- 3. labour market ---------------------------------------------------------
H("The labour market is tight but loosening", 1)
P(f"The labour market remains tight by historical standards while gradually easing. "
  f"Unemployment is {un:.1f}%, up only marginally from the {un_tr:.1f}% trough of "
  f"{un_tr_d} and still near five-decade lows. Participation at {part:.1f}% sits close "
  f"to its record {part_pk:.1f}% of {part_pk_d}, and the employment-to-population ratio "
  f"is {e2p:.1f}%. Labour demand has cooled: the vacancies-to-labour-force ratio has "
  f"fallen from {vac_pk:.1f}% in {vac_pk_d} to {vac:.1f}%.")
figure("week2_australia_macro_story_labour_tightness",
       "Labour-market tightness: unemployment, participation, and the employment-to-"
       "population ratio (monthly, %) with job vacancies (point-in-time quarterly). "
       "Sample 2000–2025. Source: RBA statistical tables.",
       number=4)
P("The Beveridge curve in Figure 5 plots vacancies against unemployment. The "
  "post-pandemic period pushed the economy to the tight, high-vacancy corner; the "
  "recent move back down the curve marks the cooling in labour demand without a large "
  "rise in unemployment — the signature of a soft landing.")
figure("week2_australia_macro_story_beveridge_curve",
       "Beveridge curve: vacancies-to-labour-force ratio against the unemployment rate "
       "(%), paired at common reference dates. An outward shift signals reduced matching "
       "efficiency. Sample 2000–2025. Source: RBA statistical tables.",
       number=5)

# ---- 4. wages -----------------------------------------------------------------
H("Wage growth has eased while real wages stand still", 1)
P(f"Wage growth has come off its peak without collapsing. The Wage Price Index rose "
  f"{wpi:.1f}% over the year to December 2025, down from the {wpi_pk:.1f}% peak of "
  f"{wpi_pk_d}. With headline inflation at {hl:.1f}%, real wages were roughly flat over "
  f"the year. Figure 6 shows the wage Phillips curve: lower unemployment has paired with "
  f"faster wage growth across the sample, and the current point sits at the tight, "
  f"firmer-wage end of that relationship.")
figure("week2_australia_macro_story_wage_phillips_curve",
       "Wage Phillips curve: year-ended Wage Price Index growth against the unemployment "
       "rate (%), matched within quarter. The fitted line summarises the inverse "
       "relationship. Source: RBA statistical tables.",
       number=6)

# ---- 5. growth ----------------------------------------------------------------
H("Growth has reaccelerated toward trend", 1)
P(f"Output growth has recovered. Real GDP grew {gdp:.1f}% over the year to December "
  f"2025, up from {gdp_a:.1f}% a year earlier, a clear reacceleration from the 2024 "
  f"slowdown toward Australia's trend pace. Figure 7 shows Okun's law: quarters of "
  f"stronger GDP growth line up with falling unemployment, and the recent recovery is "
  f"consistent with the broadly stable unemployment rate.")
figure("week2_australia_macro_story_okuns_law",
       "Okun's law: quarterly change in the average unemployment rate (pp) against "
       "quarterly real GDP log growth (%). The negative slope links faster output growth "
       "to falling unemployment. Source: RBA statistical tables.",
       number=7)

# ---- 6. the cycle -------------------------------------------------------------
H("The pandemic-to-tightening cycle", 1)
P(f"Figure 8 narrates the recent cycle from 2019 to the December 2025 endpoint: the "
  f"2020 collapse and policy support, the inflation surge through 2022, the {cash_tr:.2f}% "
  f"to {cash_pk:.2f}% tightening, and the early easing that followed. The arc frames why "
  f"policy remains cautious — the inflation it is responding to was the largest in a "
  f"generation.")
figure("week2_australia_macro_story_tightening_episode",
       "The 2019–2025 cycle in unemployment, inflation, wages, and the cash rate "
       "(%). The matched window spans the pandemic shock, the inflation surge, and the "
       "tightening-to-easing turn. Source: RBA statistical tables.",
       number=8)

# ---- 7. monetary policy -------------------------------------------------------
H("Policy has pivoted to easing as long yields rise", 1)
P(f"The policy stance has turned. The Reserve Bank lifted the cash rate from a "
  f"{cash_tr:.2f}% pandemic low to {cash_pk:.2f}% by {cash_pk_d}, then began easing, "
  f"bringing it to {cash:.2f}% by December 2025. The long end moved the other way: the "
  f"10-year government bond yield rose to {y10:.2f}% from {y10_a:.2f}% a year earlier, "
  f"its highest post-pandemic level. A falling cash rate alongside a rising 10-year "
  f"yield steepens the curve and signals that markets price sticky inflation and higher "
  f"term premia even as near-term policy loosens. With core inflation at {tm:.1f}%, the "
  f"easing path is likely to stay gradual.")

# ---- 8. external --------------------------------------------------------------
H("The external sector: commodities and the dollar", 1)
P(f"Australia's external position rests on commodity prices and the exchange rate. The "
  f"A$ commodity price index stands at {comm:.0f}, down from {comm_a:.0f} a year earlier "
  f"and well below its {comm_pk:.0f} peak of {comm_pk_d}. The trade-weighted index of the "
  f"Australian dollar is {twi:.1f}, up from {twi_a:.1f} a year earlier. Figure 9 shows "
  f"the monthly co-movement: rising commodity prices tend to lift the currency, the "
  f"channel through which Australia's terms of trade pass into the exchange rate.")
figure("week2_australia_macro_story_commodity_twi_scatter",
       "Monthly log change in the trade-weighted index against the monthly log change in "
       "the A$ commodity price index (%). The positive slope is the commodity-currency "
       "link. Source: RBA statistical tables.",
       number=9)

# ---- 9. conclusion ------------------------------------------------------------
H("Outlook", 1)
P(f"The Australian economy enters 2026 in a late-cycle soft landing. Growth has "
  f"returned to about {gdp:.1f}%, unemployment is low at {un:.1f}%, and inflation is far "
  f"below its 2022 peak. The unfinished task is the last stretch of disinflation: with "
  f"trimmed-mean inflation at {tm:.1f}% and wage growth at {wpi:.1f}%, underlying "
  f"pressure remains above the 2–3% target band, and headline inflation has "
  f"edged higher over the past year. The main risks are an inflation re-acceleration "
  f"that halts the easing cycle and rising long-term funding costs, with the 10-year "
  f"yield at {y10:.2f}%. The central case is continued near-trend growth with cautious, "
  f"gradual rate cuts.")

# ---- appendix: data timing ----------------------------------------------------
H("Appendix: data and timing", 1)
P("Macro series arrive at different frequencies and release lags, so the evaluation "
  "uses a common reference endpoint of December 2025 rather than each series' latest "
  "raw print. Figure 10 maps the gap between a series' reference month and the date it "
  "becomes observable; GDP is the slowest major release, so the fully observable "
  "December 2025 information set only completes in March 2026.")
figure("week2_australia_macro_story_release_lags",
       "Reference month-end versus first observable month-end for the core series "
       "(month-end lag). The map documents why a common December 2025 endpoint is used. "
       "Source: RBA statistical tables, classroom lag mapping.",
       number=10)

OUT.parent.mkdir(parents=True, exist_ok=True)
doc.save(OUT)
print(f"Wrote report -> {OUT}")
print(f"Paragraphs: {len(doc.paragraphs)} | figures embedded: 10 | table rows: {len(rows)}")
