#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2024/5/5 18:22
# @Author  : 刘双喜
# @File    : 59.怪猎克制素材.py
# @Description : 添加描述
import requests
import re
import pandas as pd

# 爬取数据
url = 'https://api.xiaoheihe.cn/wiki/get_article_for_app/?article_id=9351102&wiki_id=1000000020&is_share=1'
header = {
    'User-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36'}
response = requests.get(url, headers=header)
date = response.text
# 解析数据
pattern = re.compile("""\{"name":"(?P<name>.*?)","craft":"(?P<craft>.*?)","sl":"(?P<sl>.*?)","hd":"(?P<hd>.*?)","lsh":"(?P<lsh>.*?)","zq":"(?P<zq>.*?)","ry":"(?P<ry>.*?)","bx":"(?P<bx>.*?)"},""")
lines = pattern.finditer(date)
data_lst = []
for idx, line in enumerate(lines):
    line_dict = line.groupdict()
    value = list(line_dict.values())
    data_lst += [value]
df = pd.DataFrame(data_lst, columns=['怪物名称', '素材名称', '森林', '荒地','陆珊瑚', '瘴气', '熔岩', '冰雪'])
df.to_excel('..//data//59.怪猎克制素材.xlsx')
# {"name":"水妖鸟","craft":"保水滋润的喉袋","sl":"","hd":"","lsh":"o","zq":"","ry":"","bx":""},