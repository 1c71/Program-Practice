# -*- coding: utf-8 -*-   
from PyQt4.QtGui import *  
from PyQt4.QtCore import *  
import sys  
  
QTextCodec.setCodecForTr(QTextCodec.codecForName("utf8"))  
  
class MyQQ(QToolBox):  
    def __init__(self,parent=None):  
        super(MyQQ,self).__init__(parent)  
          
        toolButton1_1=QToolButton()  
        toolButton1_1.setText(self.tr("朽木"))  
        toolButton1_1.setIcon(QIcon("qq-image/9.jpg"))  
        toolButton1_1.setIconSize(QSize(60,60))  
        toolButton1_1.setAutoRaise(True)  
        toolButton1_1.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)  
  
        toolButton1_2=QToolButton()  
        toolButton1_2.setText(self.tr("Cindy"))  
        toolButton1_2.setIcon(QIcon("qq-image/8.jpg"))  
        toolButton1_2.setIconSize(QSize(60,60))  
        toolButton1_2.setAutoRaise(True)  
        toolButton1_2.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)  
  
        toolButton1_3=QToolButton()  
        toolButton1_3.setText(self.tr("了了"))  
        toolButton1_3.setIcon(QIcon("qq-image/1.jpg"))  
        toolButton1_3.setIconSize(QSize(60,60))  
        toolButton1_3.setAutoRaise(True)  
        toolButton1_3.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)  
  
        toolButton1_4=QToolButton()  
        toolButton1_4.setText(self.tr("张三虎"))  
        toolButton1_4.setIcon(QIcon("qq-image/3.jpg"))  
        toolButton1_4.setIconSize(QSize(60,60))  
        toolButton1_4.setAutoRaise(True)  
        toolButton1_4.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)  
  
        toolButton1_5=QToolButton()  
        toolButton1_5.setText(self.tr("CSDN"))  
        toolButton1_5.setIcon(QIcon("qq-image/4.jpg"))  
        toolButton1_5.setIconSize(QSize(60,60))  
        toolButton1_5.setAutoRaise(True)  
        toolButton1_5.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)  
  
        toolButton2_1=QToolButton()  
        toolButton2_1.setText(self.tr("天的另一边"))  
        toolButton2_1.setIcon(QIcon("qq-image/5.jpg"))  
        toolButton2_1.setIconSize(QSize(60,60))  
        toolButton2_1.setAutoRaise(True)  
        toolButton2_1.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)  
  
        toolButton2_2=QToolButton()  
        toolButton2_2.setText(self.tr("蓝绿不分"))  
        toolButton2_2.setIcon(QIcon("qq-image/6.jpg"))  
        toolButton2_2.setIconSize(QSize(60,60))  
        toolButton2_2.setAutoRaise(True)  
        toolButton2_2.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)  
  
        toolButton3_1=QToolButton()  
        toolButton3_1.setText(self.tr("老牛"))  
        toolButton3_1.setIcon(QIcon("qq-image/7.jpg"))  
        toolButton3_1.setIconSize(QSize(60,60))  
        toolButton3_1.setAutoRaise(True)  
        toolButton3_1.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)  
  
        toolButton3_2=QToolButton()  
        toolButton3_2.setText(self.tr("张三疯"))  
        toolButton3_2.setIcon(QIcon("qq-image/8.jpg"))  
        toolButton3_2.setIconSize(QSize(60,60))  
        toolButton3_2.setAutoRaise(True)  
        toolButton3_2.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)  
  
        groupbox1=QGroupBox()  
        vlayout1=QVBoxLayout(groupbox1)  
        vlayout1.setMargin(10)  
        vlayout1.setAlignment(Qt.AlignCenter)  
        vlayout1.addWidget(toolButton1_1)  
        vlayout1.addWidget(toolButton1_2)  
        vlayout1.addWidget(toolButton1_3)  
        vlayout1.addWidget(toolButton1_4)  
        vlayout1.addWidget(toolButton1_5)  
        vlayout1.addStretch()  
  
        groupbox2=QGroupBox()  
        vlayout2=QVBoxLayout(groupbox2)  
        vlayout2.setMargin(10)  
        vlayout2.setAlignment(Qt.AlignCenter)  
        vlayout2.addWidget(toolButton2_1)  
        vlayout2.addWidget(toolButton2_2)  
           
        groupbox3=QGroupBox()  
        vlayout3=QVBoxLayout(groupbox3)  
        vlayout3.setMargin(10)  
        vlayout3.setAlignment(Qt.AlignCenter)  
        vlayout3.addWidget(toolButton3_1)  
        vlayout3.addWidget(toolButton3_2)  
  
        self.addItem(groupbox1,self.tr("我的好友"))  
        self.addItem(groupbox2,self.tr("同事"))  
        self.addItem(groupbox3,self.tr("黑名单"))  
  
app=QApplication(sys.argv)  
myqq=MyQQ()  
myqq.setWindowTitle("My QQ")  
myqq.show()  
app.exec_()




'''
MyQQ类继承自QToolBox，QToolBox提供了一种列状的层叠窗体，本实例通过QToolBox来实现一种抽屉效果，QToolButton提供了一种快速访问命令或选择项的按钮，通常在工具条中使用。

第75行创建了一个QGroupBox类实例，在本例中对应每一个抽屉。

第12行创建了一个QToolButton类实例，在这里QToolButton分别对应于抽屉中的每一个按钮。

第13-15行对按钮的文字，图标以及大小等进行设置。

第16行设置按钮的AutoRaise属性为True，即当鼠标离开时，按钮自动恢复成弹起状态。

第17行设置按钮的ToolButtonStyle属性，ToolButtonStyle属性主要用来描述按钮的文字和图标的显示方式。Qt定义了4种QToolButtonStyle类型，分别介绍如下。

Qt.ToolButtonIconOnly：只显示图标。

Qt.ToolButtonTextOnly：只显示文字。

Qt.ToolButtonTextBesideIcon：文字显示在图标旁边。

Qt.ToolButtonTextUnderIcon：文字显示在图标下面。

程序员可以根据显示需要调整显示方式。

第76行创建一个QVBoxLayout类实例，用来设置抽屉内各按钮的布局。

第77，78行设置布局中各按钮的显示间距和显示位置。

第79-83行将抽屉内的各个按钮加入。

第84行调用addStretch()方法在按钮之后插入一个占位符，使得所有按钮能靠上对齐。并且在整个抽屉大小发生改变时，保证按钮的大小不发生变化。

其它行都是实现类似的功能。

第100-102行把准备好的抽屉插入至QToolBox中。

'''







