#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2023/4/8 21:54
# @Author  : 刘双喜
# @File    : 22.定时器.py
# @Description : 添加描述
import sched
import time


def say_hello(name1, name2):
    print(f'{name1},{name2},hello')


sche_obj = sched.scheduler(time.time, time.sleep)  # 实例化对象
sche_obj.enter(2, 1, say_hello, ('lsx', 'ntt'))  # 延时,优先级,函数,函数入参

s = time.strptime('2023:04:08:22:17:01','%Y:%m:%d:%H:%M:%S')
sche_obj.enterabs(time.mktime(s), 1, say_hello, ('lsx', 'ntt')) # 指定时间戳执行
sche_obj.run()
