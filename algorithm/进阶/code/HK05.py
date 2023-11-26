#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2023/11/22 18:45
# @Author  : 刘双喜
# @File    : HK05.py
# @Description : 双指针
# 求字符串中子串中，不包含指定元素且子串重复元素最多2个的，最长子串
# fun1暴力遍历，fun2在暴力遍历的基础上优化判断有么有不允许字符和字符数量的复杂度到1，但没啥用
# fun3双指针最好，左右都用0开始，右指针+1，遇到新字符的数量大于2时，移动左指针，直到小于2再继续。遇到不允许的字符时，左右指针都跳过从其后开始。

# 输入
# D
# ABACA123D
# 输出7
import time


def fun1():
    no_s = 'D'
    s = 'ABACA123DC' * 58000
    st = time.time()

    s_len = len(s)
    res = 0
    for i in range(s_len):
        for j in range(i, s_len):
            sub_s = s[i:j + 1]
            if no_s in sub_s or max([sub_s.count(k) for k in sub_s]) > 2:
                break
            elif len(sub_s) > res:
                res = len(sub_s)
    print(res)
    print('fun1', time.time() - st)


def fun2():
    no_s = 'D'
    s = 'ABACA123DC' * 58000
    st = time.time()

    s_len = len(s)
    count = dict()
    total_res = 0
    for i in range(s_len):
        # 统计当前子串字母个数
        res = 0
        s_sub = s[i:s_len]
        for j in s_sub:
            count[j] = count.get(j, 0) + 1
            if j == no_s or count[j] > 2:
                break
            else:
                res += 1
        count.clear()
        if total_res < res:
            total_res = res
    print(total_res)
    print('fun2', time.time() - st)


def fun3():
    char = 'D'
    s = 'ABACA123DC' * 58000 * 10
    st = time.time()
    left, right = 0, 0
    res = 0
    char_count = {}
    while True:
        # 现在的字符
        now = s[right]
        # 现在的字符为题目不允许的字符时，从这个字符后面继续开始
        if now == char:
            left = right = right + 1
            char_count.clear()
            continue
        # 当当前字符的数量超过2时，先将当前左指针的字符的次数减1，再移动左指针
        if char_count.setdefault(now, 1) > 2:
            char_count[s[left]] -= 1
            left += 1
            continue
        # 更新最大值
        now_long = right - left + 1
        if now_long > res:
            res = now_long
        right += 1
        if right < len(s):
            now = s[right]
            char_count[now] = char_count.get(now, 0) + 1
        else:
            break
    print(res)
    print('fun4', time.time() - st)


# fun1()
# fun2()
fun3()
