import math

class Vector2(object):
    def __init__(self, x=0.0, y=0.0):
        self.x = x
        self.y = y
    def __str__(self):
        return "(%s, %s)"%(self.x, self.y)
 
    @classmethod
    def from_points(cls, P1, P2):
        return cls( P2[0] – P1[0], P2[1] – P1[1] )

     
# 向量的大小
# 向量的大小可以简单的理解为那根箭头的长度，勾股定理熟稔的各位立刻知道怎么计算了:
    def get_magnitude(self):
         return math.sqrt( self.x**2 + self.y**2 )


    def normalize(self):
        magnitude = self.get_magnitude()
        self.x /= magnitude
        self.y /= magnitude


#向量运算
        
    def __add__(self, rhs):
        return Vector2(self.x + rhs.x, self.y + rhs.y)
    def __sub__(self, rhs):
        return Vector2(self.x - rhs.x, self.y - rhs.y)


# 向量的乘除并不是发生在两个向量直接，而是用一个向量来乘/除一个数，
# 其实际意义就是，向量的方向不变，而大小[放大/缩小]多少倍。
    def __mul__(self, scalar):
        return Vector2(self.x * scalar, self.y * scalar)
    def __div__(self, scalar):
        return Vector2(self.x / scalar, self.y / scalar)


# 向量的运算被广泛的用来计算到达某个位置时的中间状态，比如我们知道一辆坦克从A到B，
# 中间有10帧，那么很显然的，把步进向量通过(B-A)/10计算出来，
# 每次在当前位置加上就可以了。很简单吧？


     
#我们可以使用下面的方法来计算两个点之间的向量
A = (10.0, 20.0)
B = (30.0, 35.0)
AB = Vector2.from_points(A, B)
print AB
