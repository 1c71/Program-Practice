import sys

from PySide.QtGui import QApplication, QMainWindow, QTextEdit, QPushButton

from ui_licence import 
# 从 ui_licence.py 导入 Ui_MainWindow 这个类




class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        '''Mandatory initialisation of a class.'''
        super(MainWindow, self).__init__(parent)
        self.setupUi(self)
        # setupUi是ui_licence.py界面文件里的一个函数
        self.showButton.clicked.connect(self.fileRead)
        # 那个文件里也有一个按钮叫做showButton
        
    def fileRead(self):
        '''Read and display GPL licence.'''
        self.textEdit.setText(open('COPYING.txt').read())
        # 界面文件中有textEdit
        
if __name__ == '__main__':
    app = QApplication(sys.argv)
    frame = MainWindow()
    frame.show()
    app.exec_()
    
