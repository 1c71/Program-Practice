import pygame,sys

pygame.init()


class Car(pygame.sprite.Sprite):

    def __init__(self,filename,initial_position):
        
        pygame.sprite.Sprite.__init__(self)
        
        self.image=pygame.image.load(filename) # 根据参数给的文件名载入文件
        
        self.rect=self.image.get_rect() #获取图像大小
        #self.rect.topleft=initial_position
        self.rect.bottomright=initial_position   #参数赋值给rect.bottomright
        # 这样你就能做到 让图片的某一个角 显示在你希望的地方
        print self.rect.right

         
screen=pygame.display.set_mode([640,480])
screen.fill([255,255,255])


f='pi.jpg'
b=Car(f,[150,100])
# 实例化并传入参数


screen.blit(b.image,b.rect)
print b.rect
pygame.display.update()


while True:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
            sys.exit()






















            
