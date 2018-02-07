# 12306_vision
该项目用来爬取12306的列车数据，并将其可视化

****
    
|Author1|lingshhy|
|---|---
|E-mail|3063007539@qq.com

|Author2|vorphan|
|---|---
|E-mail|vorphan@qq.com

****
## 目录
* [待办清单](#待办清单)
* [数据库结构](#数据库结构)

****
### 待办清单
-----------
- [ ] 爬取车次数据
- [ ] 爬取车站映射表
- [ ] 数据库构建（包装成一个py文件）并且为爬虫添加扫尾（写入数据库）文件
- [ ] 后续的数据分析
- [ ] 爬取车站地理位置

****
### 数据库结构
-----------
|station_train_code|arrive_time|start_time|station_name|station_no|stoppover_time|
|:--:|:-------------:|:-----------:|:------:|:------:|:---:|
|G101|06:43|06:43|北京南|01|3分钟|

|station_id|station_name|
|:----------:|:-----:|
|BJP|北京|

|station_id|coordinate|
|:----------:|:-----:|
|BJP|地理坐标|