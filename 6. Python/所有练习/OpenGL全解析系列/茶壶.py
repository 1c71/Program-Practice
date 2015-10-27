
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *


 
def drawFunc():    # 这里是实际绘图的函数
    
    glClear(GL_COLOR_BUFFER_BIT)  
    # 把先前的画面给清除
    
    glRotatef(1, 0, 1, 0)
    # 我们以后会详细讲的函数，简单来说四个参数第一个是角度，后三个是一个向量，
    
    glutWireTeapot(0.5)
    # 是glut提供的绘制犹他茶壶的工具函数，  

    glFlush()

    # 它是处理OpenGL的渲染流水线，让所有排队中的命令得到执行。







 
glutInit()          #是用glut来初始化OpenGL的.


glutInitDisplayMode(GLUT_SINGLE | GLUT_RGBA)
# GLUT_RGBA和GLUT_RGB是其实是等价的
# 而GLUT_SINGLE意味着所有的绘图操作都直接在显示的窗口执行


glutInitWindowSize(400, 400)
# 设置出现的窗口的大小


glutCreateWindow("First")
# 一旦调用了，就出现一个窗口了，参数就是窗口的标题


glutDisplayFunc(drawFunc)
# 是glut非常讨人喜欢的一个功能，它注册了一个函数，用来绘制OpenGL窗口，
# 这个函数里就写着很多OpenGL的绘图操作等命令，也就是我们主要要学习的东西。


glutIdleFunc(drawFunc)
# 又是一个激动人心的函数，可以让OpenGL在闲暇之余，调用一下注册的函数，这是是产生动画的绝好方法。




glutMainLoop()
# 主循环，一旦调用了，我们的OpenGL就一直运行下去了。
















