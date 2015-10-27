import pygame, sys
from pygame.locals import *

pygame.init()

screen = pygame.display.set_mode((640,360), 0, 32)

color=(30,155,220)
rectangle=(40,80,250,90)
#4个数字分别代表 x,y,宽,高

while True:
     
     for event in pygame.event.get():
          if event.type == QUIT:
               pygame.quit() 
               sys.exit()    

     
     screen.lock()

     pygame.draw.ellipse(screen, color, rectangle)
     
     screen.unlock()

     
     pygame.display.update()
                    
                    
                    
               
          























