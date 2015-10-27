# encoding = utf-8


# 运行环境要求:
# Python 3.3
# 文件目录里不能有非英文字符


# 程序说明:
# 字幕文件必须是这样的: 中文 \N 英文
# 我们用split获得中文那一段  把所有的逗号和句号换成空格


import sys
import pysubs


#
# filepath 是可选的文件路径变量
# 里面填写的是字幕文件的全路径
# 如果为空 那就用的是拖入  如果不为空  那就处理这变量指向的文件
#
filepath = r''















###############################
#
# 如果没填路径就肯定是拖入了
#
###############################

if filepath == '':    # 如果没填 filepath
    try:
        print (sys.argv[1])
        filepath = sys.argv[1]
        print ()
    except:
        print('请拖入需要去中文字幕里逗号句号的字幕文件  不要直接运行  按[回车键]退出')
        input()
        exit()
else:    # 如果填了 filepath
    print ("代码里的 filepath 变量已被填写 ")
    print ("程序会处理: " + filepath)











###########################################################################
#
# 这部分代码会在代码退出前执行 哪怕代码报错也会执行 对于看错误信息很有用
#
###########################################################################

def exit_handler():
    print ('按[回车]退出')
    input ()

import atexit
atexit.register(exit_handler)








##########################
#
# 正式开始处理字幕文件
#
##########################

try:
    subs = pysubs.load(filepath, encoding='utf-8')
except:
    print('字幕文件打开失败 程序退出')


for line in subs:
    
    try:
        whole_Sentence = line.text
        l = whole_Sentence.split(r'\N')
        l[0] = l[0].replace(',', ' ')
        l[0] = l[0].replace('.', ' ')
        l[0] = l[0].replace('，', ' ')
        l[0] = l[0].replace('。', ' ')
    except:
        pass
    
    line.text = r'\N'.join(l)


#
# 提示下
#
print ("===========================")
print (' 中文字幕里的逗号句号都换成空格了 ')
print ("===========================")
print ()

#
# 保存修改
#
subs.save(filepath)







