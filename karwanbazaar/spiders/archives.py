"""
Crawls the file generated from index spider
Writes archive list urls to a json file
"""


import scrapy
import os


class ArchivesSpider(scrapy.Spider):
    name = "archives"

    def start_requests(self):
        urls = [
            f"file://{os.getcwd()}/output/index.html"
        ]

        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        # get selectors for the archives list
        selectors = response.css("div.cell.cell-3")

        # css query to get the urls
        archives_root_urls = selectors.css("ul li a::attr(href)").extract()

        # save urls to a file
        with open(f"{os.getcwd()}/output/archive_root_urls.txt", "w") as f:
            for url in archives_root_urls:
                f.write(url + "\n")

        # log
        self.log(f"Saved archives root urls -> {os.getcwd()}/output/archive_root_urls.txt")
