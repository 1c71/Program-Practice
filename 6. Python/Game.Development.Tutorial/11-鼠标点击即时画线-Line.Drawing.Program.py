import pygame, sys
from pygame.locals import *

pygame.init()
screen = pygame.display.set_mode((640,360), 0, 32)

color=(200,100,64)
points=[]

while True:
     
     for event in pygame.event.get():
          if event.type == QUIT:
               pygame.quit() 
               sys.exit()
          if event.type ==MOUSEBUTTONDOWN:
               points.append(event.pos)
          #每次点击鼠标按钮都会把xy位置添加到points里

     
     if len(points)>1:
          # 第三个参数False,如果改成True,每次点击画的线是2条，其中一条一定是从第一次点击延伸过来的
          # 视频没讲清楚到底代表什么意思
          pygame.draw.lines(screen, color, False, points, 5)

     
     pygame.display.update()
                    
                    
                    
               
          























