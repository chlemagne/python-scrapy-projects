import scrapy


class LatestTechStoriesSpider(scrapy.Spider):
    name = "latest-technology-stories"

    def start_requests(self):
        urls = [
            "https://technology.inquirer.net/category/latest-stories",
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        for story in response.css("#ch-ls-box"):
            yield {
                "category": story.css("#ch-cat::text").get(),
                "date": story.css("#ch-postdate span:nth-child(1)::text").get(),
                "author": story.css("#ch-postdate span:nth-child(2)::text").get(),
                "title": story.css("#ch-ls-head h2 a::text").get()
            }
