#!/bin/sh

test -e /var/lib/tahoe/tahoe-client.tac || tahoe create-node --location=AUTO --webport=tcp:3456:interface=0.0.0.0 --port=tcp:27577:interface=0.0.0.0 /var/lib/tahoe/
tahoe start /var/lib/tahoe --nodaemon --logfile=-
