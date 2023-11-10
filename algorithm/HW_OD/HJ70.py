#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2023/11/10 20:31
# @Author  : 刘双喜
# @File    : HJ70.py
# @Description : https://www.nowcoder.com/practice/15e41630514445719a942e004edc0a5b?tpId=37&tqId=21293&rp=1&ru=/exam/oj/ta&qru=/exam/oj/ta&sourceUrl=%2Fexam%2Foj%2Fta%3Fpage%3D1%26pageSize%3D50%26search%3D%26tpId%3D37%26type%3D37&difficulty=undefined&judgeStatus=undefined&tags=&title=
# 核心解题思路：方法1：用一个字典存储每个字母的矩阵。 while循环查找 ) ,找到时计算其左边两个字母，得到结果后替换掉要计算的字符串，并且更新字典
# 方法2：遍历计算法则，遇到字母则添加字母对应矩阵到带计算的列表order，遇到 ) 则用order.pop删除最后2个字母并计算值，再添加新的矩阵到order。


def fun():
    import string
    n = int(input())
    alpha_map_size = {i: list(map(int, input().split(' '))) for i in string.ascii_uppercase[0:n]}
    rule = input()
    res = 0
    while True:
        # 寻找要计算的字符串组合
        sub_rule = rule[rule.index(')') - 2:rule.index(')')]
        # 计算字符串
        a1 = alpha_map_size.get(sub_rule[0])
        a2 = alpha_map_size.get(sub_rule[1])
        sub_value, new_size, new_alpha = a1[0] * a1[1] * a2[1], [a1[0], a2[1]], sub_rule[0]
        # 更新信息
        res += sub_value
        rule, alpha_map_size[new_alpha] = rule.replace(rule[rule.index(')') - 3:rule.index(')') + 1], new_alpha), new_size
        if len(rule) == 1:
            break
    print(res)



def fun2():
    n = int(input())
    arr = [list(map(int, input().split())) for i in range(n)]
    order, res = [], 0
    f = input()
    for i in f:
        if i.isalpha():
            order.append(arr[ord(i) - 65])  # 将字母转换成第几个矩阵的处理信息
        elif i == ')' and len(order) >= 2:  # 读到右括号就处理最近的两个矩阵相乘的结果
            b = order.pop()
            a = order.pop()
            res += a[1] * b[1] * a[0]  # 累计到res中
            order.append([a[0], b[1]])
    print(res)


fun()
