"""       turtle-example-suite:

           tdemo_graviturtle.py

Very simple prototype of a gravitational
system consisting of a central body and
an orbiting turtle.

Demonstrates specifically the use of the
Vec2D class and corresponding properties
of turtles for doing vector calculations.

An only little more sophisticated approach
is used by the other gravitation examples.
"""
from turtle import *

def main():
    color("orange")
    dot(10)
    center = pos()
    color("blue")
    shape("turtle")
    speed(0)
    pu(); goto(200,0); pd()

    G = 800
    v = Vec2D(0, 1)
    t = 0
    dt = 1
    while t < 1100:
        goto(pos() + v*dt)
        setheading(towards(center))
        r = distance(center)
        acc = (-G/r**3)*pos()
        v = v + acc*dt
        t = t + dt
    return "DONE!"

if __name__ == "__main__":
    msg = main()
    print(msg)
    mainloop()   
    
    
    
        
