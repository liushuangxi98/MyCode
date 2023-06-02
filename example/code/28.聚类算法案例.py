#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2023/5/2 13:44
# @Author  : 刘双喜
# @File    : 28.聚类算法案例.py
# @Description : 添加描述
import matplotlib.pyplot as plt
from sklearn.datasets._samples_generator import make_blobs
from sklearn.cluster import KMeans
from sklearn.metrics import calinski_harabasz_score

# 创建数据集
# x为样本特征值，y为样本簇类别
x, y = make_blobs(n_samples=1000,  # 样本数量
                  n_features=2,    # 特征类别数量
                  centers=[[-1, -1], [0, 0], [1, 1], [2, 2]],  # 围绕的簇中心数量和位置
                  cluster_std=[0.4, 0.2, 0.2, 0.2],  # 簇方差
                  random_state=9)
plt.scatter(x[:,0], x[:,1], marker='+')  #
plt.show()

y_pred = KMeans(n_clusters=2,random_state=9).fit_predict(x)
plt.scatter(x[:,0], x[:,1],c=y_pred)
plt.show()

# CH评估聚类分数
print(calinski_harabasz_score(x, y_pred))
