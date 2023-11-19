#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2023/11/12 12:20
# @Author  : 刘双喜
# @File    : HJ82.py
# @Description : DFS+基础数学
# https://www.nowcoder.com/practice/e0480b2c6aa24bfba0935ffcca3ccb7b?tpId=37&tqId=21305&rp=1&ru=/exam/oj/ta&qru=/exam/oj/ta&sourceUrl=%2Fexam%2Foj%2Fta%3Fpage%3D1%26pageSize%3D50%26search%3D%26tpId%3D37%26type%3D37&difficulty=undefined&judgeStatus=undefined&tags=&title=
# 核心解题思路：用递归，每次求刚好比分数n小的分子是1的分数res就行。每次递归将求的res保存，n减去res，继续递归。

def fun():
    n, res = list(map(int,input().split('/'))), []

    def dfs(num):
        num = [1, num[1] // num[0]] if num[1] % num[0] == 0 else num  # 如果可以约分，则约分
        if num[0] == 1:  # 分子已经是1
            return res.append(num[1])
        i = (num[1] // num[0]) + 1  # 临近num的最大的分数的分母
        res.append(i)
        return dfs([num[0]*i - num[1], num[1]*i][::])  # num做减法后，寻找下一个num的结果

    dfs(n[::])
    print('+'.join([f'1/{i}' for i in res]))

fun()