FROM python:3.9 as base

ENV PYTHONUNBUFFERED=1 \
    PIP_NO_CACHE_DIR=1 \
    PIP_DISABLE_PIP_VERSION_CHECK=1

COPY . .

RUN pip3 install poetry

RUN poetry config virtualenvs.create false

RUN poetry install --no-dev

COPY ./sharpnet/nginx.conf /sharpnet/nginx.conf
COPY ./docker/flask_entrypoint.sh /entry/flask.sh
COPY ./docker/grpc_entrypoint.sh /entry/grpc.sh

RUN chmod +x /entry/flask.sh
RUN chmod +x /entry/grpc.sh

CMD [ "/entry/flask.sh" ]