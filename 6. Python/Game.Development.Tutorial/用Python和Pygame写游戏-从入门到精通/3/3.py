# 这是一个练习全屏与窗口之间切换的例子


background_image_filename = 'xielaoban.jpg'
 
import pygame
from pygame.locals import *
from sys import exit
 
pygame.init()

screen = pygame.display.set_mode((640, 480), 0, 32)
# 设置显示模式

background = pygame.image.load(background_image_filename).convert()
#载入图像并且转换

 
Fullscreen = False
 
while True:
 
    for event in pygame.event.get():
        if event.type == QUIT:
            exit()
    if event.type == KEYDOWN:
        if event.key == K_f: # 如果按下f键
            Fullscreen = not Fullscreen
            # 会把是否全屏的变量true和false之间转换
            
            if Fullscreen: # 判断全屏变量是否为真，为真则全屏
                screen = pygame.display.set_mode((640, 480), FULLSCREEN, 32)
            else:
                screen = pygame.display.set_mode((640, 480), 0, 32)
 
    screen.blit(background, (0,0))
    pygame.display.update()











