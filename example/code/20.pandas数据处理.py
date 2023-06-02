#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2023/4/6 23:51
# @Author  : 刘双喜
# @File    : 20.pandas数据处理.py
# @Description : 添加描述
import pandas as pd

data = pd.read_excel('18.excel-demo.xlsx')

print(data.iterrows())
for i in data.iterrows():
    print(i)
print(data.to_dict('dict'))
print(data.to_dict('list'))
print(data.to_dict('records'))
print(data.to_dict('split'))