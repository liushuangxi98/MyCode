#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2023/7/12 20:23
# @Author  : 刘双喜
# @File    : 48.module_save_load.py
# @Description : 添加描述
import torch
from torchvision.models import VGG16_Weights, vgg16

vgg16_model = vgg16(weights=VGG16_Weights.IMAGENET1K_V1)

# 方法1
torch.save(vgg16_model, '..\\data\\48.module_test\\vgg16_method.pth')
model1 = torch.load('..\\data\\48.module_test\\vgg16_method.pth')

# 方法2
torch.save(vgg16_model.state_dict(), '..\\data\\48.module_test\\vgg16_method2.pth')
model1 = torch.load('..\\data\\48.module_test\\vgg16_method2.pth')

print(model1)