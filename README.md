# Ecommerce-ChatbotSupport-RAG-LangChain-Qdrant

A production-oriented Retrieval-Augmented Generation (RAG) support chatbot for e-commerce using LangChain, Qdrant, FastAPI and LLMs.

## What it includes

- PDF, Markdown, text and product-catalog ingestion
- Cleaning, metadata enrichment, deduplication and chunking
- Hugging Face embeddings and Qdrant vector search
- Dense, MMR and reciprocal-rank-fusion retrieval helpers
- Source-aware prompting and grounded fallback behavior
- E-commerce intents for returns, refunds, shipping, warranty, payment and product questions
- FastAPI service contract with health/chat endpoints
- Offline evaluation for recall, MRR, citations, latency and regressions
- Privacy-safe logging, cost telemetry and failure analysis
- Prompt-injection checks, input validation and rate limiting
- Docker, Compose, CI, tests, runbooks and 25 notebooks

## Architecture

```text
Documents / Catalog
      │
      ▼
Load → Clean → Metadata → Chunk → Embed
                                │
                                ▼
                           Qdrant index
                                │
Customer question → Intent → Retrieve → Rerank/Filter
                                │
                                ▼
                      Grounded prompt + LLM
                                │
                                ▼
                  Answer + sources + escalation
```

## Quick start

```bash
cp .env.example .env
docker compose up --build
```

Then open `http://localhost:8000/health`.

## Local Python

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
pip install -e .
pytest -q
uvicorn ecommerce_rag.api.app:app --reload
```

## Repository layout

```text
src/ecommerce_rag/    core application code
data/                 sample product/support/evaluation data
scripts/              ingestion, evaluation and operations helpers
tests/                unit/regression tests
notebooks/            25 focused RAG experiments
docs/                 architecture, evaluation, security and runbooks
.github/workflows/    CI
```

## Production notes

Use authenticated systems for transactional order/payment actions. Treat retrieved documents as untrusted data, enforce tenant filters where needed, avoid logging unnecessary PII, measure retrieval quality before tuning generation, and pin infrastructure/model versions for reproducibility.

## License

Apache License 2.0. See `LICENSE`.
