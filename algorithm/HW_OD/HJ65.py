#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2023/11/10 18:48
# @Author  : 刘双喜
# @File    : HJ65.py
# @Description : https://www.nowcoder.com/practice/181a1a71c7574266ad07f9739f791506?tpId=37&tqId=21288&rp=1&ru=/exam/oj/ta&qru=/exam/oj/ta&sourceUrl=%2Fexam%2Foj%2Fta%3Fpage%3D1%26pageSize%3D50%26search%3D%26tpId%3D37%26type%3D37&difficulty=undefined&judgeStatus=undefined&tags=&title=
# 核心解题思路：遍历短串索引i，再遍历短串每个i到末尾、末尾-1，。。。，i的子串。判断子串是否在长串内，再即可braak当前索引。

def fun():
    s1, s2 = input(), input()
    max_com_sub_s = ''
    s1, s2 = (s1, s2) if len(s1) < len(s2) else (s2, s1)  # s1是短的
    for i in range(len(s1)):  # 遍历短的
        for j in range(len(s1), i, -1):  # 从末尾开始遍历，有子串时即可退出
            if s1[i:j] in s2 and len(s1[i:j]) > len(max_com_sub_s):  # 找到子串并且长度更大
                max_com_sub_s = s1[i:j]  # 替换最大子串
                break
    print(max_com_sub_s)


def fun_dp():
    s1, s2 = input(), input()
    s1, s2 = (s1, s2) if len(s1) < len(s2) else (s2, s1)  # s1是短的
    dp = [[0 for _ in s2] for _ in s1]  # s1的i位和s2的j位时的最大公共子串长度
    max_len, max_com_sub_s = 0, ''
    for i in range(0, len(s1)):  # 遍历s1的每个位置
        for j in range(0, len(s2)):  # 遍历s2的每个位置
            if s1[i] == s2[j]:  # 当前位置相等时，
                if i == 0 or j == 0:  # 如果是开头，那自然是1
                    dp[i][j] = 1
                else:   # 动态转移方程为s1 s2上一位的dp值+1
                    dp[i][j] = dp[i-1][j-1] + 1
                if dp[i][j] > max_len:  # 更新最大值，因为最大值不是dp[-1][-1]
                    max_len = dp[i][j]
                    max_com_sub_s = s2[j-max_len+1:j+1]
    print(max_com_sub_s)


fun_dp()
