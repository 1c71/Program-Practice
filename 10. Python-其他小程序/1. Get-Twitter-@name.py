# 程序用于获取Twitter用户名

s1 = '''
RT @EMCPROVEN: Extreme Cert Challenge for Presales Partners - Conference Winners FINAL
'''
# 期待输出： EMCPROVEN

s2 = '''
@realist_thaps: Whoa! Trying? RT @justinbieber: trying to get to South Africa!" Trying
'''
# 期待输出: realist_thaps, justinbieber

s3 = '''
The sounds of metal cleats on concrete! (via @BaseballBliss)
'''
# 期待输出: BaseballBliss

s4 = '''
@ionthegeek is the wrist band for the Elect or for the ecn part ?
'''
# 期待输出: ionthegeek

#------------------------------------------------------------

import re


result = re.findall(r'@[\w]+', s4)
# 提取s4中的用户名
# re.findall方法返回的是列表
# print (result)     # 你可以输出结果看看



for index,value in enumerate(result):
    result[index] = value.replace('@', '')
# 只提取名字的话,就把@符号去掉
# print (result)















