#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2023/11/26 18:40
# @Author  : 刘双喜
# @File    : HK2.py
# @Description : 从第一个城市出发，到最后一个城市，求所有路径中的最短路径
import itertools


def tsp1(dis):
    # n 是城市的数量
    n = len(dis)
    # INF 是一个表示无穷大的值，用于初始化 dp 数组
    inf = float('inf')
    # dp[i][j] 表示访问过的城市集合为 j，当前在城市 i 的最短路径长度
    dp = [[inf] * (1 << n) for _ in range(n)]
    # 初始化 dp 数组，如果我们直接从城市 0 出发到城市 i，那么路径长度就是 dis[i][0]
    for i in range(n):
        dp[i][0] = dis[i][0]

    # 遍历所有可能的城市集合 j
    for j in range(1, 1 << n):
        # 对于每个集合，我们遍历每个城市 i
        for i in range(n):
            # 如果 i 不在 j 中，我们就跳过
            if ((j >> i) & 1) == 0:
                continue
            # 我们尝试从一个不同的城市 k 转移到 i
            for k in range(n):
                # 如果 k 和 i 是同一个城市，我们就跳过
                if k == i:
                    continue
                # 我们更新 dp[i][j] 为所有可能的 dp[k][j^(1<<i)] + dis[k][i] 的最小值
                dp[i][j] = min(dp[i][j], dp[k][j ^ (1 << i)] + dis[k][i])
    # 我们返回从任何一个城市出发，访问所有城市并返回原点的最短路径长度
    return min(dp[i][(1 << n) - 1] + dis[i][0] for i in range(n))

# @Description : 从第一个城市出发，到最后一个城市，求所有路径中的最短路径
def tsp2(dis):
    # n 是城市的数量
    n = len(dis)
    # INF 是一个表示无穷大的值，用于初始化 dp 数组
    inf = float('inf')
    # dp[i][j] 表示访问过的城市集合为 j，当前在城市 i 的最短路径长度
    dp = [[inf] * (1 << n) for _ in range(n)]
    # 初始化 dp 数组，如果我们直接从城市 0 出发到城市 i，那么路径长度就是 dis[i][0]
    for i in range(n):
        dp[i][0] = dis[i][0]

    # 遍历所有可能的城市集合 j
    for j in range(1, 1 << n):
        # 对于每个集合，我们遍历每个城市 i
        for i in range(n):
            # 如果 i 不在 j 中，我们就跳过. 当前在的城市i一定在已访问的集合j中，不在则无意义
            if (j // (2 ** i)) % 2 == 0:
                continue
            # 我们尝试从一个不同的城市 k 转移到 i
            for k in range(n):
                # 如果 k 和 i 是同一个城市，我们就跳过
                if k == i:
                    continue
                # 我们更新 dp[i][j] 为所有可能的 dp[k][j - (2 ** i)] + dis[k][i] 的最小值
                dp[i][j] = min(dp[i][j], dp[k][j - (2 ** i)] + dis[k][i])
    # 我们返回从任何一个城市出发，访问所有城市并返回原点的最短路径长度
    return min(dp[i][(1 << n) - 1] + dis[i][0] for i in range(n))

def tsp3(dis):
    # dp记录所在城市和去过城市信息，dp[i][j]为在i城市，去过j城市时的最短距离
    # 在i城市去过j城市的最短距离 = 上一步的最短距离 = 从其他城市来i城市的最短的那个
    might_go = 1
    dp = [[float('inf') for i in itertools.permutations()] for j in range(len(dis))]
    for i in range(len(dp)):
        for j in dp[i]:
            pass
    pass

# dis[i][j]城市i到城市j的距离
dis = [[0, 3, 6, 7],
       [5, 0, 2, 3],
       [6, 4, 0, 2],
       [3, 7, 5, 0]]
print(tsp2(dis))

