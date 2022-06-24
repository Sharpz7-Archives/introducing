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

| Name          | Description                                                     | Required |
|---------------|-----------------------------------------------------------------|----------|
| FLASK_APP     | Should be set to `introducing/app.py`                           | Y        |
| FLASK_ENV     | Should be set to `development` or `production`                  | Y        |
| TRUE_AGE      | TRUE for real AI Detection, FALSE for not, see [Here](https://labs.everypixel.com/api/account/balance) as there is a limit on usage) | N        |
| CLIENT_ID     | The Client ID for [EveryPixel](https://labs.everypixel.com)     | N        |
| CLIENT_SECRET | The Client Secret for [EveryPixel](https://labs.everypixel.com) | N        |

## Backend

**For all of these tasks, please clone the repository first**

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

To run in docker:

```bash
sudo docker-compose up -d --build
sudo docker-compose logs -f
```

## Frontend

To run the frontend:

- [install node](https://nodejs.org/en/download/)
- [install yarn](https://classic.yarnpkg.com/lang/en/docs/install/)
- [install mui](yarn add @mui/material @emotion/react @emotion/styled
)

**To get all the dependencies**

```bash
npm install
yarn install
```

# Maintainers

- [Adam McArthur](https://github.com/Sharpz7)
- [Precious Amarachi Onyeukwu](https://github.com/kindyluv)
