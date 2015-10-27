from PyQt4 import QtCore, QtGui
 
#QCheckBoxExtended
#Subclassed QCheckBox and added a method that unchecks it IF the value is true
class QCheckBoxExtended(QtGui.QCheckBox):
    def __init__(self, parent=None):
        super(QCheckBoxExtended, self).__init__(parent)
 
    def setUnchecked(self, value):
        if value is True:
            self.setChecked(False)
 
         
#QCheckBoxGroup
#Subclassed QGroupBox and added a method that handles the connections so that one checkbox unchecks the other!
class QCheckBoxGroup(QtGui.QGroupBox):
    def __init__(self, parent=None):
        super(QCheckBoxGroup, self).__init__(parent)
        self.layout = QtGui.QVBoxLayout(self)
        self.checkBoxList = []
     
    def addCheckBox(self, checkBox):
 
        for cb in self.checkBoxList:
            checkBox.connect(cb, QtCore.SIGNAL("toggled(bool)"), checkBox.setUnchecked)
            cb.connect(checkBox, QtCore.SIGNAL("toggled(bool)"), cb.setUnchecked)
         
        self.checkBoxList.append(checkBox)
        self.layout.addWidget(checkBox)
 
 
#We run a test application here
if __name__ == '__main__':
    import sys
 
    app = QtGui.QApplication(sys.argv)
    widget = QCheckBoxGroup()
    widget.addCheckBox(QCheckBoxExtended())
    widget.addCheckBox(QCheckBoxExtended())
    widget.addCheckBox(QCheckBoxExtended())    
    widget.show()
    sys.exit(app.exec_())
