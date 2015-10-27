#!/usr/bin/python
"""       turtle-example-suite:

            tdemo_mill1.py

Demonstrates a user defined 'three winged'
pen. Pen rotates via left() method AND
moves via setpos() method.
Pensize changes via turtlesize() method.

Be patient. (You migkht want to enlarge your
xturtleDemo window or use the canvas'
scrollbars to search for the wheel.)
"""
from turtle import *
from time import clock

WINGSIZE = 135

def main():
    reset()
    ht()
    tracer(0)
    lt(75)
    pu()
    fd(WINGSIZE)
    x,y=pos()
    bk(WINGSIZE)
    pd()

    begin_poly()
    for i in range(3):
        fd(WINGSIZE)
        lt(105)
        fd(2*x)
        lt(105)
        fd(WINGSIZE)
        rt(90)
    end_poly()
    mill=get_poly()
    register_shape('mill', mill)

    reset()
    lt(90)
    pu()
    fd(60)
    pd()
    pensize(20)
    color("blue", "yellow")
    rt(15)
    begin_fill()
    bk(WINGSIZE*1.2)
    rt(75)
    fd(2*x*1.2)
    lt(105)
    fd(WINGSIZE*1.2)
    end_fill()
    ht()


    p=Turtle()
    p.ht()
    p.pu()
    p.shape('mill')
    p.resizemode("user")
    p.turtlesize(outline=3)
    p.fillcolor("red")
    p.lt(90)
    p.fd(60)
    p.st()
    tracer(True)
    p.speed(10)

    ta = clock()
    anglevel = 2
    for i in range(180):
        p.lt(anglevel)

    tb = clock()
    sizefactor = 1
    vel = 1
    for i in range(200):
        anglevel += .3
        p.lt(anglevel)
        if i > 60:
            sizefactor *= 0.985
            vel *=1.01
            x,y = p.pos()
            p.setpos(x+vel,y+vel)
            p.turtlesize(sizefactor)
    tc = clock()
    return "Runtime: %.1fsec. / %.1fsec." % (tb-ta, tc-tb)

if __name__ == '__main__':
    msg = main()
    print(msg)
    mainloop()    

## on my laptop: 6 sec. / 12.4 sec
