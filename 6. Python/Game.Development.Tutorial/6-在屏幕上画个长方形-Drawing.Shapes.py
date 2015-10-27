import pygame, sys
from pygame.locals import *

pygame.init()

screen = pygame.display.set_mode((640,360), 0, 32)
# 第二个是一个标志位，如果不用什么特性，就指定0；第三个为色深。
'''
标志位	            功能
FULLSCREEN	创建一个全屏窗口
DOUBLEBUF	创建一个“双缓冲”窗口，建议在HWSURFACE或者OPENGL时使用
HWSURFACE	创建一个硬件加速的窗口，必须和FULLSCREEN同时使用
OPENGL	        创建一个OPENGL渲染的窗口
RESIZABLE	创建一个可以改变大小的窗口
NOFRAME	        创建一个没有边框的窗口
'''

while True:
     
     for event in pygame.event.get():
          if event.type == QUIT:
               pygame.quit() # 让pygame退出
               sys.exit()    # 程序退出


     # 当锁定屏幕的时候, 屏幕上什么都不会发生, 直到解锁位置
     screen.lock()
     
     #第二个参数是颜色，第三个参数是画图形，里面第一个参数是top,left位置，第二个是宽高
     #draw.rect意思是画正方形
     pygame.draw.rect(screen, (140,240,200), Rect((100,100),(130,170)))

     screen.unlock()
     #解锁之后其他的东西才能继续
     
     pygame.display.update()
                    
                    
                    
               
          























