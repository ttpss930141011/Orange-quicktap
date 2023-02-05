from PyQt5 import QtCore
from controller.SniperContorller import Sniper_Window
class Sniper_factory():

    factory_stack = []
    key_record_stack = [
        {'text':'Q','key':QtCore.Qt.Key_Q},
        {'text':'A','key':QtCore.Qt.Key_A},
        {'text':'Z','key':QtCore.Qt.Key_Z},
        {'text':'W','key':QtCore.Qt.Key_W},
        {'text':'S','key':QtCore.Qt.Key_S},
        {'text':'X','key':QtCore.Qt.Key_X}
    ]

    def __init__(self):
        print('Sniper_factory')

    def createSniper(self):
        if len(self.key_record_stack) == 0:
            print('No more trigger to create')
            return
        sniper_key_record = self.key_record_stack.pop()
        new_sniper = Sniper_Window(sniper_key_record)
        self.factory_stack.append(new_sniper)
        return new_sniper

    def deleteSniper(self):
        if len(self.factory_stack) > 0:
            deleted_sniper = self.factory_stack.pop()
            self.key_record_stack.append(deleted_sniper.sniper_key_record)
        else:
            print('No more trigger to delete')

    def allSniperSetTransparent(self,transparent):
        for sniper in self.factory_stack:
            sniper.setTransparentForMouseEvents(transparent)