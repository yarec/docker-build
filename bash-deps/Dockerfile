# bash on alpine
#
# VERSION               0.0.2

FROM yarec/bash

RUN echo "==> Installing dependencies... => for openresty" \
 && apk update \
 && apk add --virtual build-deps \
    make gcc musl-dev \
    pcre-dev openssl-dev zlib-dev ncurses-dev readline-dev \
    curl perl \
    wget ca-certificates openssl
