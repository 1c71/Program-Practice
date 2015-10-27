
'''
注意: 程序运行路径中不能有中文

【说明】:
程序仅用于批量重命名 Crash Course 美国历史的[.mp4视频文件]和[.srt完整字幕文件]
程序会给文件加上数字前缀.
除此之外其他地方不会有修改.
仅仅只是加数字前缀而已.

The Rise of Conservatism- Crash Course US History #41.mp4
会变成: 41. The Rise of Conservatism- Crash Course US History #41.mp4


(English)The 1960s in America- Crash Course US History #40.srt
会变成: 40. (English)The 1960s in America- Crash Course US History #40.srt


---------------------------------------------------------------------

【Explanation】
This program only for Crash Course.
Program will rename .mp4 file and .srt file.


【Rename Example】
input:       The Rise of Conservatism- Crash Course US History #41.mp4
output:  41. The Rise of Conservatism- Crash Course US History #41.mp4

input:       The Cold War in Asia- Crash Course US History #38.mp4
output:  38. The Cold War in Asia- Crash Course US History #38.mp4

input:      (English)Civil Rights and the 1950s- Crash Course US History #39.srt
output: 39. (English)Civil Rights and the 1950s- Crash Course US History #39.srt


【Usage】
1. Double click this file. (you need install python3.3)
2. just wait.

'''


##############################
#
# error handler
# 错误处理
#
##############################
def exit_handler():
    print ("Press [Enter] Exit.")
    input('')
import atexit
atexit.register(exit_handler)
# 告诉程序在退出前执行这个函数, 即便程序出错时它也是可以运行的







##############################
#
# import module
# 导入所需模块
#
##############################
import glob # for get filename.
import os   # for rename file.







##############################
#
# process .mp4 file
# 处理mp4文件
#
##############################

filename_list = glob.glob("[a-zA-Z]*.mp4")
# 这个正则的意思是: 把第一个字母是英文字母, 而且后缀是mp4的文件全挑出来.

# Civil Rights and the 1950s- Crash Course US History #39.mp4
# 上面这个能通过

# 38. The Cold War in Asia- Crash Course US History #38.mp4
# 上面这个不能通过

# 这样的话, 已被重命名过的文件就不会再被重命名一次.

for filename in filename_list:
    try:
        number = filename.split("#")[1].split(".")[0]
        # 拿到数字, 比如 Civil Rights and the 1950s- Crash Course US History #39.mp4 最后的那个39
        new_filename = number + ". " + filename
        # 拼接新文件名 [数字][.][一个空格][原文件名]
        os.rename(filename, new_filename)
        # 真正重命名文件的是这一行代码.
    except:
        print ("Fail rename: " + filename)





##############################
#
# process .srt file
# 处理srt完整字幕
#
##############################
filename_list = glob.glob("*.srt")
for filename in filename_list:
    try:
        if filename.startswith("(English)"):
            # 如果文件名以 (English) 开头, 那么说明是完整字幕. 我们这里不处理自动字幕.
            
            number = filename.split("#")[1].split(".")[0]
            # 拿到原文件名最后的数字

            new_filename = number + ". " + filename
            # 拼接出新文件名 (注意此时还没有重命名文件, 只是拼接出新文件名而已)

            os.rename(filename, new_filename)
            # 真正重命名文件的代码是上面这一行
    except:
        print ("Fail rename: " + filename)






##############################
#
# told user program finish running.
# 告诉用户程序运行完成
#
##############################
print("Everything done.")
print("")








