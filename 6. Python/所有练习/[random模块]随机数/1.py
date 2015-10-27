# -*- coding: gb2312 -*- 

import random, string



#print random.randint(1,29)
# 生成一个该范围内的随机数


#print random.randrange(0,30,5)
# 随机出一个范围内的数，以第三个参数为步进,也就是只能取0,5,10,15,20,25,30这几个值，


#print random.random()
# 生成0到1之间的浮点随机数, 注意, 不能传参数


#print random.uniform(1,20)
# 生成1到20之间的浮点随机数



#print '随机生成的字符(a~z)：%c' %random.choice('abcdefghijklmnopqrstuvwxyz')
#print '随机生成的字符串(春、夏、秋、冬)：%s' %random.choice(['spring', 'summer',
#'fall', 'winter'])
# 随机从字符串中选择一个字符, 或是从列表中选择一个元素#





print random.sample('abcdefghijklmnopqrstuvwxyz', 4)
# 从字符串中随机选择4个字符，以列表方式返回
# 例如: ['e', 'y', 'u', 'f'] 





'''
print '随机生成的字符串：%s' % string.join(
    random.sample('abcdefghijklmnopqrstuvwxyz', 4), '')
'''
# 随机生成一个 4个字符 的字符串

#join将一个字符串列表中的各个字符串连接起来，中间插入指定的字符串














