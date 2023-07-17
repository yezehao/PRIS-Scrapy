# PRIS-Scrapy
This is a project aimed to gather the data from the [PRIS](https://pris.iaea.org/PRIS/home.aspx) database published by *IAEA*. 
Due to unforeseen factors, it was not feasible to develop the desired web scraping programme using a simple script. Therefore, the [Scrapy](https://github.com/scrapy/scrapy) framework was employed to accomplish the data retrieval task.

## Getting Started
Before running the programme, it is necessary to modify specific parameters to ensure smooth operation. The marked sections should be modified according to the actual circumstances to facilitate proper execution of the programme.
+ MySQL database
  The parameters of the MySQL database are configured in file `/pris_mysql/pris_mysql/settings.py`. It is necessary to modify the following MySQL database parameters in the file to ensure correct operation of the programme.  
  MySQL in programme:  
  📚Database ==> **pris**   
  👤User ==> **intern@localhost**  
  🔑Password ==> **favEkJr8**  
  ```
  MYSQL_HOST = 'localhost'     # MySQL主机名
  MYSQL_DATABASE = 'pris'      # 数据库名
  MYSQL_USER = 'intern'        # 用户名
  MYSQL_PASSWORD = 'favEkJr8'  # 密码
  ```
+ Python Module
  I have configured a virtual environment for my project to run the programme, and I have uploaded the venv files to GitHub. To activate the virtual environment in the PRIS-Scrapy folder, you can use the command `venv\Scripts\activate`🚀. In case the virtual environment doesn't work, I have listed the installed Python modules below to help you configure the environment more easily.
+ Programme Execution
  To run the program, navigate to the correct location by the following command:  
  `cd /PRIS-Scrapy/pris-mysql/`🚀
  This command will take you to the specified folder `/PRIS-Scrapy/pris-mysql/`. Once you are in the correct folder, you can proceed with running the program with following command.
  `python allspiders.py`🚀
  By following these steps, you will be in the appropriate location to run the program successfully. 

## Module Requirement
<details open>
  <summary>Requirement</summary>
This section highlights the additional Python modules utilized to efficiently retrieve information from the PRIS webpage and store it in the respective database.  

| Module | Description | Usage | Installation | Version |
| ----- | ----- | ----- | ----- | ----- |
| [Scrapy](https://scrapy.org/) | An open source and collaborative framework for extracting the data you need from websites. In a fast, simple, yet extensible way. | Extrcting information from the PRIS database | `pip install scrapy`🚀  | 2.9.0 |
| [mysql.connector](https://github.com/mysql/mysql-connector-python) | MySQL driver written in Python which does not depend on MySQL C client libraries and implements the DB API v2.0 specification (PEP-249). | Transmit data to MySQL database | `pip install mysql-connector-python`🚀 | 8.0.33 |
| [schedule](https://pypi.org/project/schedule/) | Python job scheduling for humans. Run Python functions (or any other callable) periodically using a friendly syntax. | Run the main programme at intervals | `pip install schedule`🚀 | 1.2.0 |
</details>

<details>
  <summary>pip list</summary>

| Package | Version |
| ------- | ------- |
|attrs                 |23.1.0
Automat                |22.10.0
certifi                |2023.5.7
cffi                   |1.15.1
charset-normalizer     |3.2.0
constantly             |15.1.0
cryptography           |41.0.2
cssselect              |1.2.0
filelock               |3.12.2
hyperlink              |21.0.0
idna                   |3.4
incremental            |22.10.0
itemadapter            |0.8.0
itemloaders            |1.1.0
jmespath               |1.0.1
lxml                   |4.9.3
mysql-connector-python |8.0.33
packaging              |23.1
parsel                 |1.8.1
pip                    |22.2.1
Protego                |0.2.1
protobuf               |3.20.3
pyasn1                 |0.5.0
pyasn1-modules         |0.3.0
pycparser              |2.21
PyDispatcher           |2.0.7
pyOpenSSL              |23.2.0
queuelib               |1.6.2
requests               |2.31.0
requests-file          |1.5.1
schedule               |1.2.0
Scrapy                 |2.9.0
service-identity       |23.1.0
setuptools             |63.2.0
six                    |1.16.0
tldextract             |3.4.4
Twisted                |22.10.0
twisted-iocpsupport    |1.0.3
typing_extensions      |4.7.1
urllib3                |2.0.3
w3lib                  |2.1.1
zope.interface         |6.0
</details>

## References - SCRAPY
+ [Documentation about scrapy](https://docs.scrapy.org/en/latest/)
+ [GitHub about scrapy](https://github.com/scrapy/scrapy)

## command for JSON saving
+ Command template
  + create the new scrapy project: `scrapy startproject Scrapy` 🚀
  + run the programme and save result in json file: `scrapy crawl (name) -O (filename)` 🚀
+ run pris_country and save result in pris_country.json:   
  + `scrapy crawl pris_country -o pris_country.json` 🚀  
  + corresponding python file: `/pris_spider/pris_spider/spiders/PRIS_country.py` 🌟

+ run pris_region and save result in pris_region.json:  
  + `scrapy crawl pris_region -o pris_region.json` 🚀
  + corresponding python file: `/pris_spider/pris_spider/spiders/PRIS_region.py` 🌟

+ run pris_type and save result in pris_type.json:  
  + `scrapy crawl pris_type -o pris_type.json` 🚀
  + corresponding python file: `/pris_spider/pris_spider/spiders/PRIS_type.py` 🌟

+ run pris_trend and save result in pris_trend.json:  
  + `scrapy crawl pris_trend -o pris_trend.json` 🚀
  + corresponding python file: `/pris_spider/pris_spider/spiders/PRIS_trend.py` 🌟

+ run pris_age and save result in pris_age.json:  
  + `scrapy crawl pris_age -o pris_age.json` 🚀
  + corresponding python file: `/pris_spider/pris_spider/spiders/PRIS_age.py` 🌟


## command for MySQL database exportation
+ `cd '.\Program Files\MySQL\MySQL Server 8.0\bin'` 🚀
+ `.\mysqldump -u root -p pris > C:\Users\30348\Desktop\hequtech\PRIS-Scrapy\output_file.sql` 🚀


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
 ┃
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
 ┃
 ┣ 📂pris_mysql
 ┃ ┗ 📜scrapy.cfg
 ┃ ┣ 📂pris_mysql
 ┃ ┃ ┣ 📜__init__.py
 ┃ ┃ ┣ 📜items.py
 ┃ ┃ ┣ 📜middlewares.py
 ┃ ┃ ┣ 📜pipelines.py
 ┃ ┃ ┗ 📜settings.py
 ┃ ┃ ┣ 📂__pycache__
 ┃ ┃ ┣ 📂spiders
 ┃ ┃ ┃ ┣ 📂__pycache__
 ┃ ┃ ┃ ┣ 📜debug-mysql.sql
 ┃ ┃ ┃ ┣ 📜__init__.py
 ┃ ┃ ┃ ┣ 📜PRIS_age.py
 ┃ ┃ ┃ ┣ 📜PRIS_country.py
 ┃ ┃ ┃ ┣ 📜PRIS_region.py
 ┃ ┃ ┃ ┣ 📜PRIS_trend.py
 ┃ ┃ ┃ ┗ 📜PRIS_type.py
 ┗ 📜README.md
</pre>