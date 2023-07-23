#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2023/7/22 14:18
# @Author  : 刘双喜
# @File    : 51.base_cifar.py
# @Description : 添加描述
import torchvision
import matplotlib.pyplot as plt


train_data = torchvision.datasets.CelebA('../../dataset/51.datasets',
                                        # transform=torchvision.transforms.ToTensor(),
                                         download=True)
# test_data = torchvision.datasets.CIFAR100('../../dataset/51.datasets', train=False,
#                                          #transform=torchvision.transforms.ToTensor(),
#                                          download=True)
image, label = train_data[0]

# 显示图片
plt.imshow(image)
plt.show()
print()