from PySide6.QtCore import Qt, QCoreApplication, QUrl, QRect
from PySide6.QtNetwork import QNetworkProxyFactory
from PySide6.QtWebEngineWidgets import QWebEngineView
from PySide6.QtWidgets import *


class Window(QWidget):
    def __init__(self):
        super().__init__()
        # self.btn_min =  QPushButton("btn_min")
        # self.btn_close = QPushButton("btn_close")


        self.loadWebPage(True, "http://dashboard.coulsonzero.top")
        # 最后执行
        self.initUi()


    def initUi(self):
        self.setWindowTitle("测试窗口")
        self.resize(1000, 800)
        # self.setWindowFlags(Qt.FramelessWindowHint)       # 去边框
        self.setAttribute(Qt.WA_TranslucentBackground)    # 窗口透明


    def loadWebPage(self, enable, url):
        self.frame = QFrame(self)
        self.frame.setObjectName("frame")
        self.frame.setGeometry(QRect(0, 0, 1200, 800))

        # 浏览器
        self.browser = QWebEngineView(self.frame)
        self.browser.setObjectName("browser")
        self.browser.setGeometry(10, 60, self.frame.width() - 20, self.frame.height() - 70)
        QNetworkProxyFactory.setUseSystemConfiguration(False)  # 取消代理，加快网页加载速度
        # 加载网页(主页/指定页面)

        if enable:
            self.browser.load(QUrl(url))
            self.browser.show()
            self.browser.urlChanged.connect(
                lambda: self.lineEdit_search.setText(self.browser.url().toDisplayString()))  # 获取当前网页网址，并显示到导航栏上


if __name__ == '__main__':
    app = QApplication([])
    win = Window()
    win.show()
    app.exec()
