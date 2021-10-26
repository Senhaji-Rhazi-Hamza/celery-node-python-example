from celery import Celery
from py_workers.config import CeleryConfig
from celery.utils.imports import qualname

celery_app = Celery(    
main=CeleryConfig.CELERY_APP_NAME,
    backend=CeleryConfig.CELERY_RESULT_BACKEND,
    broker=CeleryConfig.BROKER_URL,
                    )
# use celery queue if you haven't started your worker with a queue
queue='pyqueue'

my_task = celery_app.signature('py_workers.tasks.example.arithmetic.add')
result = my_task.apply_async(args=[2,2],queue=queue )
print(result.get())
