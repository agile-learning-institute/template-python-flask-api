# template-python-flask-api

# INSTRUCTIONS
This is a template repo - Do these things in each file. (s/from/to/g is global search/replace)
- [ ] README.md (this file)
     - [ ] Primary Collection s/COLLECTION/<collection>/g (all lower case)
     - [ ] Default API Port s/PORT/1234/g
     - [ ] Default Test Data _id s/TEST_ID/<24byte-hex>/g
     - [ ] Search for TODO and Do the thing
- [ ] [Github Actions](./.github/workflows/docker-push.yml)
     - [ ] Primary Collection s/COLLECTION/<collection>/g (all lower case)
- [ ] [Swagger](./docs/openapi.yaml) 
     - [ ] Primary Collection s/COLLECTION/<collection>/g (all lower case)
     - [ ] Search for TODO and Do the thing
- [ ] [config object](./src/config/config.py)
     - [ ] Search for TODO and Do the thing
- [ ] [COLLECTION Routes](./src/routes/COLLECTION_routes.py)
     - [ ] Rename the file
     - [ ] Primary Collection s/COLLECTION/<collection>/g (all lower case)
- [ ] [COLLECTION Service](./src/services/COLLECTION_services.py)
     - [ ] Rename the file
     - [ ] Primary Collection s/COLLECTION/<collection>/g (all lower case)
     - [ ] Search for TODO and Do the thing
- [ ] [MongoIO](./src/utils/mongo_io.py)
     - [ ] Primary Collection s/COLLECTION/<collection>/g (all lower case)
     - [ ] Search for TODO and Do the thing
- [ ] [server.py](/src/server.py)
     - [ ] Primary Collection s/COLLECTION/<collection>/g (all lower case)
     - [ ] Search for TODO and Do the thing
- [ ] [Dockerfile](./Dockerfile)
     - [ ] Primary Collection s/COLLECTION/<collection>/g (all lower case)
- [ ] [Pipfile](./Pipfile)
     - [ ] Primary Collection s/COLLECTION/<collection>/g (all lower case)
- [ ] [All Test Files](./test/)
     - [ ] Primary Collection s/COLLECTION/<collection>/g (all lower case)
     - [ ] Default Test Data _id s/TEST_ID/<24byte-hex>/g
     - [ ] Search for TODO and Do the thing

Now you can remove these instructions from the readme, 

## Overview

This is a template repo for a simple Flask API that provides Get/Post/Patch services for documents in the COLLECTION collection. This API uses data from a [backing Mongo Database](https://github.com/agile-learning-institute/mentorHub-mongodb), and supports a [Single Page Application.](https://github.com/agile-learning-institute/mentorHub-COLLECTION-ui)

The OpenAPI specifications for the api can be found in the ``docs`` folder, and are served [here](https://agile-learning-institute.github.io/mentorHub-COLLECTION-api/)

## Prerequisites

- [Mentorhub Developer Edition](https://github.com/agile-learning-institute/mentorHub/blob/main/mentorHub-developer-edition/README.md)
- [Python](https://www.python.org/downloads/)
- [Pipenv](https://pipenv.pypa.io/en/latest/installation.html)

### Optional

- [Mongo Compass](https://www.mongodb.com/try/download/compass) - if you want a way to look into the database

## Install Dependencies

```bash
pipenv install
```

## Run Unit Testing

```bash
pipenv run test
```

## {re}start the containerized database and run the API locally

```bash
pipenv run local
```

## Run the API locally (assumes database is already running)

```bash
pipenv run start
```

## Build and run the API Container

```bash
pipenv run container
```

This will build the new container, and {re}start the mongodb and API container.

## Run StepCI end-2-end testing
NOTE: Assumes the API is running at localhost:PORT

```bash
pipenv run stepci
```

## Run StepCI load testing
NOTE: Assumes the API is running at localhost:PORT

```bash
pipenv run load
```

# Project Layout
- ``/src`` this folder contains all source code
- ``/src/server.py`` is the main entrypoint, which initializes the configuration and registers routes with Flask
- ``/src/config/config.py`` is the singleton config object that manages configuration values and acts as a cache for enumerators and other low volatility data values.
- ``/src/models`` contains helpers related to creating transactional data objects such as breadcrumbs or RBAC tokens
- ``/src/routes`` contains Flask http request/response handlers
- ``/src/services`` service interface that wraps database calls with RBAC, encode/decode, and other business logic
- ``/src/utils/mongo_io.py`` is a singleton that manages the mongodb connection, and provides database io functions to the service layer. 
- ``/test`` this folder contains unit testing, and testing artifacts. The sub-folder structure mimics the ``/src`` folder

# API Testing with CURL

If you want to do more manual testing, here are the curl commands to use

### Test Health Endpoint

This endpoint supports the Prometheus monitoring standards for a health check endpoint

```bash
curl http://localhost:PORT/api/health/
```

### Test Config Endpoint

```bash
curl http://localhost:PORT/api/config/
```

### Test get a document

```bash
curl http://localhost:PORT/api/COLLECTION/TEST_ID/
```

### Test add a Document 

```bash
curl -X POST http://localhost:PORT/api/COLLECTION/TEST_ID/ \
     -d '{}' TODO: Provide simple test data
```

### Test update a Document

```bash
curl -X PATCH http://localhost:PORT/api/COLLECTION/TEST_ID/ \
     -d '{}' TODO: Provide simple test data
```

## Observability and Configuration

The ```api/config/``` endpoint will return a list of configuration values. These values are either "defaults" or loaded from a singleton configuration file, or an Environment Variable of the same name. Configuration files take precedence over environment variables. The environment variable "CONFIG_FOLDER" will change the location of configuration files from the default of ```./```

The ```api/health/``` endpoint is a [Prometheus](https://prometheus.io) Health check endpoint.

The [Dockerfile](./Dockerfile) uses a 2-stage build, and supports both amd64 and arm64 architectures. 
