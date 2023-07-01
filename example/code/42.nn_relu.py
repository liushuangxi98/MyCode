#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2023/6/29 20:37
# @Author  : 刘双喜
# @File    : 41.nn_maxpool.py
# @Description : 添加描述
import torchvision
from torch import nn
from torch.utils.data import DataLoader, Subset
from torchvision.datasets import CIFAR10
from torch.nn import Conv2d, MaxPool2d, ReLU, Sigmoid
from torch.utils.tensorboard import SummaryWriter


class Demo(nn.Module):
    def __init__(self):
        super(Demo, self).__init__()
        self.relu = ReLU()
        self.sigmoid = Sigmoid()

    def forward(self, x):
        return self.sigmoid(x)


test_data = torchvision.datasets.CIFAR10('../../dataset/36.datasets', train=False,
                                         transform=torchvision.transforms.ToTensor(),
                                         download=True)
test_data = Subset(test_data, range(1000))

test_loader = DataLoader(dataset=test_data, batch_size=64, shuffle=False, num_workers=0, drop_last=True)

demo = Demo()
#  tensorboard --logdir='.\\example\\data\\42.nn_relu' --port=6012
with SummaryWriter('..\\data\\42.nn_relu') as write:
    for step, data in enumerate(test_loader):
        imgs, lables = data
        write.add_images('input', imgs, step)
        output = demo(imgs)
        write.add_images('output', output, step)

