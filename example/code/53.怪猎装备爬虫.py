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
url = 'https://api.xiaoheihe.cn/wiki/get_article_for_app/?article_id=1257268&wiki_id=582010&is_share=1'
header = {'User-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36'}
response = requests.get(url, headers=header)
date = response.text
# 解析数据
pattern = '{"id":"(?P<name>.*?)","def_img":"(?P<img_path>.*?)","rare":"(?P<class>.*?)","def":"(?P<def>.*?)",' \
          '"socket1":"(?P<socket1>.*?)","socket2":"(?P<socket2>.*?)","socket3":"(?P<socket3>.*?)",' \
          '"skill_n1":"(?P<skill_name_1>.*?)","skill_l1":"(?P<skill_level_1>.*?)",' \
          '"skill_n2":"(?P<skill_name_2>.*?)","skill_l2":"(?P<skill_level_2>.*?)",' \
          '"series":"(.*?)"}'
pattern = re.compile(pattern)
lines = pattern.finditer(date)
# 存储数据
data_lst = []
for idx, line in enumerate(lines):
    line_dict = line.groupdict()
    line_dict['part'] = line_dict.pop('img_path')[-7:-5]
    data_lst += [line_dict]
df = pd.DataFrame(data_lst)
df.to_excel('..//data//54.怪猎防具.xlsx')
