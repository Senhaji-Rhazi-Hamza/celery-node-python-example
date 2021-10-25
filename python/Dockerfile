FROM python:3.8

RUN mkdir /app/

COPY /py_workers /app/py_workers

COPY pyproject.toml app/

COPY scripts/entrypoints/start_worker_pyqueue.sh app/docker-entrypoint.sh

WORKDIR /app

ENV PYTHONPATH=${PYTHONPATH}:${PWD}

RUN pip3 install poetry

RUN poetry config virtualenvs.create false

RUN poetry install --no-dev

CMD [ "bash","./docker-entrypoint.sh" ]
