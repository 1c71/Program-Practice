# -*- coding: utf-8 -*-  
import re
import zipfile


#  网上来的代码
# 这一关是要读取文件的commit, 不是向第4关一样一直访问下一个文件.

openzip = zipfile.ZipFile('6_channel.zip', 'r')

firstname = "90052"
char_map = ''


while True:
    filename = firstname + ".txt"

    m_comment = openzip.getinfo(filename).comment

    char_map += m_comment.decode('GB2312')
    
    filedata = openzip.read(filename)

    data = filedata.decode('GB2312')


    
    #先运行过到达46145.txt，留有信息Collect the comments.原来又是字符图画。
    if filename=="46145.txt":
        break
    
    # 从filedata里面匹配下一个文件的数字, 然后又放到filename里面
    firstname = ''.join(re.findall('[0-9]',data))

print (char_map)




















