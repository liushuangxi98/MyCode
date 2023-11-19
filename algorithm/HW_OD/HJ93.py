#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2023/11/15 18:39
# @Author  : 刘双喜
# @File    : HJ93.py
# @Description : DFS
# https://www.nowcoder.com/practice/9af744a3517440508dbeb297020aca86?tpId=37&tqId=21316&rp=1&ru=/exam/oj/ta&qru=/exam/oj/ta&sourceUrl=%2Fexam%2Foj%2Fta%3Fpage%3D1%26pageSize%3D50%26search%3D%26tpId%3D37%26type%3D37&difficulty=undefined&judgeStatus=undefined&tags=&title=
# 核心解题思路：将数据分为3组，3整除和5整除和任意组。递归任意组每一个数，分别尝试将它放入3组和5组，直到递归到最后一位时结算，是否相等。
# 核心解题思路2：欲得res=arr3-arr5=0，所以直接计算arr3-arr5结果，再遍历每一个任意组的数，res加它或者减它。遍历完后判断res里是否有为0的结果，有则相等。

def fun():
    def dfs(_arr_3, _arr_5, i):
        if i == len(arr_other):  # 结算
            return True if sum(_arr_3) == sum(_arr_5) else False
        if dfs(_arr_3 + [arr_other[i]], _arr_5, i + 1) or dfs(_arr_3, _arr_5 + [arr_other[i]], i + 1):
            return True
        else:
            return False

    n, arr = input(), list(map(int, input().strip().split(' ')))
    arr_3, arr_5, arr_other = [i for i in arr if i % 3 == 0 and i % 5 != 0], [i for i in arr if i % 5 == 0], \
        [i for i in arr if i % 3 != 0 and i % 5 != 0]
    print('true' if dfs(arr_3, arr_5, 0) else 'false')


def fun2():
    def dfs(_res, idx):
        if idx == len(arr_else):
            return True if _res == 0 else False
        if dfs(_res + arr_else[idx], idx + 1) or dfs(_res - arr_else[idx], idx + 1):
            return True
        else:
            return False

    n, arr = input(), list(map(int, input().strip().split(' ')))
    res = sum([i if i % 3 == 0 and i % 5 != 0 else (-i if i % 5 == 0 else 0) for i in arr])
    arr_else = [i for i in arr if i % 3 != 0 and i % 5 != 0]
    print('true' if dfs(res, 0) else 'false')

fun2()
