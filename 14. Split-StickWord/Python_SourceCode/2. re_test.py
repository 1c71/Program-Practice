# encoding = utf-8

import re
import doctest


'''
doctest这个模块用来测试程序, 下面这几个函数里写的注释就是用来测试的

如果你想弄懂doctest的相关东西.
建议去看 Coursera 的 Learn to Program: Crafting Quality Code
https://class.coursera.org/programming2-001/lecture/index

看 Week2 的 Completed Testing Automatically Using doctest (6:47) 就行了.
'''





# 逗号后面如果有英文字母, 那么加个空格
def test_Comma(string):
    '''
    >>> test_Comma('but,i')
    'but, i'
    
    >>> test_Comma('$80,000')
    '$80,000'
    '''
    p = re.compile(r'(\,)([a-zA-z])')
    return p.sub(r'\1 \2', string)




# 数字前面或后面如果有英文字母, 那么加个空格
def test_Number(string):
    '''
    >>> test_Number('$11,000')
    '$11,000'
    
    >>> test_Number('i have $80,000dollor')
    'i have $80,000 dollor'
    
    >>> test_Number('you got150pound?')
    'you got 150 pound?'
    '''
    Front = re.compile(r'([a-zA-Z])([0-9])')
    Behind = re.compile(r'([0-9])([a-zA-Z])')
    f = Front.sub(r'\1 \2', string)
    b = Behind.sub(r'\1 \2', f)
    return b



# 句号后面如果有字母或数字, 那么给句号后面加上一个空格
def test_Period(string):
    '''
    >>> test_Period('egg.that')
    'egg. that'
    
    >>> test_Period('oh.....crap')
    'oh..... crap'
    '''
    p = re.compile(r'(\.)([a-zA-Z]|[0-9])')
    return p.sub(r'\1 \2', string)










# 注意下面这句...
doctest.testmod()


# 如果程序啥也没输出, 说明一切正常




