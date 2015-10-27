"""       turtle-example-suite:

           tdemo_illusion_1.py

A simple drawing suitable as a beginner's
programming example.

This script uses user defined coordinates
in a way that the intersection points of
the lines have integer coordinates. 
Stamps squares and circles.

White circles on a gray background produce
an illusion of the circles changing colors
between black and white, depending on
where you focus your eyes.

Inspired by NetLogo's model of optical
illusions.
"""

from turtle import *

def main():
    setup(800, 600)
    bgcolor("gray60")
    setworldcoordinates(-4.4, -3.3, 4.4, 3.3)
    ht()
    pu()
    tracer(False)
    color("black")
    shape("square")
    shapesize(3.4)
    for col in range(-5, 5):
        for row in range(-4, 4):
            goto(col+0.5, row+0.5)
            stamp()
    color("white")
    shape("circle")
    shapesize(1.6)
    for col in range(-5, 5):
        for row in range(-4, 4):
            goto(col, row)
            stamp()
    tracer(True)
    return "DONE!"

if __name__ == "__main__":
    msg = main()
    print(msg)
    mainloop()
    
