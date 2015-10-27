
# 程序利用谷歌翻译翻译字幕文件里的一句字幕.
# 只是一句字幕而已. 


import os
import sys
import pysubs    # Additional modules
import requests  # Additional modules





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




###################################################################
#
# atexit模块可以在程序退出前做些事情, 哪怕报错什么的, 这段代码也能运行.
#
####################################################################

def exit_handler():
    print ('按[回车]退出')
    print ('Press [Enter] Exit')
    input ()

import atexit
atexit.register(exit_handler)







####################################################
#
# 从字幕文件里取一行字幕. 待会我们翻译它.
#
######################################################

subs = pysubs.load(file_full_path, encoding='utf-8')
# 打开字幕文件

e_txt = subs[4].text.replace('\\N', ' ')
# 获取一行字幕. 并且把换行去掉, 因为英文字幕有时会分成几行.
# 这个换行符也拿去翻译的话后面的处理会很麻烦. 所以直接删掉.
# 这里的数字4可任意替换

print (e_txt)
print()
# 把原文输出来.




################################
#
# 原语言和目标语言
#
################################

sl = 'en'
# source language

tl = 'zh-CN'
# target language






####################################################
#
# 此函数返回原原本本的结果.
#
######################################################

def pure_google_translate(translate_string):

    r = requests.get(
        'http://translate.google.cn/translate_a/t?client=t&hl=zh-CN&sl='+sl+'&tl='+tl+'&ie=UTF-8&oe=UTF-8&multires=1&otf=2&ssel=0&tsel=0&sc=1&q=' + translate_string,
        timeout = 5
    )
    # timeout参数是超时时间

    web_content = r.text    # 拿到返回的响应
    
    return web_content  # 返回结果







###########################
#
# 算出字幕可以用句号分成几行, 保存在 how_many_line 变量里
#
############################
how_many_line = 0
e_txt_list = e_txt.split(".")
for one in e_txt_list:
    if one != '':
        how_many_line = how_many_line + 1





############################
#
# 翻译
#
############################

p_txt = pure_google_translate(e_txt)
# 1. 拿到纯翻译 (格式非常复杂, 你可以输出 p_txt 看看)


a_list = p_txt.split('"')
# 2. 以双引号分割成一个列表. 存到 a_list 里



def is_cn_char(i): 
    return 0x4e00<=ord(i)<0x9fa6 
# 3. 定义一个判断字符是否为中文的函数, 这个函数的代码来自网络.



ChineseChar_List = []
for one_item in a_list:
    for one_char in one_item:
        if is_cn_char(one_char): 
            ChineseChar_List.append(one_item)
            break
# 4. 循环 a_list 列表里的每个字符串
# 5. 判断字符串里是否包含中文, 如果包含就推入 ChineseChar_List 保存.



final_result_string = ""
for i in range(0, how_many_line):
    final_result_string = final_result_string + ChineseChar_List[i]
print (final_result_string)
print ()
# 6. 根据 how_many_line 循环 ChineseChar_List 相应次数, 拼接在一起.
# 这就是最终翻译结果了.



