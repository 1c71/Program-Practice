
from PyQt4 import QtGui
import sys


app = QtGui.QApplication(sys.argv)


w = QtGui.QWidget()

w.resize(250, 150)
w.move(300, 300)

w.setWindowTitle('Simple')
w.show()


tuopan = QtGui.QSystemTrayIcon(w)
icon1 = QtGui.QIcon('tuopan.jpg')
tuopan.setIcon(icon1)
tuopan.show()
tuopan.showMessage("haha","content",icon=3)
#如果不show(), 便不会显示, 后面的showMessage也会失效.



def message():
    print ("弹出的信息被点击了")
    
tuopan.messageClicked.connect(message)
# 弹出的信息被点击就会调用messageClicked连接的函数



def a():
    print ("系统托盘图标被点击了")
    
tuopan.activated.connect(a)
# 在系统托盘区域的图标被点击就会触发activated连接的函数(此例中是a函数)


sys.exit(app.exec_())


