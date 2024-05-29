#!/bin/bash

filestamp=$(date +"%Y-%m-%d_%H-%M-%S")

source venv/bin/activate

pip install -r requirements.txt

# Activate your Python virtual environment if necessary
# source /home/ubuntu/scrapy_project/venv/bin/activate
# Run the Scrapy command
scrapy crawl louiserardspider -o output_${filestamp}.csv




################### CRON FILE #######################
#* * * * * /home/ubuntu/scrapy_project/louisErard/init.sh
#####################################################