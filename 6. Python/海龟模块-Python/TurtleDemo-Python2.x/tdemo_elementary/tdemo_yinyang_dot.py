#!/usr/bin/python
"""        turtle-example-suite:

           tdemo_yinyang_dot.py

Another drawing suitable as a beginner's
programming example.

The small circles are drawn by the dot
command. For an alternative solution
using the circle command see example
yinyang_circle.

"""

from turtle import *

def yin(radius, color1, color2):
    width(3)
    color(color1)
    begin_fill()
    circle(radius/2., 180)
    circle(radius, 180)
    left(180)
    circle(-radius/2., 180)
    end_fill()
    color(color2)
    left(90)
    up()
    forward(radius/2.)
    dot(radius/4.)
    back(radius/2.)
    down()
    left(90)

def yinyang(radius, color1, color2):
    yin(radius, color1, color2)
    yin(radius, color2, color1)

def main():
    reset()
    speed(0)
    hideturtle()
    bgcolor(.4,.1,0)
    yinyang(200, "blue", "yellow")
    hideturtle()
    return "Done!"

if __name__ == '__main__':
    main()
    mainloop()
