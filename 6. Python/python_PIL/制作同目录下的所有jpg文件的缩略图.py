
# 制作同目录下, 所有jpg文件的缩略图


from PIL import Image
import glob, os

size = (128, 128)

for infile in glob.glob("*.jpg"):
    file, ext = os.path.splitext(infile)
    # 分解文件名的扩展名

    im = Image.open(infile)

    im.thumbnail(size, Image.ANTIALIAS)
    # 第二個參數可以省略，是用來指定變更時使用的內插法，預設是 Image.NEAREST (取最近點)，

    im.save(file + ".thumbnail.jpg", "JPEG")



