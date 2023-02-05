from ctypes import windll
import os
from random import randint
from PyQt5.QtWidgets import QMainWindow, QLabel
from PyQt5 import QtCore
import re
from os import listdir
from os.path import isfile, join
from sys import exit
from views.components.SniperUI import Sniper_UI
class Sniper_Window(QMainWindow,Sniper_UI):

    def __init__(self, new_sniper_key_record):
        super().__init__()
        print('Sniper_Window',new_sniper_key_record)
        self.sniper_key_record = new_sniper_key_record
        self.new_sniper_key = self.sniper_key_record['key']
        self.new_sniper_key_text = self.sniper_key_record['text']
        self.setAttribute(QtCore.Qt.WA_TransparentForMouseEvents, True)
        self.__initUi()

    def __initUi(self):
        self.defaultKey = QLabel(self)
        self.defaultKey.setText(self.new_sniper_key_text)     # 設定標籤文字
        self.defaultKey.setGeometry(23, 0, 15, 7)           # 設定標籤位置與大小

    def mousePressEvent(self, event):
        self.offset = event.pos()

    def mouseMoveEvent(self, event):
        x = event.globalX()
        y = event.globalY()
        x_w = self.offset.x()
        y_w = self.offset.y()
        self.move(x - x_w, y - y_w)
    
    def setTransparentForMouseEvents(self, transparent):
        print('setTransparentForMouseEvents',transparent)
        self.setAttribute(QtCore.Qt.WA_TransparentForMouseEvents, transparent)
        self.update()
        
    def getWindowPosition(self):
        return self.pos().x()-5, self.pos().y()-5
    
   