#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2025/3/9 21:10
# @Author  : 刘双喜
# @File    : feature1.py
# @Description : 添加描述
# features/feature1.py
# features/feature1.py
import time
from PyQt6.QtCore import QObject, pyqtSignal, QRunnable, QThreadPool


class Feature1Signals(QObject):
    finished = pyqtSignal()
    error = pyqtSignal(str)
    progress = pyqtSignal(int)  # 新增进度信号


class Feature1Worker(QRunnable):
    def __init__(self):
        super().__init__()
        self.signals = Feature1Signals()
        self._is_running = True  # 添加运行状态标识

    def run(self):
        try:
            for i in range(5):
                if not self._is_running:
                    return
                self.signals.progress.emit((i+1)*20)
                time.sleep(1)
            print("功能1已执行")
            self.signals.finished.emit()
        except Exception as e:
            self.signals.error.emit(str(e))

    def cancel(self):
        """取消任务"""
        self._is_running = False


class Feature1Controller(QObject):
    def __init__(self):
        super().__init__()
        self.threadpool = QThreadPool()
        self.active_worker = None  # 改为更明确的属性名
        self.signals = Feature1Signals()  # 添加控制器级信号

    def execute(self):
        """启动新的工作线程"""
        if self.active_worker:
            return  # 防止重复执行

        self.active_worker = Feature1Worker()
        self.active_worker.signals.progress.connect(self.signals.progress)
        self.active_worker.signals.finished.connect(self._on_worker_finished)
        self.active_worker.signals.error.connect(self._on_worker_error)
        self.threadpool.start(self.active_worker)

    def _on_worker_finished(self):
        """工作线程完成回调"""
        print("功能1执行成功")
        self.signals.finished.emit()
        self.active_worker = None  # 重置引用

    def _on_worker_error(self, msg):
        """工作线程错误回调"""
        print(f"执行出错: {msg}")
        self.signals.error.emit(msg)
        self.active_worker = None