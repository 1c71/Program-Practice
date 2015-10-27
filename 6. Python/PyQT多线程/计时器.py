# -*- coding:utf-8-*-

from PyQt4.QtGui import *
from PyQt4.QtCore import *
from time import *
import sys

class Windows(QDialog):

    def __init__(self, parent=None):
        super(Windows, self).__init__(parent)
        
        self.startButton = QPushButton("Start")
        self.stopButton = QPushButton("Stop")
        self.stopButton.setEnabled(False)
        
        self.statusLable = QLabel("Please click \"start\"")
        self.statusLable.setFrameStyle(QFrame.StyledPanel|
                                         QFrame.Plain)

        topLayout = QHBoxLayout()
        topLayout.addWidget(self.startButton)
        topLayout.addWidget(self.stopButton)
        
        layout = QVBoxLayout()
        layout.addLayout(topLayout)
        layout.addWidget(self.statusLable)
        
        self.timer = Timer()
        
        self.connect(self.startButton, SIGNAL("clicked()")
                        , self.start)
        self.connect(self.stopButton, SIGNAL("clicked()")
                        , self.stop)
        self.connect(self.timer, SIGNAL("updateTime()")
                        , self.updateTime)
        
        self.setLayout(layout)
        self.setWindowTitle("Timer")
        self.setWindowFlags(Qt.WindowMinimizeButtonHint)
        
    def updateTime(self):
        self.statusLable.setText("Time: %s s" % QString.number(self.sec))
        self.sec += 1

    def start(self):
        self.sec = 0
        self.startButton.setEnabled(False)
        self.stopButton.setEnabled(True)
        self.timer.start()

    def stop(self):
        self.timer.stop()
        self.stopButton.setEnabled(False)
        self.startButton.setEnabled(True)
        self.statusLable.setText("Timer stoped.")


class Timer(QThread):
    
    def __init__(self, parent=None):
        super(Timer, self).__init__(parent)
        self.stoped = False
        self.mutex = QMutex()

    def run(self):
        with QMutexLocker(self.mutex):
            self.stoped = False
        while True:
            if self.stoped:
                return

            self.emit(SIGNAL("updateTime()"))
            sleep(1)
    
    def stop(self):
        with QMutexLocker(self.mutex):
            self.stoped = True
        
    def isStoped(self):    
        with QMutexLocker(sellf.mutex):
            return self.stoped



app = QApplication(sys.argv)
windows = Windows()
windows.show()
app.exec_()