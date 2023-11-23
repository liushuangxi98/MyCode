#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2023/11/23 20:17
# @Author  : 刘双喜
# @File    : HK10.py
# @Description : 添加描述
import sys
import time


def fun1():
    sys.set_int_max_str_digits(10000000)
    st = time.time()
    _s = '34533'
    _s = '5445795045'*10000
    for i in _s[::]:
        if _s.count(i) <= 1:
            continue
        else:
            # 查找所有出现过数字i的位置，依次替换，找到最大值
            res, start = [], 0
            while True:
                idx = _s[start:].find(i)
                if idx != -1:
                    res.append(_s[0:idx + start] + _s[idx + 1 + start:])
                    start = start + idx + 1
                else:
                    break
            _s = str(max(res, key=int))
    print(_s)
    print('fun1',time.time()-st)


def fun2():
    stt = time.time()
    cnt = [0] * 10  # 数字都是0-9呀，所以。
    s = []
    vis = [0] * 10
    n = '5445795045'
    # n = '12341'
    # 统计字符出现的次数
    for c in n:
        cnt[int(c)] += 1
        s.append(int(c))  # 转化为int型再添加进去。
    st = []  # 定义栈
    for i in range(len(s)):
        cnt[s[i]] -= 1  # 要对这个字符进行处理，所以先要减去1
        if not st:
            # 栈为空，那就要把他加进来
            st.append(s[i])
            vis[s[i]] = 1  # 这个数标记为已经访问了。
        else:
            # 栈不为空，就要进行单调栈处理逻辑
            # 栈不为空，当前值大于栈顶元素，
            # cnt[st[-1]]>0 不然你把它弹出，后面没有了就尴尬了
            # vis[s[i]] 要为0,不能访问过。如果访问过一定在里边，或者后面还有。
            while st and st[-1] < s[i] and cnt[st[-1]] and not vis[s[i]]:
                vis[st[-1]] = 0  # 弹出之后，要把这个标记为未访问。这个重要。
                st.pop()
            # 弹栈完了,vis[s[i]]不能访问过。
            if not vis[s[i]]:
                st.append(s[i])  # 加入单调栈里。
                vis[s[i]] = 1  # 标记为已访问。
    # 栈里的元素保留的就是最棒的。
    print(int("".join(map(str, st))))
    print('fun2', time.time()-stt)


# fun1()
fun2()
