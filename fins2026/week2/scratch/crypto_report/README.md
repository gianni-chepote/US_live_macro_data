# crypto_report

Cryptocurrency investment performance analysis for a Senior Partner briefing.

## What This Produces
A Word report (`report/crypto_report.docx`) covering price dynamics, return
distributions, risk, drawdowns, and correlations across five coins:
**ADA, BTC, DOGE, ETH, LINK** — daily data from January 2020 to June 2026.

## Quick Start

```bash
# Run from repo root
.venv/bin/python fins2026/week2/scratch/crypto_report/code/analysis.py
.venv/bin/python fins2026/week2/scratch/crypto_report/code/build_report.py
```

`analysis.py` downloads the data, computes metrics, and saves six FT-style
figures to `output/figures/`. `build_report.py` assembles those figures and
a performance table into the final Word document.

## Assumptions
- Risk-free rate = 0.
- Annualisation uses 365 trading days (crypto markets run daily).
- Returns are daily simple returns computed from close prices.

## Folder Structure
```
crypto_report/
├── data/           cleaned parquet and summary CSV
├── code/           analysis and report scripts
├── output/figures/ FT-style PNG figures
├── report/         final Word deliverable
├── AGENTS.md       AI context and conventions
└── README.md       this file
```

## Data Source
Open Bond Asset Pricing:
`https://openbondassetpricing.com/wp-content/uploads/2026/06/crypto_panel.csv`
