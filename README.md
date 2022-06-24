[![CircleCI](https://dl.circleci.com/status-badge/img/gh/Sharpz7/introducing/tree/main.svg?style=svg)](https://dl.circleci.com/status-badge/redirect/gh/Sharpz7/introducing/tree/main)

![](https://files.mcaq.me/5395a.jpg)

## A Tool that allows for a random, fake person to come to life!
<br>

![](https://files.mcaq.me/60k66.jpg)

## Currently Generates

- Fake AI Face
- Location
- Job Title
- Age based on Fake Face
- Location Picture
- Backstory

## How it works

![](https://files.mcaq.me/x02ar.jpg)

### Uses [GRPC-IO](https://grpc.io/) and [Flask](https://flask.palletsprojects.com/en/2.1.x/)

# Quickstart Guide

## Enviroment

| Name                  | Description                                                     | Required |
|-----------------------|-----------------------------------------------------------------|----------|
| FLASK_APP             | Should be set to `introducing/app.py`                           | Y        |
| FLASK_ENV             | Should be set to `development` or `production`                  | Y        |
| TRUE_AGE              | `TRUE` for real AI Detection, `FALSE` for not, see [Here](https://labs.everypixel.com/api/account/balance) as there is a limit on usage) | N        |
| CLIENT_ID             | The Client ID for [EveryPixel](https://labs.everypixel.com)     | N        |
| CLIENT_SECRET         | The Client Secret for [EveryPixel](https://labs.everypixel.com) | N        |
| DONT_DOWNLOAD_STUB    | When set to `TRUE`, will not download [service.proto](https://github.com/Sharpz7/introducing/blob/main/proto/service.proto)         | N        |

## Backend

**For all of these tasks, please clone the repository first**

## Flask

To run as a test server:

```bash
poetry install
poetry run flask run --host=0.0.0.0 -p 5000
```

To run as a production server:

```bash
poetry install
poetry run gunicorn --bind 0.0.0.0:5000 introducing.wsgi:app
```

## GRPC

To run the grpc server:

```bash
poetry run python -m introducing.grpc_app
```

To run a client, please see the README's for each client:

- [C#](https://github.com/Sharpz7/introducing/tree/main/clients/dotnet)
- [Python](https://github.com/Sharpz7/introducing/tree/main/clients/python)


## Frontend

To run the frontend:

- [install node](https://nodejs.org/en/download/)
- [install yarn](https://classic.yarnpkg.com/lang/en/docs/install/)
- [install mui](https://mui.com/material-ui/getting-started/installation/)

**To get all the dependencies**

```bash
npm install
yarn install
```

Then run

```bash
npm run start
```

## Docker

This will run both the flask backend, the grpc server and the React Frontend.

**NOTE: This needs [Docker](https://docs.docker.com/get-docker/) and [Docker Compose](https://docs.docker.com/compose/install/) to be installed!**

To run in docker:

```bash
make docker_run
```

# Maintainers

- [Adam McArthur](https://github.com/Sharpz7)
- [Precious Amarachi Onyeukwu](https://github.com/kindyluv)
