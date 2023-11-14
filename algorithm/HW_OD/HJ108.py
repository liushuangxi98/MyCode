#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2023/11/13 21:46
# @Author  : 刘双喜
# @File    : HJ108.py
# @Description : https://www.nowcoder.com/practice/22948c2cad484e0291350abad86136c3?tpId=37&tqId=21331&rp=1&ru=/exam/oj/ta&qru=/exam/oj/ta&sourceUrl=%2Fexam%2Foj%2Fta%3Fpage%3D3%26pageSize%3D50%26search%3D%26tpId%3D37%26type%3D37&difficulty=undefined&judgeStatus=undefined&tags=&title=
# 最大公倍数一定是a,b某个数的倍数。遍历到a*b即可，步长以a,b中的较大值为步长。
# 不用2个数取余，对较小数取余即可，因为步长是较大数
# 循环起始点为较大值即可

def fun():
    a, b = list(map(int, input().split(' ')))
    a, b = (a, b) if a > b else (b, a)
    for i in range(a, 1 + a * b, a):
        if i == 0:
            continue
        if i % b == 0 and i != 0:
            return print(i)


fun()
