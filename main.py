"""
run all the defined spiders sequentially
https://docs.scrapy.org/en/latest/topics/practices.html
"""

from twisted.internet import reactor, defer
from scrapy.crawler import CrawlerRunner
from scrapy.utils.log import configure_logging

# import all spiders
from karwanbazaar.spiders import index, archives, article_urls, article_content

spiders = {
    0: index.IndexSpider,
    1: archives.ArchivesSpider,
    2: article_urls.ArticleURLSpider,
    3: article_content.ArticleContentScraper
}

configure_logging()
runner = CrawlerRunner()


@defer.inlineCallbacks
def run_all():
    for spider_id in spiders.keys():
        spider = spiders[spider_id]
        print(f"Running Spider :: {spider}")
        yield runner.crawl(spider)
    reactor.stop()


# start
run_all()
reactor.run()
