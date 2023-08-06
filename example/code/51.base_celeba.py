import torch.optim
import torchvision
from torch import nn
from torch.utils.data import DataLoader, Subset
from torch.utils.tensorboard import SummaryWriter
from torch.nn import Conv2d, MaxPool2d, Flatten, Linear, Sequential, Sigmoid
import time
from PIL import Image
import numpy as np
import os
from COMMON_DATA_FUN import ComDataFun


class Model(nn.Module):
    def __init__(self):
        super(Model, self).__init__()
        self.feature_process = Sequential(Conv2d(3, 30, kernel_size=50, stride=1, padding=0),
                                          MaxPool2d(2),
                                          Flatten(),
                                          Linear(30 * 84 * 64, 40),
                                          Sigmoid()
                                          )

    def forward(self, x):
        x = self.feature_process(x)
        return x


# 数据集
dataset_path = r'E:\file\python\MyCode\dataset\51.datasets'
train_data = torchvision.datasets.CelebA(root=dataset_path, split='train', target_type='attr',
                                         transform=torchvision.transforms.ToTensor(), download=False)
test_data = torchvision.datasets.CelebA(root=dataset_path, split='test', target_type='attr',
                                        transform=torchvision.transforms.ToTensor(), download=False)

train_loader = DataLoader(dataset=train_data, batch_size=100, shuffle=False)
test_loader = DataLoader(dataset=test_data, batch_size=100, shuffle=False)

# 全局变量
cuda_available = torch.cuda.is_available()  # GPU是否可用
device = torch.device('cuda' if cuda_available else 'cpu')
# 创建模型
demo = Model()
demo.to(device)
# 损失函数
loss_fn = nn.BCEWithLogitsLoss()
loss_fn.to(device)
# 优化器
learn_rate = 1e-2
optim = torch.optim.SGD(demo.parameters(), lr=learn_rate)
# 画板 tensorboard --logdir='.\\example\\data\\40.nn_Conv2d' --port=6012
write = SummaryWriter('..\\data\\51.base_celeba')

# 开始训练
total_train_step, epochs = 0, 10
for epoch in range(1, 1 + epochs):
    print(f'第{epoch}轮训练'.center(50, '-'))
    epochs_train_loss = 0  # 批次训练集总损失
    for data in train_loader:
        imgs, labels = data
        imgs = imgs.to(device)
        labels = labels.float()
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
    print(f'第{epoch}轮训练完成，总损失{epochs_train_loss}')

    torch.save(demo.state_dict(), f'..\\data\\51.base_celeba\\CelebA_module_epoch{epoch}')

    epochs_test_loss, correct_rate_ls = 0, []  # 批次训练集总损失
    with torch.no_grad():  # 测试的时候进入没有梯度计算模式，节省内存消耗并加快计算速度
        for data in test_loader:
            imgs, labels = data
            imgs = imgs.to(device)
            labels = labels.to(device)
            labels = labels.float()
            outputs = demo(imgs)
            # 计算测试集损失
            loss = loss_fn(outputs, labels)
            epochs_test_loss += loss.item()
            # 计算正确率
            correct_rate = ComDataFun.model_eval(torch.round(outputs).int(), labels, 'precision')
            correct_rate_ls.append(correct_rate)
    print(f'epoch{epoch}正确率', sum(correct_rate_ls)/len(correct_rate_ls))
    print(f'第{epoch}批次测试，损失{epochs_test_loss}')
    write.add_scalar('test_loss', epochs_test_loss, epochs)
