import sys
from PyQt4 import QtGui


class Example(QtGui.QWidget):
    
    def __init__(self):
        super(Example, self).__init__()
        
        self.initUI()
        
    def initUI(self):
        
        QtGui.QToolTip.setFont(QtGui.QFont('SansSerif', 10))
        # 这个静态方法设置工具提示使用什么字体渲染。这里我们使用10px的SANSSERIF的字体。
        
        self.setToolTip('This is a <b>QWidget</b> widget')
           # 为了创建一个tooltip, 我们需要调用setToolTop方法. 我们可以使用富文本格式
        
        btn = QtGui.QPushButton('Button', self)
        btn.setToolTip('This is a <b>QPushButton</b> widget')
           #我们创建一个按钮, 并给他设置工具提示


        btn.resize(btn.sizeHint())
        btn.move(50, 50)   
        # 这个按钮被重设大小,并且移动到窗口的指定位置
        # sizeHint()方法，给出了一个建议的大小的按钮。
        
        self.setGeometry(300, 300, 250, 150)
        self.setWindowTitle('Tooltips')    
        self.show()
        
def main():
    
    app = QtGui.QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
