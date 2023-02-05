
from views.components.SniperUI import Sniper_Window

class Sniper_factory():

    factory_stack = []

    def __init__(self):
        print('Sniper_factory')

    def createSniper(self):
        new_sniper = Sniper_Window()
        self.factory_stack.append(new_sniper)
        return new_sniper

    def deleteSniper(self):
        if len(self.factory_stack) > 0:
            self.factory_stack.pop()
        else:
            print('No more trigger to delete')