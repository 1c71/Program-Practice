import sys
from PyQt4 import QtGui

 # 这个类继承自QtGui.QWidget类
class Example(QtGui.QWidget):
    
    def __init__(self):
        super(Example, self).__init__()
             # 这个super()方法返回Example类的父对象. __init__()方法是python的构造函数
        # 其实整句话的意思就是获得父类,然后调用他的构造函数来初始化    
    
        self.initUI() # 调用本类里的 initUI() 函数
        
    def initUI(self):
        
        self.setGeometry(300, 300, 250, 150)
        self.setWindowTitle('Icon')
        self.setWindowIcon(QtGui.QIcon('icon.jpg'))    
        # 这3个方法都继承自 QtGui.QWidget 类

# setGeometry()函数只干两件事. 设置窗口的大小, 和窗口在屏幕上的位置. 前2个参数是x,y位置,后2个参数是窗口的宽和高.
# 事实上, 这是一个整合了resize()方法和move()方法的函数.
 
# setWindowTitle()方法设置窗口的title

# setWindowIcon()方法设置应用程序图标。要做到这一点，我们需要创建了一个QtGui.QIcon对象。
# Qtgui.Qicon接收我们要显示的ICON的路径

    
        self.show()


        
def main():
    
    app = QtGui.QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()    

