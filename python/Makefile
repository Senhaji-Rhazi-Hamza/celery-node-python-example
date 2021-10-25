PY_MAKEFILE_PATH := $(abspath $(lastword $(MAKEFILE_LIST)))
PY_MAKEFILE_DIR := $(dir $(PY_MAKEFILE_PATH))

build-py-worker: ## building docker image for python worker
	docker build -f ${PY_MAKEFILE_DIR}Dockerfile -t py_worker  ${PY_MAKEFILE_DIR}
