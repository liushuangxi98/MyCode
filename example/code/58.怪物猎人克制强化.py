#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2024/5/5 17:18
# @Author  : 刘双喜
# @File    : 58.怪物猎人克制强化.py
# @Description : 添加描述
import requests
import re
import pandas as pd

# 爬取数据
url = 'https://api.xiaoheihe.cn/wiki/get_article_for_app/?article_id=3005700&wiki_id=1000000020&is_share=1'
header = {
    'User-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36'}
response = requests.get(url, headers=header)
date = response.text
# 解析数据
pattern = re.compile("""\{"name":"(?P<name>.*?)","rare":"(?P<rare>.*?)","type":"(?P<type>.*?)","level":"(?P<level>.*?)","num":"(?P<num>.*?)","craft_1":"(?P<craft_1>.*?)","craft_2":"(?P<craft_2>.*?)","craft_3":"(?P<craft_3>.*?)","craft_4":"(?P<craft_4>.*?)","cost":"(?P<cost>.*?)"},""")
lines = pattern.finditer(date)
data_lst = []
for idx, line in enumerate(lines):
    line_dict = line.groupdict()
    value = list(line_dict.values())
    sucai = [i.split('×') for i in value[5:9]]
    sucai = [i if len(i) == 2 else [i[0], '' if i[0] == '' else 1] for i in sucai]
    sucai = [j for i in sucai for j in i]
    data_lst += [value[0:5]+sucai+value[9:]]
df = pd.DataFrame(data_lst, columns=['强化名称', '武器品质', '强化方向', '强化等级','占用强化槽', '素材1', '数量', '素材2', '数量', '素材3', '数量', '素材4', '数量', '调查点数'])
df.to_excel('..//data//57.怪猎克制强化.xlsx')
# {"name":"攻击力强化Ⅰ","rare":"10","type":"攻击","level":"1","num":"3","craft_1":"摇曳炎毛皮×9","craft_2":"龙脉的强龙骨×3","craft_3":"荒地岩骨×5","craft_4":"","cost":"400"},