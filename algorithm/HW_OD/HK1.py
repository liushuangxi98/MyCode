#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2023/11/7 22:02
# @Author  : 刘双喜
# @File    : HK1.py
# @Description : 排列实现

def permute(ls):
    ret = []

    def _permute(data, i, length):
        if i == length:
            ret.append(data[::])
        else:
            for j in range(i, length):  # 函数会遍历从索引 i 到 length 的所有元素，并将它们与索引 i 处的元素交换
                data[i], data[j] = data[j], data[i]
                _permute(data, i + 1, length)
                data[i], data[j] = data[j], data[i]

    _permute(ls, 0, len(ls))
    return ret


def permute2(data):
    # 当数据集只有一个元素时，返回该元素
    # 这是递归的基本情况，也就是递归结束的条件
    if len(data) == 1:
        return [data]

    permutations = []  # 用于存储所有的排列

    # 对数据集中的每个元素，我们生成其余元素的所有排列
    for i in range(len(data)):
        # data[:i] + data[i+1:] 是一个新列表，包含了除了第i个元素之外的所有元素
        rest = data[:i] + data[i+1:]

        # 对剩余的元素进行递归，生成它们的所有排列
        for p in permute(rest):
            # 将当前元素添加到这些排列的前面，并将结果添加到排列列表中
            permutations.append([data[i]] + p)

    # 返回所有的排列
    return permutations


print(permute2([1, 2, 3, 4]))
