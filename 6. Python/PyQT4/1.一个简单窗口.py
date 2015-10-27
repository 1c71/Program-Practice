import sys
from PyQt4 import QtGui
# 基本的GUI组件在QtGui模块里
# 这句话的意思是: 从 PyQt4 模块里导入 QtGui 模块


def main():
   
    app = QtGui.QApplication(sys.argv)

    # 每个PyQT4程序都必须创建这个对象. 这个对象位于QtGui模块里
    # sys.argv参数可以接收到从命令行传送过来的参数.
    # python脚本可以从命令行执行.
   

    w = QtGui.QWidget()
    # QtGui.QWidget控件是PtQt4里, 所有用户界面对象的基础类.
    # 默认构造函数没有父. 一个控件没有父, 就被称为窗口


    w.resize(250, 150)
     # 这个 resize()方法调整控件大小. 这一行调整为250像素宽 和 150像素高

    w.move(300, 300)
    # 这个move()方法把控件设置到屏幕上x=300,y=300的位置


    w.setWindowTitle('Simple')
    # 设置窗口的title


    w.show()
     # 这个show()方法把控件显示到屏幕上. 一个控件需要先在内存中被创建, 然后显示到屏幕上.
   
    sys.exit(app.exec_())

'''
最后，我们需要进入应用程序的主循环. 事件处理从这一点开始.
主循环接收从窗口系统的事件，并将它们分派到应用程序小部件。
主循环结束. 如果我们调用exit()方法, 或main控件被销毁. 
sys.exit（）方法，确保干净地退出。运行环境会被告知，如何结束应用程序
exec_()方法有一个下划线。这是因为exec是一个Python关键字。因此用exec_() 代替。
'''


if __name__ == '__main__':
    main()
