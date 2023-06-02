#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2023/4/21 21:23
# @Author  : 刘双喜
# @File    : 25.决策树算法鸢尾花数据演示.py
# @Description : 添加描述
import pandas as pd
from sklearn.feature_extraction import DictVectorizer
from sklearn.tree import DecisionTreeClassifier, export_graphviz


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
print(transfer.get_feature_names_out())

# 3、机器学习
## 实例化估计器
estimator = DecisionTreeClassifier(criterion='entropy', max_depth=5)
## 训练
estimator.fit(x_train,y_train)

# 4、模型评估
socre = estimator.score(x_test,y_test)
print('分数：', socre)
y_predict = estimator.predict(x_test)
print('预测值：', y_predict)

# 5、保存树的结构到dot文件
export_graphviz(estimator, out_file='25.titanic_tree.dot', feature_names=transfer.get_feature_names_out())
# 查看dot文件http://webgraphviz.com/