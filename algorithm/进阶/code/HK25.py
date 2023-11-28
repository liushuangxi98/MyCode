#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2023/11/22 22:24
# @Author  : 刘双喜
# @File    : HK25.py
# @Description : 机器人的最大活动区域，dfs
# 预期输出6
m, n = 4, 4
maze = [[1, 2, 5, 2], [2, 4, 4, 5], [3, 5, 7, 1], [4, 6, 2, 4]]


def fun1():
    def dfs(i, j, value):
        nonlocal step
        if abs(maze[i][j] - value) > 1 or [i, j] in step_visit:
            return False
        else:
            step_visit.append([i, j])
            step += 1
        if i - 1 >= 0:  # 向上
            dfs(i - 1, j, maze[i][j])
        if i + 1 < m:  # 向下
            dfs(i + 1, j, maze[i][j])
        if j - 1 >= 0:  # 向左
            dfs(i, j - 1, maze[i][j])
        if j + 1 < n:  # 向右
            dfs(i, j + 1, maze[i][j])

    max_step = 1
    for i in range(m):
        for j in range(n):
            step = 0  # 本次能活动的最大的区域
            step_visit = []  # 已访问的活动区域
            dfs(i, j, maze[i][j])
            max_step = max(max_step, step)
    print(max_step)


fun1()
