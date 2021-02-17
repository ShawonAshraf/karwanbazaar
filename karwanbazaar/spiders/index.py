"""
IndexSpider

Crawls the mainpage of Motikontho
"""

import scrapy


class IndexSpider(scrapy.Spider):
    name = "index"

    def start_requests(self):
        urls = [
            "https://motikontho.wordpress.com/"
        ]

        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        # decode bytes to utf8 strings
        decoded = response.body.decode("utf-8")

        # write to file
        with open("./output/index.html", "w") as f:
            f.write(decoded)

        # log
        self.log("Saved file -> index.html")
