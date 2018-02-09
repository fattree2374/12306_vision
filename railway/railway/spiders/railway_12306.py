# -*- coding: utf-8 -*-
import scrapy
import json
from railway.items import RailwayItem
import requests
import csv

train_list = []
with open('train_list.csv','r',newline='') as fd:
    reader = csv.reader(fd)
    for row in reader:
        train_list.append(row)
    fd.close()

class Railway12306Spider(scrapy.Spider):
    name = 'railway_12306'
    allowed_domains = ['kyfw.12306.cn']
    # start_urls = ['https://kyfw.12306.cn/otn/leftTicket/queryZ?leftTicketDTO.train_date=2018-02-08&leftTicketDTO.from_station=BJP&leftTicketDTO.to_station=SHH&purpose_codes=ADULT']

    def start_requests(self):
        for sel in train_list:
            data = RailwayItem()
            data['date'] = sel[0]
            data['train_id'] = sel[1]
            train_url = 'https://kyfw.12306.cn/otn/czxx/queryByTrainNo?train_no={0}&from_station_telecode={1}&to_station_telecode={2}&depart_date={3}'.format(sel[2],sel[5],sel[6],sel[0])
            yield scrapy.Request(train_url, meta={'item':data}, callback=self.parse)

    def parse(self, response):
        for sel in json.loads(response.body.decode('utf-8'))['data']['data']:
            data = response.meta['item']
            data['station_no'] = sel['station_no']
            data['start_time'] = sel['start_time']
            data['station_name'] = sel['station_name']
            data['stopover_time'] = sel['stopover_time']
            data['arrive_time'] = sel['arrive_time']
            yield data

