#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2023/7/13 22:55
# @Author  : 刘双喜
# @File    : 49.CIFAR10_Train.py
# @Description : 添加描述
import time
import torch.optim
import torchvision
from torch import nn
from torch.utils.data import DataLoader
from torch.utils.tensorboard import SummaryWriter
from torch.nn import Conv2d, MaxPool2d, Flatten, Linear, Sequential


# 模型
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

# =======================================================全局变量=====================================================
cuda_avaiable = torch.cuda.is_available()  # GPU是否可用
device = torch.device('cuda' if cuda_avaiable else 'cpu')
demo = Demo()
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
write = SummaryWriter('..\\data\\49.CIFAR10_Train')

#  ======================================================获取数据集合===================================================
train_data = torchvision.datasets.CIFAR10('../../dataset/36.datasets', train=True,
                                         transform=torchvision.transforms.ToTensor(),
                                         download=True)
test_data = torchvision.datasets.CIFAR10('../../dataset/36.datasets', train=False,
                                         transform=torchvision.transforms.ToTensor(),
                                         download=True)

train_loader = DataLoader(dataset=train_data, batch_size=64, shuffle=False)
test_loader = DataLoader(dataset=test_data, batch_size=64, shuffle=False)
train_data_len = len(train_data)
test_data_len = len(test_data)

#  =====================================================开始训练====================================================
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
            write.add_scalar('train_loss', loss.item(), total_train_step)
    print(f'第{epoch}批次训练，损失：{loss.item()},耗时{time.time()-start_time},进度{round(epoch/epochs, 4) * 100}%'.center(
            50, '-'))

    # 测试集测试
    start_time = time.time()
    total_test_loss = 0  # 批次测试集总损失
    right_num = 0   # 正确个数
    with torch.no_grad():  # 测试的时候进入没有梯度计算模式，节省内存消耗并加快计算速度
        for data in test_loader:
            imgs, labels = data
            imgs = imgs.to(device)
            labels = labels.to(device)
            outputs = demo(imgs)
            # 计算测试集损失
            loss = loss_fn(outputs, labels)
            total_test_loss += loss.item()
            # 测试集预测值
            predict = outputs.argmax(dim=1)
            # 预测正确的个数 累加
            right_num += (predict == labels).sum()
    right_rate = right_num / test_data_len
    print(f'第{epoch}批次测试，损失{total_test_loss}, 正确率{right_rate},耗时{time.time()-start_time}'.center(50, '-'))
    write.add_scalar('test_loss', total_test_loss, epochs)

    torch.save(demo.state_dict(), f'..\\data\\49.CIFAR10_Train\\module_epoch{epoch}')
write.close()
