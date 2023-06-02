#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2023/3/31 21:07
# @Author  : 刘双喜
# @File    : 16.癌症分类预测.py
# @Description : 添加描述
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report
from sklearn.metrics import roc_auc_score
# 1.获取数据
# 2.基本数据处理
# 2.1 缺失值处理
# 2.2 确定特征值,目标值
# 2.3 分割数据
# 3.特征工程(标准化)
# 4.机器学习(逻辑回归)
# 5.模型评估

# 获取数据
name = ['示例编号', '肿块厚度', '细胞大小均匀性', '细胞形状均匀性',
        '边际附着力', '单个上皮细胞大小', '裸核', '乏味的染色质',
        '正常的核仁', '有丝分裂', '类别']
data = pd.read_csv('16.breast-cancer-wisconsin.data', names=name)

# 缺失值处理
# 1.替换成平均值
# data = data.replace('?', np.nan)  # 将？替换成nan
# for i in data.columns[1:-1]:
#     data[i] = data[i].astype(float)  # 转为float，便于求平均值
#     try:
#         data[i].fillna(data[i].mean(), inplace=True)
#     except Exception as e:
#         print(e)
# 2.删除缺失值
data = data.replace('?', np.nan)
data = data.dropna()

# 确定特征值和目标值
x, y = data.iloc[:, 1:-1], data.iloc[:, -1]

# 分割数据
x_train, x_test, y_train, y_test = train_test_split(x,y,random_state=22)

# 标准化
transfer = StandardScaler()
x_train = transfer.fit_transform(x_train)
x_test = transfer.fit_transform(x_test)

# 机器学习
estimator = LogisticRegression()
estimator.fit(x_train, y_train)

# 模型评估
y_predict = estimator.predict(x_test)
print(f'特征值的测试集的预测结果为：{y_predict}')
score = estimator.score(x_test, y_test)
print(f'分数：{score}')
is_equal = np.equal(y_predict, y_test)
true_count = np.count_nonzero(is_equal == True)
print(f'准确率:{true_count/len(y_predict)}')

# 分类评估方法
ret = classification_report(y_test,y_predict,labels=[2, 4], target_names=['良性', '恶性'])
print(f'分类评估方法：精确率和召回率：\n{ret}')

# AUC计算
y_true = np.where(y_test>2.5,1,0)
print(f'AUC指标：{roc_auc_score(y_true,y_predict)}')