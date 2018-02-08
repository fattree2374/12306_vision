import csv
import requests
import json

# 读取车站和对应电报码文件，构造字典
# dict{ key = station_name, value = station_telecode }
station_map = dict()
with open('station_id_name_map.csv','r',newline='') as fd:
    reader = csv.reader(fd)
    for row in reader:
        station_map[row[1]] = row[0]
    fd.close()

response = requests.get('https://kyfw.12306.cn/otn/resources/js/query/train_list.js?scriptVersion=1.0')
train_set = set()  # 车次信息的集合，用于去重
data = json.loads(response.text[16:])

# 打开车次列表文件
with open('train_list.csv', 'a+', newline='') as csvfile:
    writer = csv.writer(csvfile)
    for (ate,date_train) in data.items():  # 迭代所有日期
        for (train_type, train_list) in date_train.items():  # 迭代同一日期的车次类型
            for train in train_list:
                # train 数据结构 {"station_train_code":"D1(北京-沈阳)","train_no":"24000000D10V"}
                train_no = train['train_no']  # 列车编号

                # 获得 车次，起点站，终点站
                code, from_station, to_station = train['station_train_code'].replace('(','-').replace(')','').split('-')
                from_station_telecode = station_map.get(from_station, '')  # 起点站电报码
                to_station_telecode = station_map.get(to_station, '')  # 终点站电报码

                # 按照 “车次-列车编号” 的格式作为集合的元素进行查重
                train_set_item = '%s-%s' % (code, train_no)

                if train_set_item not in train_set:  # 如果不是重复数据
                    train_set.add(train_set_item)  # 并入集合

                    # 写入csv文件
                    writer.writerow([code, train_no, from_station, to_station, from_station_telecode, to_station_telecode])

    csvfile.close()  # 关闭文件
print('总共抓取%d条车次信息' % len(train_set))

