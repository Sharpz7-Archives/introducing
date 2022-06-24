FROM python:3.9 as base

ENV PYTHONUNBUFFERED=1 \
    PIP_NO_CACHE_DIR=1 \
    PIP_DISABLE_PIP_VERSION_CHECK=1

COPY . .

RUN pip3 install poetry

RUN poetry config virtualenvs.create false

RUN poetry install --no-dev

COPY ./sharpnet/nginx.conf /sharpnet/nginx.conf
COPY ./docker/docker_entrypoint.sh /entry/docker.sh

RUN chmod +x /entry/docker.sh

CMD [ "/entry/docker.sh" ]