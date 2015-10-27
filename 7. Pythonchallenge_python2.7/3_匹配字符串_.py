import urllib.request
import re

urldata=urllib.request.urlopen("http://www.pythonchallenge.com/pc/def/equality.html")

geturldata=urldata.read()

a = re.findall("[^A-Z][A-Z]{3}[a-z][A-Z]{3}[^A-Z]", str(geturldata))
# 不以大写字母开头的一个字符，然后是3个大写字符，1个小写字符，再3个大写字符，最后1个字符不是大写字母
print (a)

# 把匹配出来的列表形式答案的每第4个字符拼合起来
print("".join(c[4] for c in a) )


# 合在一起就是:
# print ("".join(c[4] for c in re.findall("[^A-Z][A-Z]{3}[a-z][A-Z]{3}[^A-Z]", str(geturldata)))  )
