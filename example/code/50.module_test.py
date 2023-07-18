#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2023/7/17 21:02
# @Author  : 刘双喜
# @File    : 50.module_test.py
# @Description : 添加描述
import time
import torch.optim
from torch import nn
from torch.utils.data import DataLoader
from torch.utils.tensorboard import SummaryWriter
from torch.nn import Conv2d, MaxPool2d, Flatten, Linear, Sequential
import torchvision
from PIL import Image
import numpy as np


img_path = '..\\data\\50.model\\person1.png'
img = Image.open(img_path)
img = img.convert("RGB")
transform = torchvision.transforms.Compose([torchvision.transforms.Resize((32,32)),
                                           torchvision.transforms.ToTensor()])
img = transform(img)

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
            Linear(64*4*4, 64),
            Linear(64, 10),
        )

    def forward(self, x):
        return self.module1(x)


demo = Demo()
demo.load_state_dict(torch.load('..\\data\\50.model\\module_epoch30.pth', map_location=torch.device('cpu')))
demo.eval()

img = torch.reshape(img, (1,  3, 32, 32))

class_to_idx = {'airplane': 0, 'automobile': 1, 'bird': 2, 'cat': 3, 'deer': 4, 'dog': 5, 'frog': 6, 'horse': 7, 'ship': 8, 'truck': 9}
idx_to_class = {v: k for k, v in class_to_idx.items()}
with torch.no_grad():
    output = demo(img)
    predict_label_idx = output.argmax(1)
    print(idx_to_class.get(predict_label_idx.item()))
