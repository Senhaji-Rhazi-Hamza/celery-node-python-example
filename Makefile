
MAKEFILE_PATH := $(abspath $(lastword $(MAKEFILE_LIST)))
MAKEFILE_DIR := $(dir $(MAKEFILE_PATH))

include ${MAKEFILE_DIR}/python/Makefile
include ${MAKEFILE_DIR}/node/Makefile

workers_up:  ## docker compose up for workers only
	docker-compose -f ${MAKEFILE_DIR}docker-compose.yml up

workers_down:  ## docker compose down for workers only
	docker-compose -f ${MAKEFILE_DIR}docker-compose.yml down
