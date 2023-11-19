#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2023/11/15 21:56
# @Author  : 刘双喜
# @File    : HJ77.py
# @Description : DFS
# https://www.nowcoder.com/practice/97ba57c35e9f4749826dc3befaeae109?tpId=37&tqId=21300&rp=1&ru=/exam/oj/ta&qru=/exam/oj/ta&sourceUrl=%2Fexam%2Foj%2Fta%3FjudgeStatus%3D2%26page%3D1%26pageSize%3D50%26search%3D%26tpId%3D37%26type%3D37&difficulty=undefined&judgeStatus=3&tags=&title=
# 核心解题思路：递归当前进站的车，待进的车，站外的车，下一种情况是进还是出的所有可能。站内站外都没车了时退出，得一个结果
# 思路1：没进过的必须进，全进了必须出。两种情况之外递归一次进，一次出。
# 思路2：可以进则进，可以出则出。


def fun():
    def dfs(left: list, right: list, res_temp: list):
        # left代表站内的，right代表站外的,res_temp代表出战的
        if not right and not left:
            return res_list.append(res_temp)
        if not left:  # 没进过只能进
            dfs(left + [right[0]], right[1:], res_temp)
        elif not right:  # 进完了只能出
            dfs(left[:-1], right, res_temp + [left[-1]])
        else:
            dfs(left + [right[0]], right[1:], res_temp)  # 想进就进
            dfs(left[:-1], right, res_temp + [left[-1]])  # 想出就出

    n, train, res_list = input(), input().split(' '), []
    dfs([], train, [])
    [print(' '.join(i)) for i in sorted(res_list)]


fun()
