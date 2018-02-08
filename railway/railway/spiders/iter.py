# -*- coding: utf-8 -*-
import scrapy
import json
from railway.items import RailwayItem
import csv

# 读取车站和对应电报码文件，构造字典
station_map = dict()
with open('station_id_name_map.csv','r',newline='') as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        station_map[row[1]] = row[0]
    csvfile.close()


class Railway12306Spider(scrapy.Spider):
    name = 'railway_12306'
    allowed_domains = ['kyfw.12306.cn']
    start_urls = ['https://kyfw.12306.cn/otn/resources/js/query/train_list.js?scriptVersion=1.0']

    def parse(self, response):
        train_set = set()  # 车次信息的集合，用于去重
        data = json.loads(response.body.decode('utf-8')[16:])
        for (date,date_train) in data.items():  # 迭代所有日期
            for (train_type, train_list) in date_train.items():  # 迭代同一日期的车次类型
                for train in train_list:
                    train_no = train['train_no']  # 列车编号
                    # 车次，起点站，终点站
                    code, from_station, to_station = train['station_train_code'].replace('(','-').replace(')','').split('-')

                    # 按照 “车次-列车编号-起点站-终点站” 的格式加入集合
                    train_set.add('%s-%s-%s-%s' % (code, train_no, from_station, to_station))

        # 迭代参数格式
        iter_format = 'train_no=%s&from_station_telecode=%s&to_station_telecode=%s'
        for train in train_set:
            code, train_no, from_station, to_station = train.split('-')
            from_station_telecode = station_map[from_station]
            to_station_telecode = station_map[to_station]
            yield iter_format % (train_no, from_station_telecode, to_station_telecode)