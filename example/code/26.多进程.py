#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2023/4/23 22:57
# @Author  : 刘双喜
# @File    : 26.多进程.py
# 我有一个python的功能函数fun要运行10000次，我如何用多进程的方法来执行它@Description : 直接运行run1:52.50s
import re
import time
from concurrent.futures import ProcessPoolExecutor
from multiprocessing import Process
from multiprocessing import Pool

s = '# @Description : 添加描述'
res_list = []
st = time.time()
cnt = 10000000
cnt = 10000


def fun(s, i = 1):
    res = re.findall(':..', s)
    res = ' '.join(' ')
    res_list.append(res)
    print(round(i/cnt,4)*100, '%')

def run1():
    for i in range(cnt):
        fun(s, i)

def run2():
    for i in range(cnt):
        p = Process(target=fun, args=(s,i,))
        p.start()

def run3():
    pool = Pool(processes=4)  # 创建进程池，使用4个进程
    result = pool.map(fun, range(cnt))  # 在进程池中重复运行fun函数
    pool.close()  # 关闭进程池
    pool.join()  # 阻塞主进程，直到所有子进程完成任务

def run4():
    with ProcessPoolExecutor() as pool:
        res = pool.map(fun, [(s, i) for i in range(cnt)])

if __name__ == '__main__':
    # run2()
    # print('end', time.time() -st)
    st = time.time()
    x=8
    y=x
    for i in range(x):
        x=pow(x,y)
    print(x)
    print('end', time.time() - st)