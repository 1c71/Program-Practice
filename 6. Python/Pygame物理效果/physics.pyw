
import sys, pygame
import pygame.mixer  # 用于播放声音
from pygame.locals import *
import random
import euclid
import math


pygame.init()
clock = pygame.time.Clock()


screen_size = screen_width, screen_height = 600,400

screen = pygame.display.set_mode(screen_size)
pygame.display.set_caption("pygame")



red = 255,0,0
black = 0,0,0
blue = 0,0,255
yellow = 0,255,255

colors = [red,black,blue,yellow]
# 用于随机选颜色


gravity = euclid.Vector2(0.0, 80.0)
# 重力
drag = 0.1
initial_velocity = 20
# 初始速度




class MyCircle:
    
    def __init__(self, position, size, color=(255,255,255), velocity = euclid.Vector2(0,0), accel = euclid.Vector2(0,0),  width=1 ):
        self.position = position
        self.size = size #球的大小
        self.color = color
        self.width = width
        self.velocity = velocity #速度
        self.accel = accel      # accel是acceleration的缩写. 意思是加速度

    
    def display(self):
        rx, ry = int(self.position.x), int(self.position.y)
        pygame.draw.circle(screen, self.color, (rx, ry), self.size, self.width)


    def move(self):
        self.position += self.velocity * dtime + 0.5*(self.accel * (dtime ** 2))
        # 速度*时间=路程。基于上一次的位置接着设置
        self.velocity += self.accel * dtime
        self.velocity -= self.velocity * drag * dtime
        self.bounce() #弹跳函数,碰到边框反弹
        

        # 调用这个方法就可以改变self.velocity. 也就是速度
    def change_velocity(self, velocity):
        self.velocity = velocity

    def bounce(self):
            if self.position.x <= self.size:
                self.position.x = 2*self.size - self.position.x
                self.velocity = self.velocity.reflect(euclid.Vector2(1,0))

                # 如果x坐标超出屏幕
            elif self.position.x >= screen_width - self.size:
                self.position.x = 2*(screen_width - self.size) - self.position.x
                self.velocity = self.velocity.reflect(euclid.Vector2(1,0))

            if self.position.y <= self.size:
                self.position.x = 2*self.size - self.position.y
                self.velocity = self.velocity.reflect(euclid.Vector2(0,1))

                # 如果x坐标超出屏幕
            elif self.position.y >= screen_height - self.size:
                self.position.y = 2*(screen_height - self.size) - self.position.y 
                self.velocity = self.velocity.reflect(euclid.Vector2(0,1))


    #计算表面之间的距离的方程
    def surface_distance(self, other, time):
        radiiAB = self.size + other.size
        posA = self.position + self.velocity * dtime + 0.5*(self.accel * (dtime ** 2))
        posB = other.position + self.velocity * dtime + 0.5*(self.accel * (dtime ** 2))
        posAB = abs(posA - posB)
        return posAB - radiiAB

    # 碰撞函数
    def collide(self, other):
        if self.surface_distance(other, dtime) <= 0:  #当表面之间的距离小于等于0
            collision_vector = self.position - other.position
            collision_vector.normalize()
            self.velocity = self.velocity.reflect(collision_vector)
            other.velocity = other.velocity.reflect(collision_vector)
            # reflect 反射
            # normalize 使正常化；使标准化



# 这个函数用于拿到一个随机的速度
def get_random_velocity():
    new_angle = random.uniform(0, math.pi*2)  
    # random.uniform用于生成一个指定范围内的随机符点数. 两个参数其中一个是上限,一个是下限
    new_x = math.sin(new_angle)
    new_y = math.cos(new_angle)
    new_vector = euclid.Vector2(new_x, new_y)
    new_vector.normalize()
    new_vector *= initial_velocity  #像素 每秒
    return new_vector








number_of_circles = 10   #圆圈的数量
my_circles = []    #

for n in range(number_of_circles):
    size = random.randint(10,20) #随机一个10~20的整数出来
    x = random.randint(size, screen_width-size)  #随机出一个小于屏幕宽度的x坐标
    y = random.randint(size, screen_height-size) #随机出一个小于屏幕高度的y坐标
    color = random.choice(colors) #随机从颜色列表中取出一个颜色

    velocity = get_random_velocity()
    my_circle = MyCircle(euclid.Vector2(x, y), size, color, velocity, gravity)
    # 注意这里的velocity, gravity
    my_circles.append(my_circle)

    # 要注意my_circle和my_circles的不同点,后面多了个s.


direction_tick = 0.0
# 方向


# my_circle = MyCircle((100,100), 10, red)
# my_circle2 = MyCircle((20,200), 40, blue, 7)
# my_circle3 = MyCircle((40,400), 20, yellow, 4)



fps_limit = 60
run_me = True


while run_me:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run_me = False
        elif event.type == KEYDOWN and event.key == K_q:
            run_me = False

    dtime_ms = clock.tick(fps_limit)   # 控制帧数
    dtime = dtime_ms/1000.0



    screen.lock()
    screen.fill((255,255,255)) 

    #enumerate在for循环中得到计数
    for i, my_circle in enumerate(my_circles):
        my_circle.move()
        for my_circle2 in my_circles[i+1:]:
            my_circle.collide(my_circle2)
        my_circle.display()

    screen.unlock()
    
    pygame.display.flip()
    


pygame.quit()
sys.exit()










