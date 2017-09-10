# Use Alpine Linux
FROM yarec/php

RUN apk add --no-cache php-mysqli php-zlib php-intl php-posix php-xsl

# Set Workdir
WORKDIR /www

# Expose volumes
VOLUME ["/www"]

# Expose ports
EXPOSE 9000

# Entry point
ENTRYPOINT ["/usr/bin/php-fpm"]
