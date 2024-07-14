#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2023/10/31 19:26
# @Author  : 刘双喜
# @File    : HJ16.py
# @Description : 动态规划；多个转移方程；
# https://www.nowcoder.com/practice/f9c6f980eeec43ef85be20755ddbeaf4?tpId=37&tqId=21239&rp=1&ru=%2Fexam%2Foj%2Fta&qru=%2Fexam%2Foj%2Fta&sourceUrl=%2Fexam%2Foj%2Fta%3Fpage%3D1%26pageSize%3D50%26search%3D%26tpId%3D37%26type%3D37&difficulty=undefined&judgeStatus=undefined&tags=&title=&dayCountBigMember=30%E5%A4%A9&topicName_var=%E5%8D%8E%E4%B8%BA%E6%9C%BA%E8%AF%95&topicID_var=37
# 解题核心思路：建立二维动态规划表，横轴是最大使用金额，纵轴是最大购买商品数量，值为当前购买物品和使用金额的最大价值
# 遍历金额，动态转移方程就是 当最大使用金额大于当前物品金额时，当前最大价值 = 不买上个物品，买当前物品，使用金额为扣去当前物品金额后的金额，加上当前物品的价值

money, number = list(map(int, input().strip().split()))
money = money // 10
main = [[[0, 0], [0, 0], [0, 0]] for _ in range(number + 2)]  # 依次存放第一个主件和它的附件
for i in range(1, 1 + number):
    v, p, q = list(map(int, input().strip().split()))
    if q == 0:  # 主件
        main[i][0] = [v // 10, v * p]
    else:
        if main[q][1][0] == 0:
            main[q][1] = [v // 10, v * p]
        else:
            main[q][2] = [v // 10, v * p]
main = [i for i in main if i[0][0] != 0]  # 去掉编号是空的主件
dp = [[0 for i in range(1 + money)] for j in range(1 + len(main))]
for num in range(1, 1 + len(main)):
    for mon in range(1 + money):
        dp[num][mon] = dp[num - 1][mon]  # 当前物品继承上一个物品的最大价值
        (p1, v1), (p2, v2), (p3, v3) = main[num - 1]
        # 不买这个物品（买前一个物品） 和 不买前一个物品买这个物品的最大值
        if mon >= p1 + p2 + p3:  # 这里必须是dp[num][mon]不能是dp[num-1][mon]，因为这个值是在每个if更新的
            # 当前的钱够买p1+p2+p3时，退回到dp的mon-p1-p2-p3时的最大价值
            dp[num][mon] = max(dp[num][mon], dp[num - 1][mon - p1 - p2 - p3] + v1 + v2 + v3)
        if mon >= p1 + p3:
            dp[num][mon] = max(dp[num][mon], dp[num - 1][mon - p1 - p3] + v1 + v3)
        if mon >= p1 + p2:
            dp[num][mon] = max(dp[num][mon], dp[num - 1][mon - p1 - p2] + v1 + v2)
        if mon >= p1:
            dp[num][mon] = max(dp[num][mon], dp[num - 1][mon - p1] + v1)

print(dp[-1][-1])
