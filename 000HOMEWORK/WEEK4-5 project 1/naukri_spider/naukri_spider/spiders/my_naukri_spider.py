import scrapy,csv
class MySpider(scrapy.Spider):
    name = "my_naukri_spider"

    def start_requests(self):
        urls = [
            "https://www.naukri.com/data-analytics-jobs-in-delhi-ncr"
            ]
        for i in urls :
            yield scrapy.Request(url=i,callback=self.parse)
            
    def parse(self,response):
        filename = "naukri_dataanalytics.csv"
        l=[]
        rows=(response.css('.row'))
        for r in rows:
            m=[]
            POSITION        =str(r.css('.desig::text').extract_first())
            LINK            =str(r.css('.row>a::attr(href)').extract_first())
            ORG             =str(r.css('.org::text').extract_first())
            LOCATION        =str(r.css('.loc>span::text').extract_first())
            EXP             =str(r.css('.exp::text').extract_first())
            DESCRIPTION     =str(r.css('.more>span:nth-child(4)::text').extract_first())
            SKILL           =str(r.css('.skill::text').extract_first())
            SALARY          =str(r.css('.salary::text').extract_first())
            DATE            =str(r.css('.date::text').extract_first())
            
            
            m.append(POSITION)
            m.append(LINK)
            m.append(ORG)
            m.append(LOCATION)
            m.append(EXP)
            m.append(SKILL)
            m.append(DESCRIPTION)
            m.append(SALARY)
            m.append(DATE)
            
            l.append(m)
            
        with open(filename,'w',newline='') as f:
            writerObj=csv.writer(f)
            for i in l:
                if(i[0]!='None'):
                    writerObj.writerow(i)
