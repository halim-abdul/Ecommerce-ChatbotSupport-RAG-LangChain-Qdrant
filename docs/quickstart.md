# Quickstart

1. Copy `.env.example` to `.env` and set the model key.
2. Run `docker compose up --build`.
3. Ingest support documents.
4. Verify Qdrant collection contents.
5. Send a question to `POST /v1/chat`.
6. Run `pytest -q` and the evaluation script before deployment.
