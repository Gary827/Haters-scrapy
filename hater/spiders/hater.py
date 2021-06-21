from hater.items import HaterItem
import scrapy
import time

class PTTSpider(scrapy.Spider):
    name = 'hater'
    allowed_domains = ['ptt.cc']
    start_urls = ['https://www.ptt.cc/bbs/Hate/index3994.html']

    def parse(self, response):
        for i in range(3993, 0, -1):
            url = 'https://www.ptt.cc/bbs/Hate/index'+ str(i) +'.html'
            yield scrapy.Request(url, self.parse)

        for href in response.css('.r-ent > div.title > a::attr(href)'):
            url = response.urljoin(href.extract())
            yield scrapy.Request(url, callback=self.parse_hater)

        
    def parse_hater(self, response):
        item = HaterItem()
        item['title'] = response.xpath('//meta[@property="og:title"]/@content').extract()
        item['author'] = response.xpath('//div[@class="article-metaline"]/span[text()="作者"]/following-sibling::span[1]/text()')[0].extract().split(' ')[0]
        item['content'] = response.xpath('//div[@id="main-content"]/text()')[0].extract()

        yield item