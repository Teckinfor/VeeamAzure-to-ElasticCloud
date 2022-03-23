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

## [Container](https://hub.docker.com/r/teckinfor/veeamtoelk)
### How to use
The configuration is done through environment variables.

Here is the list of the necessary environment variables:
  - CLOUD_ID = *cloud id*
  - CLOUD_PASSWORD = *cloud password*
  - VEEAM_USERNAME = *veeam username*
  - VEEAM_PASWORD = *veeam password*
  - VEEAM_HOST = *IP or host of the Veeam VM*
