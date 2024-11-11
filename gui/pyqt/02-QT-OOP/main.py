from PySide6.QtCore import Qt, QCoreApplication
from PySide6.QtWidgets import *


class Window(QWidget):
    def __init__(self):
        super().__init__()
        # self.btn_min =  QPushButton("btn_min")
        # self.btn_close = QPushButton("btn_close")
        self.initButton()
        # 最后执行
        self.initUi()


    def initUi(self):
        self.setWindowTitle("测试窗口")
        self.setGeometry(500, 300, 500, 300)
        # self.setWindowFlags(Qt.FramelessWindowHint)       # 去边框
        # self.setAttribute(Qt.WA_TranslucentBackground)    # 窗口透明



    def initButton(self):
        btn = QPushButton("button", self)  # 创建按钮，名称
        btn.move(100, 50)  # 移动按钮位置，默认左上角


if __name__ == '__main__':
    app = QApplication([])
    win = Window()
    win.show()
    app.exec()
