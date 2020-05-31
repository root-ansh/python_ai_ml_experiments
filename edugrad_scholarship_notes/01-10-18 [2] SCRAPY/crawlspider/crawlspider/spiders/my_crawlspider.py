import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor


class my_crawlspider(CrawlSpider):
    name = "my_crawler"
    allowed_domains = ['un.org']
    start_urls = [
        "http://www.un.org"
    ]
    rules = (Rule(LinkExtractor(allow="funds-programmes-specialized-agencies-and-others"), callback='parse_page'),)

    def parse_page(self, response):
        list_of_leafs = response.css('.leaf > a::text').extract()

        for i in range(len(list_of_leafs)):
            s = str(i) + "\t:\t" + list_of_leafs[i] + '\n'
            with open('agencies.txt', 'a+') as f:
                f.write(s)
