import os
from random import randint
from PyQt5 import QtCore
from PyQt5.QtWidgets import QMainWindow, QApplication,QMessageBox
import re
from os import listdir
from os.path import isfile, join
from controller.SniperFactory import Sniper_factory
from views.UI import Main_UI
from sys import exit

class Window(QMainWindow,Main_UI):

    def __init__(self):
        super().__init__()
        self.__initUi()
        # self.__initVal()
        self.sniper_factory = Sniper_factory()
        self.sniper_transparent = False
    
    def __initUi(self):
        self.addTabButton.clicked.connect(self.add_new_sniper)
        self.delTabButton.clicked.connect(self.delete_last_sniper)

    def keyPressEvent(self, event):
        if event.modifiers() & QtCore.Qt.ControlModifier and event.key() == QtCore.Qt.Key_R:
            print('Ctrl+R')
            QMessageBox.warning(self, "Warning", 'Ctrl+R')
            

    def add_new_sniper(self):
        sniper = self.sniper_factory.createSniper()
        if sniper == None:
            QMessageBox.warning(self, "Warning", "The maximum number of windows is 6")
            return
        sniper.show()              # 顯示新視窗
        x = sniper.pos().x()       # 取得新視窗目前 x 座標
        y = sniper.pos().y()       # 取得新視窗目前 y 座標
        new_x = randint(0, 300)
        new_y = randint(0, 300)
        sniper.move(x+new_x, y+new_y)  # 移動新視窗位置

    def delete_last_sniper(self):
        self.sniper_factory.deleteSniper()