#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2025/3/8 22:43
# @Author  : 刘双喜
# @File    : home_page.py
# @Description : 添加描述
from PyQt6.QtWidgets import QWidget, QVBoxLayout, QLabel


class HomePage(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        layout = QVBoxLayout()
        self.title = QLabel("Welcome to My Application")
        self.desc = QLabel("Select a section from the left navigation")

        layout.addWidget(self.title)
        layout.addWidget(self.desc)
        layout.addStretch()
        self.setLayout(layout)
