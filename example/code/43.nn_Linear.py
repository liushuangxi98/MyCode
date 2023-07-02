#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2023/7/2 16:33
# @Author  : 刘双喜
# @File    : 43.nn_Linear.py
# @Description : 添加描述
import torch
import torchvision
from torch import nn
from torch.utils.data import DataLoader, Subset
from torchvision.datasets import CIFAR10
from torch.nn import Conv2d, MaxPool2d, ReLU, Sigmoid, Linear
from torch.utils.tensorboard import SummaryWriter


class Demo(nn.Module):
    def __init__(self):
        super(Demo, self).__init__()
        self.linear = Linear(196608, 10)

    def forward(self, x):
        return self.linear(x)


test_data = torchvision.datasets.CIFAR10('../../dataset/36.datasets', train=False,
                                         transform=torchvision.transforms.ToTensor(),
                                         download=True)
test_data = Subset(test_data, range(640))

test_loader = DataLoader(dataset=test_data, batch_size=64, shuffle=False, num_workers=0, drop_last=True)

demo = Demo()
#  tensorboard --logdir='.\\example\\data\\42.nn_linear' --port=6012

for step, data in enumerate(test_loader):
    imgs, lables = data
    output = torch.flatten(imgs)
    print('展平后的形状', output.shape)
    # output = torch.reshape(imgs, (1, 1, 1, -1))
    # print('reshape后的形状', output.shape)
    output = demo(output)
    print('线性变换后的形状', output.shape)
