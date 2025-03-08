#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2025/3/8 22:44
# @Author  : 刘双喜
# @File    : main_controller.py
# @Description : 添加描述
# controllers/main_controller.py
from PyQt6.QtCore import QObject


class MainController(QObject):
    def __init__(self, window):
        super().__init__()
        self.window = window
        self.setup_connections()

    def setup_connections(self):
        """集中管理所有信号连接"""
        nav_buttons = {
            "home": self.window.btn_home,
            "data": self.window.btn_data,
            "settings": self.window.btn_settings
        }

        for page_name, btn in nav_buttons.items():
            btn.clicked.connect(
                lambda checked, pn=page_name: self.window.switch_page(pn)
            )

        # 添加按钮激活样式
        self.window.content_area.currentChanged.connect(
            self.update_button_styles
        )

    def update_button_styles(self):
        """更新导航按钮激活状态"""
        current_page = self.window.content_area.currentWidget()
        page_names = {v: k for k, v in self.window.pages.items()}

        # 重置所有按钮样式
        for btn in [self.window.btn_home,
                    self.window.btn_data,
                    self.window.btn_settings]:
            btn.setStyleSheet("")

        # 设置当前按钮激活样式
        if current_page in page_names:
            current_btn = getattr(self.window, f"btn_{page_names[current_page]}")
            current_btn.setStyleSheet("""
                background-color: #3498db !important;
                font-weight: bold;
            """)