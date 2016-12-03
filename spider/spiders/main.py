from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from scrapy.selector import Selector
from scrapy.http import Request


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
        next_page = response.xpath('//a[@class="button next"]/@href').extract_first()
        if next_page is not None:
            next_page = response.urljoin(next_page)
            yield Request(next_page, callback=self.parse)
   