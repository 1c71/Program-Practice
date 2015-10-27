import sys
from PyQt4.QtCore import * 
from PyQt4.QtGui import * 

LIST_DATA = ['a', 'aardvark', 'aardvarks', 'aardwolf', 'aardwolves',
             'abacus', 'babel', 'bach', 'cache', 
             'daggle', 'facet', 'kabob', 'kansas']

#################################################################### 
def main(): 
    app = QApplication(sys.argv) 
    w = MyWindow() 
    w.show() 
    sys.exit(app.exec_()) 

#################################################################### 
class MyWindow(QWidget): 
    def __init__(self, *args): 
        QWidget.__init__(self, *args) 

        # create objects
        self.la = QLabel("Start typing to match items in list:")
        self.le = MyLineEdit()
        self.lm = MyListModel(LIST_DATA, self)
        self.lv = QListView()
        self.lv.setModel(self.lm)

        # layout
        layout = QVBoxLayout()
        layout.addWidget(self.la)
        layout.addWidget(self.le)
        layout.addWidget(self.lv) 
        self.setLayout(layout)

        # connections
        self.connect(self.le, SIGNAL("textChanged(QString)"),
                     self.text_changed)
        self.connect(self.le, SIGNAL("tabPressed"),
                     self.tab_pressed)

    def text_changed(self):
        """ updates the list of possible completions each time a key is 
            pressed """
        pattern = str(self.le.text())
        self.new_list = [item for item in LIST_DATA if item.find(pattern) == 0]
        self.lm.setAllData(self.new_list)

    def tab_pressed(self):
        """ completes the word to the longest matching string 
            when the tab key is pressed """

        # only one item in the completion list
        if len(self.new_list) == 1:
            newtext = self.new_list[0] + " "
            self.le.setText(newtext)

        # more than one remaining matches
        elif len(self.new_list) > 1:
            match = self.new_list.pop(0)
            for word in self.new_list:
                match = string_intersect(word, match)
            self.le.setText(match)

####################################################################
class MyLineEdit(QLineEdit):
    def __init__(self, *args):
        QLineEdit.__init__(self, *args)
        
    def event(self, event):
        if (event.type()==QEvent.KeyPress) and (event.key()==Qt.Key_Tab):
            self.emit(SIGNAL("tabPressed"))
            return True
        return QLineEdit.event(self, event)

#################################################################### 
class MyListModel(QAbstractListModel): 
    def __init__(self, datain, parent=None, *args): 
        """ datain: a list where each item is a row
        """
        QAbstractTableModel.__init__(self, parent, *args) 
        self.listdata = datain
 
    def rowCount(self, parent=QModelIndex()): 
        return len(self.listdata) 
 
    def data(self, index, role): 
        if index.isValid() and role == Qt.DisplayRole:
            return QVariant(self.listdata[index.row()])
        else: 
            return QVariant()

    def setAllData(self, newdata):
        """ replace all data with new data """
        self.listdata = newdata
        self.reset()

####################################################################
def string_intersect(str1, str2):
    newlist = []
    for i,j in zip(str1, str2):
        if i == j:
            newlist.append(i)
        else:
            break
    return ''.join(newlist)

####################################################################
if __name__ == "__main__": 
    main()
