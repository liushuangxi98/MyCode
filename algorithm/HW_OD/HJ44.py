#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2023/11/5 23:03
# @Author  : 刘双喜
# @File    : HJ44.py
# @Description : https://www.nowcoder.com/practice/78a1a4ebe8a34c93aac006c44f6bf8a1?tpId=37&tqId=21267&rp=1&ru=/exam/oj/ta&qru=/exam/oj/ta&sourceUrl=%2Fexam%2Foj%2Fta%3Fpage%3D1%26pageSize%3D50%26search%3D%26tpId%3D37%26type%3D37&difficulty=undefined&judgeStatus=undefined&tags=&title=

# 找到第一个空格（我们可以从左上角开始）。
# 尝试在这个空格中填入一个数字（从1到9）。
# 检查填入的数字是否满足数独的规则（即在同一行、同一列和同一个3x3的格子中没有重复的数字）。
# 如果满足规则，我们就在这个空格中填入这个数字，并递归地尝试填入下一个空格。
# 如果不满足规则，或者递归填入下一个空格失败，我们就撤销当前填入的数字，并尝试下一个数字。
# 如果所有的数字都尝试过，但都不能满足规则，那么就返回失败。
def fun():

    def judge(x, y):
        pass

    def find_zero():
        pass

    # 从0,0开始，遍历它的所有合法取值，即行列九宫格都不包含的数字
    def dfs(x, y):
        # 如果已经遍历到了最后一个(8,8),则返回True
        # 如果这个格子已经填了，dfs下一个
        # 如果这个格式是空格子，遍历所有合法取值，dfs下一个
        pass

    pass
