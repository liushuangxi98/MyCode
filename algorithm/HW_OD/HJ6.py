#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2023/11/4 20:40
# @Author  : 刘双喜
# @File    : HJ6.py
# @Description : https://www.nowcoder.com/practice/196534628ca6490ebce2e336b47b3607?tpId=37&rp=1&ru=%2Fexam%2Foj%2Fta&qru=%2Fexam%2Foj%2Fta&sourceUrl=%2Fexam%2Foj%2Fta%3Fpage%3D1%26pageSize%3D50%26search%3D%26tpId%3D37%26type%3D37&difficulty=&judgeStatus=&tags=&title=&gioEnter=menu
# 核心解题思路：求一个数的因子，只用求到它根号+1的值就行。例如求16的因子，因为是从小求到大，所以因子不会超过4+1

def fun1():
    def is_prime(x):
        if x == 1:
            return False
        for _i in range(2, 1 + int(x ** 0.5)):
            if x % _i == 0:
                return False
        return True

    n = int(input())
    res = []
    i = 2
    while i < 1 + int(n ** 0.5):
        # 如果是因子，且是质数，则不断除以此数
        if n % i == 0:  # and is_prime(i):  # 由于n已经对比i小的所有数取余过了，所以如果能对i取余为0，则i必是质数
            while n % i == 0:
                n //= i
                res.append(str(i))
        i += 1
    if is_prime(n):
        res.append(str(n))
    print(' '.join(res))


def fun2():
    n = int(input())
    if 1 < n <= 3:
        print(n)
    i = 2
    while i < int(n ** 0.5) + 1:
        while n % i == 0:  # 由于n已经对比i小的所有数取余过了，所以如果能对i取余为0，则i必是质数
            n = n // i
            print(i, end=' ')
        i += 1

    if n > 1:
        print(n)

fun2()