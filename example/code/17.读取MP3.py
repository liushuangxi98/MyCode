#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2023/3/29 23:12
# @Author  : 刘双喜
# @File    : 17.读取MP3.py
# @Description : 添加描述
from mutagen.mp3 import MP3
import os


count = 0
for i in os.listdir('E:\\music'):
    if i == '排行榜':
        continue
    for j in os.listdir(f'E:\\music\\{i}'):
        if '.flac' in j:
            continue
        audio = MP3(f'E:\\music\\{i}\\{j}')
        if audio.info.length < 90:
            os.remove(f'E:\\music\\{i}\\{j}')
            count += 1
            print(j)
print(count)