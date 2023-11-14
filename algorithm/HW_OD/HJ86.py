#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2023/11/12 16:06
# @Author  : 刘双喜
# @File    : HJ86.py
# @Description : https://www.nowcoder.com/practice/4b1658fd8ffb4217bc3b7e85a38cfaf2?tpId=37&tqId=21309&rp=1&ru=/exam/oj/ta&qru=/exam/oj/ta&sourceUrl=%2Fexam%2Foj%2Fta%3Fpage%3D1%26pageSize%3D50%26search%3D%26tpId%3D37%26type%3D37&difficulty=undefined&judgeStatus=undefined&tags=&title=


def fun():
    a = bin(int(input().strip()))[2:]
    res_range = [0, len(a)]  # 结果应在的范围
    while True:
        # 二分法的范围已经够小了就暴力遍历
        if res_range[1] - res_range[0] < 5:
            for i in range(res_range[1], res_range[0]-1, -1):
                if i*'1' in a:
                    print(i)
                    return
        # 二分过程
        ''.strip()
        mid = sum(res_range) // 2
        if mid * '1' in a:
            res_range = [mid, res_range[1]]
        else:
            res_range = [res_range[0], mid]

fun()