#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2025/3/8 22:46
# @Author  : 刘双喜
# @File    : logger.py
# @Description : 添加描述
import logging
from services.database import get_db
from pymongo import MongoClient
from logging.handlers import TimedRotatingFileHandler


class MongoDBHandler(logging.Handler):
    def __init__(self):
        super().__init__()
        self.db = get_db()

    def emit(self, record):
        log_entry = self.format(record)
        self.db.logs.insert_one({
            "message": log_entry,
            "level": record.levelname,
            "timestamp": datetime.datetime.now()
        })


def setup_logging():
    logger = logging.getLogger()
    logger.setLevel(logging.INFO)

    # MongoDB 日志
    mongo_handler = MongoDBHandler()
    formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
    mongo_handler.setFormatter(formatter)
    logger.addHandler(mongo_handler)

    # 本地文件日志（可选）
    file_handler = TimedRotatingFileHandler(
        'app.log',
        when='midnight',
        backupCount=7
    )
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)