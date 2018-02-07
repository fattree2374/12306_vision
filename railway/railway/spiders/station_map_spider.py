# -*- coding: utf-8 -*-
import scrapy
import json
from railway.items import StationMapItem
import requests
import re


class StationMapSpider(scrapy.Spider):
    name = 'station_map_spider'
    allowed_domains = ['kyfw.12306.cn']
    start_urls = ['https://kyfw.12306.cn/otn/resources/js/framework/station_name.js?station_version=1.9018']

    def parse(self, response):
        station_string = re.search(r'(?<=\').+(?=\')', response.body.decode('utf-8'), re.DOTALL).group()
        station_maps = station_string.split('@')
        del station_maps[0]
        for item in station_maps:
            station = item.split('|')
            station_map = StationMapItem()
            station_map['station_id'] = station[2]
            station_map['station_name'] = station[1]
            yield station_map
