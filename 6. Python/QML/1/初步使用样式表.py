

from  PyQt4 import QtCore
from  PyQt4 import QtGui
import sys
import sip



class MainWindow(QtGui.QMainWindow):

    def __init__(self, parent=None, uniqueHandle="TestWindow"):
        """
        """
        QtGui.QMainWindow.__init__(self, parent)
        self.setWindowTitle("New Test windows")
        self.setObjectName(uniqueHandle)
        self.resize(640,480)
        self.styleData = ""

        self.setWindow()


    def setWindow(self):

        central_widget = QtGui.QWidget()
        central_layout = QtGui.QGridLayout()

        central_widget.setLayout(central_layout)
        self.setCentralWidget(central_widget)

        btn = QtGui.QPushButton("coolio")
        btn.setStyleSheet("background-color: #f96")

        central_layout.addWidget(btn)





if __name__ == "__main__":

    app = QtGui.QApplication(sys.argv)
    app.setStyle("Plastique")
    
    mw = MainWindow()
    mw.show()
    
    sys.exit(app.exec_())

