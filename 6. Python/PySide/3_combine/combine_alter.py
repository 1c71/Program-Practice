import sys
import platform
 
import PySide
from PySide.QtGui import QApplication, QMainWindow, QTextEdit, QPushButton,\
                         QMessageBox,  QIcon

__version__ = '0.0.0'
from ui_combine import Ui_MainWindow as Ui
import qrc_combine

class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        ui = Ui()
        # Store ui as class variable self.ui
        self.ui = ui
        ui.setupUi(self)
        ui.actionShow_GPL.triggered.connect(self.showGPL)
        ui.action_About.triggered.connect(self.about)        
        iconToolBar = self.addToolBar("iconBar.png") 
#------------------------------------------------------
# Add icons to appear in tool bar - step 1
        ui.actionShow_GPL.setIcon(QIcon(":/showgpl.png"))
        ui.action_About.setIcon(QIcon(":/about.png"))
        ui.action_Close.setIcon(QIcon(":/quit.png"))
#------------------------------------------------------
# Show a tip on the Status Bar - step 2
        ui.actionShow_GPL.setStatusTip("Show GPL Licence")
        ui.action_About.setStatusTip("Pop up the About dialog.")
        ui.action_Close.setStatusTip("Close the program.")
#------------------------------------------------------        
        iconToolBar.addAction(ui.actionShow_GPL)
        iconToolBar.addAction(ui.action_About)
        iconToolBar.addAction(ui.action_Close)
        
    def showGPL(self):
        '''Read and display GPL licence.'''
        self.ui.textEdit.setText(open('COPYING.txt').read())
        
    def about(self):
        '''Popup a box with about message.'''
        QMessageBox.about(self, "About PyQt, Platform and the like",
                """<b> About this program </b> v %s
                <p>Copyright &copy; 2010 Joe Bloggs. 
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
