#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2023/11/1 19:14
# @Author  : 刘双喜
# @File    : HJ24.py
# @Description : https://www.nowcoder.com/practice/6d9d69e3898f45169a441632b325c7b4?tpId=37&tqId=21247&rp=1&ru=/exam/oj/ta&qru=/exam/oj/ta&sourceUrl=%2Fexam%2Foj%2Fta%3Fpage%3D1%26pageSize%3D50%26search%3D%26tpId%3D37%26type%3D37&difficulty=undefined&judgeStatus=undefined&tags=&title=
# 解题核心思路：求出从左往右的每个位置左边最长递增子序列，再求出右往左每个位置最长递增子序列，相加减去本身即可
# 求最长递增子序列：列出了两种方法。
# 第一种：建立一维动态规划表，代表每个位置的最长递增子序列长度。遍历元素到i时，要求出i之前比i小的元素里最大的递增子序列长度。
# 方法是遍历i之前的元素j到i，如果i更大，且i的最长子序列比j小或者相等时，i的最长子序列长度+1

import bisect


def left_to_right_max_count(ls):
    """
    找出从左往右每个位置左侧最长递增子序列元素数量。
    1、循环列表每个元素i。
    2、循环列表当前元素的前面的元素j。
    3、如果当前元素i比前面的元素j大，且dp[i]较小，则dp更新当前元素i位置的数量为j元素数量+1
    :param ls:
    :return:
    """
    count = len(ls)
    dp = [1 for _ in range(count)]
    for i in range(0, len(ls)):
        for j in range(0, i):
            if ls[i] > ls[j] and dp[i] <= dp[j]:  # 注意and后面进行判断再赋值速度更快
                dp[i] = dp[j] + 1
    return dp

def left_to_right_max_count2(in_arr):
    """
    1.先取出列表第一个元素放在待定的最长递增子序列列表里，再循环其他元素，
    2.如果i大于最长递增子序列就添加到其最后,当前位置的最长递增子序列数量为列表长度
    3.如果i小于就把i替换掉最长递增子序列比它大的第一个数，当前位置的最长递增子序列数量和前一个一致
    :param in_arr:
    :return:
    """
    longest = [1] * len(in_arr)
    result = [in_arr[0]]
    arr_ls = list(enumerate(in_arr, 0))
    for idx, value in arr_ls[1:]:
        if value > result[-1]:
            result.append(value)
            longest[idx] = len(result)
        else:
            idx = bisect.bisect_left(result, value)
            result[idx] = value
            longest[idx] = longest[idx - 1]
    return longest


n = int(input())
hight_ls = list(map(int, input().split(' ')))
left = left_to_right_max_count2(hight_ls)
right = left_to_right_max_count(hight_ls[::-1])[::-1]
total = [left[i] + right[i] - 1 for i in range(len(left))]
print(len(hight_ls) - max(total))
