#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 25/9/2022 下午5:00
# @Author  : 刘双喜
# @File    : COMMON_DATA_FUN.py
# @Description : 数据处理公共库
import torch
from torch import Tensor


class ComDataFun:
    def __init__(self):
        pass

    @staticmethod
    def is_prime(num: int) -> bool:
        """
        判断是不是素数
        :param num:入参整型数字
        :return: bool类型
        """
        if num <= 1:
            return False
        for i in range(2, num):
            if num % i == 0:
                return False
        return True

    @staticmethod
    def model_eval(output: Tensor, target: Tensor, mode: str = 'precision'):
        """
        模型评估, 计算精确率和召回率
        :param output:一维张量或多维张量
        :param target:一维张量或多维张量
        :param mode:precision
        :return:总体的精确率或召回率
        """
        if mode == 'precision':
            zl = (output == 1)
            zzl = (output == 1) & (target == 1)
            rate = zzl.sum() / zl.sum()
        else:
            raise
        return rate
