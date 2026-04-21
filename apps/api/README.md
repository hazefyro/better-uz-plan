# uz-plan-api

FastAPI service for scraping and caching UZ schedule data using Redis.

This app now lives inside the `better-uz-plan` monorepo at `apps/api`.

From the monorepo root you can run:

```bash
uv sync
uv run --package uz-plan-api pytest
uv run --package uz-plan-api uvicorn app.main:app --reload --app-dir apps/api
```
