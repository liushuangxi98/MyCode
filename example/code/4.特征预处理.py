#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 4/11/2022 下午9:59
# @Author  : 刘双喜
# @File    : 4.特征预处理.py
# @Description : 添加描述

# 归一化
# from sklearn.datasets import load_iris, fetch_20newsgroups
# import pandas as pd
# from sklearn.preprocessing import MinMaxScaler
#
# iris = load_iris()
# iris_pd = pd.DataFrame(iris["data"], columns=iris.feature_names)
# # 实例化转换器转换
# transfer = MinMaxScaler(feature_range=(0, 1))
# iris_pd_processed = transfer.fit_transform(iris_pd[['sepal length (cm)', 'sepal width (cm)']])
# print(iris_pd_processed)

# 标准化
from sklearn.preprocessing import StandardScaler
import pandas as pd
from sklearn.datasets import load_iris

iris = load_iris()
iris_pd = pd.DataFrame(iris["data"], columns=iris.feature_names)
# 实例化转换器
transfer = StandardScaler()
iris_pd_processed = transfer.fit_transform(iris_pd[['sepal length (cm)', 'sepal width (cm)']])
print(iris_pd_processed)
