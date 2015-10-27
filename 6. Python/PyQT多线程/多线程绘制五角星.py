import math, random, sys
from PyQt4.QtCore import *
from PyQt4.QtGui import *





#主窗口从QWidget继承。同时创建一个Worker线程用于完成相关操作。
class Window(QWidget):

    def __init__(self, parent = None):
        QWidget.__init__(self, parent)
        self.thread = Worker()



# 主窗口包含一个label，一个spin box（用于设置要绘制的五角星数目），一个按钮，
# 线程输出的 图象在另一个QLabel（viewer）中显示。
        label = QLabel(self.tr("Number of stars:"))
        self.spinBox = QSpinBox()
        self.spinBox.setMaximum(10000)
        self.spinBox.setValue(1000)
        self.startButton = QPushButton(self.tr("&Start"))
        self.viewer = QLabel()
        self.viewer.setFixedSize(300, 300)



# 线程的finished()和terminated()信号被连接到self.updateUi，用于更新界面。
# output(QRect, QImage) 信号连接到addImage()，用于绘制单个的五角星。
        self.connect(self.thread, SIGNAL("finished()"), self.updateUi)
        self.connect(self.thread, SIGNAL("terminated()"), self.updateUi)
        self.connect(self.thread, SIGNAL("output(QRect, QImage)"), self.addImage)
        self.connect(self.startButton, SIGNAL("clicked()"), self.makePicture)

# 按钮的clicked()信号连接到makePicture()，用于启动work线程。
# 每个部件元素通过grid布局管理器 来管理。然后设置窗口标题。
        layout = QGridLayout()
        layout.addWidget(label, 0, 0)
        layout.addWidget(self.spinBox, 0, 1)
        layout.addWidget(self.startButton, 0, 2)
        layout.addWidget(self.viewer, 1, 0, 1, 3)
        self.setLayout(layout)
        
        self.setWindowTitle(self.tr("Simple Threading Example"))


# makePicture()主要完成个操作：1. 禁止修改界面；2. 重新生成一个新的pixmap；3. 开始工作 线程的绘制操作。
    def makePicture(self):
    
        self.spinBox.setReadOnly(True)
        self.startButton.setEnabled(False)

        pixmap = QPixmap(self.viewer.size())
        pixmap.fill(Qt.black)
        self.viewer.setPixmap(pixmap)

        self.thread.render(self.viewer.size(), self.spinBox.value())



# 我们用viewer的大小和五角星的数目作为参数传递给work线程的render函数进行绘制操作。 
# 其中五角星的数目从滑块获取（spinBox.value()）。

# 当work完成一个五角星的绘制时，会发射一个信号，调用addImage()槽。
# addImage()槽根据五角星的 所在位置和对应的pixmap在view中显示。然后更新窗口。
    def addImage(self, rect, image):
    
        pixmap = self.viewer.pixmap()
        painter = QPainter()

        painter.begin(pixmap)
        painter.drawImage(rect, image)
        painter.end()

        self.viewer.update(rect)
    




# 我们通过QPainter完成绘制操作。
# updateUi()槽在work线程完成全部操作的时候被触发。同时恢复窗口按钮和滑块的状态。
    def updateUi(self):
        self.spinBox.setReadOnly(False)
        self.startButton.setEnabled(True)





# Worker线程
# 为了能在线程中更好的使用Qt的信号槽特性，我们使用PyQt中的线程来代替Python本身的线程机制。
class Worker(QThread):

    def __init__(self, parent = None):
    
        QThread.__init__(self, parent)
        self.exiting = False
        self.size = QSize(0, 0)
        self.stars = 0


# 在work线程中保存一些基本的绘制信息，并对它们进行初始化。其中exiting用于记录线程的 工作状态。
# 每个五角星都通过QPainterPath绘制：
        self.path = QPainterPath()
        angle = 2*math.pi/5
        self.outerRadius = 20
        self.innerRadius = 8
        self.path.moveTo(self.outerRadius, 0)
        for step in range(1, 6):
            self.path.lineTo(
                self.innerRadius * math.cos((step - 0.5) * angle),
                self.innerRadius * math.sin((step - 0.5) * angle)
                )
            self.path.lineTo(
                self.outerRadius * math.cos(step * angle),
                self.outerRadius * math.sin(step * angle)
                )
        self.path.closeSubpath()



# 当work线程对象在被销毁的时候，需要停止线程。在__del__函数中调用线程的wait()等待 线程的退出。
    def __del__(self):
    
        self.exiting = True
        self.wait()



# 在渲染五角星之前，我们先记录相关的绘制信息，然后开启线程。
    def render(self, size, stars):
    
        self.size = size
        self.stars = stars
        self.start()





# start()方式用来启动线程，并且运行线程类中的run()方法。在这里我们重新实现了run()方法。 
# 我们通过render()函数来代替直接调用run()，这样我们就可以通过render给线程传递相关信息。 
# run()方法定义如下：
    def run(self):
        
        # Note: This is never called directly. It is called by Qt once the
        # thread environment has been set up.
        
        random.seed()
        n = self.stars
        width = self.size.width()
        height = self.size.height()


# 前面已经保存的属性信息对应要绘制五角星的数目和对应的绘制区域。
# 在绘制每个五角星的时候，我们检测self.exiting的状态，这样可以确保在任何时刻都可以退出 线程。
        while not self.exiting and n > 0:
        
            image = QImage(self.outerRadius * 2, self.outerRadius * 2,
                           QImage.Format_ARGB32)
            image.fill(qRgba(0, 0, 0, 0))
            
            x = random.randrange(0, width)
            y = random.randrange(0, height)
            angle = random.randrange(0, 360)
            red = random.randrange(0, 256)
            green = random.randrange(0, 256)
            blue = random.randrange(0, 256)
            alpha = random.randrange(0, 256)
            
            painter = QPainter()
            painter.begin(image)
            painter.setRenderHint(QPainter.Antialiasing)
            painter.setPen(Qt.NoPen)
            painter.setBrush(QColor(red, green, blue, alpha))
            painter.translate(self.outerRadius, self.outerRadius)
            painter.rotate(angle)
            painter.drawPath(self.path)
            painter.end()


# 具体的绘制代码和多线程关系并不大，我们只是在区域内随机地点绘制不同的五角星。

# 当每个五角星被绘制完成时刻，我们通过发射"output(QRect, QImage)"信号来通知GUI线程 来执行相关的操作。

            self.emit(SIGNAL("output(QRect, QImage)"),
                      QRect(x - self.outerRadius, y - self.outerRadius,
                            self.outerRadius * 2, self.outerRadius * 2), image)
            n -= 1
# 用这种方式可以在不同线程之间传递QRect和QImage对象。






if __name__ == "__main__":

    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec_())





#maximumSize
#minimunSize








