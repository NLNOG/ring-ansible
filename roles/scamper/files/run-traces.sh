#!/usr/bin/env bash

filename="$(hostname)-$(date +%s).warts"

timeout -k 2450 2400 /usr/bin/sc_attach -p 23456 -c 'trace' -i /etc/ring/node-list.txt -o /tmp/$$.${filename} && \
    mv /tmp/$$.${filename} /home/scamper/traces/${filename} && \
    gzip /home/scamper/traces/${filename}

chown scamper.ring-users /home/scamper/traces/${filename}.gz

