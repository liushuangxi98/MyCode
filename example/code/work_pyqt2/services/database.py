#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2025/3/8 22:45
# @Author  : 刘双喜
# @File    : database.py
# @Description : 添加描述
from pymongo import MongoClient
import os


class Database:
    _instance = None

    def __new__(cls):
        if not cls._instance:
            cls._instance = super().__new__(cls)
            cls._client = MongoClient(os.getenv("MONGO_URI", "mongodb://localhost:27017/"))
            cls._db = cls._client["myapp"]
        return cls._instance


def get_db():
    return Database()._db