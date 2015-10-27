import Image
 
img = Image.open("7_oxygen.png")



print (img.size) # size是图片的宽和高, 元组

# 这里取的是高度, 然后除了2.
j = img.size[1] / 2     # size => (width, height)






row = [img.getpixel((i, j)) for i in range(0, img.size[0], 7)] 
# RGBA...
gray = [r for r, g, b, a in row if r == g == b]
print "".join(map(chr, gray))
result = [105, 110, 116, 101, 103, 114, 105, 116, 121]
print "".join(map(chr, result))

















