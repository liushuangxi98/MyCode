#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2023/7/22 14:18
# @Author  : 刘双喜
# @File    : 51.base_celeba.py
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

cuda_avaiable = torch.cuda.is_available()  # GPU是否可用
device = torch.device('cuda' if cuda_avaiable else 'cpu')

demo = Model()
demo.to(device)  # 创建模型

loss_fn = nn.CrossEntropyLoss()  # 损失函数
loss_fn.to(device)
# 优化器
learn_rate = 1e-2
optim = torch.optim.SGD(demo.parameters(), lr=learn_rate)
# 训练次数
epochs = 2
total_train_step = 0

# 画板 tensorboard --logdir='.\\example\\data\\40.nn_Conv2d' --port=6012
write = SummaryWriter('..\\data\\51.base_celeba')

dataset_path = r'D:\file\python\MyCode\dataset\51.datasets'
train_data = torchvision.datasets.CelebA(root=dataset_path, split='train',target_type='attr',transform=None, download=False)
test_data = torchvision.datasets.CelebA(root=dataset_path, split='test',target_type='attr',transform=None, download=False)
train_loader = DataLoader(dataset=train_data, batch_size=100, shuffle=False)
test_loader = DataLoader(dataset=test_data, batch_size=100, shuffle=False)

for epoch in range(1, 1 + epochs):
    print(f'第{epoch}轮训练'.center(50, '-'))
    start_time = time.time()
    epochs_train_loss = 0  # 批次训练集总损失
    for data in train_loader:
        imgs, labels = data
        imgs = imgs.to(device)
        labels = labels.to(device)
        # 卷积层 - 处理特征
        outputs = demo(imgs)
        # 损失函数层 - 计算损失
        loss = loss_fn(outputs, labels)
        # 优化器 - 算法优化参数
        optim.zero_grad()
        loss.backward()
        optim.step()
        # 累加损失
        epochs_train_loss += loss.item()
        total_train_step += 1
        if total_train_step % 100 == 0:
            print(total_train_step,epochs_train_loss)
            epochs_train_loss = 0