#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2023/7/13 22:55
# @Author  : 刘双喜
# @File    : 49.CIFAR10_Train.py
# @Description : 添加描述
import torch.optim
import torchvision
from torch import nn
from torch.utils.data import DataLoader
from torch.utils.tensorboard import SummaryWriter
from torch.nn import Conv2d, MaxPool2d, Flatten, Linear, Sequential


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

train_data = torchvision.datasets.CIFAR10('../../dataset/36.datasets', train=True,
                                         transform=torchvision.transforms.ToTensor(),
                                         download=True)
test_data = torchvision.datasets.CIFAR10('../../dataset/36.datasets', train=False,
                                         transform=torchvision.transforms.ToTensor(),
                                         download=True)

write = SummaryWriter('..\\data\\49.CIFAR10_Train')
# tensorboard --logdir='.\\example\\data\\40.nn_Conv2d' --port=6012
train_loader = DataLoader(dataset=train_data, batch_size=64, shuffle=False)
test_loader = DataLoader(dataset=test_data, batch_size=64, shuffle=False)

train_data_len = len(train_data)
test_data_len = len(test_data)

demo = Demo()

# 计算损失
loss_fn = nn.CrossEntropyLoss()

# 优化器
learn_rate = 1e-2
optim = torch.optim.SGD(demo.parameters(), lr=learn_rate)

# 训练次数
epochs = 3
total_train_step = 0
for epoch in range(epochs):
    print(f'第{epoch}轮训练'.center(50, '-'))
    epochs_train_loss = 0
    for data in train_loader:
        imgs, labels = data
        # 卷积层 - 处理特征
        outputs = demo(imgs)
        # 损失函数层 - 计算损失
        loss = loss_fn(outputs, labels)
        # 优化器 - 算法优化参数
        optim.zero_grad()
        loss.backward()
        optim.step()
        epochs_train_loss += loss.item()
        total_train_step += 1
        if total_train_step % 100 == 0:
            print(f'第{total_train_step}次训练，损失：{loss.item()},进度{round((total_train_step/(len(train_loader)*epochs))*100, 4)}%'.center(50, '-'))
            write.add_scalar('train_loss', loss.item(), total_train_step)
    # 测试集测试
    total_test_loss = 0
    with torch.no_grad():
        for data in test_loader:
            imgs, labels = data
            outputs = demo(imgs)
            loss = loss_fn(outputs, labels)
            total_test_loss += loss.item()
    print(f'测试集损失{total_test_loss}'.center(50, '-'))
    write.add_scalar('test_loss', total_test_loss, epochs)

    torch.save(demo.state_dict(), f'..\\data\\49.CIFAR10_Train\\module_epoch{epoch}')
write.close()

argmax