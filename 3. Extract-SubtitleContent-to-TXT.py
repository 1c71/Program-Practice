# encoding = utf-8
# Test Environment: Windows7 x64 + Python 3.3

# Author Name: Cheng Zheng (郑诚)
# Author Email: guokrfans@gmail.com
# Author Github Username: 1c7
# Program have not been test on Unix/Linux, Mac


# 说明:
# 程序会把字幕文件内容复制到一个新txt文件中.
# 原字幕文件并不会被修改.




import os
import sys
import pysubs  




############################################
#
# 判断是[直接运行]还是[拖入运行]
# 如果是直接运行就提示: "需要拖入文件"
# 然后等待用户按[回车键]退出程序
#
############################################

try:
    file_full_path = sys.argv[1]
except:
    print('请拖入字幕文件, 不要直接运行, 按[回车键]退出程序.')
    input()
    exit()
    





################################################################
#
# [拼接新文件名]
# 格式是: 原文件名 + .txt
# 我们假设拖入的文件是 C:\User\Administrator\Desktop\test.ass )
#
################################################################


dirname = os.path.dirname(file_full_path)
# 文件路径(最后不带\)
# 比如: C:\User\Administrator\Desktop


full_filename = os.path.basename(file_full_path)
# 文件名(带后缀)
# 比如: test.ass


filename = full_filename.split('.')[0]
# 文件名(不带后缀)
# 比如: test


txt_path = dirname + os.sep + filename + ".txt"
# 新txt文件的文件名
# os.sep可获得路径分隔符 windows上是 '\'






#####################################
#
# 开始处理
#
#####################################


sub = pysubs.load(file_full_path, encoding='utf-8')
# 打开字幕文件

txt = open(txt_path, mode="a", encoding='utf-8')
# 打开txt文件


for line in sub:
    sentence_list = line.text.split("\\N")
    # 以\\N拆成列表
    
    for one in sentence_list:
        txt.write(one.strip())  # 去掉左右两边的多余空格
        txt.write('\n') # 中英文之间的换行
    
    txt.write('\n\n')
    # 一整句之间的换行


txt.close()
# 关闭txt文件



