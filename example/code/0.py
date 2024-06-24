from PyQt6.QtWidgets import QApplication, QMainWindow, QLabel
from PyQt6.QtGui import QPixmap
from PyQt6.QtCore import Qt

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle('测试窗口')
        self.setGeometry(0, 0, 1500, 1500)

        # 创建一个QLabel对象，加载并显示图片
        label = QLabel(self)
        pixmap = QPixmap(r'E:\\file\\python\\MyCode\\example\\code\\61.data\\2.png')
        label.setPixmap(pixmap.scaled(self.size(), Qt.AspectRatioMode.KeepAspectRatio))

        self.setCentralWidget(label)

if __name__ == '__main__':
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec()
