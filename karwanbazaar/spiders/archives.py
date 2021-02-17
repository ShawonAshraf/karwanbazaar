"""
Crawls the file generated from index spider
Writes archive list urls to a json file
"""


import scrapy
import os
import json


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

        # create a dict for json
        url_dict = dict()
        for idx, url in enumerate(archives_root_urls):
            url_dict[idx] = url

        # save urls to a file
        with open(f"{os.getcwd()}/output/archive_root_urls.json", "w") as f:
            json.dump(url_dict, f, indent=4)

        # log
        self.log(f"Saved archives root urls -> {os.getcwd()}/output/archive_root_urls.json")
