import pygame,sys

pygame.init()

class Car(pygame.sprite.Sprite):
     
    def __init__(self,filename,initial_position):
         
        pygame.sprite.Sprite.__init__(self)
        
        self.image=pygame.image.load(filename) # 通过参数读取图片
        self.rect=self.image.get_rect()  # 获得图片宽高
        self.rect.bottomright=initial_position  # 设置右下角位置

         
screen=pygame.display.set_mode([640,480])
screen.fill([255,255,255])


fi='pi.jpg'
locationgroup=([150,200],[350,360],[250,280])
Cargroup=[]


for lo in locationgroup:
    Cargroup.append(Car(fi,lo)) # 用循环往空列表添加对象
    
for carlist in Cargroup:
    screen.blit(carlist.image,carlist.rect) # 根据列表中的对象数, 逐个显示到屏幕上


    
pygame.display.update()


while True:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
             pygame.quit()
             sys.exit()









