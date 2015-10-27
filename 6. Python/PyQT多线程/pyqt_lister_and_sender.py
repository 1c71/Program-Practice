from PyQt4 import QtCore,QtGui
import time

class Listener(QtCore.QThread):
    def __init__(self):
        super(Listener,self).__init__()

    def run(self):
        print('listener: started')
        while True:
            time.sleep(2)

    def connect_slots(self, sender):
        self.connect(sender, QtCore.SIGNAL('testsignal'), self.say_hello)

    def say_hello(self):
        print('listener: received signal')

class Sender(QtCore.QThread):
    def __init__(self):
        super(Sender,self).__init__()

    def run(self):
        for i in range(5):
            print('sender: sending signal')
            self.emit(QtCore.SIGNAL('testsignal'))
            time.sleep(2)
        print('sender: finished')

if __name__ == '__main__':
    o_qapplication = QtGui.QApplication([])
    my_listener = Listener()
    my_sender = Sender()
    my_listener.connect_slots(my_sender)
    my_listener.start()
    my_sender.start()
    i_out = o_qapplication.exec_()