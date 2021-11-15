import os

class CeleryConfig:
  APP_NAME = os.environ.get('APP_NAME', 'my_celery_app')
  REDIS_URL = os.environ.get('REDIS_URL', 'redis://localhost:6379/0')
  BROKER_URL = REDIS_URL
  CELERY_RESULT_BACKEND = REDIS_URL
  QUEUE = os.environ.get('PY_QUEUE', 'py-queue')
