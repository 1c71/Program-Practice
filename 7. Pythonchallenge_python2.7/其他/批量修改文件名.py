# encoding:utf-8


import os,re


fs = os.listdir(os.getcwd())
# 得到当前目录下的所有文件名



for f in fs:

	#用正则替换
	dirtymatch = re.search('.mp3', f) #第一个参数是匹配模式,第二个是要匹配的字符串
	
	if dirtymatch: # 如果匹配成功
                
		dirtystring = dirtymatch.group(0) # 获得分组信息
		
		newname = f.replace(dirtystring, '') + 'pdf' # 拼接新名字
		# 把文件名里面匹配到的替换成空, 然后+上一个字符串
		
		os.rename(f, newname)  #第1个参数是文件名. 第2个是新的文件名
        
	#注意：可以直接用re.sub方法进行正则替换掉文件名中不需要字符







