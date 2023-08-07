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
        精确率：预测结果为正例中真实为正例的比例。 精确度低代表过拟合
        召回率：真实结果为正例中预测为正例的比例。 召回率低代表欠拟合
        :param output:一维张量或多维张量
        :param target:一维张量或多维张量
        :param mode:precision
        :return:总体的精确率或召回率
        """
        if mode == 'precision':
            zl = (output == 1)  # 预测正例
            zzl = (output == 1) & (target == 1)  # 预测正例中实际正例数
            rate = zzl.sum() / zl.sum()
        elif mode == 'recall':
            zl = (target == 1)  # 实际正例
            zzl = (target == 1) & (output == 1)  # 实际正例中预测正例数
            rate = zzl.sum() / zl.sum()
        else:
            raise
        return rate
