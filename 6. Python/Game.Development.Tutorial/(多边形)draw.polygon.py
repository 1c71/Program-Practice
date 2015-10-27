'''
polygon可以用来画多边形

用法：pygame.draw.polygon(Surface, color, pointlist, width=0)

polygon就是多边形，用法类似rect，第一、第二、第四的参数都是相同的，
只不过polygon会接受一系列坐标的列表，代表了各个顶点。
最后一个顶点会自动连线到第一个顶点，形成一个形状，而不是形成一些线段

'''

import pygame, sys
from pygame.locals import *

pygame.init()

screen = pygame.display.set_mode((640,360), 0, 32)
pointlist=[(20,10),(200,100),(0,100)]

while True:
     
     for event in pygame.event.get():
          if event.type == QUIT:
               pygame.quit()
               sys.exit()    


     screen.lock()
     
     pygame.draw.polygon(screen, (120,120,244), pointlist, 3)

     screen.unlock()
     
     pygame.display.update()
                    
                    
                    
               
          























