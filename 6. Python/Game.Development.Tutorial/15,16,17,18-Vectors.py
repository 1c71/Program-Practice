# 他说这是3D基础什么的。。

#运行不正常。。

import math

class vector(object):

     def __init__(self, list1, list2):
          self.diff=(list2[0]-list1[0], list2[1]-list1[1])
          print self.diff


     # 返回计算出的三角形的斜边长度
     def distance(self):
          self.a=self.diff[0]
          self.b=self.diff[1]
          return math.sqrt(self.a**2 + self.b**2)


     # 
     def unit(self):
          distance = self.distance()
          self.aunit=self.a/distance
          self.bunit=self.b/distance
          return self.aunit, self.bunit

     def add(self,one,two):
          self.sum=(one[0]+two[0]), one[1]+two[1]
     

          

a = (20.0, 25.0)
b = (45.0, 65.0)
thing = vector(a,b)
thing.distance()
thing.unit()
vector1=(20,20)
vector2=(-10,10)
print "the sum is ", thing.add(vector1, vector2)

          
          
