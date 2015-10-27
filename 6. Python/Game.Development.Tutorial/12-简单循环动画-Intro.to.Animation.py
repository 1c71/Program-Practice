bif = "bg.jpg"
mif = "ball.png"

import pygame, sys
from pygame.locals import *

pygame.init()

# 设置窗口大小,读取图片并转换
screen = pygame.display.set_mode((640,360), 0, 32)
background = pygame.image.load(bif).convert()
ball = pygame.image.load(mif).convert_alpha()


x=0


while True:
     for event in pygame.event.get():
          if event.type == QUIT:
               pygame.quit() 
               sys.exit()

               

     screen.blit(background, (0,0))
     screen.blit(ball, (x,160))
     x+=1
     
     # 一直加下去会跑出屏幕，所以大于640就置0
     if x>=640:
          x=0


     pygame.display.update()
                    
                    
                    
               
          























