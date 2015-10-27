#!/usr/bin/python
"""       turtle-example-suite:

              tdemo_mill1.py

Demonstrates a user defined 'three winged'
pen. Pen rotates via left() command (as usual).
"""
from turtle import *

def main():
    reset()
    speed(1)
    lt(75)

    # create three-winged shape for
    # new turtle
    begin_poly()
    for i in range(3):
        fd(100)
        if i == 0:
            x=xcor() # turtle 'measures' length of
                     # half basis of triangle
        lt(105)
        fd(2*x)
        lt(105)
        fd(100)
        rt(90)
    end_poly()
    register_shape('mill', get_poly())

    # the mill
    reset()
    shape('mill')
    resizemode("user")
    turtlesize(outline=5)
    speed(1)
    lt(90)
    pu()
    bk(120)
    pd()
    pensize(20)
    pencolor("blue")
    fd(180)
    
    # the wheel ...
    pu()
    color("green","red")
    # .. rotates
    anglevel=3.6
    speed(5)
    for i in range(360):
        lt(anglevel)
        anglevel-=0.0098
    return "Done!"

if __name__ == '__main__':
    msg = main()
    print(msg)
    mainloop()
