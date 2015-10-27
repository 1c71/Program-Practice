import sys
from PyQt4 import QtGui, QtCore
# 在这个例子中,我们会使用QtCore模块中的一个对象,所以要导入


class Example(QtGui.QWidget):
    
    def __init__(self):
        super(Example, self).__init__()
        
        self.initUI()
        
    def initUI(self):               
        

        qbtn = QtGui.QPushButton('Quit', self)

        # 我们创建了一个按钮. 这个按钮是Qtgui.QPushButton的一个实例. 第一个参数是按钮的标签。
        # 第二个参数是父控件的名字. 此例中是Example控件. 它继承自QtGui.QWidget


        qbtn.clicked.connect(QtCore.QCoreApplication.instance().quit)

# PyQt4 中事件处理系统内置信号和槽机制。如果我们按下按钮，将发送clicked信号. 槽可以是任何一个Qt槽或可调用的Python语句。
# QtCore.QCoreApplication 包含主事件循环。它处理和派遣所有事件。
# instance() 方法为我们提供了其当前实例。
# 注意，QtCore.QCoreApplication 是和 QtGui.QApplication一起创建的
# clicked信号和quit()方法互联. 该方法终止应用程序。
# 两个对象之间进行通信。发送器和接收器。发件器是按钮，接收器是应用程序对象。


        qbtn.resize(qbtn.sizeHint())
        qbtn.move(50, 50)       
        
        self.setGeometry(300, 300, 250, 150)
        self.setWindowTitle('Quit button')    
        self.show()
        
def main():
    
    app = QtGui.QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()


