# Squeeze Radar — Free One-Click Web App

This repo contains a **single Render service** (backend + static frontend) so you can deploy for free with no coding.

## Deploy on Render (Free)
1. Push these files to a new GitHub repo.
2. Sign in at https://render.com → **New +** → **Blueprint** → connect your repo.
3. Render will detect `render.yaml`. Choose the **Free** plan and click **Deploy**.

The app builds both the API (FastAPI) and the frontend (Vite/React) and starts Uvicorn.

### Configure Tickers
- In Render dashboard → **squeeze-app** → **Environment** → add/update `TICKERS` (comma-separated list, e.g. `TSLA,AMD,GME,IONQ`), then **Save** and **Deploy**.

## What it does
- Fetches **1‑minute Yahoo Finance** data for each ticker.
- Computes a **squeeze** (BB inside KC + volume expansion + MACD > signal).
- Saves latest boolean per symbol.
- Frontend lists all tickers and shows **YES/NO**.
- Click **Refresh now** (or wait 5 minutes auto-refresh) to re-scan.

## Endpoints
- `GET /api/health`
- `GET /api/symbols`
- `GET /api/signals`
- `POST /api/refresh`

## Local dev (optional)
```bash
pip install -r requirements.txt
(cd frontend && npm ci && npm run build)
uvicorn backend.main:app --reload
```
Then open http://127.0.0.1:8000
