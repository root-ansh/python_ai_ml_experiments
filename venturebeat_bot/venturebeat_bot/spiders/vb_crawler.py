import scrapy
from datetime import datetime, timedelta


class VbCrawlerSpider(scrapy.Spider):
    name = 'vb_crawler'
    tot_articles = 1

    # this function manually scraps every archive article on venturebeat , simply by crating urls in the form of
    # xyz.com/yyyy/mm/dd and yielding scrapy.Request(...).
    # function parse_item(self) and function start_requests(self): both yield a new request(..) catched by scrappy.
    def start_requests(self):
        date = datetime(2018, 12, 1)  # starting date
        page_id = 1  # for testing
        while date <= datetime.now():
            url = 'https://venturebeat.com/' + date.strftime("%Y/%m/%d") + "/"

            new_request = scrapy.Request(url=url, callback=self.parse)
            new_request.meta["url"] = url  # we can also pass metadata, which is a kind of key-value storage
            new_request.meta["page_id"] = page_id  # which we can easily retrieve in parse()
            new_request.meta["date"] = date
            yield new_request

            print("scanned Page number:", page_id)  # for Testing purposes
            page_id += 1  # for Testing purposes
            date += timedelta(days=1)

        print("total articles scanned:", self.tot_articles)

    # parse is an "abstract method"(wow, i didn't know that) and is compulasory to be implemented
    # scrappy analyses the response and passes to parse() function as response, where the user can extract perticular
    # info using response.css(...).extract()  or  response.css(...).extract_first()  or  response.xpath(...).extract()
    # or  response.xpath(...).extract_first()
    # we can also extrct perticular respnse urls from buttons(the links which will open on a perticular button click)
    # and request a response for that url(s) in some other function self.second_parse(...), in the same manner as we did
    # before.
    def parse(self, response):
        r_page_id = response.meta["page_id"]
        # print("recieved response with age id:",r_page_id)  # Testing

        # even better way to extract text. check pic in main folder to find the exact path, html tag,  class name and link
        articles_url_list = response.css('h2.article-title a::attr(href)').extract()
        article_id = 1
        for url in articles_url_list:
            print("page - ", r_page_id, ":caught url no.", article_id, ":", url[0:50] + '...')

            new_request = scrapy.Request(url=url, callback=self.parse_article)
            new_request.meta["page_id"] = r_page_id
            new_request.meta["article_id"] = article_id
            yield new_request

            article_id += 1
            self.tot_articles += 1

    def parse_article(self, response) -> None:
        r_page_id = response.meta["page_id"]
        r_article_id = response.meta["article_id"]

        print("recieved response with page id:", r_page_id, "article id:", r_article_id)  # Testing

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
