#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2023/11/7 22:54
# @Author  : 刘双喜
# @File    : HJ52.py
# @Description : https://www.nowcoder.com/practice/3959837097c7413a961a135d7104c314?tpId=37&tqId=21275&rp=1&ru=/exam/oj/ta&qru=/exam/oj/ta&sourceUrl=%2Fexam%2Foj%2Fta%3Fpage%3D1%26pageSize%3D50%26search%3D%26tpId%3D37%26type%3D37&difficulty=undefined&judgeStatus=undefined&tags=&title=
# 核心解题思路：dp为有i位字符和j位字符的编辑距离；0位字符就是另一个字符串的长度；转移方程为两个字符串各少一位的最小值+1和同时少一位加上当前位是否相等

def fun():
    n = input()
    m = input()
    dp = [[0 for i in range(len(m)+1)] for j in range(len(n)+1)]  # i和j位时的编辑距离，因为有0位，所以要+1
    for i in range(len(m)+1):  # 给默认值当一个字符串是空串时，编辑距离就是另一个字符串的长度
        dp[0][i] = i
    for i in range(len(n)+1):  # 给默认值当一个字符串是空串时，编辑距离就是另一个字符串的长度
        dp[i][0] = i
    for i in range(1, len(n)+1):  # 因为0字符的时候已经有默认值了，所以从1个字符开始遍历
        for j in range(1, len(m)+1):
            # 有i个或者j个字符的时候对应的是字符串索引是i-1或者j-1
            dp[i][j] = min(dp[i - 1][j] + 1, dp[i][j - 1] + 1, dp[i - 1][j - 1] + (n[i-1] != m[j-1]))
    print(dp[-1][-1])


fun()
