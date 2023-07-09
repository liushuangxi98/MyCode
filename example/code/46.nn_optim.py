#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2023/7/9 13:03
# @Author  : 刘双喜
# @File    : 46.nn_optim.py
# @Description : 添加描述
import torch.optim
import torchvision
from torch import nn
from torch.nn import Conv2d, MaxPool2d, Flatten, Linear, Sequential
from torch.utils.data import Subset, DataLoader
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
            Linear(1024, 64),
            Linear(64, 10),
        )

    def forward(self, x):
        return self.module1(x)


test_data = torchvision.datasets.CIFAR10('../../dataset/36.datasets', train=False,
                                         transform=torchvision.transforms.ToTensor(),
                                         download=True)
test_data = Subset(test_data, range(1000))

test_loader = DataLoader(dataset=test_data, batch_size=64, shuffle=False, num_workers=0, drop_last=True)


loss= nn.CrossEntropyLoss()
demo = Demo()
optim = torch.optim.SGD(demo.parameters(), lr=0.01)
for epoch in range(200):
    epoch_loss = 0
    for data in test_loader:
        imgs, targets = data
        output = demo(imgs)
        res_loss = loss(output, targets)
        optim.zero_grad()
        res_loss.backward()
        optim.step()
        epoch_loss += res_loss
    print(epoch_loss)