from celery import Celery
from celery.utils.imports import qualname


celery_app = Celery('app',
                    backend='redis://localhost',
                    broker='redis://localhost',
                    )
# use celery queue if you haven't started your worker with a queue
queue='pyqueue'

my_task = celery_app.signature('py_workers.tasks.example.arithmetic.add')
result = my_task.apply_async(args=[2,2],queue='pyqueue' )
print(result.get())
