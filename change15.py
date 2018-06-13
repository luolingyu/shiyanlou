# -*- coding:utf-8 -*-
import scrapy
from datetime import datetime

class Shiyanlougithubscrapy(scrapy.Spider):
    name = 'shiyanlou-github'
    @property
    def start_urls(self):
        url_tmpl = 'https://github.com/shiyanlou?page={}&tab=repositories'
        return (url_tmpl.format(i) for i in range(1,5))

    def parse(self,response):
        for github in response.css('li.col-12'):
            yield{
                "name":github.xpath('.//h3/a/text()').re_first('\n\s*(.*)'),
                "update_time":datetime.strptime(github.xpath('.//relative-time/@datetime').extract_first(),'%Y-%m-%dT%H:%M:%SZ')
                    }
