import pygame
import sys
import math
from pygame.locals import *


pygame.init()
clock = pygame.time.Clock()


background_colour = (255,255,255)
(width, height) = (600, 400)

screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Tutorial 1')
screen.fill(background_colour)



angle = 30
speed = 20

# python中的函数是弧度,不是角度,所以要转换成角度
#角度=弧度*180.0/PI
#弧度=角度*PI/180.0
_cos = math.cos(angle*math.pi/180.0)
_sin = math.sin(angle*math.pi/180.0)

# 线段的起点和终点
pos1=[288,350]
pos2=[333,200]




#x方向上的速度
fps_limit = 40

x = 0+50
y = 0+50


# velocity_x = (speed * scale_x)
# velocity_y = (speed * scale_y)

screen.fill((0,0,0))


running = True
while running:
	 
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False
		if event.type == KEYDOWN and event.key == K_LEFT:
			# pos_x =  abs(pos2[0]-pos1[0])  #x方向上的距离
			# pos_y = abs(pos2[1]-pos1[1])   #y方向上的距离
			# result = pos_x**2 + pos_y**2
			# print (math.sqrt(result))    #根据勾股定理求距离,也就是求斜边

			# new_x = (pos2[0]*_cos) + (pos2[1]*_sin)
			# new_y = (-pos2[0]*_sin) + (pos2[1]*_cos)
			# pos2 = [int(new_x), int(new_y)]
			# pygame.draw.aaline(screen, (255,255,255), pos1, pos2)
			# print "working"
			# print pos2

			





		# if event.type == KEYDOWN and event.key == K_RIGHT:
		# 	x = int(math.ceil(x + velocity_x))
		# 	y = int(math.ceil(y + velocity_y))
	
	ms = clock.tick(fps_limit)   # 控制帧数
	ms = ms/1000.0

    # 最后2个参数是半径和厚度

	screen.lock()
	pygame.draw.circle(screen, (0,0,255), (x,y), 50, 2)
	

	pygame.draw.aaline(screen,(255,255,255), pos1, pos2)

	screen.unlock()


	pygame.display.flip()

pygame.quit()
sys.exit()

    

# 查一下pygame.locals里面的reflect， normalize














    
