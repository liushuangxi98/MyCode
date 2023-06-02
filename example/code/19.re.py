#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2023/4/6 23:41
# @Author  : 刘双喜
# @File    : 19.re.py
# @Description : 添加描述
import re
s = '我的姓名是刘双喜，我的性别是男，我的年龄是24岁'

res_tuple = re.search('姓名是(.*?)，.*?性别是(.*?)，.*?年龄是(.*?)岁', s)
res_dict = re.search('姓名是(?P<name>.*?)，.*?性别是(?P<sex>.*?)，.*?年龄是(?P<age>.*?)岁', s)
print(res_tuple.groups())
print(res_dict.groupdict())