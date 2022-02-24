# Celery-node-python-example

This article serves as a boilerplate/example template for an hybrid Celery architecture using Python and Javascript (can be extended to other programming language as well)



### Philosophy :

You will see how you can layout your code to maintain 2 or more development flows (here 2, one in python and the other in node)

We have a folder for python, another one for node, each is structured as much as possible as an independent project with it's own Dockerfile, Makefile.

Each of Python's and Node's folder provide a worker that listens on queue ready to be used by celery in order to perform
one of the tasks defined in it's tasks package (see folder structure)

At the root of the project we have one Makefile that glue everything together by including the Makefiles from python 
and node folders (to build worker docker images), starting the message broker, the result-backend, the workers through a docker-compose.yml file


### Project layout


* [configmaps/](./celery-node-python-example/configmaps)
  * [pyenvs/](./celery-node-python-example/configmaps/pyenvs)
* [node/](./celery-node-python-example/node)
  * [js_workers/](./celery-node-python-example/node/js_workers)
    * [tasks/](./celery-node-python-example/node/js_workers/tasks)
    * [client_example.js](./celery-node-python-example/node/js_workers/client_example.js)
    * [config.js](./celery-node-python-example/node/js_workers/config.js)
    * [worker.js](./celery-node-python-example/node/js_workers/worker.js)
  * [Dockerfile](./celery-node-python-example/node/Dockerfile)
  * [Makefile](./celery-node-python-example/node/Makefile)
  * [package-lock.json](./celery-node-python-example/node/package-lock.json)
  * [package.json](./celery-node-python-example/node/package.json)
  * [yarn.lock](./celery-node-python-example/node/yarn.lock)
* [python/](./celery-node-python-example/python)
  * [py_workers/](./celery-node-python-example/python/py_workers)
    * [tasks/](./celery-node-python-example/python/py_workers/tasks)
    * [utils/](./celery-node-python-example/python/py_workers/utils)
    * [__init__.py](./celery-node-python-example/python/py_workers/__init__.py)
    * [client_example.py](./celery-node-python-example/python/py_workers/client_example.py)
    * [config.py](./celery-node-python-example/python/py_workers/config.py)
    * [worker.py](./celery-node-python-example/python/py_workers/worker.py)
  * [scripts/](./celery-node-python-example/python/scripts)
    * [entrypoints/](./celery-node-python-example/python/scripts/entrypoints)
  * [tests/](./celery-node-python-example/python/tests)
    * [__init__.py](./celery-node-python-example/python/tests/__init__.py)
    * [test_py_worker.py](./celery-node-python-example/python/tests/test_py_worker.py)
  * [Dockerfile](./celery-node-python-example/python/Dockerfile)
  * [Makefile](./celery-node-python-example/python/Makefile)
  * [poetry.lock](./celery-node-python-example/python/poetry.lock)
  * [pyproject.toml](./celery-node-python-example/python/pyproject.toml)
* [.gitignore](./celery-node-python-example/.gitignore)
* [LICENSE](./celery-node-python-example/LICENSE)
* [Makefile](./celery-node-python-example/Makefile)
* [README.md](./celery-node-python-example/README.md)
* [docker-compose.yml](./celery-node-python-example/docker-compose.yml)



### Schema, Demo & Infos

#### Schema
You can check the schema bellow :

![Celery](static/celery-Celery-diagram.png)

#### Demo
You can check a complete demo video of the project in [YouTube](https://www.youtube.com/watch?v=TqYq8gkCTjM)

#### Infos
For more complete information you can check my [medium article](https://hamza-senhajirhazi.medium.com/how-to-build-a-hybrid-python-javascript-asynchronous-task-queue-system-for-your-server-web-5941504a5bf2) about this pattern