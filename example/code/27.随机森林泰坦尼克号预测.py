#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2023/4/24 22:13
# @Author  : 刘双喜
# @File    : 27.随机森林泰坦尼克号预测.py
# @Description : 添加描述
import pandas as pd
from sklearn.feature_extraction import DictVectorizer
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import GridSearchCV

# 1、获取数据
data_train = pd.read_csv('25.titanic\\train.csv')

# 2、数据基本处理
## 确定目标值、特征值
x_train = data_train[["Pclass", "Age", "Sex"]]
y_train = data_train['Survived']
## 处理缺失值
x_train['Age'].fillna(x_train['Age'].mean(), inplace=True)
## 数据集划分
x_test = pd.read_csv('25.titanic\\test.csv')[["Pclass", "Age", "Sex"]]
y_test = pd.read_csv('25.titanic\\gender_submission.csv')['Survived']
## 处理缺失值
x_test['Age'].fillna(x_train['Age'].mean(), inplace=True)
# 特征工程
transfer = DictVectorizer(sparse=False)
x_train = transfer.fit_transform(x_train.to_dict('records'))
x_test = transfer.fit_transform(x_test.to_dict('records'))
print('提取特征后的特征名：', transfer.get_feature_names_out())

# 3、机器学习
## 实例化估计器
estimator = RandomForestClassifier()
# 实例化网格搜索对象，训练
param_grid = {"n_estimators": [120, 200, 300, 500, 800, 1200], "max_depth": [5, 8, 15, 25, 30]}
estimator = GridSearchCV(estimator, param_grid=param_grid, cv=5)
## 训练
estimator.fit(x_train, y_train)

# 4、模型评估
# 最好的模型
best_estimator = estimator.best_estimator_
print('最好的模型: ', best_estimator)
# 分数
socre = estimator.score(x_test, y_test)
print('分数：', socre)
y_predict = estimator.predict(x_test)
print('预测值：', y_predict)
