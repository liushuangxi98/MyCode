#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2023/11/9 23:32
# @Author  : 刘双喜
# @File    : HJ60.py
# @Description : https://www.nowcoder.com/practice/f8538f9ae3f1484fb137789dec6eedb9?tpId=37&tqId=21283&rp=1&ru=/exam/oj/ta&qru=/exam/oj/ta&sourceUrl=%2Fexam%2Foj%2Fta%3Fpage%3D1%26pageSize%3D50%26search%3D%26tpId%3D37%26type%3D37&difficulty=undefined&judgeStatus=undefined&tags=&title=


def fun():
    def is_prime(num):
        if num == 1:
            return False
        if num <= 3:
            return True
        for i in range(3, int(num ** 0.5)+1):
            if num % i == 0:
                return False
        return True

    n = int(input())
    if n == 4:
        print(2)
        print(2)
        exit()
    for i in range(n//2, n+1, 1):
        if i % 2 == 0:
            continue
        if is_prime(i) and is_prime(n - i):
            break
    print(n - i)
    print(i)

fun()