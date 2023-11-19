#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2023/11/10 19:55
# @Author  : 刘双喜
# @File    : HJ69.py
# @Description : 逻辑
# https://www.nowcoder.com/practice/ebe941260f8c4210aa8c17e99cbc663b?tpId=37&tqId=21292&rp=1&ru=/exam/oj/ta&qru=/exam/oj/ta&sourceUrl=%2Fexam%2Foj%2Fta%3Fpage%3D1%26pageSize%3D50%26search%3D%26tpId%3D37%26type%3D37&difficulty=undefined&judgeStatus=undefined&tags=&title=


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