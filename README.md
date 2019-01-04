
# Venturebeat Article Analyser  
 a simple project to show some cool visualisations and analysis of venturebeat's article archive.  
The following project required the following libraries to be installed in users system:  
- scrapy
- jupyter-notebook
- numpy, pandas and matplotlib  
(All in compliance to python v3 7.)  

## How it works? 
**Step 0** : `git clone https://github.com/root-ansh/VenturebeatArticleAnalyser.git` **Step 1 : Customisations**   
**Step 1** Customisations.  
1.1 (compulsory) : edit the local copy of https://github.com/root-ansh/VenturebeatArticleAnalyser/blob/master/venturebeat_bot/venturebeat_bot/spiders/vb_crawler.py and change the `file1` and `file2`  to your pc's location of these files.  

1.2 (optional) : edit the `date` variable to your desired starting date. Note that the farther your date is from current date, the longer the bot will take to extract information.

**Step 2** :open cmd in folder  `Venturebeat Article Analyser`  
**Step 3** : `cd venturebeat_bot`  
**Step 4**  `scrapy crawl vb_crawler`  
**Step 5**  `cd.. `  
**Step 6**  `jupyter-notebook` 
**Step 7**  then run all the text boxes of ipynb file from 1st to last, and you will find beautiful visualisations of :
    1.  Barchart showing top 20 authors for the given time period.  
    2. A list of tuples showing top 200 words frequently used words for that time.  



