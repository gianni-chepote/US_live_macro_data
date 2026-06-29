# Week 2 App Deployment Checklist

Use this checklist to rehearse a final project deployment.
For the plain-English full workflow, see
`docs/apps/streamlit/student-quickstart.md`.

## Readiness Command

Run from the repo root:

```bash
python tools/workflow.py check-app-submission --target fins2026/week2 --entrypoint fins2026/week2/app/streamlit_app.py
```

Resolve every blocking issue before deployment or grading.

## Clean Deploy Repository

To prepare a minimal private-repo rehearsal bundle, run from the course repo
root:

```bash
python tools/workflow.py prepare-app-repo --source fins2026/week2 --dest ../week2-month-end-market-macro --repo week2-month-end-market-macro --entrypoint fins2026/week2/app/streamlit_app.py
```

After the private repo is pushed, use `docs/apps/streamlit/finish-deployment.md`
for the Streamlit browser steps.

## Required Deployment Fields

- Public Streamlit app URL: TODO
- GitHub repository URL accessible to the teaching team: TODO
- Branch: `main`
- App entrypoint: `fins2026/week2/app/streamlit_app.py`
- Final commit hash: TODO

## Before Hand-In

- [ ] The latest code is committed and pushed to GitHub.
- [ ] The app runs locally from the repo root with
  `streamlit run fins2026/week2/app/streamlit_app.py`.
- [ ] The Streamlit Community Cloud app loads in an incognito browser.
- [ ] The Streamlit app is public for grading: app list three-dot menu ->
  `Settings` -> `Sharing` -> `Who can view this app` ->
  `This app is public and searchable`.
- [ ] The teaching team can access the GitHub repository if it remains private.
- [ ] No secrets, `.streamlit/secrets.toml`, `.env`, `.venv/`, local absolute
  paths, or private raw data are committed.

A `localhost` URL is not a valid submission. It only works on the student's own
computer while the local Streamlit process is running.
