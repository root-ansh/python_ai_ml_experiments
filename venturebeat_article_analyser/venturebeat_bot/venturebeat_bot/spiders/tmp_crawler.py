import scrapy


class tmp_crawler(scrapy.Spider):
    name = 'tmp_crawler'
    allowed_domains = [
        r'https://venturebeat.com/2018/02/01/ai-powered-customer-engagement-isnt-optional-anymore-vb-live/']
    start_urls = [r'https://venturebeat.com/2018/02/01/ai-powered-customer-engagement-isnt-optional-anymore-vb-live/']

    def parse(self, response):
        author_list = response.css('a.author::text').extract()
        content_paras = response.css('div.article-content p::text').extract()

        file1 = r'C:\Users\anshs\00ANSH_PYTHON\My_Projects\NewsSiteCrawler\Authorlist.txt'
        file2 = r'C:\Users\anshs\00ANSH_PYTHON\My_Projects\NewsSiteCrawler\raw_article.txt'

        with open(file1, 'a') as f:
            f.writelines("%s\n" % author for author in author_list)

        with open(file2, 'a') as f:
            f.writelines("%s\n" % para for para in content_paras)

        print("scraped successfully")

# scrapy crawl --nolog botname : for no log generation
