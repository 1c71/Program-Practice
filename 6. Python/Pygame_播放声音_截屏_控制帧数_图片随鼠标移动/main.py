
import sys, pygame
import pygame.mixer  # 用于播放声音
from pygame.locals import *


pygame.init()

sound = pygame.mixer.Sound("rain.wav")
#sound.play() 
Sword = pygame.mixer.Sound("Swords.wav")

clock = pygame.time.Clock()




size = width, height = 600,400
color = 0,0,0

screen = pygame.display.set_mode(size)
pygame.display.set_caption("pygame")


img = pygame.image.load("firzen_f.bmp")
img2 = pygame.transform.scale(img, (92,92))

x = 0
y = 0

r = 0


while 1:
	mx,my = pygame.mouse.get_pos() #拿到鼠标的位置
	print mx,my

	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			sys.exit()
		elif event.type == KEYDOWN and event.key == K_ESCAPE:
			sys.exit()
		elif event.type == KEYDOWN and event.key == K_q:
			sys.exit()
		elif event.type == MOUSEBUTTONDOWN:
			Sword.play()   #按下鼠标就剑的声音
		elif event.type == KEYDOWN and event.key == K_SPACE:
			pygame.image.save(screen,"screenshot.png")
			# 按下空格保存游戏截图

	screen.fill(color) 
	#screen.fill((r,0,0))  
	# 2.加上上面这一句之后，每次绘制都会把屏幕的背景绘制为黑色。
	# 问题就解决了。

	screen.blit(img, (x,y))
	screen.blit(img2, (mx-50,my-50))
	x = x+1
	clock.tick(60)   # 控制帧数

	pygame.display.flip()
	# 1.每次绘制的时候都会在旧图片上接着画，所以会产生这种效果。

	# if r == 255:
	# 	r1 = -1
	# 	#sound.play()  #每次颜色变换都会播放声音
	# elif r == 0:
	# 	r1 = 1
	# 	#sound.play()

	# r = r + r1
	# 第一次循环的时候r是0, 于是r1=1, 接着就是一直+1. 直到255再一直-1
















