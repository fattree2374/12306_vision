# -*- coding: utf-8 -*-
import scrapy
import json
from railway.items import RailwayItem
import requests


class Railway12306Spider(scrapy.Spider):
    name = 'railway_12306'
    allowed_domains = ['kyfw.12306.cn']
    start_urls = ['https://kyfw.12306.cn/otn/leftTicket/queryZ?leftTicketDTO.train_date=2018-02-08&leftTicketDTO.from_station=BJP&leftTicketDTO.to_station=SHH&purpose_codes=ADULT']

    def start_requests(self):
        for url in self.start_urls:
            response = requests.get(url)
            for sel in json.loads(response.text)['data']['result']:
                sel_list = sel.split('|')
                date = sel_list[13][0:4]+'-'+sel_list[13][4:6]+'-'+sel_list[13][6:8]
                train_url = 'https://kyfw.12306.cn/otn/czxx/queryByTrainNo?train_no={0}&from_station_telecode={1}&to_station_telecode={2}&depart_date={3}'.format(sel_list[2],sel_list[4],sel_list[5],date)
                yield scrapy.Request(train_url, callback=self.parse)

    def parse(self, response):
        for sel in json.loads(response.body.decode('utf-8'))['data']['data']:
            data = RailwayItem()
            data['station_no'] = sel['station_no']
            data['start_time'] = sel['start_time']
            data['isEnabled'] = sel['isEnabled']
            data['station_name'] = sel['station_name']
            data['stopover_time'] = sel['stopover_time']
            data['arrive_time'] = sel['arrive_time']
            yield data

