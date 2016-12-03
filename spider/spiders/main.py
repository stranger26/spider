from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from scrapy.selector import Selector


class MySpider(CrawlSpider):
    name = "craigs"
    allowed_domains = ["sfbay.craigslist.org"]
    start_urls = ["http://sfbay.craigslist.org/search/npo"]

    def parse(self, response):
        for title in response.xpath('//p[@class="result-info"]'):
            yield {
                'link': title.xpath("a/@href").extract_first(),
                'title': title.xpath("a/text()").extract_first()
                }
