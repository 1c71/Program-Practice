import sys
import platform
 
import PySide
 
from PySide.QtCore import QRect
from PySide.QtGui import QApplication, QMainWindow, QTextEdit, QPushButton,\
                         QMessageBox,  QIcon, QAction, QWidget, QGridLayout,\
                         QTextEdit, QMenuBar, QMenu, QStatusBar
 
__version__ = '0.0.0'
import qrc_combine
 
class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
#        self.setObjectName("MainWindow")
        self.resize(731, 475)
        centralwidget = QWidget(self)
#        centralwidget.setObjectName("centralwidget")
        gridLayout = QGridLayout(centralwidget)
#        gridLayout.setObjectName("gridLayout")
        # textEdit needs to be a class variable.
        self.textEdit = QTextEdit(centralwidget)
#        self.textEdit.setObjectName("textEdit")
        gridLayout.addWidget(self.textEdit, 0, 0, 1, 1)
        self.setCentralWidget(centralwidget)
        menubar = QMenuBar(self)
        menubar.setGeometry(QRect(0, 0, 731, 29))
#        menubar.setObjectName("menubar")
        menu_File = QMenu(menubar)
#        menu_File.setObjectName("menu_File")
        self.setMenuBar(menubar)
        statusbar = QStatusBar(self)
#        statusbar.setObjectName("statusbar")
        self.setStatusBar(statusbar)
        actionShow_GPL = QAction(self)
#        actionShow_GPL.setObjectName("actionShow_GPL")
        actionShow_GPL.triggered.connect(self.showGPL)
        action_About = QAction(self)
#        action_About.setObjectName("action_About")
        action_About.triggered.connect(self.about)        
        iconToolBar = self.addToolBar("iconBar.png")
#------------------------------------------------------
# Add icons to appear in tool bar - step 1
        actionShow_GPL.setIcon(QIcon(":/showgpl.png"))
        action_About.setIcon(QIcon(":/about.png"))
        action_Close = QAction(self)
        action_Close.setCheckable(False)
        action_Close.setObjectName("action_Close")        
        action_Close.setIcon(QIcon(":/quit.png"))
#------------------------------------------------------
# Show a tip on the Status Bar - step 2
        actionShow_GPL.setStatusTip("Show GPL Licence")
        action_About.setStatusTip("Pop up the About dialog.")
        action_Close.setStatusTip("Close the program.")
#------------------------------------------------------
        menu_File.addAction(actionShow_GPL)
        menu_File.addAction(action_About)
        menu_File.addAction(action_Close)
        menubar.addAction(menu_File.menuAction())
 
        iconToolBar.addAction(actionShow_GPL)
        iconToolBar.addAction(action_About)
        iconToolBar.addAction(action_Close)
        action_Close.triggered.connect(self.close)
             
    def showGPL(self):
        '''Read and display GPL licence.'''
        self.textEdit.setText(open('COPYING.txt').read())
       
    def about(self):
        '''Popup a box with about message.'''
        QMessageBox.about(self, "About PyQt, Platform and the like",
                """<b> About this program </b> v %s
               <p>Copyright � 2011 Your Name.
               All rights reserved in accordance with
               GPL v2 or later - NO WARRANTIES!
               <p>This application can be used for
               displaying OS and platform details.
               <p>Python %s - PySide version %s - Qt version %s on %s""" % \
                (__version__, platform.python_version(), PySide.__version__,\
                 PySide.QtCore.__version__, platform.system()))      
       
if __name__ == '__main__':
    app = QApplication(sys.argv)
    frame = MainWindow()
    frame.show()
    sys.exit(app.exec_())
