#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2023/11/9 23:44
# @Author  : 刘双喜
# @File    : HJ68.py
# @Description : sort排序
# https://www.nowcoder.com/practice/8e400fd9905747e4acc2aeed7240978b?tpId=37&tqId=21291&rp=1&ru=/exam/oj/ta&qru=/exam/oj/ta&sourceUrl=%2Fexam%2Foj%2Fta%3Fpage%3D1%26pageSize%3D50%26search%3D%26tpId%3D37%26type%3D37&difficulty=undefined&judgeStatus=undefined&tags=&title=


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