


#python 2.7中需要导入string,并且用法稍有不同
import string


str1="""g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp.
bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle
qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."""

str2="abcdefghijklmnopqrstuvwxyz"
str3="cdefghijklmnopqrstuvwxyzab"


table = string.maketrans(str2,str3)


print (str1.translate(table,''))
# 第二个参数是”deletechars“, 如果给了这个参数，在转换前先把字符串里与他相同的字母删掉

#大概意思就是，如果调用translate函数的时候给出了deletechars这个参数，
#先把deletechars里面的存在的字母从字符串S里面删除，然后再把字符数过滤。

print ("-------------------------------------")
print ("map".translate(table,''))



'''

案例：
>>> import string
>>> table = string.maketrans('ab','AB')
>>> s = 'lovedboy.tk'
>>> s1 = s.translate(table,'')
>>> s1
'lovedBoy.tk'
>>> s2 = s.translate(table,'.tk')
>>> s2
'lovedBoy'


'''






































