#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2025/3/8 22:44
# @Author  : 刘双喜
# @File    : settings_page.py
# @Description : 添加描述
# views/settings_page.py
# views/settings_page.py
from PyQt6.QtWidgets import QWidget, QVBoxLayout, QLabel, QPushButton
from PyQt6.QtWidgets import QWidget, QVBoxLayout, QLabel, QPushButton, QProgressBar


class SettingsPage(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        layout = QVBoxLayout()

        self.title = QLabel("Settings Page")
        self.back_btn = QPushButton("Back to Home")
        self.do_btn = QPushButton("Do Something")
        self.progress_bar = QProgressBar()
        self.progress_bar.setRange(0, 100)  # 设置进度范围
        self.progress_bar.setValue(0)  # 初始值归零
        self.progress_bar.hide()

        layout.addWidget(self.title)
        layout.addWidget(self.back_btn)
        layout.addWidget(self.do_btn)
        layout.addWidget(self.progress_bar)
        layout.addStretch()

        self.setLayout(layout)
        # 设置对象名称方便样式控制
        self.do_btn.setObjectName("actionButton")
        self.back_btn.setObjectName("backButton")
        self.progress_bar.setObjectName("feature1Progress")
        # 正确连接信号到控制器（应移除直接的事件处理）
        # self.back_btn.clicked.connect(self.on_back_clicked)  # 删除这行

    # 删除旧的页面跳转方法
    # def on_back_clicked(self):
    #    self.window().navigate_to("home")  # 错误方法