#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2025/3/8 22:46
# @Author  : 刘双喜
# @File    : styles.py
# @Description : 添加描述
def load_stylesheet():
    return """
    /* 主窗口样式 */
    QWidget {
        background-color: #ffffff;
        font-family: 'Segoe UI';
    }

    /* 侧边栏样式 */
    #sidebar {
        background-color: #2c3e50;
        border-right: 1px solid #34495e;
    }

    /* 导航按钮基础样式 */
    QPushButton#navButton {
        color: #ecf0f1;
        background-color: transparent;
        text-align: left;
        padding: 12px 20px;
        border-radius: 5px;
        font-size: 14px;
    }

    /* 按钮悬停效果 */
    QPushButton#navButton:hover {
        background-color: #34495e;
    }

    /* 按钮按下效果 */
    QPushButton#navButton:pressed {
        background-color: #2980b9;
    }

    /* 页面标题样式 */
    QLabel {
        font-size: 24px;
        color: #2c3e50;
        padding: 20px 0;
    }

    /* 表格样式 */
    QTableWidget {
        background-color: #f8f9fa;
        border: 1px solid #dee2e6;
        border-radius: 4px;
    }

    QHeaderView::section {
        background-color: #3498db;
        color: white;
        padding: 8px;
    }
    """