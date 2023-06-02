#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2023/4/6 22:36
# @Author  : 刘双喜
# @File    : 18.excel画图.py
# @Description : 添加描述
from openpyxl.chart import LineChart,Reference
from openpyxl import load_workbook


excel = load_workbook('18.excel-demo.xlsx')
sheet = excel['Sheet1']

# 实例化图表
chart = LineChart()

# 选择数据来源
data = Reference(sheet, min_col=2, min_row=1, max_col=3, max_row=9)
# 标签数据来源
categories = Reference(sheet, min_col=1, min_row=1, max_col=1, max_row=9)  # X轴标签来源

# 设置图表属性
chart.x_axis.title = "工龄"
chart.y_axis.title = "工资"
# 设置图表属性 - 添加数据
chart.add_data(data, titles_from_data=True, from_rows=False)  # from_rows:以行数据画图
# 设置图表属性 - 设置标签
chart.set_categories(categories)

# 添加图表
sheet.add_chart(chart, 'A11')
excel.save('18.excel-demo.xlsx')

"""
chart图表属性
# 创建LineChart对象
chart = LineChart()
# 给图表设置标题
chart.title = "Report"
# 给x轴和y轴设置标题
chart.x_axis.title = "Date"
chart.y_axis.title = "Price"
# 设置大小
chart.width = 15
chart.height = 12
# 设置图表的风格
chart.style = 15
# 设置数据点的分组方式
chart.grouping = "standard"
# 设置数据点的形状和大小
chart.shape = "circle"
chart.marker_size = 8
# 设置曲线是否光滑
chart.smooth = True
# 设置图例
chart.legend.position = "right"
chart.legend.include_in_layout = False
# 设置数据标签
chart.data_labels.font = "Calibri"
chart.data_labels.position = "inside"
# 添加数据
chat.add_data(data,titles_from_data=True,from_rows=False)
"""