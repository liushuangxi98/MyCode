#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2023/6/24 14:25
# @Author  : 刘双喜
# @File    : 38.torch.nn.py
# @Description : 添加描述
import torch
from torch import nn


class Demo(nn.Module):
    def __init__(self):
        super(Demo, self).__init__()

    def forward(self, input):
        return input + 1

obj = Demo()
a = torch.tensor(1)
print(obj(a))