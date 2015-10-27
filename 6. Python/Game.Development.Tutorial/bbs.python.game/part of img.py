man = "right.bmp"
bg = "bg.jpg"

import pygame,time
# 导入pygame库

from pygame.locals import *
# 导入一些常用的函数和常量

from sys import exit
# 向sys模块借一个exit函数用来退出程序


pygame.init()
# 初始化pygame, 为使用硬件做准备

screen = pygame.display.set_mode( (640, 480), 0, 32 )
# 创建了一个窗口, 第一个参数是分辨率, 第二个是标志位，如果不指定就用0，第三个参数是色深

pygame.display.set_caption("Game")
# 设置窗口标题


man = pygame.image.load(man).convert_alpha()
back = pygame.image.load(bg).convert_alpha()
# 加载并转换图像
# convert函数是将图像数据都转化为Surface对象

fpsClock = pygame.time.Clock()

while True:  

    for event in pygame.event.get():
        if event.type == pygame.QUIT: #如果关闭窗口就退出
            pygame.quit()
            exit()

    screen.blit(back,(0,0))
    screen.blit(man,(0,0),(0,0,80,80))
    
    pygame.display.update()
    fpsClock.tick(30)








































