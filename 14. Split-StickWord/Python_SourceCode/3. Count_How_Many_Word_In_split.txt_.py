# encoding = utf-8
# Author email: guokrfans@gmail.com


'''
功能:
    数split.txt里到底有多少"对"单词
    注意 程序不负责纠错单词

思路:
    1. 去掉所有以#开头的行
    2. 去掉所有中文
    3. 计数

'''



def exit_handler():
    print ("按[回车]退出")
    print ("Press [Enter] Exit")
    input('')

import atexit
atexit.register(exit_handler)





import os
import sys



split_txt = open(os.path.dirname(sys.argv[0])+"\split.txt", encoding='utf8')
content = split_txt.read()
content = content.replace('\ufeff','')
# 去掉\ufeff.  这好像是UTF-8文件的BOM头什么的.





new_content = ''
for onechar in content:
    if ord(str(onechar)) < 127:
        new_content = new_content + onechar

# -- 去掉split.txt里的中文 --






line_list = new_content.splitlines()
line_list = [i for i in line_list if i != '']
# -- 以换行符分割 并去掉列表里的空元素 --









new_list = []

for index,line in enumerate(line_list):
    if str(line).startswith("#"):
        continue
    else:
        new_list.append(line_list[index]) 

lines_list = new_list

# -- 去掉以#开头的行 -- 
# 不要 print (lines_list)
# 这个列表太大, 会很卡



number = len(lines_list)
pair = len(lines_list) / 2



print ( '一共有 %s 个单词' % number )
print ( '一共有 %s 对单词' % pair )






