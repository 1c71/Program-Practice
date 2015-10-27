'''

mystr[x:y:z]

第一个参数 x表示开始位置
第二个参数 y表示终止位置
第三个参数 z表示步长

如果 x,y,z是正数表示从左边开始计数
x,y,z为负数表示从右边开始数

# 如果第三位为负数，要从后往前数，第一位不写表示从末尾开始数，第二位不写表示数到头
>>> s[:3:-1]
'gnirt'
>>> s[3::-1]
's ym'

'''

def reverse(string): 
    return string[::-1]

print reverse("o2YG87RQXKw3COflBT6ViDxIazb?/ziuq/moc.oaboat.deu//:ptth")
print reverse("w2YPYrQTXKw3COfltG6d62wMK2b?/ziuq/moc.oaboat.deu//:ptth")
s = raw_input("input string: ")
print reverse(s)
