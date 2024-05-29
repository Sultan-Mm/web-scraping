OUTPUT_DIR="/home/s1122/RCP/Real_client_project_Group5_LouisErard/louisErard/output"
mkdir -p $OUTPUT_DIR
docker run --rm -v $OUTPUT_DIR:/app/output louiserardspider scrapy crawl louiserardspider -o /app/output/NewResult.csv
