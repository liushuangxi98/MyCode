#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2023/11/20 22:46
# @Author  : 刘双喜
# @File    : HK36.py
# @Description : 添加描述
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
