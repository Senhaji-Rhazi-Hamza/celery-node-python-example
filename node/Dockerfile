FROM node:14-alpine

RUN mkdir /app/

COPY /js_workers /app/js_workers

COPY /package.json /yarn.lock app/

WORKDIR /app

RUN yarn install

CMD [ "node", "js_workers/worker.js" ]
