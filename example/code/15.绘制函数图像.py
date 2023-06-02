#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2023/3/30 21:09
# @Author  : 刘双喜
# @File    : 15.绘制函数图像.py
# @Description : 添加描述
import matplotlib.pyplot as plt
import math


plt.figure()
x = [i*0.00001 for i in range(1,99999)]
y = [math.log((1-i)/i,math.e)/2 for i in x]
y = [pow(math.e, i) for i in y]
plt.rcParams['font.sans-serif']=['SimHei']
plt.title('预测值不等于真实值')
plt.plot(x,y)
plt.show()