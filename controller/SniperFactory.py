from controller.SniperContorller import Sniper_Window
class Sniper_factory():

    factory_stack = []
    key_record_stack = ['q','a','z','w','s','x']

    def __init__(self):
        print('Sniper_factory')

    def createSniper(self):
        if len(self.key_record_stack) == 0:
            print('No more trigger to create')
            return
        new_sniper_key = self.key_record_stack.pop()
        new_sniper = Sniper_Window(new_sniper_key)
        self.factory_stack.append(new_sniper)
        return new_sniper

    def deleteSniper(self):
        if len(self.factory_stack) > 0:
            deleted_sniper = self.factory_stack.pop()
            self.key_record_stack.append(deleted_sniper.new_sniper_key)
        else:
            print('No more trigger to delete')