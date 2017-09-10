# bash on alpine
#
# VERSION               0.0.2

FROM alpine:latest

# make sure the package repository is up to date
RUN apk update && apk upgrade
RUN apk add bash
RUN sed -i -e "s/bin\/ash/bin\/bash/" /etc/passwd
