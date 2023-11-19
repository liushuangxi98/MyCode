#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2023/11/12 17:57
# @Author  : 刘双喜
# @File    : HJ89.py
# @Description : DFS
# https://www.nowcoder.com/practice/7e124483271e4c979a82eb2956544f9d?tpId=37&tqId=21312&rp=1&ru=/exam/oj/ta&qru=/exam/oj/ta&sourceUrl=%2Fexam%2Foj%2Fta%3Fpage%3D1%26pageSize%3D50%26search%3D%26tpId%3D37%26type%3D37&difficulty=undefined&judgeStatus=undefined&tags=&title=
# 同24点计算一类题目，不过由于要打印计算过程，递归的时候需要记录
from itertools import permutations


def fun():
    s_map_int = {'A': 1, 'J': 11, 'Q': 12, 'K': 13, 'joker': 'ERROR', 'JOLER': 'ERROR'}
    int_map_s = {v:k for k,v in s_map_int.items()}
    p = [s_map_int.get(i) or int(i) for i in input().split(' ')]

    def dfs(value, n, idx):
        if idx == 4:
            return True if value == 24 else False
        if dfs(value + n[idx], n, idx + 1):
            res.append('+')
            return True
        if dfs(value - n[idx], n, idx + 1):
            res.append('-')
            return True
        if dfs(value * n[idx], n, idx + 1):
            res.append('*')
            return True
        if dfs(value // n[idx], n, idx + 1):
            res.append('/')
            return True

    if 'ERROR' in p:
        return print('ERROR')
    # 能得到24点的所有排序
    for n_i in list(permutations(p)):
        res, res_print = [], list(range(7))
        if dfs(n_i[0], n_i, 1):  # 能计算为24
            res_print[0::2], res_print[1::2] = [int_map_s.get(i) or str(i) for i in n_i], res[::-1]
            return print(''.join(res_print))
    return print('NONE')


fun()
