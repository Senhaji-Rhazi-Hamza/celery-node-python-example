import celery from "celery-node";

import celeryConfig from './config.js'

const jsClient = celery.createClient(
  celeryConfig.BROKER_URL,
  celeryConfig.CELERY_RESULT_BACKEND,
  celeryConfig.QUEUE
);

//const task = jsClient.createTask("app.tasks.add");
const task = jsClient.createTask("js_workers.tasks.example.arithmetic.add");
const result = task.applyAsync([1, 2]);
result.get().then(data => {
  console.log('Result for js-queue queue executed by worker: 1 + 2 = ' + data);
  jsClient.disconnect();
});


const pyClient = celery.createClient(
  celeryConfig.BROKER_URL,
  celeryConfig.CELERY_RESULT_BACKEND,
  'py-queue'
);

//const task = pyClient.createTask("app.tasks.add");
const pyTask = pyClient.createTask("py_workers.tasks.example.arithmetic.add");
const pyResult = pyTask.applyAsync([3, 2]);
pyResult.get().then(data => {
  console.log('Result for py-queue queue executed by python worker: 3 + 2 = ' + data);
  pyClient.disconnect();
});
