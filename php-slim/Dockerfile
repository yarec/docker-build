# Use Alpine Linux
FROM yarec/composer

RUN mkdir -p /data
VOLUME /data
WORKDIR /data

COPY ep.sh /ep.sh
COPY composer.json /

RUN chmod +x /ep.sh \
    && composer install -d /

#ENTRYPOINT ["/ep.sh"]

# Entry point
#CMD ["/usr/bin/php", " -S 127.0.0.1:8000 -t /data/public "]

CMD ["/ep.sh"]
