#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2025/3/8 23:17
# @Author  : 刘双喜
# @File    : data_page.py
# @Description : 添加描述
# views/data_page.py
from PyQt6.QtWidgets import (QWidget, QVBoxLayout, QLabel,
                             QTableWidget, QTableWidgetItem, QHeaderView,
                             QHBoxLayout, QGroupBox)
from PyQt6.QtGui import QColor
from services.database import Database


class DataPage(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        layout = QVBoxLayout()
        layout.setContentsMargins(20, 20, 20, 20)

        # 标题
        self.title = QLabel("Data Management")
        self.title.setProperty("cssClass", "pageTitle")

        # 测试用例信息面板
        self.create_test_info_box()

        # 数据表格
        self.table = QTableWidget()
        self.table.setObjectName("dataTable")
        self.table.verticalHeader().setVisible(False)

        self.init_table()

        layout.addWidget(self.title)
        layout.addWidget(self.test_info_box)
        layout.addWidget(self.table)
        self.setLayout(layout)

    def create_test_info_box(self):
        """创建测试信息展示区"""
        test_info = Database.get_test_info()

        self.test_info_box = QGroupBox("当前测试状态")
        box_layout = QHBoxLayout()

        # 测试用例ID
        self.lbl_case_id = QLabel(f"用例ID: {test_info['TestCaseId']}")
        self.lbl_case_id.setObjectName("testCaseLabel")

        # 测试结果
        self.lbl_result = QLabel(f"结果: {test_info['Result']}")
        self.lbl_result.setObjectName("testResultLabel")

        # 执行时间
        self.lbl_time = QLabel(f"执行时间: {test_info['ExecutionTime']}")
        self.lbl_time.setObjectName("testTimeLabel")

        box_layout.addWidget(self.lbl_case_id)
        box_layout.addWidget(self.lbl_result)
        box_layout.addWidget(self.lbl_time)
        self.test_info_box.setLayout(box_layout)

    def init_table(self):
        """初始化表格数据和样式"""
        headers = ["ID", "Name", "Value", "Status"]
        self.table.setColumnCount(len(headers))
        self.table.setHorizontalHeaderLabels(headers)

        header = self.table.horizontalHeader()
        header.setSectionResizeMode(QHeaderView.ResizeMode.Stretch)

        self.populate_sample_data()

    def populate_sample_data(self):
        """填充示例数据"""
        sample_data = [
            [1, "Temperature", "25°C", "Normal"],
            [2, "Pressure", "1013hPa", "Warning"],
            [3, "Humidity", "65%", "Normal"]
        ]

        self.table.setRowCount(len(sample_data))
        for row_idx, row_data in enumerate(sample_data):
            for col_idx, cell_data in enumerate(row_data):
                item = QTableWidgetItem(str(cell_data))
                if col_idx == 3:  # 状态列特殊样式
                    item.setForeground(QColor("red" if cell_data == "Warning" else "green"))
                self.table.setItem(row_idx, col_idx, item)