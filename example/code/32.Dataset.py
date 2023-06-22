#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2023/6/3 19:00
# @Author  : 刘双喜
# @File    : 32.Dataset.py
# @Description : Dataset类演示
from torch.utils.data import Dataset, ConcatDataset
import os
from PIL import Image


class GetImgData(Dataset):
    def __init__(self, src_dir, label_dir):
        self.src_dir, self.label_dir = src_dir, label_dir
        self.path = os.path.join(src_dir, label_dir)
        self.label_ls = os.listdir(self.path)

    def __getitem__(self, item):
        item_path = os.path.join(self.path, self.label_ls[item])
        # 打开对应列表索引的名称的图片
        img = Image.open(item_path)
        return img

    def __len__(self):
        return len(self.label_ls)

    def __add__(self, other):
        return ConcatDataset([self, other])


if __name__ == '__main__':
    src_dir = '..\\..\\dataset\\32.Dataset\\hymenoptera_data\\train'
    ants = GetImgData(src_dir, 'ants')
    bees = GetImgData(src_dir, 'bees')
    all = ants + bees
    all[1].show()
