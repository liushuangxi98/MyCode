#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2025/3/8 22:44
# @Author  : 刘双喜
# @File    : main_controller.py
# @Description : 添加描述
# controllers/main_controller.py
from datetime import datetime

from PyQt6.QtCore import QObject
from features.feature1 import Feature1Controller
from services.database import Database


class MainController(QObject):
    def __init__(self, window):
        super().__init__()
        self.window = window
        self.feature1_ctrl = Feature1Controller()
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

        # 设置页返回按钮
        self.window.pages["settings"].back_btn.clicked.connect(
            lambda: self.window.switch_page("home")
        )

        settings_page = self.window.pages["settings"]
        settings_page.do_btn.clicked.connect(self.execute_feature1)

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

    def execute_feature1(self):
        """执行功能1的完整流程"""
        settings_page = self.window.pages["settings"]

        # 更新UI状态
        settings_page.do_btn.setEnabled(False)
        settings_page.progress_bar.show()
        self.window.log_message("开始执行功能1...")

        # 连接控制器级信号
        self.feature1_ctrl.signals.finished.connect(
            lambda: self.on_feature1_complete(True)
        )
        self.feature1_ctrl.signals.error.connect(
            lambda msg: self.on_feature1_complete(False, msg)
        )
        # 进度条
        self.feature1_ctrl.signals.progress.connect(
            lambda p: self.window.log_message(f"当前进度: {p}%")
        )
        self.feature1_ctrl.signals.progress.connect(
            settings_page.progress_bar.setValue  # 直接绑定到进度条
        )

        # 开始执行（必须在信号连接之后）
        self.feature1_ctrl.execute()

    def on_feature1_complete(self, success, error_msg=None):
        """完成回调"""
        # 断开信号防止重复连接
        self.feature1_ctrl.signals.finished.disconnect()
        self.feature1_ctrl.signals.error.disconnect()
        self.feature1_ctrl.signals.progress.disconnect()

        settings_page = self.window.pages["settings"]
        settings_page.do_btn.setEnabled(True)
        settings_page.progress_bar.setValue(0)  # 重置进度条
        settings_page.progress_bar.hide()

        if success:
            print("操作成功完成")
            # 记录成功日志
            Database().log_operation(
                "feature1_success",
                {"status": "completed"}
            )
            self.window.log_message("功能1执行成功")
        else:
            print(f"操作失败: {error_msg}")
            # 记录错误日志
            Database().log_operation(
                "feature1_error",
                {"error": error_msg}
            )
            self.window.log_message(f"执行失败: {error_msg}")
