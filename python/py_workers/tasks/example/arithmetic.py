#arithmetic.py
from py_workers.worker import celery_app


@celery_app.task
def add(x, y):
    return x + y


@celery_app.task
def mul(x, y):
    return x * y
