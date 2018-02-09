# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class StationMapItem(scrapy.Item):
    station_id = scrapy.Field()
    station_name = scrapy.Field()


class RailwayItem(scrapy.Item):
    # define the fields for your item here like:
        date = scrapy.Field()
        train_id = scrapy.Field()
        station_no = scrapy.Field()
        start_time = scrapy.Field()
        station_name = scrapy.Field()
        stopover_time = scrapy.Field()
        arrive_time = scrapy.Field()
