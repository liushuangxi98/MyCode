#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2024/1/30 22:41
# @Author  : 刘双喜
# @File    : 54.硬币分钱.py
# @Description : 添加描述
money = 10


def fun1(_money):
    def dfs(n, res_ls, _res_ls_all):
        """
        n分钱的所有分的方案，是求的分的排列
        :param n: 剩余钱
        :param res_ls: 每次分的方法的结果列表
        :param _res_ls_all: 所有的分的结果
        :return: 是否分完
        """
        if n <= 0:
            _res_ls_all.append(sorted(res_ls[::]))
            return True
        # 剩余钱大于3,2,1时，不同的情况
        if n >= 3:
            dfs(n - 3, res_ls + [3], _res_ls_all)
        if n >= 2:
            dfs(n - 2, res_ls + [2], _res_ls_all)
        if n >= 1:
            dfs(n - 1, res_ls + [1], _res_ls_all)

    # 所有的结果和去重后的结果
    res_ls_all, _res_ls_all = [], []
    dfs(_money, [], res_ls_all)
    for i in res_ls_all:
        if i not in _res_ls_all:
            _res_ls_all.append(i)
    print(len(_res_ls_all))


def fun2(_money):
    res = 0
    for i in range(0, _money // 3 + 1, 1):
        # 3分钱i个
        for j in range(0, (_money - 3 * i) // 2 + 1, 1):
            # 2分钱j个
            rest, res = _money - 2 * j - 3 * i, res + 1
    print(res)


def fun3(_money):
    # 3分的有i个时，剩余的钱
    sub1 = [_money - 3 * i for i in range(0, _money // 3 + 1)]
    # 3分的有i个时，剩余的钱可以买j个2分
    sub2 = [r // 2 + 1 for r in sub1]
    print(sum(sub2))


fun1(money)
fun2(money)
fun3(money)
