# encoding = utf-8


'''
Author Email: guokrfans@gmail.com
Versions: Python3.3



程序会删掉第二行字幕
'''

def exit_handler():
    print ("按[回车]退出")
    input('')

import atexit
atexit.register(exit_handler)
# 告诉程序在退出前执行这个函数, 即便程序出错它也是可以运行的




import os
import sys
import pysubs






try:
    file_path = sys.argv[1]
except:
    print('请拖入文件')
    input()
    exit()
# 如果不是拖入字幕文件来运行  就提示需要拖入文件







subs = pysubs.load(file_path, encoding="utf-8")

for line in subs:
    text = line.text

    try:
        text = text.split(r'\N')
        if len(text) == 2:
            text = str(text[0])
        else:
            text = str(text[1])
        line.text = text
    except:
        pass

subs.save(file_path)





print ('')
print ("处理完毕")
print ('')

