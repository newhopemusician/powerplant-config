#!/bin/bash

crontab < /tmp/powerplant-config/newcron
cp /tmp/powerplant-config/insttype.sh /tmp/
chmod 755 /tmp/insttype.sh
