# PRIS-Scrapy
This is a project aimed to gather the data from the [PRIS](https://pris.iaea.org/PRIS/home.aspx) database published by *IAEA*. 
Due to unforeseen factors, it was not feasible to develop the desired web scraping program using a simple script. Therefore, the [Scrapy](https://github.com/scrapy/scrapy) framework was employed to accomplish the data retrieval task.

## References - SCRAPY
+ [Documentation about scrapy](https://docs.scrapy.org/en/latest/)
+ [GitHub about scrapy](https://github.com/scrapy/scrapy)

## Command template
+ create the new scrapy project: `scrapy startproject Scrapy` 🚀
+ run the programme and save result in json file: `scrapy crawl (name) -O (filename)` 🚀

## command for usage
+ run pris_country and save result in pris_country.json:   
  + `scrapy crawl pris_country -o pris_country.json` 🚀  
  + corresponding python file: `/pris_spider/pris_spider/spiders/PRIS_country.py` 🌟

+ run pris_region and save result in pris_region.json:  
  + `scrapy crawl pris_region -o pris_region.json` 🚀
  + corresponding python file: `/pris_spider/pris_spider/spiders/PRIS_region.py` 🌟




## Structure of the Repository

<pre>
📦PRIS
 ┣ 📂__pycache__
 ┣ 📂venv
 ┣ 📂mysql
 ┃ ┣ 📚Database: pris
 ┃ ┣ 👤User:intern@localhost
 ┃ ┣ 🔑Password:favEkJr8
 ┃ ┣ 📜PRIS_age_creation.sql
 ┃ ┣ 📜PRIS_country_creation.sql
 ┃ ┣ 📜PRIS_region_creation.sql
 ┃ ┣ 📜PRIS_trend_creation.sql
 ┃ ┗ 📜PRIS_type_creation.sql
 ┣ 📂pris_spider
 ┃ ┣ 📜pris_age.json
 ┃ ┣ 📜pris_country.json
 ┃ ┣ 📜pris_region.json
 ┃ ┣ 📜pris_trend.json
 ┃ ┣ 📜pris_type.json
 ┃ ┗ 📜scrapy.cfg
 ┃ ┣ 📂pris_spider
 ┃ ┃ ┣ 📜__init__.py
 ┃ ┃ ┣ 📜items.py
 ┃ ┃ ┣ 📜middlewares.py
 ┃ ┃ ┣ 📜pipelines.py
 ┃ ┃ ┗ 📜settings.py
 ┃ ┃ ┣ 📂__pycache__
 ┃ ┃ ┣ 📂spiders
 ┃ ┃ ┃ ┣ 📂__pycache__
 ┃ ┃ ┃ ┣ 📜__init__.py
 ┃ ┃ ┃ ┣ 📜PRIS_age.py
 ┃ ┃ ┃ ┣ 📜PRIS_country.py
 ┃ ┃ ┃ ┣ 📜PRIS_region.py
 ┃ ┃ ┃ ┣ 📜PRIS_trend.py
 ┃ ┃ ┃ ┗ 📜PRIS_type.py
 ┗ 📜README.md
</pre>