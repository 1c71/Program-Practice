#-*- encoding: gb18030 -*-
import sys, string, os
import pygame

#初始化
pygame.init()
# 设置窗口大小
window = pygame.display.set_mode((800, 600))
# 设置窗口标题
pygame.display.set_caption('Test Window')

# 事件循环
while True:    
    for event in pygame.event.get():
        if event.type == pygame.QUIT: #如果关闭窗口就退出
            sys.exit()
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE: # 如果按下Esc键也退出
            sys.exit()
