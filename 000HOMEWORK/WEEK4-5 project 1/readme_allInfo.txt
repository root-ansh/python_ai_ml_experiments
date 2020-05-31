The project contains the following files: 
--allinfo.txt	                
(\allinfo.txt) : this file

--naukri_spider folder             
(\naukri_spider) : files related to scrapy/ spider

-- my_naukri_spider.py            
( \naukri_spider\naukri_spider\spiders\my_naukri_spider.py)
the web scraper that will scrape naukri.com and create a csv file

--naukri_dataanalytics.csv 
(\naukri_spider\naukri_dataanalytics.csv) 
 the csv file generated using the above script

--save_to_database.py
(\save_to_database.py)
python script that will be creating a database , and saving the data from csv file into that database

--CreateDatabaseAndTables.SQL
(\CreateDatabaseAndTables.SQL )
 the sql file having commands to create database and tables.

HOW THIS WORKS?

Prerequisites:
To run this Project, the following things are mandatory:
- pip and conda to be installed.(already comes pre installed with anaconda)
- scrapy to be installed sucessfully
- mysql-connector modules to be installed in main python shell using : `conda install -c anaconda mysql-connector-python`
- mysql server to be installed and setted up with a username/password.
i will be  using my username as 'root' and password : '1234'

STEPS TO RUN:
1)user first opens the terminal inside \naukri_spider folder
2) user then runs the spider  using command `scrapy crawl my_naukri_spider.py`
-------> the above command scrapes naukri.com, and generates a csv file out of all the posts.
4) user then moves back one folder inside the terminal using 'cd..'
5) user then executes another script  using command `python save_to_database.py`
-------> this command does 5 things:
	1.  reading CreateDatabaseAndTables.SQL: It reads database-creation SQL file and stores in a list of commands(`all_sql`)
	2. create DB : it connects to the localhosted mysql server and creates DB by executing commands lines(from step1)one by one.
	3. load CSV : it loads the complete csv file into a 2D list
	4. split Location data : it converts the 2DList generated in last step to a kind-of 3D list.
	5. insertion of data : it finally adds the complete csv data to 2 tables in DB 


