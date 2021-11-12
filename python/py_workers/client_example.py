from celery import Celery
from py_workers.config import CeleryConfig
from celery.utils.imports import qualname

celery_app = Celery(
    main=CeleryConfig.APP_NAME,
    backend=CeleryConfig.CELERY_RESULT_BACKEND,
    broker=CeleryConfig.BROKER_URL,
)
# use celery queue if you haven't started your worker with a queue
py_queue = "py-queue"
js_queue = "js-queue"

my_py_task = celery_app.signature("py_workers.tasks.example.arithmetic.add")
result = my_py_task.apply_async(args=[4, 2], queue=py_queue)
print("Result for py-queue queue executed by python worker : 4 + 2 = " + result.get())

my_js_task = celery_app.signature("js_workers.tasks.example.arithmetic.add")
result = my_js_task.apply_async(args=[2, 2], queue=js_queue)
print("Result for js-queue queue executed by js worker : 2 + 2 = " + result.get())