#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2023/7/9 16:35
# @Author  : 刘双喜
# @File    : 47.torchvision.models.vgg16.py
# @Description : 添加描述
import torchvision
from torch import nn
from torchvision.models import VGG16_Weights, vgg16

vgg16_model = vgg16(weights=VGG16_Weights.IMAGENET1K_V1)
vgg16_model.classifier[6] = nn.Linear(4096, 100)  # 修改在classifier层的第6个模块
vgg16_model.classifier.add_module('7', nn.Linear(100, 10))  # 在classifier层增加一个模块，将线性回归1000个类别变成10个
print(vgg16_model)  # 打印模型的结构
print(vgg16_model.state_dict())  # 打印模型的权重和偏置
print(vgg16_model.state_dict()['classifier.0.weight'])  # 打印模型特定层的权重偏置