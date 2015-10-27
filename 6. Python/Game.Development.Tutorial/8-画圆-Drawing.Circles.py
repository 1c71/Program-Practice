import pygame, sys
from pygame.locals import *

pygame.init()

screen = pygame.display.set_mode((640,360), 0, 32)
color=(230,155,20)
position=(100,188)
radius=(60)


while True:
     
     for event in pygame.event.get():
          if event.type == QUIT:
               pygame.quit() 
               sys.exit()    

     
     screen.lock()
     pygame.draw.circle(screen, color, position, radius)
     screen.unlock()

     
     pygame.display.update()
                    
                    
                    
               
          























