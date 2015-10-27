from turtle import *


'''
def f(length, depth):
   if depth == 0:
     forward(length)
   else:
     f(length/3, depth-1)
     right(60)
     f(length/3, depth-1)
     left(120)
     f(length/3, depth-1)
     right(60)
     f(length/3, depth-1)

f(500, 4)
'''


# 非递归实现
def snowflake(length):
    yield length/3
    right(60)
    yield length/3
    left(120)
    yield length/3
    right(60)
    yield length/3

for a in snowflake(400):
    for b in snowflake(a):
        forward(b)




















