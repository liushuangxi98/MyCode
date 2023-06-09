#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2023/7/3 21:00
# @Author  : 刘双喜
# @File    : 44.nn_seq.py
# @Description : 添加描述
import torch
from torch import nn
from torch.nn import Conv2d, MaxPool2d, Flatten, Linear, Sequential
from torch.utils.tensorboard import SummaryWriter


class Demo(nn.Module):
    def __init__(self):
        super(Demo, self).__init__()
        self.module1 = Sequential(
            Conv2d(3, 32, 5, padding=2),
            MaxPool2d(2),
            Conv2d(32, 32, 5, padding=2),
            MaxPool2d(2),
            Conv2d(32, 64, 5, padding=2),
            MaxPool2d(2),
            Flatten(),
            Linear(64*4*4, 64),
            Linear(64, 10),
        )

    def forward(self, x):
        return self.module1(x)

demo = Demo()
input = torch.ones((64, 3, 32, 32))
output = demo(input)
print(output.shape)
with SummaryWriter('..\\data\\44.nn_seq') as write:
    write.add_graph(demo, input, verbose=True)