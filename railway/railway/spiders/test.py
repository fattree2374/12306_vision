# -*- coding: utf-8 -*-
import csv
from geopy.geocoders import Nominatim
from urllib.error import HTTPError

stations = []
no_stations = []
with open('station_id_name_map.csv','r',newline='') as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        stations.append(row[1]+'站')
    csvfile.close()

def query_coordinate(index,station):
    geolocator = Nominatim()
    try:
        location = geolocator.geocode(station, timeout=None)
    except HTTPError:
        return station,'HTTPError'
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

for index,station in enumerate(stations):
    query_coordinate(index, station)

print(no_stations)

















# for i in itertools.combinations(stations,2):
#     print(i)
# print(len([x for x in itertools.combinations(stations,2)]))
