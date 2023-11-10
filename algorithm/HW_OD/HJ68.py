#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2023/11/9 23:44
# @Author  : 刘双喜
# @File    : HJ68.py
# @Description : 添加描述


def fun():
    n = int(input())
    seq = True if input().strip() == '0' else False
    info = []
    for _ in range(n):
        name, grade = input().split(' ')
        info.append([name, grade])
    info.sort(key=lambda x: int(x[1]), reverse=seq)
    for i in info:
        print(' '.join(i))
fun()