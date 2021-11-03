import celery from "celery-node";

import celeryConfig from './config.js'

import {add} from './tasks/example/arithmetic.js'

const worker = celery.createWorker(
  celeryConfig.BROKER_URL,
  celeryConfig.CELERY_RESULT_BACKEND,
  celeryConfig.QUEUE
);

worker.register("js_workers.tasks.example.arithmetic.add", add);
worker.start();
