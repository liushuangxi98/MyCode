#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2023/6/11 12:40
# @Author  : 刘双喜
# @File    : 36.datasets.py
# @Description : 添加描述
import torchvision
from torch.utils.tensorboard import SummaryWriter


transforms = torchvision.transforms.Compose([
    torchvision.transforms.ToTensor()
])

train_data = torchvision.datasets.CIFAR10('../../dataset/36.datasets', train=True, transform=transforms, download=True)
test_data = torchvision.datasets.CIFAR10('../../dataset/36.datasets', train=False, transform=transforms, download=True)

with SummaryWriter('..\\data\\36.datasets') as write:
    for i in range(2000):
        img, label = train_data[i]
        if label == 8:
            write.add_image("train_data", img, i)
