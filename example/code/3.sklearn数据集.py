#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 27/10/2022 下午8:51
# @Author  : 刘双喜
# @File    : sklearn数据集.py
# @Description : 添加描述
from sklearn.datasets import load_iris, fetch_20newsgroups

iris = load_iris()  # 返回值是一个继承自字典的Bench
print("鸢尾花数据集的返回值：\n", iris)
print("鸢尾花的特征值:\n", iris["data"])  # 特征数据数组，是 [n_samples * n_features] 的二维 numpy.ndarray 数组
print("鸢尾花的目标值：\n", iris.target)  # 标签(目标值)数组，是 [n_samples * n_features] 的二维 numpy.ndarray 数组
print("鸢尾花特征的名字：\n", iris.feature_names)    # 特征名,新闻数据，手写数字、回归数据集没有
print("鸢尾花目标值的名字：\n", iris.target_names)  # 标签(目标值)名
print("鸢尾花的描述：\n", iris.DESCR)  # 数据描述
