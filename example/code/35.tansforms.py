#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2023/6/4 20:11
# @Author  : 刘双喜
# @File    : 35.tansforms.py
# @Description : 添加描述
import os
from torch.utils.tensorboard import SummaryWriter
from torchvision import transforms
import cv2
from PIL import Image

# 预处理-转换为张量
# preprocess = transforms.ToTensor()
# 定义预处理过程集合
preprocess = transforms.Compose([
    transforms.Resize(256),  # 缩放到256像素
    transforms.CenterCrop(224),  # 在中心裁剪出224*224像素
    transforms.ToTensor()  # 转换为张量
])
dir_img = '..\\..\\dataset\\34.tensorboard_img_test\\train\\ants_image'
with SummaryWriter('..\\data\\34.tensorborad_img') as write:
    for idx, img_name in enumerate(os.listdir(dir_img)):
        # 读取图片
        # img = cv2.imread(os.path.join(dir_img, img_name))  # 不能读git, 返回数组类型,不能用于tansforms
        img = Image.open(os.path.join(dir_img, img_name))
        if img is not None:
            # 预处理
            tensor_img = preprocess(img)
            # 写入事件文件
            write.add_image('ants', tensor_img, idx, dataformats='CHW')