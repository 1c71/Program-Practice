'''
这个程序可以遍历当前整个文件夹里的每个文件，
删掉文件名里的特定字符串。
你只需要替换 <something you want delete> 变成你想删除的字符串即可.

'''
import glob 
import os   



filename_list = glob.glob("*")


for filename in filename_list:
    try:
        new_filename = filename.replace("<something you want delete>", "")  
        os.rename(filename, new_filename)
    except:
        print ("rename " + filename + " fail.")


print ("yeah")







