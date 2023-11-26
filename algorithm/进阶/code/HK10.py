#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2023/11/23 20:17
# @Author  : 刘双喜
# @File    : HK10.py
# @Description : 单调栈
# 数字字符串中，去除重复数字能保留下来的最大数字
import random
import time


def fun2(n):
    # n = '9855408780'
    stt = time.time()
    cnt = [0] * 10  # 数字都是0-9呀，所以。
    s = []
    vis = [0] * 10
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
            while st and s[i] > st[-1] and cnt[st[-1]] > 0 and not vis[s[i]]:
                vis[st[-1]] = 0  # 弹出之后，要把这个标记为未访问。这个重要。
                st.pop()
            # 弹栈完了,vis[s[i]]不能访问过。
            if not vis[s[i]]:
                st.append(s[i])  # 加入单调栈里。
                vis[s[i]] = 1  # 标记为已访问。
    # 栈里的元素保留的就是最棒的。
    return "".join(map(str, st)), time.time() - stt


def fun3(n):
    # n = '9855408780'
    st = time.time()
    stack = []
    n = list(map(int, n))
    count = [n.count(i) for i in range(0, 10)]
    for i in n:
        if i in stack and stack.count(i) >= 2:  # 当前元素已经在栈内了,栈内已经容纳满了该元素
            count[i] -= 1
            continue
        elif stack:  # 栈非空则判断栈顶是否合法
            while True:  # '5445795045'
                # 栈顶的元素，如果比当前元素小并且有重复并且当前元素不在栈内，则需要出栈
                if stack and stack[-1] <= i and count[stack[-1]] >= 3:
                    out = stack.pop()
                    count[out] -= 1
                else:
                    # 如果当前元素不在栈内则入栈
                    stack.append(i)
                    break
        else:
            stack.append(i)  # 栈是空则入栈
    return ''.join(map(str, stack)), time.time() - st


# for i in range(10):
#     n = '5445795045'
#     n = str(random.randint(1111111111, 9999999999))
#     # n = n*10000
#     # n = '8448796048'
#
#     s2, t2 = fun2(n)
#     s3, t3 = fun3(n)
#     if len(set([s2, s3])) != 1:
#         print(n, s2, s3)

s1,t1 = fun3('34533')
print(s1)