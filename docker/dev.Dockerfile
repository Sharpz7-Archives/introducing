FROM ubuntu:latest

COPY ./sharpnet/nginx.dev.conf /sharpnet/nginx.conf

ENTRYPOINT ["tail", "-f", "/dev/null"]