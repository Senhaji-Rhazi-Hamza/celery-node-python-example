PY_MAKEFILE_PATH := $(abspath $(lastword $(MAKEFILE_LIST)))
PY_MAKEFILE_DIR := $(dir $(PY_MAKEFILE_PATH))

build-py-worker: ## building docker image for python worker
	docker build -f ${PY_MAKEFILE_DIR}Dockerfile -t py_worker  ${PY_MAKEFILE_DIR}

run-py-worker-standalone-docker: build-py-worker  ## runing the py worker in a standalone docker container (network mapped with localhost)
	docker run -it --network="host" py_worker