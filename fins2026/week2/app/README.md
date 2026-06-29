# U.S. Month-End Market and Macro App

This app tracks U.S. rates, labour, activity, policy, volatility, and equity
market measures from a unified month-end panel built from public FRED data. It
keeps the product focused: sample daily market data at month-end, align monthly
macro releases to the same calendar endpoint, choose one series, choose a
comparison window, and inspect the time series cleanly.

Run locally from the repo root:

```bash
streamlit run fins2026/week2/app/streamlit_app.py
```

Default mode uses frozen validation fixtures. Live mode pulls a no-key FRED
graph CSV. If live FRED is unavailable, the app falls back to the fixture.

What this app does:

- choose fixture or live FRED data
- resample daily market data to month-end
- align monthly macro series to month-end
- merge those columns into one month-end panel
- keep the merged panel on the latest 10 years
- choose one level, change, growth, or return series
- change the sample window
- plot one clean time-series chart
- inspect and download the displayed data

Product design choices:

- daily market series are sampled at month-end before comparison
- monthly macro releases are aligned to the same endpoint
- the panel supports levels, changes, growth rates, and returns rather than
  forcing every series into one scale

Examples now included in the app:

- rate levels
- rate changes in bp
- unemployment changes in pp
- industrial-production and payroll log growth
- S&P 500 return, log return, and cumulative return

What this app does not do:

- no stress score
- no yield-curve interpretation layer
- no forecasts
- no backtests
- no GDP view

Those extensions move to Week 3.

Before deployment, run from the repo root:

```bash
python tools/workflow.py check-app-submission --target fins2026/week2 --entrypoint fins2026/week2/app/streamlit_app.py
```
