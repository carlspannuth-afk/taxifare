include .env

GCP_IMAGE = $(GCP_REGION)-docker.pkg.dev/$(GCP_PROJECT)/$(ARTIFACT_REPO)/$(IMAGE_NAME):latest

run-api:
	uv run uvicorn api.fast:app --reload --port 8000

build-docker-local:
	docker build -t $(IMAGE_NAME) .

docker-run:
	docker run --rm -p $(PORT):$(PORT) --env-file .env $(IMAGE_NAME)

build-docker-cloud:
	docker build --platform linux/amd64 -t $(GCP_IMAGE) .

push-docker:
	docker push $(GCP_IMAGE)

deploy:
	gcloud run deploy $(SERVICE_NAME) --image $(GCP_IMAGE) --region $(GCP_REGION) --project $(GCP_PROJECT) --port $(PORT) --allow-unauthenticated
