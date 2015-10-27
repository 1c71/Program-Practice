background_image_filename = "a.jpg"
mouse_image_filename = "b.jpg"

import pygame
# 导入pygame库

from pygame.locals import *
# 导入一些常用的函数和常量

from sys import exit
# 向sys模块借一个exit函数用来退出程序

pygame.init()
# 初始化pygame, 为使用硬件做准备

screen = pygame.display.set_mode( (640, 480), 0, 32 )
# 创建了一个窗口, 第一个参数是分辨率, 第二个是标志位，如果不指定就用0，第三个参数是色深


pygame.display.set_caption("Hello, World!")
# 设置窗口标题


background = pygame.image.load(background_image_filename).convert()
mouse_cursor = pygame.image.load(mouse_image_filename).convert_alpha()
# 加载并转换图像
# convert函数是将图像数据都转化为Surface对象



while True:
# 游戏主循环
    for event in pygame.event.get():
         if event.type == QUIT:
              # 接收到退出事件后退出程序
              exit()
     
    screen.blit(background, (0,0))
    # 将背景图画上去

    x, y = pygame.mouse.get_pos()
    # 获得鼠标位置
    
    x -= mouse_cursor.get_width() / 2
    y -= mouse_cursor.get_height() / 2
    # 计算光标的左上角位置

    screen.blit(mouse_cursor, (x,y))
    # 把光标画上去
    # blit是个重要函数，第一个参数为一个Surface对象，第二个为左上角位置。
    # 画完以后一定记得用update更新一下，否则画面一片漆黑。

    pygame.display.update()
    # 刷新一下画面












































