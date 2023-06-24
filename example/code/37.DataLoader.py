#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2023/6/23 23:53
# @Author  : 刘双喜
# @File    : 37.DataLoader.py
# @Description : 添加描述
import torchvision
from torch.utils.data import DataLoader
from torch.utils.tensorboard import SummaryWriter

test_data = torchvision.datasets.CIFAR10('../../dataset/36.datasets', train=False,
                                         transform=torchvision.transforms.ToTensor(),
                                         download=True)

test_loader = DataLoader(dataset=test_data, batch_size=100, shuffle=True, num_workers=0, drop_last=True)

with SummaryWriter('..\\data\\37.dataloader') as write:
    for epoch in range(2):
        idx = 0
        for data in test_loader:
            imgs, labels = data
            write.add_images(f"Epoch:{epoch}", imgs, idx)
            idx += 1