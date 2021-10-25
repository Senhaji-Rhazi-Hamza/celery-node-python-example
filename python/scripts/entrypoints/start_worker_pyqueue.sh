#!/bin/bash

celery -A py_workers.worker worker --loglevel=INFO -Q pyqueue
