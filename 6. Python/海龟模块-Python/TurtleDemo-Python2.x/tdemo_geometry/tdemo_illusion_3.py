"""       turtle-example-suite:

           tdemo_illusion_3.py

A simple drawing suitable as a beginner's
programming example.

This version makes the turtle have a
rectangular shape and uses the stamp()
command to draw rectangles.

The perpendicular lines that do not match
row to row create an illusion of the lines
between them being not parallel.

Inspired by NetLogo's model of optical
illusions.
"""

from turtle import *

def main():
    bgcolor("gray60")

    pu()
    speed(0)
    ht()
    shape("square")
    shapesize(3.2, 3.5)

    shift = [10, 0, 10, 28,
             10, 0, 10, 28, 10]

    tracer(False)
    for i in range(9):
        goto(-365 + shift[i], 267-66*i)
        color("black")
        for i in range(11):
            stamp()
            fd(70)
            if pencolor() == "white":
                color("black")
            else:
                color("white")
    tracer(True)
    return "DONE!"

if __name__ == "__main__":
    msg = main()
    print(msg)
    mainloop()


