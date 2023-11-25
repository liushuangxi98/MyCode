#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2023/11/20 22:46
# @Author  : 刘双喜
# @File    : HK36.py
# @Description : 红黑图染色方案，枚举所有方案，再排除不符合条件的方案

def fun():
    # 读取节点数和边数
    n, m = map(int, input().split())
    # 使用列表推导式创建一个空的邻接矩阵
    edges = [list(map(int, input().split())) for _ in range(m)]
    # 计算总的染色方案数
    total = 1 << n
    # 初始化结果为总的染色方案数
    res = total
    # 遍历所有的染色方案
    for i in range(total):
        # 使用位运算快速计算每个节点的颜色
        colors = [(i >> j) & 1 for j in range(n)]
        print(colors)
        # 检查每条边的两个节点是否都被染成红色
        for u, v in edges:
            if colors[u] == colors[v] == 0:
                # 如果两个节点都被染成红色，则该染色方案不符合要求
                res -= 1
                break
    # 输出结果
    print(res)

def fun2():
    n, m = map(int, input().split())
    # 相邻的节点
    adjoin_point = [list(map(int, input().split())) for _ in range(m)]
    # 所有染色的方案总数
    total = 2 ** n
    # 合格方案数
    res = 0
    for i in range(total):
        # 某种染色方案，红为1，黑为0
        i = bin(i)[2:].rjust(n, '0')
        # 遍历相邻节点
        legal = True
        for point in adjoin_point:
            # 相邻的节点都为红色时代表不合题意，退出
            if i[point[0]] == i[point[1]] == '1':
                legal = False
                break
        if legal:
            print(i)
        res += legal
    print(res)

def fun3():
    def check_color(i, c, color, adjoin_point):
        # 检查所有的边
        for point in adjoin_point:
            # 如果边的两个节点颜色相同，则不能给节点 i 染色 c
            if (point[0] == i and color[point[1]] == c) or (point[1] == i and color[point[0]] == c):
                return False
        return True

    def dfs(i, n, color, adjoin_point):
        # 当所有节点都被染色时，合格方案数加一
        if i == n:
            return 1
        res = 0
        # 尝试给节点 i 染色，颜色可以是 1 或 2
        for c in [1, 2]:
            # 如果可以给节点 i 染色 c
            if check_color(i, c, color, adjoin_point):
                # 给节点 i 染色 c
                color[i] = c
                # 继续尝试给下一个节点染色
                res += dfs(i + 1, n, color, adjoin_point)
                # 回溯前，把节点 i 的颜色清除
                color[i] = 0
        return res

        # 输入节点数和边数

    n, m = map(int, input().split())
    # 输入每条边的两个节点
    adjoin_point = [list(map(int, input().split())) for _ in range(m)]
    # 初始化节点颜色
    color = [0] * n
    # 输出合格方案数
    print(dfs(0, n, color, adjoin_point))


fun()