install:
	pip install -r requirements.txt && pip install -e .

test:
	pytest -q

lint:
	ruff check src tests

serve:
	uvicorn ecommerce_rag.api.app:app --reload

stack:
	docker compose up --build
