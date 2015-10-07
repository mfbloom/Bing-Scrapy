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

class myspider(CrawlSpider):
    name = "myspider"
    allowed_domains = ["bing.com"]
    start_urls = (
        'http://www.bing.com/search?q=site%3Awww.linkedin.com%2Fpub%20text%3A(security%20or%20jsp)%20and%20(pseg)%20&qs=n&form=QBRE&pq=site%3Awww.linkedin.com%2Fpub%20text%3A(security%20or%20jsp)%20and%20(pseg)%20&sc=0-0&sp=-1&sk=&cvid=C5CF9D6062CD4BB3A7057092A2DB9BAE',
    )
    
    rules=(Rule(LinkExtractor(allow=(), restrict_xpaths=('//a[@class="sb_pagN"]',)), callback="parse_page", follow= True),)


    def parse_page(self, response):
        questions = scrapy.Selector(response).xpath('//*[@id="b_results"]/li')

        #myjobs = []
        for question in questions:
            item = LocalwebItem()
            item['positionURL'] = question.xpath('h2/a/@href').extract()
            #item['employeeName'] = question.xpath('h2/a/strong/text()').extract()
            #item['positionTitle'] = question.xpath('div/ul/li/text()').extract()
            yield item
            
        pass
    