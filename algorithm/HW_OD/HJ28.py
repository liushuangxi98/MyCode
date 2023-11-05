#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2023/11/1 23:05
# @Author  : 刘双喜
# @File    : HJ28.py
# @Description : https://www.nowcoder.com/practice/b9eae162e02f4f928eac37d7699b352e?tpId=37&tqId=21251&rp=1&ru=/exam/oj/ta&qru=/exam/oj/ta&sourceUrl=%2Fexam%2Foj%2Fta%3Fpage%3D1%26pageSize%3D50%26search%3D%26tpId%3D37%26type%3D37&difficulty=undefined&judgeStatus=undefined&tags=&title=
# 核心解题思路：组成素数伴侣的必定是奇数+偶数；转换为二分图求最大匹配问题，左边是奇数，右边是偶数；先统一求出左右两边可以匹配的组合，二维数组表示。
# 遍历左，依次寻找左边每个元素的增广路径。创建右的访问列表，每次find确保右每个元素不会重复访问，
# 再遍历右，判断右的每个元素在没有被访问的情况下能否构成素数伴侣，满足则标记已访问，
# 右边元素是单身的情况下，直接构成素数伴侣，记录右边元素的伴侣，返回True
# 右边元素不是单身的情况，给右边元素的伴侣重新找一个

def fun():
    def is_prime(num):
        if num <= 1:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True

    def find(l_idx, visited):
        for r_idx in range(len(right_ls)):
            if left_add_right_is_prime[l_idx][r_idx] and not visited[r_idx]:  # 如果能找到且未访问过
                visited[r_idx] = True  # 标记为已访问
                if r_find_l_idx[r_idx] == -1 or find(r_find_l_idx[r_idx], visited):  # 被使用了，如果能给他再找一个，就抢了
                    r_find_l_idx[r_idx] = l_idx
                    return True
        return False

    n = int(input())
    n_ls = list(map(int, input().split(' ')))
    left_ls = [i for i in n_ls if i % 2 == 1]  # 奇数
    right_ls = [i for i in n_ls if i % 2 == 0]  # 偶数
    left_add_right_is_prime = [[True if is_prime(l + r) else False for r in right_ls] for l in left_ls]
    if left_ls is [] or right_ls is []:
        return 0
    # 遍历左边
    count = 0
    r_find_l_idx = [-1 for _ in right_ls]  # 右边的有没有找到左边的，找到了就写入左边的数
    for l_idx in range(len(left_ls)):
        # 寻找右边的匹配项
        visited = [False for _ in right_ls]  # 初始化visited数组
        if find(l_idx, visited):
            count += 1
    return count


print(fun())
