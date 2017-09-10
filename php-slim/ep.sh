#!/bin/sh
mip=`/sbin/ifconfig -a|grep inet|grep -v 127.0.0.1|grep -v inet6|awk '{print $2}'|tr -d "addr:"`

env VENDER_PATH=/ php -S $mip:8000 -t /data/public
