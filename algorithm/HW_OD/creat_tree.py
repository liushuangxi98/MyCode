#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2023/11/25 22:38
# @Author  : 刘双喜
# @File    : creat_tree.py
# @Description : 添加描述
# 树节点类
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# 广度优先搜索构造树
def create_tree(_lst):
    if not _lst:
        return None
    # 创建根节点
    _root = TreeNode(_lst[0])
    # 将根节点加入队列
    queue = [_root]
    i = 1
    # 广度优先搜索
    # 1、队列弹出，对弹出节点左、右结点创建树枝。
    # 2、将左、右节点加入队列。
    # 3、循环1~2. 第n层队列将有2**(n-1)个节点等待赋值和创建
    while queue:
        node = queue.pop(0)
        if i < len(_lst) and _lst[i] is not None:
            node.left = TreeNode(_lst[i])
            queue.append(node.left)
        i += 1
        if i < len(_lst) and _lst[i] is not None:
            node.right = TreeNode(_lst[i])
            queue.append(node.right)
        i += 1
    return _root


# 输入数据
lst = list(map(lambda x: int(x) if x != 'null' else None, input().split()))
# 构造树
root = create_tree(lst)
# 输出结果
print(root.val)
