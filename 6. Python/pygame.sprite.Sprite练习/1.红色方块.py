import pygame,sys

pygame.init()


class Temp(pygame.sprite.Sprite):
    def __init__(self,color,initial_position):

        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.Surface([30,30]) # 定义显示30*30的一个距形surface
        self.image.fill(color)      # 用color来填充颜色
        
        self.rect=self.image.get_rect() # 获取self.image大小。
        self.rect.topleft=initial_position # 确定左上角显示位置


screen=pygame.display.set_mode([640,480])
# 设置屏幕大小
screen.fill([255,255,255])
# 填充成白色

b=Temp([255,0,0],[50,100])

screen.blit(b.image,b.rect)


pygame.display.update()


while True:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
             pygame.quit()
             sys.exit()
