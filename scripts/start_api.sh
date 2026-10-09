#!/usr/bin/env bash
set -euo pipefail
exec uvicorn ecommerce_rag.api.app:app --host 0.0.0.0 --port "${PORT:-8000}"
