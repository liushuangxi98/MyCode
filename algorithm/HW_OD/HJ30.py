#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2023/11/5 15:47
# @Author  : 刘双喜
# @File    : HJ30.py
# @Description : https://www.nowcoder.com/practice/d3d8e23870584782b3dd48f26cb39c8f?tpId=37&tqId=21253&rp=1&ru=/exam/oj/ta&qru=/exam/oj/ta&sourceUrl=%2Fexam%2Foj%2Fta%3Fpage%3D1%26pageSize%3D50%26search%3D%26tpId%3D37%26type%3D37&difficulty=undefined&judgeStatus=undefined&tags=&title=

def fun():
    s = list(input().replace(' ', ''))
    s[0::2] = sorted(s[0::2])
    s[1::2] = sorted(s[1::2])
    for i in s:
        if i in '0123456789abcdefABCDEF':
            i = int(i, base=16)  # 转16进制
            i = bin(i)[2:].rjust(4, '0')  # 转二进制并去掉前两位
            i = i[::-1]  # 二进制倒置
            i = int(i,base=2)  # 二进制转10
            i = hex(i)[2:]  # 十进制转16去掉前缀
            i = i.upper()  # 转大写
        print(i, end='')


fun()
