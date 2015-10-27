import sys
import platform
 
import PySide
from PySide.QtGui import QApplication, QMainWindow, QTextEdit,\
                         QPushButton,  QMessageBox, QIcon
 
__version__ = '0.0.2'
from ui_combine import Ui_MainWindow
# 从这个界面文件中导入这个类

import qrc_combine

 
class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.setupUi(self)
        
        self.actionShow_GPL.triggered.connect(self.showGPL)
        self.action_About.triggered.connect(self.about)
        #这2个都是QtGui.QAction的实例
        iconToolBar = self.addToolBar("iconBar.png")
#------------------------------------------------------
# Add icons to appear in tool bar - step 1
        self.actionShow_GPL.setIcon(QIcon(":/showgpl.png"))
        self.action_About.setIcon(QIcon(":/about.png"))
        self.action_Close.setIcon(QIcon(":/quit.png"))
#------------------------------------------------------
# Show a tip on the Status Bar - step 2
        self.actionShow_GPL.setStatusTip("Show GPL Licence")
        self.action_About.setStatusTip("Pop up the About dialog.")
        self.action_Close.setStatusTip("Close the program.")
#------------------------------------------------------        
        iconToolBar.addAction(self.actionShow_GPL)
        iconToolBar.addAction(self.action_About)
        iconToolBar.addAction(self.action_Close)




        
               
    def showGPL(self):
        '''Read and display GPL licence.'''
        self.textEdit.setText(open('COPYING.txt').read())
        # 有这个控件,在界面文件中
       
    def about(self):
        '''Popup a box with about message.'''
        QMessageBox.about(self, "About PyQt, Platform and the like",
                """<b> About this program </b> v %s
               <p>Copyright � 2010 Joe Bloggs.
               All rights reserved in accordance with
               GPL v2 or later - NO WARRANTIES!
               <p>This application can be used for
               displaying OS and platform details.
               <p>Python %s -  PySide version %s - Qt version %s on %s""" % \
                (__version__, platform.python_version(), PySide.__version__,\
                 PySide.QtCore.__version__, platform.system()))      
       
if __name__ == '__main__':
    app = QApplication(sys.argv)
    frame = MainWindow()
    frame.show()
    app.exec_()























