from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton, QMenu, QStackedWidget, QLabel, QVBoxLayout, QWidget
from PyQt6.QtGui import QPainter, QTransform
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QAction

class RotatedButton(QPushButton):
    def __init__(self, text, parent=None):
        super().__init__(text, parent)
        self.angle = 45  # 设置旋转角度为45度

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.RenderHint.Antialiasing)
        painter.setTransform(QTransform().rotate(self.angle))  # 设置旋转变换
        painter.drawText(self.rect(), Qt.AlignmentFlag.AlignCenter, self.text())  # 绘制文本

app = QApplication([])

window = QMainWindow()

# 创建一个旋转的按钮
button = RotatedButton("Rotated Button", window)

# 移动按钮到窗口中的其他位置
button.move(100, 100)

window.show()

app.exec()
