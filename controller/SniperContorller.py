import os
from random import randint
from PyQt5.QtWidgets import QMainWindow, QApplication,QMessageBox
import re
from os import listdir
from os.path import isfile, join
from sys import exit

from views.components.SniperUI import Sniper_UI

class Sniper_Window(QMainWindow,Sniper_UI):

    def __init__(self,new_sniper_key):
        super().__init__()
        print('Sniper_Window',new_sniper_key)
        self.new_sniper_key = new_sniper_key
    
    def mousePressEvent(self, event):
        self.offset = event.pos()

    def mouseMoveEvent(self, event):
        x = event.globalX()
        y = event.globalY()
        x_w = self.offset.x()
        y_w = self.offset.y()
        self.move(x - x_w, y - y_w)