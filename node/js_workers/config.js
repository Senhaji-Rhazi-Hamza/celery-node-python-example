
const celeryConfig = {
 APP_NAME : 'my_celerey_app',
 REDIS_URL : process.env.REDIS_URL || 'redis://localhost:6379/0',
 BROKER_URL : process.env.BROKER_URL ||  process.env.REDIS_URL || 'redis://localhost:6379/0',
 CELERY_RESULT_BACKEND : process.CELERY_RESULT_BACKEND ||  process.env.REDIS_URL || 'redis://localhost:6379/0',
 QUEUE : process.JS_QUEUE || 'js-queue',
}

export default celeryConfig
