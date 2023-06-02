#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2023/3/18 23:17
# @Author  : 刘双喜
# @File    : 13.创建文件夹.py
# @Description : 添加描述
import os

songer_list = ['周杰伦', '林俊杰', '金莎',]
f = open('13.歌手.txt','r',encoding='utf-8')
for i in f.readlines():
    i = i.strip()
    if i not in os.listdir('13'):
        os.mkdir(f'13/{i}')