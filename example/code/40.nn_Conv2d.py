#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2023/6/26 21:59
# @Author  : 刘双喜
# @File    : 40.nn_Conv2d.py
# @Description : 添加描述
import torch
import torchvision
from torch import nn
from torch.nn import Conv2d
from torch.utils.data import DataLoader
from torch.utils.tensorboard import SummaryWriter


class Demo(nn.Module):
    def __init__(self):
        super(Demo, self).__init__()
        self.conv = Conv2d(in_channels=3, out_channels=6, kernel_size=3, stride=1, padding=0)

    def forward(self, x):
        return self.conv(x)


test_data = torchvision.datasets.CIFAR10('../../dataset/36.datasets', train=False,
                                         transform=torchvision.transforms.ToTensor(),
                                         download=True)

test_loader = DataLoader(dataset=test_data, batch_size=100, shuffle=False, num_workers=0, drop_last=True)

demo = Demo()
#  tensorboard --logdir='.\\example\\data\\40.nn_Conv2d' --port=6012
with SummaryWriter('..\\data\\40.nn_Conv2d') as write:
    for step, data in enumerate(test_loader):
        if step > 50:
            continue
        imgs, lables = data
        # print(imgs.shape)  torch.Size([64, 3, 32, 32])
        conv_imgs = demo(imgs)
        # print(conv_imgs.shape) torch.Size([64, 6, 30, 30])
        conv_imgs = torch.reshape(conv_imgs, (-1, 3, 30, 30))
        # print(conv_imgs.shape) torch.Size([128, 3, 30, 30])
        write.add_images('input', imgs, step)
        write.add_images('output', conv_imgs, step)
