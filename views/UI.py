from PyQt5.QtWidgets import QWidget
from PyQt5.QtWidgets import QTextBrowser,  QPushButton,  QDialogButtonBox, QFormLayout, QGroupBox, QLabel, QLineEdit, QVBoxLayout, QHBoxLayout, QWidget
from PyQt5 import QtCore
from PyQt5.QtGui import QIcon
import os
import sys
from controller.SniperFactory import Sniper_factory

from views.components.SniperUI import Sniper_Window
from random import randint
class Main_Window(QWidget):

    def __init__(self, parent=None):
        super().__init__(parent)
        self.__initUi()

    def __initUi(self):
        if getattr(sys, 'frozen', None):
            basedir = f'{sys._MEIPASS}\\static'
        else:
            basedir = 'static'
        self.setWindowTitle('Orange Quicktap')
        self.setWindowIcon(QIcon(os.path.join(basedir,'favicon.ico')))
        self.resize(300, 100)

        # 第一行按钮布局管理
        self.hLayout1 = QVBoxLayout()

        self.addTabButton = QPushButton("", self)
        self.addTabButton.setIcon(QIcon(os.path.join(basedir,'add.svg')))
        self.addTabButton.setIconSize(QtCore.QSize(25, 25))
        
        self.delTabButton = QPushButton("", self)
        self.delTabButton.setIcon(QIcon(os.path.join(basedir,'delete.svg')))
        self.delTabButton.setIconSize(QtCore.QSize(25, 25))

        self.formInLineLeft = QHBoxLayout()
        self.formInLineLeft.addWidget(self.addTabButton)
        self.formInLineLeft.addWidget(self.delTabButton)
        self.controlTabLabel = QLabel("More / Less :")
        
        self.formGroupBox = QGroupBox("Control panel")
        self.formInLine = QFormLayout()
        self.formInLine.addRow(self.controlTabLabel, self.formInLineLeft)
        self.formGroupBox.setLayout(self.formInLine)
        
        self.hLayout1.addWidget(self.formGroupBox)
        self.hLayout1.setSpacing(10)

        self.lay = QHBoxLayout()
        self.lay.setSpacing(20)
        self.lay.addLayout(self.hLayout1)
        self.mainWidget = QWidget()
        self.mainWidget.setLayout(self.lay)
        self.setCentralWidget(self.mainWidget)
