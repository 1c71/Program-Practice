
import urllib2
import pickle


#根据网页提示要到此地址下载文件。
handle=urllib2.urlopen("http://www.pythonchallenge.com/pc/def/banner.p")

data=pickle.load(handle)

handle.close()


see_easy = open("5_result.txt",'a')

buf = ''

for line in data:

    for char in line:

        buf += char[0]*char[1]

    sebuf = ''

    see_easy.write( buf +'\n')

    buf =''






