my_name = "I don't want to be Loser!"

import pygame

pygame.init()

# 为了使用字体，你得先创建一个Font对象, 参数是 字体名 和 字体大小
my_font = pygame.font.SysFont("arial", 64)

# 用render方法来写字
name_surface = my_font.render(my_name, True, (0, 0, 0), (255, 255, 255))
# 第二个参数是个布尔值，以为这是否开启抗锯齿
# 第三个参数是字体的颜色；
# 第四个是背景色，如果你想没有背景色（也就是透明），那么可以不加这第四个参数。


# 保存到图片里
pygame.image.save(name_surface, "name.png")
