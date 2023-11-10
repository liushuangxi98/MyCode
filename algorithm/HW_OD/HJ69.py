#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2023/11/10 19:55
# @Author  : 刘双喜
# @File    : HJ69.py
# @Description : 添加描述


def fun():
    def get_i_j_value(i, j):
        ls_a = a[i]
        ls_b = [b_row[j] for b_row in b]
        return sum([ls_a[ret_i] * ls_b[ret_i] for ret_i in range(len(ls_a))])
    row1, col1, col2 = int(input()), int(input()), int(input())
    row2 = col1
    a = [list(map(int, input().split(' '))) for _ in range(row1)]
    b = [list(map(int, input().split(' '))) for _ in range(row2)]
    res = [[get_i_j_value(i, j) for j in range(col2)] for i in range(row1)]
    for res_row in res:
        print(' '.join(list(map(str, res_row))))

fun()