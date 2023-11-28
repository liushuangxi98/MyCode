#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2023/7/23 15:06
# @Author  : 刘双喜
# @File    : 素数筛_求小于等于n的素数的个数.py
# @Description : 添加描述
def fun1(n):
    prime = bytearray([1] * (n + 1))
    prime[0] = prime[1] = 0  # 0和1不是质数
    i = 2
    while i * i <= n:
        if prime[i]:  # 从2开始，2是质数，将2的倍数都标记为非质数。
            prime[i * i:n + 1:i] = bytearray((n - i * i) // i + 1)
        i += 1
    print(prime.count(1))

def fun2(n):
    prime = [1] * (n + 1)
    prime[0] = prime[1] = 0  # 0和1不是质数
    i = 2
    while i * i <= n:
        if prime[i]:  # 从2开始，2是质数，将2的倍数都标记为非质数。
            prime[i * i:n + 1:i] = [0] * len(prime[i * i:n + 1:i])
        i += 1
    print(sum(prime))

fun1(1000)
fun2(1000)
