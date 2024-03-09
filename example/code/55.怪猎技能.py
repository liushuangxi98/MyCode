#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2024/1/30 23:37
# @Author  : 刘双喜
# @File    : 55.怪猎技能.py
# @Description : 添加描述
#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2024/1/30 22:11
# @Author  : 刘双喜
# @File    : 53.怪猎装备爬虫.py
# @Description : 添加描述
import requests
import re
import pandas as pd


# 爬取数据
url = 'https://api.xiaoheihe.cn/wiki/get_article_for_app/?article_id=1256671&wiki_id=582010&is_share=1'
header = {'User-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36'}
response = requests.get(url, headers=header)
date = response.text
# 解析数据
pattern = '{"id":"(?P<name>.*?)","skill_img":"(?P<skill_img>.*?)","type":"(?P<Type>.*?)","series":"(?P<series>.*?)","lv1":"(?P<lv1>.*?)","lv2":"(?P<lv2>.*?)","lv3":"(?P<lv3>.*?)","lv4":"(?P<lv4>.*?)","lv5":"(?P<lv5>.*?)","lv6":"(?P<lv6>.*?)","lv7":"(?P<lv7>.*?)"}'
pattern = re.compile(pattern)
lines = pattern.finditer(date)
# 存储数据
data_lst = []
for idx, line in enumerate(lines):
    line_dict = line.groupdict()
    data_lst += [line_dict]
df = pd.DataFrame(data_lst)
df.to_excel('..//data//55.怪猎技能.xlsx')

