# -*- coding: utf-8 -*-
import scrapy
#from movie.items import MoviceItem


class MeijuSpider(scrapy.Spider):
    name = 'meiju'
    allowed_domains = ['meijutt.com']
    start_urls = ['https://www.meijutt.com/alltop_hit.html']

    def parse(self, response):
        top_list = response.xpath("//ul[@class='top-list fn-clear']/li//h5//a/text()").extract()
        i = 0
        while i < 30:
            print("%s."%(i+1)+top_list[i])
            i += 1




# jsonpyz0gchtd86i({"data":[{
#         "id":3984,
#         "name":"\u534e\u4e3a",
#         "feed":"10357954",
#         "search":677981,
#         "industry":"\u624b\u673a",
#         "industryid":"2",
#         "dimensionid":"12",
#         "rank":0}],
#         "status":0});