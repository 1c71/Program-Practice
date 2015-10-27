
import Image
im = Image.open("2.jpg")
# im.show() 注释掉,不显示原图



box = (0,0,30,300)
part = im.crop(box)
part.show()

'''

crop()
从图像中提取出某个矩形大小的图像。
它接收一个四元素的元组作为参数 (x,y,width,height)，
坐标系统的原点(0, 0)是左上角。
'''
