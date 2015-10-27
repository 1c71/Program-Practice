


# 在Python中，我们可以创建一个类来存储和获得向量
#（虽然向量的写法很像一个元组，但因为向量有很多种计算，必须使用类来完成）：




class Vector2(object):

    def __init__(self, x=0.0, y=0.0):
        self.x = x
        self.y = y

    def __str__(self):
        return "(%s, %s)"%(self.x, self.y)
 
    @classmethod
    def from_points(cls, P1, P2):
        return cls( P2[0]-P1[0], P2[1]-P1[1] )


#向量的大小可以简单的理解为那根箭头的长度，勾股定理熟稔的各位立刻知道怎么计算了
    def get_magnitude(self):
        return math.sqrt( self.x**2 + self.y**2 )



'''
在向量的大家族里，有一种比较特殊的向量叫“单位向量”，意思是大小为1的向量，
我们还能把任意向量方向不变的缩放（体现在数字上就是x和y等比例的缩放）到一个单位向量，
这叫向量的规格（正规）化，代码体现的话：
'''
#使用过normalize方法以后，向量就成了一个单位向量。
    def normalize(self):
        magnitude = self.get_magnitude()
        self.x /= magnitude
        self.y /= magnitude


# 这2个是向量的加法和减法重载
# 两个下划线“__”为首尾的函数，在Python中一般就是重载的意思
    def __add__(self, rhs):
        return Vector2(self.x + rhs.x, self.y + rhs.y)
    def __sub__(self, rhs):
        return Vector2(self.x - rhs.x, self.y - rhs.y)



# 有加减法，那乘除法呢？当然有！不过向量的乘除并不是发生在两个向量直接，
# 而是用一个向量来乘/除一个数，
# 其实际意义就是，向量的方向不变，而大小放大/缩小多少倍。如下图：

    def __mul__(self, scalar):
        return Vector2(self.x * scalar, self.y * scalar)
    def __div__(self, scalar):
        return Vector2(self.x / scalar, self.y / scalar)






#我们可以使用下面的方法来计算两个点之间的向量
A = (10.0, 20.0)
B = (30.0, 35.0)
AB = Vector2.from_points(A,B)
print AB



#网上有别人写好的gameobject. 现成的库























