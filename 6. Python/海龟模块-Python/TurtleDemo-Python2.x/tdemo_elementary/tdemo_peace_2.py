#!/usr/bin/python
"""         turtle-example-suite:

              tdemo_peace_2.py

A very simple drawing suitable as a beginner's
programming example. (Scaled up to graphics
window size)

Uses only commands, which are also available in
old turtle.py.

Intentionally no variables are used except for the
colorloop:
"""

from turtle import *

F = 1.32

def main():
    peacecolors = ("red3",  "orange", "yellow",
                   "seagreen4", "orchid4",
                   "royalblue1", "dodgerblue4")
    reset()
    up()
    goto(-320*F,-195*F)
    width(70*F)

    for pcolor in peacecolors:
        color(pcolor)
        down()
        forward(640*F)
        up()
        backward(640*F)
        left(90)
        forward(66*F)
        right(90)

    width(25*F)
    color("white")
    goto(0,-170*F)
    down()

    circle(170*F)
    left(90)
    forward(340*F)
    up()
    left(180)
    forward(170*F)
    right(45)
    down()
    forward(170*F)
    up()
    backward(170*F)
    left(90)
    down()
    forward(170*F)
    up()

    goto(0,300*F) # vanish if hideturtle() is not available ;-)
    return "Done!!"

if __name__ == "__main__":
    main()
    mainloop()
