#!/usr/bin/python
"""       turtle-example-suite:

          tdemo_sierpinski2.py

This program draws a coloured sierpinski
triangle. This version draws the small
filled triangles by stamping a triangle
shaped turtle

Each vertex of the triangle is associated
with a color - in the case of this example
red, green and blue. The colors of the
triangular cells of the Sierpinski triangle
are computed by interpolation.
"""

from turtle import *
from time import clock

class Vec3(tuple):   #######  rudimentary, just as needed
    def __new__(cls, x, y, z):
        return tuple.__new__(cls, (x, y, z))
    def __add__(self, other):
        return Vec3(self[0]+other[0], self[1]+other[1], self[2]+other[2])
    def __truediv__(self, other):
        other = float(other)
        return Vec3(self[0]/other, self[1]/other, self[2]/other)

def triangle(laenge, stufe, f1, f2, f3):  # f1, f2, f3 colors of the vertices
    if stufe == 0:
        color((f1+f2+f3)/3)
        stamp()
    else:
        c12 = (f1+f2)/2
        c13 = (f1+f3)/2
        c23 = (f2+f3)/2
        fd(laenge)
        triangle(laenge/2, stufe-1, c13, c23, f3)
        bk(laenge)
        left(120)
        fd(laenge)
        triangle(laenge/2, stufe-1, c12, c13, f1)
        bk(laenge)
        lt(120)
        fd(laenge)
        triangle(laenge/2, stufe-1, c23, c12, f2)
        bk(laenge)
        left(120)

def main():
    setup(640, 640)
    mode("logo")
    reset()
    setundobuffer(1)
    colormode(255)
    ht()
    pu()
    speed(0)
    shape("triangle")
    sierp_size = 600
    h3 = (sierp_size/6.0)*3**0.5

    depth = 6
    shapesize(sierp_size/20./(2**depth))
    tracer(1,0)
    bk(h3/2.0)
    ta = clock()
    triangle(h3, depth,
            Vec3(255.0,0,0), Vec3(0,255.0,0), Vec3(0,0,255.0))
    tracer(1)
    tb = clock()
    return "{0:.2f} sec.".format(tb-ta)

if __name__ == '__main__':
    msg = main()
    print(msg)
    mainloop()

## on my desktop-machine: approx. 0.6 sec.
