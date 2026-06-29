# crypto_report — Agent Context

## Project
Daily cryptocurrency price panel, five coins, January 2020 to June 2026.
Deliverable: FT-style figures and a Word report for a Senior Partner.

## Coins
ADA, BTC, DOGE, ETH, LINK

## Data Source
`https://openbondassetpricing.com/wp-content/uploads/2026/06/crypto_panel.csv`
Columns: date, ticker, open, high, low, close, usd_volume
2,351 trading days per coin. No missing close prices.

## Folder Layout
```
crypto_report/
├── data/                    # cleaned outputs from analysis.py
│   ├── crypto_prices.parquet
│   ├── crypto_volumes.parquet
│   └── performance_summary.csv
├── code/
│   ├── analysis.py          # data pipeline, metrics, all figures
│   └── build_report.py      # Word report assembly
├── output/
│   └── figures/             # FT-style PNGs (full_width, 6.27 × 3.75 in)
├── report/
│   └── crypto_report.docx   # final deliverable
├── AGENTS.md                # this file — do not edit from outside this subfolder
└── README.md
```

## Run Order
```bash
# from repo root
.venv/bin/python fins2026/week2/scratch/crypto_report/code/analysis.py
.venv/bin/python fins2026/week2/scratch/crypto_report/code/build_report.py
```

## Key Conventions
- Risk-free rate = 0 throughout.
- Annualisation factor = 365 (crypto trades every day).
- Returns: daily simple returns from close prices.
- Figures: FT style (ft_background=True, style="ft"), full_width spec.
- Tables: short column names (≤2 lines), values in %, 3 decimal places.
- Writing: active voice, lead with the finding, no banned words (see repo rules).

## Outputs Produced
| File | Description |
|------|-------------|
| `output/figures/fig_indexed_price.png` | Indexed close prices, base 100 at Jan 2020 |
| `output/figures/fig_cumulative_returns.png` | Cumulative simple returns |
| `output/figures/fig_rolling_vol.png` | 90-day rolling annualised volatility |
| `output/figures/fig_drawdowns.png` | Drawdown series, all coins |
| `output/figures/fig_correlation.png` | Pairwise return correlation heatmap |
| `output/figures/fig_risk_return.png` | Annualised risk–return scatter |
| `report/crypto_report.docx` | Final Word report |

## Change Policy
Edit code only inside this subfolder. Never modify context files outside
`fins2026/week2/scratch/crypto_report/`.
