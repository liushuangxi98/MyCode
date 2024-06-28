from PyQt6.QtWidgets import QWidget, QHBoxLayout, QFrame, QApplication, QGraphicsDropShadowEffect
import sys


class Example(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.setGeometry(0, 0, 1000, 500)
        self.setWindowTitle('Window with a dividing line')

        layout = QHBoxLayout()
        self.setLayout(layout)

        widget1 = QWidget(self)
        widget1.setStyleSheet("background-color: white;")
        widget1.setFixedWidth(200)
        layout.addWidget(widget1)

        line = QFrame(self)
        line.setFrameShape(QFrame.Shape.VLine)
        line.setFrameShadow(QFrame.Shadow.Sunken)
        line.setFixedHeight(500)
        shadow = QGraphicsDropShadowEffect(blurRadius=10, xOffset=5, yOffset=5)
        line.setGraphicsEffect(shadow)
        layout.addWidget(line)

        widget2 = QWidget(self)
        layout.addWidget(widget2)

        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec())
