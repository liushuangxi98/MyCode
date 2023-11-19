#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2023/11/1 23:05
# @Author  : 刘双喜
# @File    : HJ28.py
# @Description : DFS；匈牙利算法
# https://www.nowcoder.com/practice/b9eae162e02f4f928eac37d7699b352e?tpId=37&tqId=21251&rp=1&ru=/exam/oj/ta&qru=/exam/oj/ta&sourceUrl=%2Fexam%2Foj%2Fta%3Fpage%3D1%26pageSize%3D50%26search%3D%26tpId%3D37%26type%3D37&difficulty=undefined&judgeStatus=undefined&tags=&title=
# 核心解题思路：组成素数伴侣的必定是奇数+偶数；转换为二分图求最大匹配问题，左边是奇数，右边是偶数；先统一求出左右两边可以匹配的组合，二维数组表示。
# 遍历左，依次寻找左边每个元素的增广路径。创建右的访问列表，每次find确保右每个元素不会重复访问，
# 再遍历右，判断右的每个元素在没有被访问的情况下能否构成素数伴侣，满足则标记已访问，
# 右边元素是单身的情况下，直接构成素数伴侣，记录右边元素的伴侣，返回True
# 右边元素不是单身的情况，给右边元素的伴侣重新找一个

def fun2():
    def is_prime(_value):
        if _value == 1:
            return False
        for _i in range(2, 1 + int(_value ** 0.5)):
            if _value % _i == 0:
                return False
        return True

    # 遍历每一个左边节点，给它找一个右边节点
    def find(i, _left_visit_right):
        for j, right in enumerate(right_lis):  # 遍历右
            if matchable[i][j] and _left_visit_right[j] is False:  # 如果左右能匹配,且没访问过
                _left_visit_right[j] = True
                if match_dict.get(j) is None:  # 右边没有匹配
                    match_dict[j] = i  # 给右边匹配左边
                    return True
                elif find(match_dict.get(j), _left_visit_right[::]):  # 右边已经匹配上了左某，试着给左某的再找过一个
                    match_dict[j] = i  # 如果能给左某找到，则右现匹配左现
                    return True
        return False

    n = input()
    arr = list(map(int, input().split()))
    left_lis = [i for i in arr if i % 2 == 0]  # 二分图左边
    right_lis = [i for i in arr if i % 2 != 0]  # 二分图右边
    matchable = [[is_prime(i + j) for j in right_lis] for i in left_lis]  # 二分图里所有可能的路径能否匹配的结果
    match_dict = dict()
    for i, left in enumerate(left_lis):
        left_visit_right = [False for j in right_lis]  # 每一个左边保存一个它右边是否访问列表,必须在此处初始化。每次递归都是新开始
        find(i, left_visit_right)
    print(len(match_dict))


fun2()
