JS_MAKEFILE_PATH := $(abspath $(lastword $(MAKEFILE_LIST)))
JS_MAKEFILE_DIR := $(dir $(JS_MAKEFILE_PATH))

build-js-worker: ## building docker image for js worker
	docker build -f ${JS_MAKEFILE_DIR}Dockerfile -t js_worker  ${JS_MAKEFILE_DIR}

run-js-worker-standalone-docker: build-js-worker  ## runing the js worker in a standalone docker container (network mapped with localhost)
	docker run -it --network="host" js_worker