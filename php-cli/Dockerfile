# Use Alpine Linux
FROM yarec/php

RUN apk add --no-cache php-mysqli php-xsl php-intl

# Set Workdir
WORKDIR /data

# Expose volumes
VOLUME ["/data"]

# Entry point
CMD ["/usr/bin/php", "-a"]
