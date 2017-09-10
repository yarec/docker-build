FROM python:alpine

ADD pip.conf /root/.pip/pip.conf

RUN pip install wxrobot

RUN mkdir -p /data
VOLUME /data
WORKDIR /data

# Entry point
CMD [python]
