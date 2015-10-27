mif = "right.bmp"

import pygame, sys
from pygame.locals import *

pygame.init()

# 设置窗口大小,读取图片并转换
screen = pygame.display.set_mode((640,360), 0, 32)
mouse_c = pygame.image.load(mif).convert_alpha()


x,y = 0,0
movex,movey = 0,0

while True:
     # 用户触发什么事件都会被一个个捕捉到event变量里
     for event in pygame.event.get():
          if event.type == QUIT:
               pygame.quit() # 让pygame退出
               sys.exit()    # 程序退出

          #当按下按键的时候
          if event.type == KEYDOWN:

               #首先判断按下的是什么按键
               if event.key == K_LEFT:
                    movex = -1
               elif event.key == K_RIGHT:
                    movex = +1
               elif event.key == K_UP:
                    movey = -1 #距离顶部的距离-1
               elif event.key == K_DOWN:
                    movey = +1

          if event.type == KEYUP:
               if event.key == K_LEFT:
                    movex = 0
               elif event.key == K_RIGHT:
                    movex = 0
               elif event.key == K_UP:
                    movey = 0
               elif event.key == K_DOWN:
                    movey = 0

     #计算图像最终显示的x坐标            
     x+=movex
     # y坐标
     y+=movey

     screen.blit(mouse_c, (x,y))

     pygame.display.update()
                    
                    
                    
               
          























