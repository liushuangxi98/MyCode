#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2023/11/8 21:25
# @Author  : 刘双喜
# @File    : HJ53.py
# @Description : 添加描述


def fun():
    n = int(input())
    yh_triangle = [[0] * n for i in range(n)]  # 创建n行的杨辉三角，默认值
    for i in range(0, n):  # 从第1行开始遍历，
        for j in range(0, 1 + i):  # 每行遍历的值等于行号
            if j == 0:  # 如果是第一个数
                if i == 0:
                    yh_triangle[0][0] = 1  # 第一行第一个是1
                else:  # 第1行往后的第1个值位上一个第一个位置的值+2倍第二个位置的值
                    yh_triangle[i][0] = yh_triangle[i - 1][0] + 2 * yh_triangle[i - 1][1]
            else:  # 如果是第2位和往后的数
                yh_triangle[i][j] = sum(yh_triangle[i - 1][j - 1:j + 2])
    # 对杨辉三角对称处理
    ret = [yh_triangle[i][0:i + 1] for i in range(n)]
    ret = [line[1:][::-1] + line[0:1] + line[1:] for line in ret]
    for idx, i in enumerate(ret[n - 1]):
        if i % 2 == 0:
            print(idx + 1)
            return
    print(-1)
    return


# fun()

def fun2():
    def dfs(x, y):
        if y == 2 * x - 1 - 1 or y == 0:
            return -1
        if y < 0 or y > 2 * x - 1 - 1:
            return 1
        if x == 2:
            return -1
        if y == 1:
            if x % 2 == 1:
                return 1
            else:
                return -1
        return dfs(x - 1, y - 1 - 1) * dfs(x - 1, y - 1) * dfs(x - 1, y + 1 - 1)

    n = int(input())
    if n <= 2:
        print(-1)
        return
    if n % 2 == 1:
        print(2)
    else:
        for i in range(2, n - 1):
            if dfs(n, i) == 1:  # 第n行，i索引，1是偶数，-1是奇数
                print(i + 1)
                return

def fun3():
    n = int(input())
    if n <= 2:
        print(-1)
        exit()
    arr_n_1 = [1, 1, 1]
    m = 2
    while 2 < n:
        arr_n = []
        column_num = 2 * m + 1
        for i in range(column_num):
            arr_n.append(sum(arr_n_1[i - 2 if i - 2 >= 0 else 0:i + 1]))
        arr_n_1 = arr_n[::]
        m = m + 1

    def cal(arr_n):
        for i, j in enumerate(arr_n):
            if j % 2 == 0:
                return i + 1
        return -1

    index = cal(arr_n)
    print(index)
fun3()
