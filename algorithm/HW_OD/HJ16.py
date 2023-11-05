#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2023/10/31 19:26
# @Author  : 刘双喜
# @File    : HJ16.py
# @Description : https://www.nowcoder.com/practice/f9c6f980eeec43ef85be20755ddbeaf4?tpId=37&tqId=21239&rp=1&ru=%2Fexam%2Foj%2Fta&qru=%2Fexam%2Foj%2Fta&sourceUrl=%2Fexam%2Foj%2Fta%3Fpage%3D1%26pageSize%3D50%26search%3D%26tpId%3D37%26type%3D37&difficulty=undefined&judgeStatus=undefined&tags=&title=&dayCountBigMember=30%E5%A4%A9&topicName_var=%E5%8D%8E%E4%B8%BA%E6%9C%BA%E8%AF%95&topicID_var=37
# 解题核心思路：建立二维动态规划表，横轴是最大使用金额，纵轴是最大购买商品数量，值为当前购买物品和使用金额的最大价值
# 遍历金额，动态转移方程就是 当最大使用金额大于当前物品金额时，当前最大价值 = 不买上个物品，买当前物品，使用金额为扣去当前物品金额后的金额，加上当前物品的价值

# 输入
# 1000 5
# 800 2 0
# 400 5 1
# 300 5 1
# 400 3 0
# 500 2 0

total_money, goods_cnt = list(map(int, input().split(' ')))
total_money //= 10
input_list = [list(map(int, input().split(' '))) for _ in range(goods_cnt)]
main_cnt = len([i for i in input_list if i[-1] == 0])
main_sub_price = [[0, 0, 0] for _ in range(goods_cnt)]
main_sub_value = [[0, 0, 0] for _ in range(goods_cnt)]
for idx, line in enumerate(input_list, 0):
    price, value, flag = line
    flag -= 1
    if line[-1] == 0:
        main_sub_price[idx][0] = price // 10
        main_sub_value[idx][0] = price * value // 10
    else:
        if main_sub_price[flag][1] == 0:
            main_sub_price[flag][1] = price // 10
            main_sub_value[flag][1] = price * value // 10
        else:
            main_sub_price[flag][2] = price // 10
            main_sub_value[flag][2] = price * value//10
main_sub_price = [i for i in main_sub_price if i[0] != 0]
main_sub_value = [i for i in main_sub_value if i[0] != 0]
dp = [[0 for _ in range(total_money + 1)] for _ in range(1 + main_cnt)]
for goods in range(1, 1 + len(main_sub_value)):
    for use_money in range(1 + total_money):
        p1, p2, p3 = main_sub_price[goods-1]
        v1, v2, v3 = main_sub_value[goods-1]
        if use_money >= p1:
            dp[goods][use_money] = max(dp[goods-1][use_money-p1] + v1, dp[goods][use_money])
        if use_money >= p1 + p2:
            dp[goods][use_money] = max(dp[goods-1][use_money-p1-p2] + v1+v2, dp[goods][use_money])
        if use_money >= p1 + p3:
            dp[goods][use_money] = max(dp[goods-1][use_money-p1-p3] + v1+v3, dp[goods][use_money])
        if use_money >= p1 + p2+p3:
            dp[goods][use_money] = max(dp[goods-1][use_money-p1-p2-p3] + v1+v2+v3, dp[goods][use_money])
print()