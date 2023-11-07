#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2023/11/7 22:54
# @Author  : 刘双喜
# @File    : HJ52.py
# @Description : https://www.nowcoder.com/practice/3959837097c7413a961a135d7104c314?tpId=37&tqId=21275&rp=1&ru=/exam/oj/ta&qru=/exam/oj/ta&sourceUrl=%2Fexam%2Foj%2Fta%3Fpage%3D1%26pageSize%3D50%26search%3D%26tpId%3D37%26type%3D37&difficulty=undefined&judgeStatus=undefined&tags=&title=


def fun():
    n = input()
    m = input()
    dp = [[0 for i in range(len(m) + 1)] for j in range(len(n) + 1)]

    for idx, i in enumerate(n, 1):
        for jdx, j in enumerate(m, 1):
            dp[idx][jdx] = min(dp[idx - 1][jdx], dp[idx][jdx - 1])
            if i != j:
                dp[idx][jdx] += 1
    print(dp[-1][-1])


fun()
