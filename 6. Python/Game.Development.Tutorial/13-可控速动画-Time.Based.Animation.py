bif = "bg.jpg"
mif = "ball.png"

import pygame, sys
from pygame.locals import *

pygame.init()


screen = pygame.display.set_mode((640,360), 0, 32)
background = pygame.image.load(bif).convert()
ball = pygame.image.load(mif).convert_alpha()


x=0
# 创建一个跟踪时间的对象
clock=pygame.time.Clock()
speed=50


while True:
     for event in pygame.event.get():
          if event.type == QUIT:
               pygame.quit() 
               sys.exit()

               

     screen.blit(background, (0,0))
     screen.blit(ball, (x,160))


     # 更新时钟,return milliseconds
     milli = clock.tick()   
     seconds = milli/1000.0
     dm=seconds*speed
     x+=dm
    

     
     # 一直加下去会跑出屏幕，所以大于640就置0
     if x>=640:
          x=0


     pygame.display.update()
                               
                    
'''

控制定时器事件
这个方法应该每一帧都调用一次。它会计算前一次调用至今过了多少毫秒。
如果你传一个可选的帧速参数，这个函数会保持游戏以不超过给定的速度运行。
这可以帮助限制游戏运行的速度。
通过每帧调用一次Clock.tick(40)，这个程序就永远不会以超过每秒40帧的速度运行。
注意这个函数使用SDL_Delay函数，它不是在每个平台上都很精确的，但是它不会耗很多CPU。
如果要使用更精确的定时器并不在乎占用CPU，可以使用tick_busy_loop。
 
'''
          























