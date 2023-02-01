#!/bin/bash
#ec2-metadata |grep instance-type |cut -d : -f 2 > /tmp/insttype
export INSTTYPE=`ec2-metadata |grep instance-type |cut -d : -f 2`
echo $INSTTYPE

if [ $INSTTYPE == "t2.micro" ]
then
        #echo "Will shutdown webserver"
        cp /var/www/html/outofmem.html /var/www/html/index.html
	      /usr/bin/python /tmp/message1.py
        mv /tmp/message1.py /tmp/message2.py
else
        cp /var/www/html/index-orig.html /var/www/html/index.html
        #echo "All good"
fi
