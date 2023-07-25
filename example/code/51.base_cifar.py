#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2023/7/22 14:18
# @Author  : 刘双喜
# @File    : 51.base_cifar.py
# @Description : 添加描述
import torchvision
import matplotlib.pyplot as plt
import time
import torch.optim
import torchvision
from torch import nn
from torch.utils.data import DataLoader
from torch.utils.tensorboard import SummaryWriter
from torch.nn import Conv2d, MaxPool2d, Flatten, Linear, Sequential

class Model(nn.Module):
    def __init__(self):
        super(Model, self).__init__()
        self.feature_process = Sequential([])

    def forword(self, x):
        return self.feature_process(x)
dataset_path = r'D:\file\python\MyCode\dataset\51.datasets'
train_data = torchvision.datasets.CelebA(root=dataset_path, split='train',target_type='attr',transform=None, download=False)
# test_data = torchvision.datasets.CIFAR100('../../dataset/51.datasets', train=False,
#                                          #transform=torchvision.transforms.ToTensor(),
#                                          download=True)
image, label = train_data[0]

# 显示图片
plt.imshow(image)
plt.show()
print()