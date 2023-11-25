#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2023/11/23 17:50
# @Author  : 刘双喜
# @File    : HK40.py
# @Description : 栈

def fun():
    s = '{A3B1{CD}3}3'
    s = '{A3B1{C}3}3'
    stack = []
    for idx, i in enumerate(s):
        # 结算完，判断结算后右括号后有没有触发翻倍
        if i != '}':
            if i.isdigit():  # 是数字则将最后一个入栈的出栈，然后翻倍再入栈
                stack.append(stack.pop() * int(i))
            else:
                stack.append(i)
        else:
            sub_res = ''
            # 遇到右括号进入括号结算
            while True:
                last = stack.pop()  # 出栈
                sub_res = last + sub_res
                if last == '{':
                    break
            stack.append(sub_res)
    print(''.join(stack).replace('{', ''))


fun()
