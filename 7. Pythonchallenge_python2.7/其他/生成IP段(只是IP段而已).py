
# 版本: Python2.7
# 日期: 2013-7-2 更新




ip_file = file('python-ip-segment.txt', 'w')



'''
range函数文档地址: http://docs.python.org/2/library/functions.html#range

range(起始值, 结束值, 差值)

每次循环都是拿 起始值+差值, 到了结束值之后就停止..

最后输出的列表不包括结束值
例子不写了, 文档地址里有.

'''


'''
>>> range(254,0,-1)
[254, 253, ...... 3, 2, 1]
不包括0
'''


for IP1 in range(254,0,-1):
    for IP2 in range(254,0,-1):
    #for IP3 in range(254,0,-1):
        #for IP4 in range(254,0,-1):
            #print IP1,IP2
        abc= '%s.%s.%s - %s.%s.%s\n' % (IP1,IP2,"1.1",
                               IP1,IP2,"255.255")
        ip_file.write(abc)





ip_file.close()
# 关闭文件




























