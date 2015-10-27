
'''
注意: 程序运行路径中不能有中文

一句话总结: 删(auto), 加数字前缀.

程序用于批量重命名 Crash Course 自动字幕的文件名.
例子在下面.
本程序需要和 Youtube Auto Subtitle Downloader 搭配使用.
( http://userscripts.org/scripts/show/168581 )




input:  (auto)Calorimetry- Crash Course Chemistry #19.srt
output:   19. Calorimetry- Crash Course Chemistry #19.srt

input:  (auto)Nuclear Chemistry- Crash Course Chemistry #38.srt
output:   38. Nuclear Chemistry- Crash Course Chemistry #38.srt


[Usage]
2. Double click this .py file.

'''


import glob # for get filename.
import os   # for rename file.


filename_list = glob.glob("(auto)*.mp4")


for filename in filename_list:
    try:
        number = filename.split("#")[1].split(".")[0]
        # get the number.
            
        new_filename = number + ". " + filename.replace("(auto)", "")
        # get new file name.
            
        os.rename(filename, new_filename)
        # rename file.
    except:
        print ("Fail rename: " + filename)


