# Intro C# Client

Check how to start the server [here](https://github.com/Sharpz7/introducing).

The client uses the service.proto file in [./proto/service.proto](https://github.com/Sharpz7/introducing/blob/main/proto/service.proto).

# Setup

Makefiles are used for install

## Enviroment
| Name               | Description                                                     | Required |
|--------------------|-----------------------------------------------------------------|----------|
| DONT_DOWNLOAD_STUB | When set to `TRUE`, will not download [service.proto](https://github.com/Sharpz7/introducing/blob/main/proto/service.proto)         | N        |

## Run

**NOTE: This needs [Docker](https://docs.docker.com/get-docker/) and [Docker Compose](https://docs.docker.com/compose/install/) to be installed!**

```bash
make run
```