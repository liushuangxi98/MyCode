#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2023/11/4 20:40
# @Author  : 刘双喜
# @File    : HJ6.py
# @Description : https://www.nowcoder.com/practice/196534628ca6490ebce2e336b47b3607?tpId=37&rp=1&ru=%2Fexam%2Foj%2Fta&qru=%2Fexam%2Foj%2Fta&sourceUrl=%2Fexam%2Foj%2Fta%3Fpage%3D1%26pageSize%3D50%26search%3D%26tpId%3D37%26type%3D37&difficulty=&judgeStatus=&tags=&title=&gioEnter=menu
# 核心解题思路：求一个数的因子，只用求到它根号+1的值就行。（大于它根号+1还有


def fun2():
    n = m = int(input())

    if 1 < n <= 3:
        print(n)
    i = 2
    while i < int(n ** 0.5) + 1:
        while n % i == 0:
            n = n // i
            print(i, end=' ')
        i += 1

    if n > 1:
        print(n)

fun2()