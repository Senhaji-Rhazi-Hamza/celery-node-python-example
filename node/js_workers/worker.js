import celery from "celery-node";

import celeryConfig from './config.js'

import {add, mul} from './tasks/example/arithmetic.js'

const worker = celery.createWorker(
  celeryConfig.BROKER_URL,
  celeryConfig.CELERY_RESULT_BACKEND,
);

worker.register("js_workers.tasks.example.arithmetic.add", add);
worker.start();
