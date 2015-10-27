man = "right.bmp"
bg = "bg.jpg"

import pygame,time
# 导入pygame库

from pygame.locals import *
# 导入一些常用的函数和常量

from sys import exit
# 向sys模块借一个exit函数用来退出程序




# 人物类
class People(pygame.sprite.Sprite):
    def __init__(self, imgpath):
        self.imagepath = imgpath
        self.x = 0
        self.y = 0
        self.count = 0
        # 读取图片
        self.image, self.imagerec = pygame.image.load(imgpath, "0xfc02fc")
        self.subimg = []
        self.step = 0

        # 把图片中的每一小块都读到一个独立的surface上

        direct = []
        for x in xrange(0,80,160,240,320,400,480,560):
                img = window((80, 80)).convert()    # return Surface
                img.blit(self.image, (0, 0), (x, y, 80, 80))
                direct.append(img)
        self.subimg.append(direct)


    def update(self, win, direct, pos):
        self.count = self.count + 1
        
        if direct >= 0 and self.count > 2:
            window.fill((0,0,0))
            win.blit(self.subimg[direct][self.step], pos)
            self.count = 0
            
            # 人物动作只有3个
            self.step = self.step + 1
            if self.step >= 3:
                self.step = 0




pygame.init()
# 初始化pygame, 为使用硬件做准备

window = pygame.display.set_mode( (640, 480), 0, 32 )
# 创建了一个窗口, 第一个参数是分辨率, 第二个是标志位，如果不指定就用0，第三个参数是色深


pygame.display.set_caption("Game")
# 设置窗口标题

pp = People(man)

#background = pygame.image.load(man).convert_alpha()
background = pygame.image.load(bg).convert_alpha()
# 加载并转换图像
# convert函数是将图像数据都转化为Surface对象


# 复制人物图像到主surface, 左上角位置在0, 100
window.blit(pp.subimg[0][0], (100, 100))

#for x1 in xrange(0, 96, 32):
#    for y1 in xrange(0, 192, 48):
#        window.blit(pp.subimg[y1/48][x1/32], (x1, y1))

x = 100
y = 100
clock = pygame.time.Clock()

pygame.key.set_repeat()

# 方向标记
direct = -1
# 事件循环
while True:  
    # 更新显示
    clock.tick(30)
    if (x >= 400): x = 0;
    if (y >= 300): y = 0;
    
    # 更新
    pp.update(window,  direct, (x, y))
    pygame.display.update()    
        
    for event in pygame.event.get():
        if event.type == pygame.QUIT: #如果关闭窗口就退出
            sys.exit()
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE: # 如果按下Esc键也退出
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            pass    
    # 取得按键
    kname = pygame.key.get_pressed()
    #print kname
    if kname[pygame.K_LEFT]: # 左
        if x > 0: x = x -1
        direct = 1
    elif kname[pygame.K_RIGHT]: # 右
        if x < 400: x = x + 1
        direct = 3
    elif kname[pygame.K_UP]: # 上
        if y > 0: y = y -1
        direct = 2
    elif kname[pygame.K_DOWN]: # 下
        if y < 300: y = y + 1
        direct = 0
    else:
        direct = -1









































