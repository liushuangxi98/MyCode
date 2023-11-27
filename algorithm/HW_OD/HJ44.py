#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2023/11/5 23:03
# @Author  : 刘双喜
# @File    : HJ44.py
# @Description : DFS
# https://www.nowcoder.com/practice/78a1a4ebe8a34c93aac006c44f6bf8a1?tpId=37&tqId=21267&rp=1&ru=/exam/oj/ta&qru=/exam/oj/ta&sourceUrl=%2Fexam%2Foj%2Fta%3Fpage%3D1%26pageSize%3D50%26search%3D%26tpId%3D37%26type%3D37&difficulty=undefined&judgeStatus=undefined&tags=&title=
# 核心思路：方法一： 遍历所有格子，dfs每个格子，当前格子是空的则继续，否则找下一个空的。对空格找合法的值，没有合法的则False。遍历合法的值填入，dfs下一个格子。
# 方法二：dfs里遍历所有格子，遇到空的则0~9依次填一个，合法继续dfs，不合法换一个，0~9都不合法则当前false。


def fun():
    def find_legal_value(x, y):
        # 查找当前坐标点的合法可填值
        x_axis = set(board[x])
        y_axis = {board[i][y] for i in range(9)}
        sub_board = {board[_x][_y] for _x in [x - x % 3, x - x % 3 + 1, x - x % 3 + 2] for _y in
                     [y - y % 3, y - y % 3 + 1, y - y % 3 + 2]}
        legal_value = set(range(1, 10)) - x_axis - y_axis - sub_board
        if legal_value:
            return legal_value
        else:
            return False

    # 从0,0开始，遍历它的所有合法取值，即行列九宫格都不包含的数字
    def dfs(x, y):
        # 如果已经遍历到了最后一个(8,8),则返回True
        if x == 8 and y == 8:
            value = find_legal_value(8, 8)
            # 最后一个格子为空则填入
            if value:
                for i in value:
                    board[8][8] = i
            return True
        # 超出换行
        y = y + 1 if x == 9 else y
        x = x % 9
        # 找下一个为0的格子
        while board[x][y] != 0:
            x += 1
            # 超出换行
            y = y + 1 if x == 9 else y
            x = x % 9
            if x == 8 and y == 8:
                value = find_legal_value(8, 8)
                # 最后一个格子为空则填入
                if value:
                    for i in value:
                        board[8][8] = i
                return True
        # 检查当前格子是否可以填入
        legal_value = find_legal_value(x, y)
        if legal_value:
            # 可以填入则遍历所有可以填入的值
            for value in legal_value:
                board[x][y] = value  # 填入
                if dfs(x + 1, y):  # dfs下一个
                    return True
                else:
                    board[x][y] = 0  # 回溯
        else:  # 不可以则返回False
            return False

    board = [list(map(int, input().split(' '))) for _ in range(9)]
    dfs(0, 0)
    for i in board:
        i = list(map(str, i))
        print(' '.join(i))


def fun2():
    def is_legal_value(board, x, y):
        # 检查已经填入的坐标是否和列中有的元素相等
        for i in range(9):
            if i != x and board[i][y] == board[x][y]:
                return False
        # 检查已经填入的坐标是否和行中有的元素相等
        for j in range(9):
            if j != y and board[x][j] == board[x][y]:
                return False

        # 检查每个正方形是否符合（粗线框内只有1~9）
        m, n = 3 * (x // 3), 3 * (y // 3)  # 这里求出的是3x3网格的左上角的坐标
        for i in range(3):
            for j in range(3):
                if (i + m != x or j + n != y) and board[i + m][j + n] == board[x][y]:
                    return False
        return True

    def dfs(board):
        for i in range(9):
            for j in range(9):
                if board[i][j] == 0:
                    for k in '123456789':  # 从里面选择一个
                        board[i][j] = int(k)
                        if is_legal_value(board, i, j) and dfs(board):
                            return True
                        # 回溯
                        board[i][j] = 0
                    # 都不行，说明上次的数字不合理
                    return False
        # 全部便利完，返回True
        return True

    # 输入
    board = []
    for i in range(9):
        row = list(map(int, input().split()))
        board.append(row)

    dfs(board)

    for i in range(9):
        board[i] = list(map(str, board[i]))
        print(' '.join(board[i]))


fun2()
