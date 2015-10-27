# 这个程序用于输出某个目录下的所有目录名(不包括文件)

import os
import re


list_dir = "F:" + os.sep
# 你要输出的目录
# os.sep是系统的路径分隔符, 也就是"/"
# 在windows上运行等于 list_dir = 'F:/'


filenames = os.listdir(list_dir)
# 获得目录下的所有文件名(目录&文件) 


for filename in filenames:
        if os.path.isdir(list_dir + filename):
                print(filename)
                
# 循环, 如果是目录, 则输出.
