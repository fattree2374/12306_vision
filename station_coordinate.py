# -*- coding: utf-8 -*-
import csv
import time
from geopy.geocoders import Nominatim
from urllib.error import HTTPError
from geopy.exc import GeocoderTimedOut,GeocoderServiceError

stations = []
no_stations = []
with open('station_id_name_map.csv','r',newline='') as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        stations.append(row[1]+'站')
    csvfile.close()

def link_geopy(station):
    geolocator = Nominatim()
    try:
        location = geolocator.geocode(station, timeout=10)
        return location
    except GeocoderTimedOut:
        print('GeocoderTimedOut,尝试重新查询')
        time.sleep(3)
        link_geopy(station)
    except GeocoderServiceError:
        print('GeocoderServiceError,尝试重新查询')
        time.sleep(3)
        link_geopy(station)

def query_coordinate(index,station):
    location = link_geopy(station)
    if(location is None):
        print(index,station,'无地理信息')
        no_stations.append(station)
        with open('no_station_location.csv','a+',newline='') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow([station])
            csvfile.close()
    else:
        print(index,station,location.latitude,location.longitude)
        with open('station_location.csv','a+',newline='') as csvfile:
            writer = csv.writer(csvfile)
            L = [station,location.latitude,location.longitude]
            writer.writerow(L)
            csvfile.close()

for index,station in enumerate(stations[410:]):
    index+=410
    query_coordinate(index, station)

print(no_stations)


