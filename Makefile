VERSION ?= $(git describe --abbrev=0 --tags)
CI_BUILD_REF ?= $(shell git rev-parse --verify HEAD)
PROJECT_NAME = tweet2text-flax
PYFILES = tweet2text
DOCKER_ID_USER = dbandin
CONTAINER_NAME = ${DOCKER_ID_USER}/${PROJECT_NAME}

clean:
	rm -rf .eggs/ build/ dist/ logs/ *.egg-info/
	-find . -name '__pycache__' -prune -exec rm -rf "{}" \;
	-find . -name '*.pyc' -delete

install:
	pip3 install -r requirements.txt

lint:
	flake8 ${PYFILES}

pytest:
	python3 setup.py test

format:
	yapf -r -i ${PYFILES}

dk-build:
	docker build \
		-t  ${CONTAINER_NAME}:${CI_BUILD_REF} \
		-t  ${CONTAINER_NAME}:latest \
		--build-arg "commit=${CI_BUILD_REF}" \
		.

dk-run:
	docker run \
		-p 5000:5000 \
		-v $$(pwd):/opt/dbandin/${PROJECT_NAME} \
		-d \
		${CONTAINER_NAME}:latest

dk-publish: dk-build
	docker push ${CONTAINER_NAME}:latest
