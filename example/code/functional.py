#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2023/6/24 22:01
# @Author  : 刘双喜
# @File    : functional.py
# @Description : 添加描述
import torch
from torch.nn import functional as F

input = torch.tensor([[1,2,0,3,1],
                      [0,1,2,3,1],
                      [1,2,1,0,1],
                      [5,2,3,1,1],
                      [2,1,0,1,1]])

kernel = torch.tensor([[1,2,3],
                       [0,1,0],
                       [2,1,0]])

input = torch.reshape(input, (1,1,5,5))
kernel = torch.reshape(kernel, (1,1,3,3))

output1 = F.conv2d(input, kernel, stride=1)
output2 = F.conv2d(input, kernel, stride=2)

print(output1)
print(output2)