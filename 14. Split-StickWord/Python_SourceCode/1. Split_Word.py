# encoding = utf-8
# Author Name: Cheng Zheng (郑诚)
# Author Email: guokrfans@gmail.com
# Author Github username: 1c7

# Test Environment: Windows7 x64 + Python 3.3
# Program have not been test on Unix/Linux, Mac

# 功能说明:

# 1. 替换掉常见连词
# 比如: thereare, youare  替换成: there are, you are

# 2. 去掉 "\"这个符号
# 因为有些字幕里都是: don\'t  shouldn\'t  we\'ve  

# 3. 句号后面如果有字母或数字, 那么给句号后面加上一个空格
# input: egg.that        output: egg. that
# 因为句号后面如果跟一个字母的话, 谷歌翻译是不会翻译的.

# 4. 逗号后面如果有字母, 那么给它加个空格
# input: $90,000         output: $90,000
# input: ok,great        output: ok, great
# 逗号加空格只是为了美观

# 5. [分割数字] -- 此功能暂时暂停. 下个版本会启用
# input: i have 200cm              output: i have 200 cm
# input: you got150pound?          output:  you got 150 pound?




def exit_handler():
    print ("按[回车]退出")
    print ("Press [Enter] Exit")
    input('')

import atexit
atexit.register(exit_handler)
# 告诉程序在退出前执行这个函数, 即便程序出错时它也是可以运行的





import os
import sys
import re
import pysubs







#==(start) 1. 判断是[直接运行]还是[拖入运行] ==

try:
    need_split_path = sys.argv[1]
    # 用于原路径保存
except:
    print('请拖入需要分连词的字幕文件, 不要直接运行, 按[回车键]退出程序')
    print('Please drag subtitle file on this.  Do not run directly.')
    input()
    exit()
    

# 如果不是拖入字幕文件来运行, 就提示需要拖入文件.

#==(end) 1. 判断是[直接运行]还是[拖入运行] ==







# 有关下面这3个函数的具体信息, 可以去re_test.py看


# 逗号后面如果有英文字母, 那么加个空格
def Handle_Comma(string):
    p = re.compile(r'(\,)([a-zA-z])')
    return p.sub(r'\1 \2', string)




# 数字前面或后面如果有英文字母, 那么加个空格
def Handle_Number(string):
    Front = re.compile(r'([a-zA-Z])([0-9])')
    Behind = re.compile(r'([0-9])([a-zA-Z])')
    f = Front.sub(r'\1 \2', string)
    b = Behind.sub(r'\1 \2', f)
    return b



# 句号后面如果有字母或数字, 那么给句号后面加上一个空格
def Handle_Period(string):
    p = re.compile(r'(\.)([a-zA-Z]|[0-9])')
    return p.sub(r'\1 \2', string)












#== (start) 2. 处理逗号 句号 数字问题(字幕文件) ==

ugly = pysubs.load(need_split_path, encoding="utf-8")
# 打开字幕文件


# 循环每行字幕
for line in ugly:
    
    temp = line.text.split('\\N')
    # 有些英文字幕是两行的, 用了杠N隔开, 我们按照换行符号分割成列表.
    # temp 现在是个列表


    # 循环这个列表, index是索引, one是内容
    for index,one in enumerate(temp):
        temp[index] = Handle_Number(one)
        temp[index] = Handle_Period(temp[index])
        temp[index] = Handle_Comma(temp[index])
        

    line.text = '\\N'.join(temp)
    # 把列表合起来, 用\\N合起来, 这样就恢复原样了, 然后赋值回去




ugly.save(need_split_path)

#== (end) 2. 处理句号和数字问题(字幕文件) ==



















#==(start) 3. 打开[字幕文件]和[分词列表文件]==


subs_file = open(need_split_path, 'r+', encoding='utf8')    # 打开[字幕文件]

subs = subs_file.read()    # 读取全部内容作为字符串保存到subs里

subs = subs.replace("\\'","'")
# 把 \' 换成 '
# 注意 这里是把斜杠和一个点换成只剩下一个点..
# 这样就可以去掉字幕里的无谓斜线 比如 don\'t  shouldn\'t  we\'ve  



with open(need_split_path, "w", encoding='utf-8') as f:
    f.write(subs)
# 保存字幕中的替换操作   


subs_file.close()
# 关闭[字幕文件], 待会我们再用pysubs模块打开..








split_file = open(os.path.dirname(sys.argv[0])+"\split.txt", encoding='utf8')
# 打开[分词文件]..不然程序就会不知道咋分词

splie_content = split_file.read()
# 读取全部内容作为一个字符串

splie_content = splie_content.replace('\ufeff','')
# 去掉\ufeff.  这好像是UTF-8文件的BOM头什么的.


# 关于读取[分词文件]的说明
# 读这个文件会有奇葩的问题, "当前目录"会跑到window/system32里面去
# 你可以拿 os.getcwd() 看一下
# 所以我们先获取 当前这个代码文件 的路径, 拼接成寻找同目录下split.txt的路径
# 函数说明:  sys.argv[0]是当前代码文件的全路径, dirname函数获取全路径中的路径部分
# 这样就可以读取成功了


#==(end) 3. 打开[字幕文件]和[分词列表文件]==





#==(start) 4. 去掉中文 ==

new_splie_content = ''

for onechar in splie_content:
    if ord(str(onechar)) < 127:
        new_splie_content = new_splie_content + onechar

# new_splie_content 存放的是去除掉中文后的文件内容, 类型是string

#==(end) 4. 去掉中文 ==





#==(start) 5. 以换行符分割成列表, 而且去掉以#号开头的行 ==


lines_list = new_splie_content.splitlines()
# 以换行符拆分 替换词文件, 现在是列表

lines_list = [i for i in lines_list if i != '']
# 去掉列表里的空元素


new_list = []

for index,line in enumerate(lines_list):
    if str(line).startswith("#"):
        continue
    else:
        new_list.append(lines_list[index]) 
# 去掉以#号开头的注释

lines_list = new_list

'''
尝试过用del删除列表元素, 总是会有一些奇葩的错误,
比如那些以#开头的单词的数组下标都是对的, 但是删除的时候只能删除其中一半
所以这里只能拿new_list 来装那些不以#开头的单词.
最后再赋值回lines_list

'''
#==(end) 5. 以换行符分割成列表, 而且去掉以#号开头的行 ==





#==(start) 6. 处理分词列表文件, 把文件内容变成一个字典 ==

sw = {}
# sw 意思是 split word, 存放[要分割的词]和[分割后的词]


# 2个2个的循环, 循环split.txt以换行分割出来的列表.
for i in range(0, len(lines_list), 2):
    
    one = lines_list[i].encode('utf8')
    two = lines_list[i+1].encode('utf8')
    # 这里编码utf-8, 再转换成string, 后面就不会碰到奇怪的编码问题.

    # 我们先做一次判断,再把[换行符分割列表]变成[替换词字典]
    # 判断目的: 万一split.txt里写错了, 比如原本应该有3对 也就是6个单词
    # 少写了一个, 或者多写了一个, 最后导致全错位了, 那就郁闷了.
    # 所以我们判断一下我们每次循环所拿到的这2个单词是否相等..
    # 相等就啥都不管. 不相等就提示用户有错, 然后退出. 
    
    # 判断方法是: 把第二行的空格去掉, 然后两行都转换成小写, 查看是否相等
    # 不相等, 那么说明 split.txt 里有一个单词错位了.
    # 只写了替换词, 没写替换后的词. 或是正好相反. 或是不小心在哪一行打多了1个字符
    # 那我们就报错, 告诉是哪些词错了, 让用户自己去修正 split.txt 
 
    temp_one = one.strip()
    temp_two = two.strip()
    # 先去掉两边的空格.
    # 注意这个变量是临时的, 是用来检测是否有单词错位的.

    
    temp_one = str(temp_one)
    temp_two = str(temp_two)
    # 转换成字符串类型


    temp_one = temp_one.replace(' ','').lower()
    temp_two = temp_two.replace(' ','').lower()
    # 去掉单词中间的空格, [再转换成小写], 待会比对一下
    
    # split.txt文件解析后 替换模式是忽略大小写的
    # 所以split.txt里可以看见这样的 替换词组:  HEIS -- he is
    # 这就是为什么我们这里要统一转换成小写.
    # 其实统一转换成大写也行, 都可以.



    
    if temp_one != temp_two:
        print()
        print('单词 '+ one.decode('utf-8') + '--' + two.decode('utf-8') + ' 错位. 去split.txt里找到这个词然后修复这个问题吧.')
        print('Word '+ one.decode('utf-8') + '--' + two.decode('utf-8') + ' are Wrong. please check split.txt file')
        print()
        exit()
    # 如果第二个词去掉空格不等于第一个词, 那肯定是少写单词, 错位了
    # 一个错后面就全错位了
    # 我们在这里报错然后退出. 那2个空的print是为了输出俩空行, 为了格式好看.


        
    
    sw[one] = two
    # 变成字典



#==(end) 6. 处理分词列表文件, 把文件内容变成一个字典 ==









# ==(start) 7. 现在再打开一次字幕文件 ==

subs = pysubs.load(need_split_path, encoding="utf-8")

# ==(end) 7. 现在再打开一次字幕文件 ==





# ==(start) 8. 正式开始替换了 ==


'''

循环字典 每次拿出一个key和一个value (key是要替换的值, value是替换后的值)
循环每行字幕:
    以空格分割每行字幕变成列表
    循环这个列表:
        用key value去匹配和替换
    合并这个列表
    保存这一行的操作

最后保存字幕文件


'''


for key,value in sw.items():

    key = key.decode('utf8') 
    value = value.decode('utf8')
    # 还记得字典的key是要替换的值, value是替换后的值吧
    # 这里decode一下,不然会有奇怪的编码问题

    # 循环每行字幕
    for line in subs:


        t = line.text
        t = t.replace('\\N',' \\N ')
        whitespace_split_list = t.split()
        # 先用t暂存这一行字幕
        # 把 \\N 前后加1个空格
        # 再以空格分割这行字幕, 把它变成列表
        
        # 解释:
        # 给 \\N 加空格的原因是, 不加的话, 它会和单词黏在一起, 影响我们的分词



        # 循环这个列表, 其实这个列表就是一行字幕里的各个单词
        for i,word in enumerate(whitespace_split_list):
            if word.lower() == key.lower():
                whitespace_split_list[i] = value
        # 都转换成小写, 无视匹配时候的大小写.


        text = ' '.join(whitespace_split_list)
        # 再以空格为间隔合并回去


        
        line.text = text
        # 保存这行字幕


    try:
        print (key+"---"+value)
        # print 输出的时候有时候会碰到很奇怪的 gbk codec 无法编码问题..
    except:
        pass
    
# ==(end) 8. 正式开始替换了 ==






# ==(start) 9. 保存和关闭文件 ==


split_file.close()
# 关闭[分词文件] (就是那个一堆单词的文件)


subs.save(need_split_path)
# 保存字幕文件的修改操作


# ==(end) 9. 保存和关闭文件 ==






# 事情做完了, 提醒一下用户

print ('')
print ("一共有 " + str(len(sw)) + "对 替换词")
print ("we have " + str(len(sw)) + "pair 'replace word'")

print ('-------------------------------')
print ( sys.argv[1] + "  分词完成")
print ( sys.argv[1] + "  split word is done")
print ('-------------------------------')





