#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2023/11/5 16:48
# @Author  : 刘双喜
# @File    : HJ43.py
# @Description : https://www.nowcoder.com/practice/cf24906056f4488c9ddb132f317e03bc?tpId=37&tqId=21266&rp=1&ru=/exam/oj/ta&qru=/exam/oj/ta&sourceUrl=%2Fexam%2Foj%2Fta%3Fpage%3D1%26pageSize%3D50%26search%3D%26tpId%3D37%26type%3D37&difficulty=undefined&judgeStatus=undefined&tags=&title=
# 核心解题思路：建立迷宫，判断x,y坐标的地方，有哪几个方向可以走（不超迷宫且没走过）。
# 递归不碰壁的（==0的）坐标。最后找到出口时，返回True，递归返回True时，将路径记录下来。


def fun():
    def dfs(x, y):
        visit[x][y] = True
        if x == n - 1 and y == m - 1:  # 找到了迷宫出口
            maze_path.append((x, y))
            return True
        passable = [True, True, True, True]  # 上下左右是否可以通行
        if x == 0:  # 第一行
            passable[0] = False
        if x == n - 1:  # 最后一行
            passable[1] = False
        if y == 0:  # 第一列
            passable[2] = False
        if y == m - 1:  # 最后一列
            passable[3] = False
        if passable[0] and maze[x - 1][y] == '0' and (visit[x - 1][y] is False):  # 往上可行
            if dfs(x - 1, y):
                maze_path.append((x, y))
                return True
        if passable[1] and maze[x + 1][y] == '0' and (visit[x + 1][y] is False):  # 往下可行
            if dfs(x + 1, y):
                maze_path.append((x, y))
                return True
        if passable[2] and maze[x][y - 1] == '0' and (visit[x][y - 1] is False):  # 往左可行
            if dfs(x, y - 1):
                maze_path.append((x, y))
                return True
        if passable[3] and maze[x][y + 1] == '0' and (visit[x][y + 1] is False):  # 往右可行
            if dfs(x, y + 1):
                maze_path.append((x, y))
                return True
        return False

    n, m = list(map(int, input().split(' ')))  # n行， m列
    maze = [input().split(' ') for _ in range(n)]
    maze_path = []
    visit = [[False for _ in range(m)] for _ in range(n)]  # 当前点是否走过
    dfs(0, 0)
    maze_path = maze_path[::-1]  # 倒放
    for path in maze_path:
        print(f'({path[0]},{path[1]})')


fun()
