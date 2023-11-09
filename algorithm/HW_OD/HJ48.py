#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2023/11/8 21:05
# @Author  : 刘双喜
# @File    : HJ48.py
# @Description : https://www.nowcoder.com/practice/f96cd47e812842269058d483a11ced4f?tpId=37&tqId=21271&rp=1&ru=/exam/oj/ta&qru=/exam/oj/ta&sourceUrl=%2Fexam%2Foj%2Fta%3Fpage%3D1%26pageSize%3D50%26search%3D%26tpId%3D37%26type%3D37&difficulty=undefined&judgeStatus=undefined&tags=&title=


def fun():
    num, head_value, *args = input().split(' ')
    ret = [head_value]  # 最后结果
    delete_value, args = args[-1],args[0:-1]
    for i in range(0, len(args), 2):
        back, front = args[i], args[i+1]
        ret.insert(ret.index(front) + 1, back)
    ret.remove(delete_value)
    print(' '.join(ret))

fun()
