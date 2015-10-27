# coding=utf-8

import sys

from PySide.QtCore import *
from PySide.QtGui import *
from math import *


class Form(QDialog):

    def __init__(self, parent=None):
        super(Form, self).__init__(parent)

        self.browser = QTextBrowser()
        
        self.lineedit = QLineEdit()
        self.lineedit.setPlaceholderText(u"输入一个表达式并按下回车")
        self.lineedit.setTextMargins(5,5,5,5)
        # 左，上，右，下.LineEdit和里面文字的距离.
        

        layout = QVBoxLayout()
        layout.addWidget(self.browser)
        layout.addWidget(self.lineedit)
        self.setLayout(layout)


        self.lineedit.setFocus()

        self.lineedit.returnPressed.connect(self.updateUi)
        self.setWindowTitle(u"计算器")
        self.resize(400,400)


    def updateUi(self):
        try:
            text = unicode(self.lineedit.text())
            self.browser.append("%s = <b>%s</b>" % (text, eval(text)))
            
        except:
            self.browser.append(u"<font color=red>%s 是无效值</font>" % text)
            self.lineedit.selectAll()
        

    
app = QApplication(sys.argv)

form = Form()
form.show()

app.exec_()
    

    
        















































