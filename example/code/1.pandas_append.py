#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 31/10/2022 下午10:20
# @Author  : 刘双喜
# @File    : pandas_append.py
# @Description : 添加描述
import pandas as pd

data1 = [['a', 1], ['b', 2]]
data2 = [['c', 3], ['d', 4]]
pd_1 = pd.DataFrame(data1, columns=['A', 'B'])
pd_2 = pd.DataFrame(data2, columns=['A', 'B'])
pd_3 = pd_1.append(pd_2)
print(pd_3)
