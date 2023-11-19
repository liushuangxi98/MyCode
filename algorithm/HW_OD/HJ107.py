#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2023/11/13 18:34
# @Author  : 刘双喜
# @File    : HJ107.py
# @Description : 二分法；逻辑
# https://www.nowcoder.com/practice/caf35ae421194a1090c22fe223357dca?tpId=37&tqId=21330&rp=1&ru=/exam/oj/ta&qru=/exam/oj/ta&sourceUrl=%2Fexam%2Foj%2Fta%3Fpage%3D1%26pageSize%3D50%26search%3D%26tpId%3D37%26type%3D37&difficulty=undefined&judgeStatus=undefined&tags=&title=
# 核心解题思路：负数的立方根=正数，小数的立方根等于倒数的立方根再倒数。
# 先设答案必定在(1, n)。先设定在中间，如果答案的立方大于n，则答案应该更小，将范围的小值替换。

def fun():
    n = float(input())
    if n == 0:
        return print(0.0)
    # 负数结果和正数一样，转换为正数
    flag = -1 if n < 0 else 1
    n = flag * n
    # 小于1的取倒数转换为大于1的数来处理，结果再取倒数倒回来
    flag2 = '/' if 0 < n < 1 else ''
    n = 1 / n if 0 < n < 1 else n
    # 由于没有负数和小于1的数，答案应在的范围大于1
    ans_range = (1, n)
    # 默认答案从二分中间开始
    ans = (ans_range[0] + ans_range[1]) / 2
    while abs(ans * ans * ans - n) > 0.0001:
        # 大于时更新最大值，小于时更新最小值
        ans_range = [ans_range[0], ans] if ans * ans * ans > n else [ans, ans_range[1]]
        ans = (ans_range[0] + ans_range[1]) / 2
    # 是不是0到1之间的数，倒数回来
    if flag2 == '/':
        print(f'{1 / ans * flag:.1f}')
    else:
        print(f'{ans * flag:.1f}')


fun()
