#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 4/12/2022 下午3:50
# @Author  : 刘双喜
# @File    : 10.线性回归api.py
# @Description : 添加描述
from sklearn.linear_model import LinearRegression

# 构造数据集
x = [[80, 86],
     [82, 80],
     [85, 78],
     [90, 90],
     [86, 82],
     [82, 90],
     [78, 80],
     [92, 94]]
y = [84.2, 80.6, 80.1, 90, 83.2, 87.6, 79.4, 93.4]

# 实例化估计器
estimator = LinearRegression()
# fit方法训练
estimator.fit(x, y)
# 查看系数
coef = estimator.coef_
print('线性回归系数', coef)
# 预测
y_1 = estimator.predict([[100, 40]])
print(y_1)
