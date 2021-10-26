from py_workers.config import CeleryConfig
from celery import Celery

celery_app = Celery(
    "app",
    backend=CeleryConfig.CELERY_RESULT_BACKEND,
    broker=CeleryConfig.BROKER_URL,
    include=[
        "py_workers.tasks.example.arithmetic",
    ],
)


# celery_app.conf.task_routes = {'py_workers.tasks.*': {'queue': 'pyqueue'}}
celery_app.conf.task_routes = {"py_workers.tasks.*": {"queue": "pyqueue"}}

if __name__ == "__main__":
    celery_app.start()
