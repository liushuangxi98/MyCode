#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2023/3/2 23:34
# @Author  : 刘双喜
# @File    : 1.py
# @Description : 添加描述
import os
import pandas as pd
import matplotlib.pyplot as plt
plt.figure()
merged_col = list(map(int,(input('请输入要合并的列编号，用英文逗号隔开，如：3,4,5\n').split(','))))
# title_col = int(input('请输入频段列编号，如：1\n'))
# one_line_col = int(input('请输入频点或带宽列编号，如：2\n'))
# x_data_col = int(input('请输入要做为横坐标数据的列编号，如：0\n'))
plt.figure()
# 获取当前目录下所有的.xlsx文件
files = [f for f in os.listdir() if f.endswith('.xlsx')]

# 创建一个空的DataFrame来存储合并后的数据
merged_data = pd.DataFrame()

for file in files:
    if '~' in file:
        continue
    # 读取Excel文件
    data = pd.read_excel(file)
    # 选择第3、4、5列数据
    selected_data = data.iloc[:, merged_col]
    # 重命名
    columns = [list(data.columns)[i] for i in merged_col]  # 需要合并的列的列名
    # one_line_title = str(data.iloc[0,one_line_col])
    # new_columns = {column: one_line_title + str(column) for column in columns}   # 重命名
    #selected_data.rename(columns=new_columns, inplace=True)
    # 将选择的数据添加到merged_data中
    merged_data = pd.concat([merged_data, selected_data], axis=0)
# merged_data = pd.concat([data['频道'],merged_data], axis=1)

# 将合并后的数据保存到新的Excel文件中
merged_data.to_excel('merged.xlsx', index=False)

# chart_title = list(data.columns)[title_col] + str(data.iloc[title_col, 1])
# x_data_col_name = list(data.columns)[x_data_col]
#
# # 绘制图表并保存为图片文件
# merged_data.plot(x=x_data_col_name, xlabel=x_data_col_name, title=chart_title)
#
# # 重新设置字体
# plt.rcParams['font.sans-serif'] = ['KaiTi', 'SimHei', 'FangSong']
# plt.savefig('chart.png',dpi=400)