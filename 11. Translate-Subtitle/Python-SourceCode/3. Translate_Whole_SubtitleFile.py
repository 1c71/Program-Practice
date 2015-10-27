# encoding = utf-8
# Author Name: Cheng Zheng (郑诚)
# Author Email: guokrfans@gmail.com
# Author Github username: 1c7

# Test Environment: Windows7 x64 + Python 3.3
# Program have not been test on Unix/Linux, Mac





import os
import sys
import pysubs    # Additional modules
import requests  # Additional modules









################################
#
# 原语言和目标语言
#
################################

sl = 'en'
# source language

tl = 'zh-CN'
# target language









##########################################################
#
# 判断是[直接运行]还是[拖入运行]
# 如果是直接运行就提示: "需要拖入文件才能翻译", 然后退出
#
##########################################################
try:
    print (sys.argv[1])
    print()
    file_full_path = sys.argv[1]
except:
    print('请拖入文件, 不要直接运行, 按[回车键]退出程序.')
    print('Please drag file in. Do not just run program. Press [Enter] Exit.')
    input()
    exit()
    







'''

atexit模块可以在程序退出之前做一些事情, 哪怕报错什么的, 这段代码也能运行.
我们把代码放在[文件判断]的后面..

不要放在最前面, 如果这样做的话, 直接运行这个程序的时候, 就会:
input('请拖入文件, 不要直接运行, 按[回车键]退出程序')
input("按回车退出")

就是先执行了前面[文件判断]的退出机制, 然后又执行了exit_handler()
这样很2

'''


def exit_handler():
    print ('按[回车]退出')
    print ('Press [Enter] Exit')
    input ()

import atexit
atexit.register(exit_handler)










############################
#
# 拼接新文件名
#
############################

dirname = os.path.dirname(file_full_path)
# 文件路径(最后没带\)

filename = os.path.basename(file_full_path)
# 文件名(带后缀)

save_path = dirname + os.sep + '(done)' + filename
# 新文件名
# os.sep可获得路径分隔符 windows上是 '\'






########################################################
#
# 定义一个判断字符是否为中文的函数, 这个函数的代码来自网络.
#
########################################################

def is_cn_char(i): 
    return 0x4e00<=ord(i)<0x9fa6 








###############################################
#
# 函数接收一个[字符串], 返回[翻译结果]
# 超时时间是 5 秒
#
#################################################

def google_translate(translate_string):

    how_many_line = 0
    t_s_list = translate_string.split(".")
    for one in t_s_list:
        if one != '':
            how_many_line = how_many_line + 1
    # 先算出字幕可以用句号分成几行, 保存在 how_many_line 变量里

    
    
    r = requests.get(
        'http://translate.google.cn/translate_a/t?client=t&hl=zh-CN&sl='+sl+'&tl='+tl+'&ie=UTF-8&oe=UTF-8&multires=1&otf=2&ssel=0&tsel=0&sc=1&q=' + translate_string,
        timeout = 5
    )
    # timeout参数是超时时间



    web_content = r.text
    # 1. 拿到返回的响应

    a_list = web_content.split('"')
    # 2. 以双引号分割成一个列表. 存到 a_list 里

    ChineseChar_List = []
    for one_item in a_list:
        for one_char in one_item:
            if is_cn_char(one_char): 
                ChineseChar_List.append(one_item)
                break
    # 3. 循环 a_list 列表里的每个字符串
    # 4. 判断字符串里是否包含中文, 如果包含就推入 ChineseChar_List 保存.



    final_result_string = ""
    for i in range(0, how_many_line):
        final_result_string = final_result_string + ChineseChar_List[i]
    # 5. 根据 how_many_line 循环 ChineseChar_List 相应次数, 拼接在一起.
    # 这就是最终翻译结果了.


    return final_result_string







'''

思路:

1. 让 pysubs 模块读取字幕文件

2. 循环每一行:
      if 这一行里有中文:
          跳过
      else:
         翻译这一行的英文
         把 翻译结果 和 英文原句 合在一起

3. 保存



额外说明:
判断中文是用ord()把字符转换成ASCII码来判断的, ASCII码大于127我们就当作它是中文

'''



subs = pysubs.load(file_full_path, encoding='utf-8')
# 打开字幕文件

for line in subs:
    try:
        Sentence = line.text
        # 拿到字幕内容
        Sentence = Sentence.replace('\\N', ' ')
        # 把[换行]变成了[空格], 不然有些多行英文字幕会很烦人
        Sentence = Sentence.replace('’', '\'')
        Sentence = Sentence.replace('“', '\"')
        Sentence = Sentence.replace('”', '\"')
        # 把[全角符号]变成[半角符号]
    except:
        pass


    #
    # 跳过空行
    #
    if Sentence.strip() == '':
        continue



    #
    # 判断字幕里是否有中文 有则跳过 不处理这一行
    #
    have_cn = False
    
    for char in Sentence:
        if ord(str(char)) > 127:
            have_cn = True
            break

    if have_cn:
        have_cn = False
        continue




    #
    # 翻译, 拿翻译结果
    # 
    try:
        result = google_translate(Sentence)
    except:
        print ('翻译超时, 跳过这一行')
        print ('time out, skip thie line')
        continue

    data = result + '  \\N  ' + Sentence
    line.text = data



    #
    # 输出结果(有时候print会出现一些奇葩的编码错误..所以这里也用try,except)
    #
    try:
        print (data)
    except:
        continue
    


    #
    # 多换一行, 不然看着太挤
    #
    print ('')
    







#
# 收尾工作
# 
print ("===========================")
print (sys.argv[1] + '          翻译完成. ')
print (sys.argv[1] + '          translate done. ')
print ("===========================")



#
# 保存对字幕文件的修改
#
subs.save(save_path)










