FROM ubuntu:latest

COPY ./sharpnet/nginx.conf /sharpnet/nginx.conf

ENTRYPOINT ["tail", "-f", "/dev/null"]