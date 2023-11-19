#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2023/11/5 9:05
# @Author  : 刘双喜
# @File    : HJ32.py
# @Description : 逻辑方法
# https://www.nowcoder.com/practice/3cd4621963e8454594f00199f4536bb1?tpId=37&tqId=21255&rp=1&ru=/exam/oj/ta&qru=/exam/oj/ta&sourceUrl=%2Fexam%2Foj%2Fta%3Fpage%3D1%26pageSize%3D50%26search%3D%26tpId%3D37%26type%3D37&difficulty=undefined&judgeStatus=undefined&tags=&title=
# 核心解题思路：方法1：遍历字符串所有元素，求元素i位置的最大对称长度，即以i元素为中心，向左右扩展，直到不相等时break返回。
# 方法2：
# 方法3： 遍历字符串所有元素，求元素i左侧和右侧的逆序是否相等，相等则添加到列表
def fun():
    s = input()  # 12HHHHA
    s_len = len(s)
    if s_len <= 1:
        print(s_len)
        return
    max_len = 0
    # 遍历s每个位置
    for i in range(s_len):
        # 求当前位置往两边扩展，能得到的对称字符串数量，即扩展的时候相等
        def s_sub_max(s, l_idx, r_idx):
            symmetry_center = 1 if l_idx == r_idx else 0
            # 当l_idx和r_idx没达到边境时, 一直循环
            l_count, r_count = 0, 0
            while l_idx >= 0 and r_idx <= s_len - 1:
                # 当l和r相等时，对称字符串长度加1
                if s[l_idx] == s[r_idx]:
                    if l_idx != r_idx:  # 两字符串在同一位置时，不算对称
                        l_count += 1
                        r_count += 1
                else:
                    break
                # 位置移位
                l_idx -= 1
                r_idx += 1
            # 奇数对称时加上对称中心的长度
            return l_count + r_count + symmetry_center

        i_odd_max = s_sub_max(s, i, i)
        i_even_max = s_sub_max(s, i, i + 1)
        max_len = max(i_odd_max, i_even_max, max_len)
    print(max_len)
    return


def fun_manacher():
    """
    方法2：manacher算法
    :param s:
    :return:
    """
    s = input()
    # 在字符串的每个字符之间插入一个特殊字符'#'
    s = '#' + '#'.join(s) + '#'

    # 初始化回文半径数组，长度与处理后的字符串相同
    palindrome_radius = [0] * len(s)

    # 初始化最右边界和中心位置
    max_right = 0
    center = 0

    # 初始化最长回文串的长度
    max_length = 0

    # 遍历处理后的字符串
    for i in range(len(s)):
        if i < max_right:
            # 如果当前位置在最右边界内，可以利用已知的回文半径
            palindrome_radius[i] = min(palindrome_radius[2 * center - i], max_right - i)
        else:
            # 否则，只能从1开始
            palindrome_radius[i] = 1

        # 尝试扩展回文半径，注意处理边界
        while i - palindrome_radius[i] >= 0 and i + palindrome_radius[i] < len(s) and \
                s[i - palindrome_radius[i]] == s[i + palindrome_radius[i]]:
            palindrome_radius[i] += 1

        # 如果扩展后的回文串超过了最右边界，更新最右边界和中心位置
        if palindrome_radius[i] + i - 1 > max_right:
            max_right = palindrome_radius[i] + i - 1
            center = i

        # 更新最长回文串的长度
        max_length = max(max_length, palindrome_radius[i])

    # 返回最长回文串的长度，减1是因为去掉了插入的特殊字符
    print(max_length - 1)


def fun_3():
    s = input()
    n = len(s)
    if n == 1:
        print(1)
        return
    ls = []  # 初始化一个空列表，用于存储所有对称子串的长度。
    for i in range(0, n - 1):  # 外层循环，遍历字符串中的每个字符，i是当前字符的索引。
        for j in range(1, n):  # 内层循环，遍历当前字符后面的所有字符，j是当前字符的索引。
            # 如果i和j位置的字符相同，并且i和j之间的子串是对称的（即子串和它的逆序相同），那么这个子串就是一个对称子串。
            if s[j] == s[i] and s[i + 1:j] == s[j - 1:i:-1]:
                ls.append(len(s[i:j + 1]))  # 如果找到一个对称子串，就计算它的长度，并添加到列表中。
    print(max(ls))
    return

def fun_4():
    s = input()
    if len(s) == 1 or len(set(list(s))) == 1:  # 输入都是相同字母直接返回吧
        print(len(s))
        return
    longest = 0
    for i in range(len(s)):
        # 奇数对称
        left_offset, right_offset = 0, 0
        while i - left_offset >=0 and i+right_offset < len(s):
            if s[i-left_offset] == s[i+right_offset]:
                left_offset += 1
                right_offset += 1
            else:
                break
        longest = max(longest, left_offset+ right_offset - 1)
        # 偶数左开始对称
        left_offset, right_offset = 1, 0
        while i - left_offset >=0 and i+right_offset < len(s):
            if s[i-left_offset] == s[i+right_offset]:
                left_offset += 1
                right_offset += 1
            else:
                break
        longest = max(longest, left_offset+ right_offset - 1)
        # 偶数右对称
        left_offset, right_offset = 0, 1
        while i - left_offset >=0 and i+right_offset < len(s):
            if s[i-left_offset] == s[i+right_offset]:
                left_offset += 1
                right_offset += 1
            else:
                break
        longest = max(longest, left_offset+ right_offset - 1)
    print(longest)


fun()
