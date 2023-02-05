from PyQt5.QtWidgets import QWidget
from PyQt5.QtWidgets import QTextBrowser,  QPushButton,  QDialogButtonBox, QFormLayout, QGroupBox, QLabel, QLineEdit, QVBoxLayout, QHBoxLayout, QWidget
from PyQt5 import QtCore
from PyQt5.QtGui import QIcon,QPalette, QBrush, QPixmap,QPainter
import os
import sys
class Sniper_Window(QWidget):

    def __init__(self, parent=None):
        super().__init__(parent)
        self.__initUi()
        self.setStyleSheet("background: transparent;border:0px")
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        # self.setAttribute(QtCore.Qt.WA_TransparentForMouseEvents, True)
        self.setWindowFlags(QtCore.Qt.WindowStaysOnTopHint | QtCore.Qt.FramelessWindowHint | QtCore.Qt.Tool)  #窗口置顶，无边框，在任务栏不显示图标

        # self.setWindowOpacity(0.1)
    def __initUi(self):
        if getattr(sys, 'frozen', None):
            basedir = f'{sys._MEIPASS}\\static'
        else:
            basedir = 'static'
        self.setWindowTitle('Trigger window')
        self.setWindowIcon(QIcon(os.path.join(basedir,'favicon.ico')))
        self.resize(40,40)
        # self.background = QPalette()
        # self.background.setBrush(QPalette.Background, QBrush(QPixmap(os.path.join(basedir,'trigger.png'))))
        # self.setPalette(self.background)
        
        self.label = QLabel(self)
        self.label.setFixedHeight(40)
        self.label.setFixedWidth(40)
        pix = QPixmap(os.path.join(basedir,'trigger.png'))       
        self.label.setPixmap(pix)
        self.label.setScaledContents(True)

        label = QLabel(self)
        label.setText('W')     # 設定標籤文字

    def mousePressEvent(self, event):
        self.offset = event.pos()

    def mouseMoveEvent(self, event):
        x = event.globalX()
        y = event.globalY()
        x_w = self.offset.x()
        y_w = self.offset.y()
        self.move(x - x_w, y - y_w)