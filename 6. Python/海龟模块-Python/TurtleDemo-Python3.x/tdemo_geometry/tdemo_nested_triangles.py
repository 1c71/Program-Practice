"""       turtle-example-suite:

        tdemo_nested triangles.py

This script demonstrates how to use the
turtle as a 'land surveyor', i. e.
how to determine distances and angles
without trigonometical calculations.

Sort of preliminary study to round_dance.
"""
from turtle import *
import time

def main():
    mode("logo")
    shape("triangle")

    # determine shriking factor
    # and angle of rotation
    speed(1)
    forward(100)
    right(150)
    forward(20)
    setheading(towards(0,0))
    right(180)
    # now the turtle is at the tip of 
    # the inscribed triangle with heading
    # in direction of its axis.
    f = distance(0,0)/100  # 0.83282...
    phi = heading()        # 6.89636...
    time.sleep(1)

    # go home
    back(100*f)
    left(phi)
    time.sleep(1)

    # stamp nested triangles
    clear()
    s = 20
    c = 1
    for i in range(20):
        shapesize(s)
        fillcolor(c, 0.5, 1-c)
        stamp()
        s *= f
        c *= f
        right(phi)
    return "DONE!"

if __name__ == "__main__":
    msg = main()
    print(msg)
    mainloop()   
