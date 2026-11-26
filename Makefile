include .env

run-api:
	uv run uvicorn api.fast:app --reload --port 8000

build-docker-local:
	docker build -t $(IMAGE_NAME) .

docker-run:
	docker run --rm -p $(PORT):$(PORT) --env-file .env $(IMAGE_NAME)
