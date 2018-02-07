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
        # end_station_name = scrapy.Field()
        # service_type = scrapy.Field()
        station_no = scrapy.Field()
        start_time = scrapy.Field()
        # start_station_name = scrapy.Field()
        isEnabled = scrapy.Field()
        # station_train_code = scrapy.Field()
        station_name = scrapy.Field()
        stopover_time = scrapy.Field()
        arrive_time = scrapy.Field()
        # train_class_name = scrapy.Field()

    # train_id = scrapy.Field()
    # start_point = scrapy.Field()
    # end_point = scrapy.Field()
    # start_time = scrapy.Field()
    # end_time = scrapy.Field()
    # whether_today_train = scrapy.Field()
    # vip_seat = scrapy.Field()
    # 1st_seat = scrapy.Field()
    # 2nd_seat = scrapy.Field()
    # senior_soft_sleeping_ticket = scrapy.Field()
    # soft_sleeping_ticket = scrapy.Field()
    # moving_sleeping_ticket = scrapy.Field()
    # stiff_sleeping_ticket = scrapy.Field()
    # standing_ticket = scrapy.Field()
