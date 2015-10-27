import pygame
import time


clock = pygame.time.Clock()
time_passed = clock.tick()
time.sleep(1)
time_passed = clock.tick(30)

# tick返回的是2次调用之间的时间
print time_passed




'''
time_passed = clock.tick(30)
这一行非常有用，在每一个循环中加上它，那么给tick方法加上的参数就成为了游戏绘制的最大帧率，
这样的话，游戏就不会用掉你所有的CPU资源了！
'''





