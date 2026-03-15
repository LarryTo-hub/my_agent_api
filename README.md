# AlgoRhythm - Content Creator Assistant

A FastAPI app wrapping a LangGraph-powered AI agent that helps content creators plan posts, choose hashtags, and identify trending topics.

## Endpoints

| Method | Path | Description |
|---|---|---|
| `GET` | `/health` | Health check — returns `{"status": "ok"}` |
| `POST` | `/chat` | Send a message, get an AI response |
| `GET` | `/ui` | Chat UI in the browser |

## Tools

- **get_trending_topics** — returns trending topics for a given platform
- **get_content_ideas** — returns content format ideas for a given niche

## Local Setup

```bash
pip install -r requirements.txt
```

Create a `.env` file with:

```
GOOGLE_API_KEY=your_key_here
LANGSMITH_API_KEY=your_key_here
LANGSMITH_TRACING=true
LANGSMITH_PROJECT=deployment_practice
```

Run locally:

```bash
uvicorn app.main:app --host 0.0.0.0 --port 8000
```

Then open [http://localhost:8000/ui](http://localhost:8000/ui)

## Deployment (Render)

- **Build Command:** `pip install -r requirements.txt`
- **Start Command:** `uvicorn app.main:app --host 0.0.0.0 --port 8000`
- Set `GOOGLE_API_KEY`, `LANGSMITH_API_KEY`, `LANGSMITH_TRACING`, and `LANGSMITH_PROJECT` as environment variables in the Render dashboard.
