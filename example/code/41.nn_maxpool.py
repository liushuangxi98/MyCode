#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2023/6/29 20:37
# @Author  : 刘双喜
# @File    : 41.nn_maxpool.py
# @Description : 添加描述
import torchvision
from torch import nn
from torch.utils.data import DataLoader
from torchvision.datasets import CIFAR10
from torch.nn import Conv2d, MaxPool2d
from torch.utils.tensorboard import SummaryWriter


class Demo(nn.Module):
    def __init__(self):
        super(Demo, self).__init__()
        self.maxpool = MaxPool2d(kernel_size=2, ceil_mode=False)

    def forward(self, x):
        return self.maxpool(x)


test_data = torchvision.datasets.CIFAR10('../../dataset/36.datasets', train=False,
                                         transform=torchvision.transforms.ToTensor(),
                                         download=True)

test_loader = DataLoader(dataset=test_data, batch_size=64, shuffle=False, num_workers=0, drop_last=True)

demo = Demo()
with SummaryWriter('..\\data\\41.nn_maxpool') as write:
    for step, data in enumerate(test_loader):
        imgs, lables = data
        write.add_images('input', imgs, step)
        output = demo(imgs)
        write.add_images('output', output, step)

