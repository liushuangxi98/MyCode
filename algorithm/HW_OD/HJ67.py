#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2023/11/7 21:21
# @Author  : 刘双喜
# @File    : HJ67.py
# @Description : DFS
# https://www.nowcoder.com/practice/fbc417f314f745b1978fc751a54ac8cb?tpId=37&tqId=21290&rp=1&ru=/exam/oj/ta&qru=/exam/oj/ta&sourceUrl=%2Fexam%2Foj%2Fta%3Fpage%3D1%26pageSize%3D50%26search%3D%26tpId%3D37%26type%3D37&difficulty=undefined&judgeStatus=undefined&tags=&title=
from itertools import permutations


def fun():
    num = list(map(int, input().split(' ')))

    def dfs(n, value, i):
        if i == 3:  # 当前列表已经递归完
            return True if value == 24 else False  # 当前递归计算的值是不是24
        # 递归当前列表的每一种运算
        if dfs(n, value + n[i + 1], i + 1) or dfs(n, value - n[i + 1], i + 1) or dfs(n, value * n[i + 1], i + 1) or dfs(n, value / n[i + 1], i + 1):
            return True
        elif i == 1 and (dfs(n, value * (n[i+1] + n[i+2]), i+2) or dfs(n, value * (n[i+1] - n[i+2]), i+2)):  # 后两位是括号
            return True
        elif i == 1 and ((n[i+1] - n[i+2] != 0 and dfs(n, value / (n[i+1] - n[i+2]), i+2)) or dfs(n, value / (n[i+1] + n[i+2]), i+2)):  # 后两位是括号
            return True
        return False
    # 循环输入的4位数的排列
    for _n in list(permutations(num)):
        if dfs(_n, _n[0], 0):  # 只要有一种满足则停止
            print('true')
            return
    print('false')


fun()
