class a:
    a='aaaa'

class b(a):
    b='bbb'

class c:
    c='ccc'

c.__bases__ += (a,)
print c.a
print c.__bases__
