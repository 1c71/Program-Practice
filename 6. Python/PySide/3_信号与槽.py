import sys
from PySide.QtCore import *
from PySide.QtGui import *


class Form(QDialog):

    def __init__(self, parent=None):
        super(Form, self).__init__(parent)

        dia1 = QDial()
        dia1.setNotchesVisible(True)

        spinbox = QSpinBox()

        layout = QHBoxLayout()
        layout.addWidget(dia1)
        layout.addWidget(spinbox)
        self.setLayout(layout)

        self.connect(dia1, SIGNAL("valueChanged(int)"), spinbox.setValue)
        self.connect(spinbox, SIGNAL("valueChanged(int)"), dia1.setValue)

        self.setWindowTitle(u"信号和槽")
        
        
        
        

        
        
app = QApplication(sys.argv)

form = Form()
form.show()


app.exec_()


























































