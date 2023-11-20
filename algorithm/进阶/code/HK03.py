#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2023/11/20 21:59
# @Author  : 刘双喜
# @File    : HK03.py
# @Description : 添加描述

def find_max_equal_sum_subsequences(arr):
    # 创建一个字典来存储子序列的和及其对应的索引
    sum_to_subsequence_indices = {}

    # 遍历数组中的每个元素
    for i in range(len(arr)):
        sum = 0
        # 计算所有可能的连续子序列的和
        for j in range(i, len(arr)):
            sum += arr[j]
            # 如果这个和在字典中还不存在，就创建一个新的键值对
            if sum not in sum_to_subsequence_indices:
                sum_to_subsequence_indices[sum] = []
            # 将子序列的开始和结束索引添加到对应的列表中
            sum_to_subsequence_indices[sum].append((i, j))

    max_count = 0
    # 遍历字典中的每个值（即索引列表）
    for indices in sum_to_subsequence_indices.values():
        # 根据子序列的结束索引进行排序
        indices.sort(key=lambda x: x[1])
        count = 1
        end = indices[0][1]
        # 遍历索引列表中的每个元素
        for i in range(1, len(indices)):
            # 如果当前子序列的开始索引大于前一个子序列的结束索引，就增加计数
            if indices[i][0] > end:
                count += 1
                end = indices[i][1]
        # 更新最大计数
        max_count = max(max_count, count)
    return max_count


arr = [-1, 0, 4, -3, 6, 5, -6, 5, -7, -3]
print(find_max_equal_sum_subsequences(arr))
