import pygame, sys
from pygame.locals import *

pygame.init()
screen = pygame.display.set_mode((640,360), 0, 32)

color=(100,110,120)
pos1=(20,20)
pos2=(250,199)

while True:
     
     for event in pygame.event.get():
          if event.type == QUIT:
               pygame.quit() 
               sys.exit()    

     
     screen.lock()

     #可以再加一个参数代表线的宽度
     pygame.draw.line(screen, color, pos1, pos2)
     
     screen.unlock()

     
     pygame.display.update()
                    
                    
                    
               
          























