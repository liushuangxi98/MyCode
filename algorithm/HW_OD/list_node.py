#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2023/11/25 21:46
# @Author  : 刘双喜
# @File    : list_node.py
# @Description : 添加描述
class ListNode:
    def __init__(self, val=0, follow=None):
        self.val = val
        self.follow = follow


# 输入数据
lst = list(map(int, input().split()))

# 构造链表
head = ListNode()
cur = head
for num in lst:
    cur.follow = ListNode(num)
    cur = cur.follow

# 输出链表
cur = head.follow
while cur:
    print(cur.val, end=' ')
    cur = cur.follow
