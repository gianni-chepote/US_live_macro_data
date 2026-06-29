# Week 2 App Lab: First Streamlit Plotting App

This lab turns the Week 2 market-and-macro figure workflow into a first
deployable Streamlit app.

The goal is still simple:

- load public data
- resample daily series to month-end
- merge them with monthly macro data
- choose one plotting series
- show one clean time-series chart

What changes in the revised Week 2 version is the teaching emphasis. Students
should see that the plotted series does not always need to be a level.

The app should let a student inspect:

- levels such as `SP500`, `DGS10`, `UNRATE`, and `INDPRO`
- transformed series such as rate changes, unemployment changes, log growth, and returns

For the plain-English path from local app to public hand-in URL, read
`docs/apps/streamlit/student-quickstart.md`.

## Week 2 Rules

- Keep the app small enough to read in one sitting.
- Plot the time series of the data only.
- Teach the month-end resampling and merge step explicitly.
- Teach why a rate move may be plotted in bp, a labor-market move in pp, and an activity series in log growth.
- Keep the figure scripts and the app aligned to the same latest-10-year FRED panel.
- Do not add forecasting, backtests, stress-score construction, or GDP modelling.
- Keep the data source explicit and show whether the app is using a fixture or live refresh.
- Keep the labels student-facing and readable.
- Keep deployment compatibility with `fins2026/week2/app/streamlit_app.py`.

Run from the repo root:

```bash
streamlit run fins2026/week2/app/streamlit_app.py
```

Before deployment, run:

```bash
python tools/workflow.py check-app-submission --target fins2026/week2 --entrypoint fins2026/week2/app/streamlit_app.py
```

To rehearse a clean private deploy repo:

```bash
python tools/workflow.py prepare-app-repo --source fins2026/week2 --dest ../week2-month-end-market-macro --repo week2-month-end-market-macro --entrypoint fins2026/week2/app/streamlit_app.py
```

Then finish the browser deployment with
`docs/apps/streamlit/finish-deployment.md`.
