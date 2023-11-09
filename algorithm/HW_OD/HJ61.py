#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2023/11/9 18:51
# @Author  : 刘双喜
# @File    : HJ61.py
# @Description : https://www.nowcoder.com/practice/bfd8234bb5e84be0b493656e390bdebf?tpId=37&tqId=21284&rp=1&ru=/exam/oj/ta&qru=/exam/oj/ta&sourceUrl=%2Fexam%2Foj%2Fta%3Fpage%3D1%26pageSize%3D50%26search%3D%26tpId%3D37%26type%3D37&difficulty=undefined&judgeStatus=undefined&tags=&title=
# 核心解题思路： 动态规划： 盘子多的时候，多1个和n个放法是一样多的；
#                      盘子等的时候，等于少一个盘子的放法+多一个盘子多一种放法
#                      盘子空着的，加盘子不空，每个盘子放一个，多余的果放盘子的方法数
#             递归： 思路一样，边界是苹果或者盘子=1时返回1
def fun_dp():
    apple, dish = list(map(int, input().split(' ')))
    dp = [[0 for _ in range(apple + 1)] for _ in range(dish + 1)]  # 初始化dp数组
    for i in range(dish + 1):
        dp[i][0] = 1  # 0个苹果的放法只有1种
    for i in range(1, dish + 1):
        for j in range(1, apple + 1):
            if j < i:  # 盘子多 苹果少
                dp[i][j] = dp[i - 1][j]
            elif i == j:  # 盘子相等苹果，等于少一个盘子的放法+多一个盘子多一种放法
                dp[i][j] = dp[i - 1][j] + 1
            else:  # 盘子少 苹果多
                dp[i][j] = dp[i - 1][j] + dp[i][j - i]  # 盘子空着的，加盘子不空，每个盘子放一个，多余的果放盘子的方法数
    print(dp[-1][-1])


def fun_dfs():
    def dfs(apple, dish):
        if apple == 1:
            return 1
        if dish == 1:
            return 1
        if apple < dish:  # 苹果数量少
            return dfs(apple, dish - 1)
        elif apple == dish:
            return dfs(apple, dish - 1) + 1  # 相等时，等于少一个盘子的时候 + 多一个盘子的时候多1个选择
        elif apple > dish:
            # 空一个盘子 + 不空时必有apple - dish要放在dish个里
            return dfs(apple,dish -1) + dfs(apple -dish , dish)
    _apple, _dish = list(map(int, input().split(' ')))
    ret = dfs(_apple, _dish)
    print(ret)


fun_dfs()
fun_dp()
