# 第四关是让你去抓去问题里的数字，然后继续访问链接。。
# 跑了几百次之后得到peak.html

import urllib.request
import re


a = urllib.request.urlopen("http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=6711")
data = a.read()

# 把bytes转换成str
str1 = bytes.decode(data)

# 用正则匹配网页代码中的5个数字
listvalue = re.findall("\d+",str1)
strvalue = "".join(listvalue)

# 如果能抓到值就一直循环..
while strvalue != "":
    a = urllib.request.urlopen("http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=%s" % strvalue)
    data = a.read()

    # 把bytes转换成str
    str1 = bytes.decode(data)

    listvalue = re.findall("\d+",str1)
    strvalue = "".join(listvalue)
    

    if strvalue == "":
        print ("抓不到网页中的数字值了")
        print ("网页的原文是: %s " % str1)
        print ("于是我们除以2，然后填入nothing,继续爬。。")
        
    else:
        print ("http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=%s" % strvalue)


print ("完成")




























