FROM alpine:latest

#RUN echo "==> Installing dependencies... => for download source" \
#RUN apk add --update curl wget ca-certificates openssl \
  #&& rm -rf /var/cache/apk/*

RUN echo "==> Installing dependencies... => for openresty" \
 && apk update \
 && apk add --virtual build-deps \
    make gcc musl-dev \
    pcre-dev openssl-dev zlib-dev ncurses-dev readline-dev \
    curl perl \
    wget ca-certificates openssl


# remove build-deps, add libs, clean cache and source
# && apk del build-deps \
# && apk add \
#    libpcrecpp libpcre16 libpcre32 openssl libssl1.0 pcre libgcc libstdc++ \
# && rm -rf /var/cache/apk/* \
# && rm -rf /root/ngx_openresty

CMD []
