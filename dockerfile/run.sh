#!/bin/bash


rm /etc/filebeat/filebeat.yml
cp /etc/filebeat/filebeat.save /etc/filebeat/filebeat.yml

sed -i "s/cloud.id:/cloud.id: \"$CLOUD_ID\"/g" /etc/filebeat/filebeat.yml ;
sed -i "s/cloud.auth:/cloud.auth: \"elastic:$CLOUD_PASSWORD\"/g" /etc/filebeat/filebeat.yml ;

/home/veeamapi/run.py use_env & filebeat -e;