from __future__ import with_statement
import decimal


def pi_gauss_legendre():
    D = decimal.Decimal
    with decimal.localcontext() as ctx:
        ctx.prec += 2                
        a, b, t, p = 1, 1/D(2).sqrt(), 1/D(4), 1                
        pi = None
        while 1:
            an    = (a + b) / 2
            b     = (a * b).sqrt()
            t    -= p * (a - an) * (a - an)
            a, p  = an, 2*p
            piold = pi
            pi    = (a + b) * (a + b) / (4 * t)
            if pi == piold:  # equal within given precision
                break
    return +pi


decimal.getcontext().prec = 100  #改变这里的数字能够设置小数点后的值
print pi_gauss_legendre()

#http://stackoverflow.com/questions/347734/gauss-legendre-algorithm-in-python
#http://zh.wikipedia.org/wiki/%E9%AB%98%E6%96%AF-%E5%8B%92%E8%AE%A9%E5%BE%B7%E7%AE%97%E6%B3%95



