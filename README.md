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

## Backend

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

# Maintainers

- [Adam McArthur](https://github.com/Sharpz7)
- [Precious Amarachi Onyeukwu](https://github.com/kindyluv)
