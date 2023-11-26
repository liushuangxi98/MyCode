#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2023/11/26 19:46
# @Author  : 刘双喜
# @File    : HK3.py
# @Description : 求[a,b]范围内非下降数的数量，非下降数123，223，233如此
N = 15

f = [[0] * N for _ in range(N)]


# 预处理出最高位为j的i位的非下降的数的数量
def init():
    for i in range(10): f[1][i] = 1
    for i in range(2, N):
        for j in range(10):
            # 有i位时，最高位为j时的非下降数数量为少一位时，如3位4开头最大下降数数量为2位4开头+5开头+++9开头的最大下降数数量之和
            f[i][j] = sum([f[i - 1][k] for k in range(j, 10)])
    for i in range(10): f[1][i] = i+1



def dp(n):
    # 特判0，有一个数满足条件
    if not n: return 1
    nums = []
    # 处理出n的每一位，存于nums中
    while n:
        nums.append(n % 10)
        n //= 10
    res, last = 0, 0  # last存储上一层的数
    # 从高到低枚举每一位
    for i in range(len(nums) - 1, -1, -1):
        x = nums[i]
        if last > x: break  # 如果当前位能取到的最大的数小于上一层上界，则退出
        # x_i不取上界
        for j in range(last, x):
            res += f[i + 1][j]
        # 取上界
        last = x
        if not i: res += 1  # 特判最后一个数
    return res

def get_x_non_decreasing(x: int):
    x_len, x_str = len(str(x)), str(x)

    res = [f[n][int(x_str[-n])] for n in range(1, x_len+1)]
    return sum(res)

init()

l, r = map(int, input().split())
# print(dp(r) - dp(l - 1))
print(get_x_non_decreasing(r) - get_x_non_decreasing(l))