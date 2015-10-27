

# python3中可运行
import string
str1="""g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp.
bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle
qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."""

str2="abcdefghijklmnopqrstuvwxyz"
str3="cdefghijklmnopqrstuvwxyzab"


a = str1.maketrans(str2,str3)
print (str1.translate(a))
print ("-------------------------------------")
print ("map".translate(a))
