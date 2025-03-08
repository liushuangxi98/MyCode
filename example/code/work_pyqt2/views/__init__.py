#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2025/3/8 22:43
# @Author  : 刘双喜
# @File    : __init__.py
# @Description : 添加描述
# views/__init__.py
from .home_page import HomePage
from .settings_page import SettingsPage
from .data_page import DataPage

__all__ = ["HomePage", "SettingsPage", "DataPage"]