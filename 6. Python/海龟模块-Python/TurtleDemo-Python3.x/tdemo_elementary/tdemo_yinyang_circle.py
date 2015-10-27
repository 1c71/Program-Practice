#!/usr/bin/python
"""       turtle-example-suite:

         tdemo_yinyang_circle.py

Another drawing suitable as a beginner's
programming example.

The small circles are drawn by the circle
command.

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
    forward(radius*0.375)
    right(90)
    down()
    begin_fill()
    circle(radius*0.125)
    end_fill()
    left(90)
    up()
    backward(radius*0.375)
    down()
    left(90)

def main():
    reset()
    yin(200, "red", "green")
    yin(200, "green", "red")
    ht()
    return "Done!"

if __name__ == '__main__':
    main()
    mainloop()
