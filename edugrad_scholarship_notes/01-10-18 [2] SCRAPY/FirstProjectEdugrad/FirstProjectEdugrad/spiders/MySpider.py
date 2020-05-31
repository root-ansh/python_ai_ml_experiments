import scrapy
class IntroSpider(scrapy.Spider):
    name = "intro_spider"

    def start_requests(self):
        urls = [
            "http://quotes.toscrape.com/page/1/",
            "http://quotes.toscrape.com/page/2/",
            "http://quotes.toscrape.com/page/3/",
            "http://quotes.toscrape.com/page/4/",
            "http://quotes.toscrape.com/page/5/"
            ]
        for i in urls :
            yield scrapy.Request(url=i,callback=self.parse)
            
    def parse(self,response):
        filename = "quotes-list.txt"

        quotes_list = response.css(".text::text").extract()
        author_list = response.css(".author::text").extract()

        with open(filename,'a+') as f:
            for quote,author in zip(quotes_list,author_list):
                f.write(quote+','+author+'\n')


"""
    def parse(self, response):
        page = response.url.split("/")[-2]
        filename = 'quotes-%s.html' % page
        with open(filename, 'wb') as f:
            f.write(response.body)
        self.log('Saved file %s' % filename)


"""
