
# Venturebeat Article Analyser  
 a simple project to show some cool visualisations and analysis of venturebeat's article archive.  
**Requirements**  
The following project required the following libraries to be installed in users system:  
- scrapy
- jupyter-notebook
- numpy, pandas and matplotlib  
(All in compliance to python v3 7.)  

### How it works? 
**Step 0** : `git clone https://github.com/root-ansh/VenturebeatArticleAnalyser.git`   
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


### Explaination in detail.
The following project aims to display how the use of scrapy, matplotlib and NLTK library can be put together to get some meaningful analysis. Here we crawl  around 600+ articles of december 2018 from a tech-news site Venturebeat.com , put them in a large text file, and then read that file using NLTK library to build a hashmap of  unique words, filtering out the non usefult [stopwords](https://en.wikipedia.org/wiki/Stop_words).  

This helps us in formulating a frequency map of most popular words for that month. we also then build a dataframe and display the data in the form of a bar graph.  

<p align=center>
  <img src="https://github.com/chaostools/Super-Jarvis/blob/master/pics/sffs1.jpeg" width="250" height 600 />  
  <img src="https://github.com/chaostools/Super-Jarvis/blob/master/pics/ss2fff.jpeg" width="250" height 600 />

</p>

Using this data we can analyse that 'Gaming Technology' and its synonyms were the most popular trend in Decemeber 2018. At that time Games like PUBG and Fortnite were gaining mass audience support and tons of revenues, so that's probably why. This data also highlights that the word 'data' and 'infringment', 'piracy' was used a lot of times in articles, probably because of the Congress conference with Google and Facebook and GDPR enforcement.  

More research can be made on how to use this data more effectively and for predictive analysis. Apart from that a seperate frequency map for author names was created and visualised as a bar graph. Tech blogger Kyle L Wiggers has written the most number of articles in december for venturebeat
