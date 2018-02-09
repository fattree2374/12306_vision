# -*- coding: utf-8 -*-
import csv
# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html


class RailwayPipeline(object):
    def process_item(self, item, spider):
        # with open('station_id_name_map.csv','a+',newline='') as csvfile:
        #     writer = csv.writer(csvfile)
        #     L=[item['station_id'],item['station_name']]
        #     writer.writerow(L)
        #     csvfile.close()

        with open('station_data.csv','a+',newline='') as csvfile:
            writer = csv.writer(csvfile)
            L=[item['date'], item['train_id'], item['station_no'],item['station_name'],item['start_time'],item['stopover_time'],item['arrive_time']]
            writer.writerow(L)
            csvfile.close()