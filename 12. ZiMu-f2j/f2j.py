# encoding = utf-8
# Author email: guokrfans@gmail.com
# 程序用字典把文件 繁->简
# Version: Python3



import os
import sys



#
# 判断是否是以拖入文件的方式运行的
#
try:
    subtitle_path = sys.argv[1]
except:
    print('请拖入需要繁体转简体的字幕文件, 不要直接运行, 按[回车键]退出程序')
    input()
    sys.exit()





#
# 告诉程序在退出前执行这个函数, 即便程序出错时它也是可以运行的
# 
def exit_handler():
    print ("按[回车]退出")
    input('')
import atexit
atexit.register(exit_handler)







#
# 打开并读取字典文件
#
dic = open( os.path.dirname(sys.argv[0]) + r"\f2j.txt", encoding='utf8' )   
dic_content = dic.read()


lines_list = dic_content.splitlines()   # 用换行符 把字符串分割成列表
lines_list = [i for i in lines_list if i != '']     # 去掉列表里的空元素



f2j_dic = {}
for line in lines_list:
    line_list = line.split()
    if len(line_list) > 1:
        one = line_list[0]
        two = line_list[1]
        f2j_dic[one] = two
# 把f2j.txt变成一个 Python 字典, key是繁体, value是简体, 值保存到 f2j_dic 里






#
# 打开字幕文件并做一些处理
#
sub = open( subtitle_path, mode='r+', encoding='utf8' )
sub_content = sub.read()
sub_content = sub_content.replace('\ufeff', '')
# 去掉\ufeff.  这好像是UTF-8文件的BOM头什么的.





for key,value in f2j_dic.items():
    sub_content = sub_content.replace(key, value)
# 文件的繁->简已经转换完成了, 在 sub_content 里





#
# 写回文件里去(覆盖原文件)
#
sub.seek(0)
sub.write(sub_content)
sub.truncate()
sub.close()






#
# 收尾工作
#
print ('-------------------------------')
print ('替换完成')
print ('-------------------------------')








