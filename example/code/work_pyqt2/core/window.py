#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2025/3/8 22:43
# @Author  : 刘双喜
# @File    : window.py
# @Description : 添加描述
from PyQt6.QtWidgets import (QMainWindow, QWidget, QHBoxLayout,
                             QVBoxLayout, QPushButton, QStackedWidget)
from views import HomePage, DataPage, SettingsPage
from utils.styles import load_stylesheet


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Navigation Demo")
        self.resize(1024, 768)

        # 创建主布局
        main_widget = QWidget()
        self.setCentralWidget(main_widget)
        main_layout = QHBoxLayout(main_widget)
        main_layout.setContentsMargins(0, 0, 0, 0)
        main_layout.setSpacing(0)

        # 左侧导航栏
        self.sidebar = QWidget()
        self.sidebar.setObjectName("sidebar")
        sidebar_layout = QVBoxLayout(self.sidebar)
        sidebar_layout.setContentsMargins(10, 20, 10, 20)
        sidebar_layout.setSpacing(15)

        # 导航按钮
        self.btn_home = QPushButton("Home")
        self.btn_home.setObjectName("navButton")
        self.btn_data = QPushButton("Data")
        self.btn_data.setObjectName("navButton")
        self.btn_settings = QPushButton("Settings")
        self.btn_settings.setObjectName("navButton")

        # 添加按钮到侧边栏
        sidebar_layout.addWidget(self.btn_home)
        sidebar_layout.addWidget(self.btn_data)
        sidebar_layout.addWidget(self.btn_settings)
        sidebar_layout.addStretch()

        # 右侧内容区域
        self.content_area = QStackedWidget()

        # 初始化页面
        self.pages = {
            "home": HomePage(),
            "data": DataPage(),
            "settings": SettingsPage()
        }

        # 添加页面到堆栈
        for page in self.pages.values():
            self.content_area.addWidget(page)

        # 组合布局
        main_layout.addWidget(self.sidebar, stretch=1)
        main_layout.addWidget(self.content_area, stretch=4)

        # 应用样式
        self.setStyleSheet(load_stylesheet())

    def switch_page(self, page_name):
        if page_name in self.pages:
            self.content_area.setCurrentWidget(self.pages[page_name])

    # def navigate_to(self, page_name):
    #     if page_name in self.pages:
    #         self.stacked_widget.setCurrentWidget(self.pages[page_name])