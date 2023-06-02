#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2023/4/8 21:22
# @Author  : 刘双喜
# @File    : 21.简易五子棋.py
# @Description : 添加描述
import string
import time


def creat_coord(size):
    """
    创建棋盘
    :param size:棋盘大小
    :return: 棋盘列表
    """
    arr = [[0 for _ in range(size)] for _ in range(size)]  # 创造大小size的棋盘
    return arr


def print_chess(arr):
    """
    打印棋盘
    :param arr:棋盘列表
    :return: None
    """
    coord_idx, size = string.ascii_lowercase, len(arr[0])
    print('  '.join([' '] + list(coord_idx[0:size])))  # 打印第一行坐标
    for idx, i in enumerate(arr):
        col = [coord_idx[idx]] + list(map(str, i))  # 依次打印每一行坐标和棋盘
        print('  '.join(col))


def is_win(arr):
    """
    判断是否有人赢
    :param arr:棋盘列表
    :return: 1,2,0
    """
    for x, x_var in enumerate(arr[:-4]):  # 循环行
        for y, y_var in enumerate(x_var[:-4]):  # 循环列
            for i, j in [(0, 1), (1, 0), (1, 1)]:  # 循环向右向下向斜下3个方向
                five = [arr[x + i * step][y + j * step] for step in range(5)]  # 取出对于方向的五个子
                flag = (1, print('赢者玩家1')) if five.count(1) == 5 \
                    else (1, print('赢者玩家2')) if five.count(2) == 5 else (0, 0)
                if flag[0]:
                    return flag[0]
    return flag[0]


def drop(coord, player):
    coord_idx, flag = string.ascii_lowercase, True
    while flag:  # 等待有效落子
        player_a_x, player_a_y = [coord_idx.index(i) for i in list(input(f'玩家{player}落子(先列后行,如bc):'))[::-1]]
        if coord[player_a_x][player_a_y] == 0:
            coord[player_a_x][player_a_y], flag = player, False
        else:
            print('此位置已有落子，请重新下')
    return coord


if __name__ == '__main__':
    # 创建棋盘
    coord_list = creat_coord(int(input('请输入棋盘大小(0~26):')))  # a~z命名，最大26
    # 打印棋盘
    print_chess(coord_list)
    while True:
        for player in [1, 2]:
            # 玩家落子
            coord_list = drop(coord_list, player)
            # 打印棋盘
            print_chess(coord_list)
            # 是否有人赢
            if is_win(coord_list):
                time.sleep(0.5)
                exit('游戏结束')
