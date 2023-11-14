#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2023/11/12 21:15
# @Author  : 刘双喜
# @File    : HJ91.py
# @Description : https://www.nowcoder.com/practice/e2a22f0305eb4f2f9846e7d644dba09b?tpId=37&tqId=21313&rp=1&ru=%2Fexam%2Foj%2Fta&qru=%2Fexam%2Foj%2Fta&sourceUrl=%2Fexam%2Foj%2Fta%3Fpage%3D2%26pageSize%3D50%26search%3D%26tpId%3D37%26type%3D37&difficulty=undefined&judgeStatus=undefined&tags=&title=
# 核心解题思路：边界上的点都只有一种方法到达，其他点是从左边来的方法总数+从右边来的方法总数


def fun():
    n, m = list(map(int, input().strip().split(' ')))
    dp = [[1 for _ in range(m + 1)] for _ in range(n + 1)]
    for i in range(n + 1):
        for j in range(m + 1):
            dp[i][j] = dp[i - 1][j] + dp[i][j - 1] if i != 0 and j != 0 else 1
    print(dp[-1][-1])

fun()