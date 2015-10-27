

# 这是要替换的字符串
s = '{a1} error {a2} error1 {a3}'


# 替换的目标字符串
dic = {
    'a1':'apple',
    'a2':'orange',
    'a3':'water'
    }

# 期待输出:
# apple error orange error1 water

import re

for key, value in dic.items():
    s = re.sub(r'{'+key+'}', value, s)


print (s)






