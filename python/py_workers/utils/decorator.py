from config import CeleryConfig
from py_workers.main import celery_app


def default_celery_task(fn):
    return celery_app.task(
      bind=True,#will add default argument
    )(fn)

