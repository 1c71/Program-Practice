bif = "bg.jpg"
mif = "ball.png"

import pygame, sys
from pygame.locals import *

pygame.init()


screen = pygame.display.set_mode((640,360), 0, 32)
background = pygame.image.load(bif).convert()
ball = pygame.image.load(mif).convert_alpha()

x=0
y=0
clock=pygame.time.Clock()
speedx=150
speedy=170


while True:
     for event in pygame.event.get():
          if event.type == QUIT:
               pygame.quit() 
               sys.exit()


     screen.blit(background, (0,0))
     screen.blit(ball, (x,y))

     milli=clock.tick()
     seconds=milli/1000.
     dmx=seconds*speedx
     dmy=seconds*speedy
     x+=dmx
     y+=dmy

     if x>640:
          x=0

     if y>360:
          y=0


     pygame.display.update()
                               
 























