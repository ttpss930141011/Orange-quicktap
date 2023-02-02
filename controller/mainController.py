import os
from PyQt5.QtWidgets import QMainWindow, QApplication,QMessageBox
import re
from os import listdir
from os.path import isfile, join
from lib.ftplib import FTP,error_perm
from views.UI import Main_Window
from sys import exit

class Window(QMainWindow,Main_Window):
    def __init__(self):
        super().__init__()
        # self.__initVal()
        
   

