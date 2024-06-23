from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel
from PyQt6.QtCore import QTimer, QTime, Qt
from PyQt6.QtGui import QPainter, QColor, QPen
import sys
import math

class ClockWidget(QWidget):
    def __init__(self, labels):
        super().__init__()
        self.labels = labels  # 将标签列表保存为类的属性
        self.timer = QTimer()  # 创建一个定时器
        self.timer.timeout.connect(self.update)  # 当定时器超时时，更新窗口
        self.timer.start(500)  # 每秒触发一次定时器
        self.rhythm_flag = True

    def paintEvent(self, event):
        painter = QPainter(self)  # 创建一个画笔
        painter.setRenderHint(QPainter.RenderHint.Antialiasing)  # 设置抗锯齿
        painter.translate(self.width() / 2, self.height() / 2)  # 将坐标系的原点移动到窗口的中心

        self.draw_clock_progress(painter, 1)  # 绘制时钟的表面

    def draw_clock_progress(self, painter, idx):
        painter.save()  # 保存当前的画笔状态
        painter.translate(0, 100)  # 将坐标原点移动到(x, y)
        # painter.rotate(self.point_to_angle(0, 100))  # 旋转坐标系统90度
        painter.rotate(180)  # 旋转坐标系统90度
        painter.drawText(0, 0, '123')  # 在新的坐标系统中的原点处绘制文本
        painter.restore()  # 恢复到旋转前的画笔状态

    def point_to_angle(self, x, y):
        y = -y
        # 计算弧度
        radian = math.atan2(y, x)
        # 将弧度转换为度数
        degree = math.degrees(radian)
        return degree

app = QApplication(sys.argv)

labels = ['day1', 'day2', 'day3', 'night1', 'night2']  # 创建一个标签列表
clock = ClockWidget(labels)  # 创建一个ClockWidget实例
clock.show()  # 显示窗口

sys.exit(app.exec())  # 运行应用程序
