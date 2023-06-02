#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 6/11/2022 下午5:05
# @Author  : 刘双喜
# @File    : 5.鸢尾花种类预测-流程实现.py
# @Description : 添加描述
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier


# 1、获取数据
iris = load_iris()
target_data = iris.target
feature_data = iris.data
# print('目标值数据\n', target_data)
# print('特征数据\n', feature_data)
# print("鸢尾花特征的名字：\n", iris.feature_names)
# print("鸢尾花目标值的名字：\n", iris.target_names)
# print("鸢尾花的描述：\n", iris.DESCR)

# 2、数据分割测试集和训练集
feature_data_train, feature_data_test, target_data_train, target_data_test = train_test_split(feature_data, target_data,
                                                                                              test_size=0.2)
# print('训练集特征数据：\n', feature_data_train)
# print('训练集目标数据：\n', target_data_train)
# print('测试集特征数据：\n', feature_data_test)
# print('测试集目标数据：\n', target_data_test)

# 3、特征预处理，标准化训练集和测试集的特征值
# 实例化转换器
transfer = StandardScaler()
feature_data_train = transfer.fit_transform(feature_data_train)
feature_data_test = transfer.fit_transform(feature_data_test)
# print('标准化后的特征值训练数据：\n', feature_data_train)
# print('标准化后的特征值测试数据：\n', feature_data_test)

# 4、训练数据
# 实例化估计器
estimator = KNeighborsClassifier(n_neighbors=5, algorithm='auto')
estimator.fit(feature_data_train, target_data_train)

# 预测计算测试集的特征值的目标值
target_data_predict = estimator.predict(feature_data_test)
# print('预测的目标值：\n', target_data_predict)
# print('实际的目标值：\n', target_data_test)
# print('对比的目标值：\n', target_data_predict == target_data_test)

# 预测测试集，并返回测试集的准确率
score = estimator.score(feature_data_test, target_data_test)
print('k=5的测试集准确度:\n', score)

# 5、交叉验证和网格搜索
# 将估计器交叉验证实例化
k = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
cv = 20
estimator_cv = GridSearchCV(estimator, param_grid={'n_neighbors': k}, cv=cv)
estimator_cv.fit(feature_data_train, target_data_train)

# cv估计器的结果
print(f'k={k},cv={cv}时交叉验证的训练集最高准确度:\n', estimator_cv.best_score_)
# print(f'k={k},cv={cv}时交叉验证的最好的参数模型:\n', estimator_cv.best_estimator_)
print(f'k={k},cv={cv}时交叉验证的最好的参数模型的k值:\n', k_best := estimator_cv.best_estimator_.n_neighbors)
# print(f'每次交叉验证后的准确率结果:\n', estimator_cv.cv_results_)

# 6、用最好的模型训练数据
# 实例化估计器
estimator_best = KNeighborsClassifier(n_neighbors=k_best)
estimator_best.fit(feature_data_train, target_data_train)
# 预测测试集，并返回测试集的准确率
score_best = estimator_best.score(feature_data_test, target_data_test)
print('最好的模型测试集的准确度:\n', score_best)
