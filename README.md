# better-uz-plan

Python monorepo workspace for Better UZ Plan.

## Apps

- `apps/api` - FastAPI service for scraping and caching UZ schedule data

## Workspace

This repo is set up as a `uv` workspace so additional apps and shared packages can be added under the same root later.

## Commands

From the repo root:

```bash
uv sync
uv run --package uz-plan-api pytest
uv run --package uz-plan-api uvicorn app.main:app --reload --app-dir apps/api
```
