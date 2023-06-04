#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2023/6/4 15:07
# @Author  : 刘双喜
# @File    : 34.tensorboard_img.py
# @Description : 添加描述
import os
from PIL import Image
import numpy as np
from torch.utils.tensorboard import SummaryWriter


dir_img = '..\\..\\dataset\\34.tensorboard_img_test\\train\\ants_image'
with SummaryWriter('..\\data\\34.tensorborad_img') as write:
    for idx, img_name in enumerate(os.listdir(dir_img)):
        img = Image.open(os.path.join(dir_img,img_name))
        if img is not None:
            img_arr = np.array(img)
            write.add_image('ants', img_arr, idx, dataformats='HWC')