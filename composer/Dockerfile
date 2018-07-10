FROM composer

#RUN docker-php-ext-install pdo_mysql

RUN apk --update add php7-pdo_mysql php7-pdo_sqlite

RUN composer config -g repo.packagist composer https://packagist.phpcomposer.com

RUN composer global require "laravel/installer"

RUN cd /tmp && composer create-project --prefer-dist laravel/laravel
