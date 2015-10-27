import platform


print (platform.machine() )    # 获取电脑类型,比如"i386"
print (platform.node() )    # 获取机器名
print (platform.platform())    #获取操作系统版本

print (platform.architecture()) # 得到是32位还是64位
print (platform.win32_ver())  # ('XP', '5.1.2600', 'SP3', 'Multiprocessor Free')
print (platform.system())  # 返回操作系统类型, 此例中返回的是:Windows

print (platform.python_version_tuple() )  # 返回python的版本,以元组形式
print (platform.python_version() )  # 返回python的版本, 以字符串形式


print (platform.processor() )  # 返回CPU的名称,如果不能确定值,就返回空字符串
'''

x86 Family 6 Model 28 Stepping 2, GenuineIntel
Family 家用 
Model 类型、样式 
Stepping级别 
GenuineIntel 英特尔的商标

'''

























