# VeeamAzure-to-ElasticCloud
Application to retrieve logs from Veeam Backup for Microsoft Azure to Elastic Cloud 

## Prerequisites

`pip install requests`

## Configuration
First of all, you need to have Filebeat installed/downloaded.
Then replace the filebeat.yml with the one in the filebeat folder of the package.

Then, modify it by putting your cloud.id and your cloud.auth.

Finally, fill in the necessary information in the config.json.

## How to launch it ?

  1. Launch filebeat 
  2. Run the script with write rights in the /var/log/ folder
