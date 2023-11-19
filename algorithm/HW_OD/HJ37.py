#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2023/11/5 13:44
# @Author  : 刘双喜
# @File    : HJ37.py
# @Description : 动态规划；逻辑
# https://www.nowcoder.com/practice/1221ec77125d4370833fd3ad5ba72395?tpId=37&tqId=21260&rp=1&ru=/exam/oj/ta&qru=/exam/oj/ta&sourceUrl=%2Fexam%2Foj%2Fta%3Fpage%3D1%26pageSize%3D50%26search%3D%26tpId%3D37%26type%3D37&difficulty=undefined&judgeStatus=undefined&tags=&title=
# 核心解题思路：方法1：维护一个列表存储所有兔子每个兔子的年龄，循环i个月，到i月时所有兔子年龄+1。 循环所有兔子，有年龄大于等于3的则兔子列表追加1
# 方法2：第n个月的兔子个数=前一个月的数量 + 前2个月的数量（前2个月的都会生1个）。所以只用动态规划即可简单求解。

def fun():
    n = int(input())  # n个月
    rabbit_age_ls = [0]  # 每个兔子的年龄
    for i in range(1, 1 + n):  # 到了第i个月
        rabbit_age_ls = [_ + 1 for _ in rabbit_age_ls]
        for rabbit_age in rabbit_age_ls:
            if rabbit_age >= 3:
                rabbit_age_ls.append(1)
    print(len(rabbit_age_ls))


def fun2():
    n = int(input())
    dp = [0 for _ in range(n+1)]  # 第n个月的兔子数量
    dp[0] = dp[1] = dp[2] = 1  # 0月不算 前2个月兔子数量是1
    for i in range(3, 1+n):  # 从第3个月开始计算
        dp[i] = dp[i-1] + dp[i-2]
    print(dp[n])


fun2()
