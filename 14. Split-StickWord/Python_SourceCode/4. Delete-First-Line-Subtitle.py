# encoding = utf-8


'''
Author Email: guokrfans@gmail.com
语言: Python3.3
外部模块: pysubs



如果有两行字幕, 程序会清理掉第一行字幕, 比如:
"大家好 我是Hank Green 我想教你化学 \\N 
hello i'm hank green. i want teach you chemistry"

程序会把 \\N 和前面的中文字幕全部删掉
'''



delete_slash_N = True
# 用于决定是否删掉字幕文件里的\N
# \N 的用途是换行























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
    print (sys.argv[1])    # 输出拖入的文件的路径
    file_path = sys.argv[1]
except:
    print('请拖入需要删除第一行字幕的字幕文件. 不要直接运行. 按[回车键]退出程序')
    input()
    exit()
# 如果不是拖入字幕文件来运行  就提示需要拖入文件







subs = pysubs.load(file_path, encoding="utf-8")

for line in subs:
    text = line.text

    try:
        text = text.split(r'\N')
        if len(text) == 2:
            text = str(text[1])
        else:
            text = str(text[0])
        line.text = text
    except:
        pass

subs.save(file_path)





print ('')
print ("处理完毕")
print ('')















