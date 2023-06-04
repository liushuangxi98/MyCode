#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2023/6/4 11:27
# @Author  : 刘双喜
# @File    : 33.tensorboard_scalar.py
# @Description : 绘制动态图像
from torch.utils.tensorboard import SummaryWriter
import os


with SummaryWriter('..\\data\\33.tensorborad') as write:
    for i in range(100):
        # 每次给图表取名不同防止多个线条拟合在一起
        write.add_scalar(f"chart{len(os.listdir('../data/33.tensorborad'))}:y->x", i*i, i)

# 在带tensorboard的环境下运行 tensorboard --logdir=. --port=6012启动。注意log目录路径
