#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2025/3/8 22:44
# @Author  : 刘双喜
# @File    : settings_page.py
# @Description : 添加描述
# views/settings_page.py
from PyQt6.QtWidgets import QWidget, QVBoxLayout, QLabel, QPushButton


class SettingsPage(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        layout = QVBoxLayout()

        self.title = QLabel("Settings Page")
        self.back_btn = QPushButton("Back to Home")

        # 添加组件到布局
        layout.addWidget(self.title)
        layout.addStretch()  # 添加弹性空间使按钮靠下
        layout.addWidget(self.back_btn)

        self.setLayout(layout)

        # 连接信号（实际应在controller处理）
        self.back_btn.clicked.connect(self.on_back_clicked)

    def on_back_clicked(self):
        # 实际应该通过控制器处理导航
        self.window().navigate_to("home")