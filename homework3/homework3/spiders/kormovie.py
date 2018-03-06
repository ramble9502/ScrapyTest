# -*- coding: utf-8 -*-
import scrapy
from scrapy.selector import Selector
from homework3.items import *

import pdb


class KorSpider(scrapy.Spider):
    name = "kormovie"
    allowed_domains = ["www.playdb.co.kr"]

    start_urls = []
    for j in range(1, 9):
        start_urls.append(
            "http://www.playdb.co.kr/playdb/playdblist.asp?Page=" + str(j))

    def parse(self, response):
        sel = Selector(response)
        item = Homework3Item()
        sites = sel.xpath("//table[@width='760']")
        for site in sites:
            for i in range(1, 14):
                item["title"] = site.xpath(
                    "//font[@size='2']/a/text()").extract()[i]
                item["img"] = site.xpath(
                    "//div[@align='center']/img/@src").extract()[i]
                item["place"] = site.xpath(
                    "//a[contains(@href,'PlacecCD')]/text()").extract()[i]
                item["date"] = site.xpath(
                    "//table[@width='375']/tr[2]/td/text()[2]").extract()[i]
                item["style"] = site.xpath(
                    "//table[@width='375']/tr[2]/td/text()[1]").extract()[i]
                yield item
