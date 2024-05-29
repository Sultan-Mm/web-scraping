# Louis Erard Watches Scraper

This project is a web scraping application built using the Scrapy framework. It targets the Louis Erard website to extract data and information about all available watches. The extracted data includes details such as watch names, prices, descriptions, and other relevant information.


## Features

- Scrapes data from the Louis Erard website
- Extracts information about all watches
- Stores the data in a structured format

## Installation

### Prerequisites

- Python 3.6 or higher
- Docker (if you prefer to run the project in a container)

### Using Docker

1. **Build the Docker image:**
   ```bash
   docker build -t louis-erard-scraper .

2. **Run the Docker container:**
   ```bash
   docker run -it louis-erard-scraper .


### Manual Installation
    

Create a virtual environment:

bash
    - python3 -m venv venv
    - source venv/bin/activate

    
Install dependencies:

bash
    - pip install -r requirements.txt


    
Usage
Running the Scraper
Run the init.sh script to set up the environment (if applicable):

bash
    - ./init.sh


    
Run the Scrapy spider:

bash
    - scrapy crawl louiserardspider


    
Using the run_scrapy.sh Script
Make sure the run_scrapy.sh script is executable:

bash
    - chmod +x run_scrapy.sh


    
Run the script:

bash
    - ./run_scrapy.sh



    
Project Files:
- init.sh: Script to initialize the project environment.
- items.py: Defines the data structure for the scraped items.
- middlewares.py: Contains custom middlewares for the Scrapy project.
- pipelines.py: Processes the scraped data and stores it.
- settings.py: Configuration settings for the Scrapy project.
- spiders/louiserardspider.py: The main spider that performs the web scraping.
- Dockerfile: Instructions to build the Docker image for the project.
- requirements.txt: List of Python dependencies required for the project.
- run_scrapy.sh: Script to run the Scrapy spider easily.
