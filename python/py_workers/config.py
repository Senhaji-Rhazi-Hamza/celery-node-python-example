import os

class CeleryConfig:
  APP_NAME = os.environ.get('APP_NAME', 'ramify-dev')
  REDIS_URL = os.environ.get('REDIS_URL', 'redis://localhost:6379/0')
  BROKER_URL = REDIS_URL
  CELERY_RESULT_BACKEND = REDIS_URL
