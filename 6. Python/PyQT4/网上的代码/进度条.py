import sys, time
from PyQt4 import QtCore, QtGui

def progress(data, *args):
    it=iter(data)
    widget = QtGui.QProgressDialog(*args+(0,it.__length_hint__()))
    c=0
    for v in it:
        QtCore.QCoreApplication.instance().processEvents()
        if widget.wasCanceled():
            raise StopIteration
        c+=1
        widget.setValue(c)
        yield(v)

if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)

    # Do something slow
    for x in progress(xrange(50),"Show Progress", "Stop the madness!"):
        time.sleep(.2)
