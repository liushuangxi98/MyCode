#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2025/3/8 22:58
# @Author  : 刘双喜
# @File    : main.py
# @Description : 添加描述
"""
myapp/
│
├── core/                  # 核心应用逻辑
│   ├── __init__.py
│   ├── app.py            # 应用初始化
│   └── window.py         # 主窗口管理
│
├── views/                # 所有界面组件
│   ├── __init__.py
│   ├── home_page.py      # 主页
│   └── settings_page.py  # 设置页
│
├── controllers/          # 业务逻辑控制
│   ├── __init__.py
│   └── main_controller.py
│
├── services/             # 数据服务层
│   ├── __init__.py
│   ├── database.py      # MongoDB连接
│   └── data_service.py  # 数据操作
│
├── utils/               # 工具类
│   ├── __init__.py
│   ├── logger.py        # 日志配置
│   └── styles.py        # 样式表
│
├── assets/              # 静态资源
│   └── styles.qss       # QSS样式表
│
└── main.py              # 应用入口
"""
import sys
from core.app import MyApp

if __name__ == "__main__":
    app = MyApp(sys.argv)
    sys.exit(app.exec())
