#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2025/3/8 22:45
# @Author  : 刘双喜
# @File    : database.py
# @Description : 添加描述
from pymongo import MongoClient
import os
from datetime import datetime


class Database:
    _instance = None

    def __new__(cls):
        if not cls._instance:
            cls._instance = super().__new__(cls)
            cls._client = MongoClient(os.getenv("MONGO_URI", "mongodb://localhost:27017/"))
            cls._db = cls._client["myapp"]
        return cls._instance

    @classmethod
    def get_test_info(cls):
        """获取测试用例信息"""
        return {
            'TestCaseId': 'Test01',
            'Result': 'Pass',
            'ExecutionTime': '2024-02-20 14:30:00'
        }

    def log_operation(self, event_type: str, metadata: dict = None):
        """增强版日志记录"""
        log_entry = {
            "timestamp": datetime.utcnow(),
            "event_type": event_type,
            "metadata": metadata or {},
            "source": "feature1"
        }
        print(log_entry)
        return
        return self._db.app_logs.insert_one(log_entry)


def get_db():
    return Database()._db
