# 背景图片
# background image file
bif = "bg.jpg"

# 鼠标图片
# mouse image file
mif = "ball.png"

import pygame, sys
from pygame.locals import *


pygame.init()
screen = pygame.display.set_mode((640,360), 0, 32)
#32意思是多少位颜色


background = pygame.image.load(bif).convert()
#需要转换了才能用,所以convert()

mouse_c = pygame.image.load(mif).convert_alpha()
 

while True:
     for event in pygame.event.get():
          if event.type == QUIT:
               pygame.quit()
               sys.exit()


     # 让background显示到屏幕上
     screen.blit(background, (0,0))

     # 获得鼠标位置
     x,y = pygame.mouse.get_pos()

     # 让图像的中间一直跟随鼠标
     # 计算图像显示的位置
     x -= mouse_c.get_width()  
     y -= mouse_c.get_height()  

     # 把mouse_c显示到屏幕上
     screen.blit(mouse_c, (x,y))

     pygame.display.update()


























