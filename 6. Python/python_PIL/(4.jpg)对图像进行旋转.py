

import Image

im = Image.open( "4.jpg" )

im.rotate(45).show()

# 进行图像的旋转, 图像的宽和高不会变, 旋转后的其他地方会用黑色填充
