# -*- coding: utf-8 -*-
import scrapy
from scrapy.spiders import BaseSpider, Rule
from scrapy.linkextractors import LinkExtractor
from scrapy.http import FormRequest
from scrapy.spiders import CrawlSpider
from localweb.items import LocalwebItem
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
from scrapy.http import Request
from scrapy.selector import HtmlXPathSelector


class listcrawl(CrawlSpider):
    name = "listcrawl"
    allowed_domains = ["www.linkedin.com"]
    f = open("urls.txt")
    start_urls = [url.strip() for url in f.readlines()]
    f.close()
    
    def parse_page(self, response):
        
        questions = scrapy.Selector(response).xpath('//*[@id="b_results"]/li')

        #myjobs = []
        for question in questions:
            item = LocalwebItem()
            item['positionURL'] = question.xpath('h2/a/@href').extract()
            item['employeeName'] = question.xpath('h2/a/strong/text()').extract()
            item['positionTitle'] = question.xpath('div/ul/li/text()').extract()
            yield item
            
        pass
    