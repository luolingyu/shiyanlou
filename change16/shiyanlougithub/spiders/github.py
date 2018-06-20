# -*- coding: utf-8 -*-
import scrapy
from datetime import datetime
from shiyanlougithub.items import GithubItem
class GithubSpider(scrapy.Spider):
    name = 'repositories'
#    allowed_domains = ['github.com']
 #   start_urls = ['http://github.com/']
    
    @property
    def start_urls(self):
        url_tmpl = 'https://github.com/shiyanlou?page={}&tab=repositories'
        return (url_tmpl.format(i) for i in range(1,5))
    def parse(self, response):
        for repositories in response.css('li.col-12'):
            yield({
                'name':repositories.xpath('.//h3/a/text()').re_first('\n\s*(.*)'),

                'update_time':datetime.strptime(repositories.xpath('.//relative-time/@datetime').extract_first(),'%Y-%m-%dT%H:%M:%SZ')


                })
