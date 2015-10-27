
import sys
from PySide.QtCore import *
from PySide.QtGui import *




class ZeroSpinBox(QSpinBox):

    zeros = 0

    def __init__(self, parent=None):
        super(ZeroSpinBox, self).__init__(parent)

        self.connect(self, SIGNAL("valueChanged(int)"), self.checkzero )



    def checkzero(self):
        if self.value() == 0:
            self.zeros += 1
            self.emit(SIGNAL("atzero(double)"), self.zeros)


        

class Form(QDialog):

    def __init__(self, parent=None):
        super(Form, self).__init__(parent)

        dia1 = QDial()
        dia1.setNotchesVisible(True)

        zerospinbox = ZeroSpinBox()

        layout = QHBoxLayout()
        layout.addWidget(dia1)
        layout.addWidget(zerospinbox)
        self.setLayout(layout)

        self.connect(dia1, SIGNAL("valueChanged(int)"), zerospinbox.setValue)
        self.connect(zerospinbox, SIGNAL("valueChanged(int)"), dia1.setValue)
        self.connect(zerospinbox, SIGNAL("atzero(double)"), self.announce )
        self.setWindowTitle(u"信号和槽")



    def announce(self, zeros):
        print "ZeroSpinBox has been at zero " + str(zeros) + " times. "
        
        
        
        

        
        
app = QApplication(sys.argv)

form = Form()
form.show()


app.exec_()        













