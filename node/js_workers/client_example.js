import celery from "celery-node";

import celeryConfig from './config.js'

const client = celery.createClient(
  celeryConfig.BROKER_URL,
  celeryConfig.CELERY_RESULT_BACKEND,
  celeryConfig.QUEUE
);

//const task = client.createTask("app.tasks.add");
const task = client.createTask("js_workers.tasks.example.arithmetic.add");
const result = task.applyAsync([1, 2]);
result.get().then(data => {
  console.log(data);
  client.disconnect();
});
