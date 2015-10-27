"""       turtle-example-suite:

           tdemo_illusion_5.py

This script uses more advanced features
of the turtle module: Compound shapes,
that are sheared and tilted. (Naturally
a simpler solution using elemtary turtle
graphics commands only is possible.)

Circles of diamonds seem to rotate
if you focus your eyes on their center.

Inspired by NetLogo's model of optical
illusions.
"""
from turtle import *

def main():
    diamondshape = Shape("compound")
    poly1 = ((-7,-7), (7,-7), (7,7), (7,-7))
    diamondshape.addcomponent(poly1, "black")
    poly2 = ((-7,-7), (-7,7), (7,7), (-7,7))
    diamondshape.addcomponent(poly2, "white")
    register_shape("diamond", diamondshape)

    bgcolor("gray55")
    shape("diamond")
    shearfactor(0.3)
    pu()
    ht()

    tracer(False)
    left(90)
    for _ in range(40):
        fd(160)
        stamp()
        bk(160)
        rt(9)
    tilt(-73.3)
    for _ in range(32):
        fd(125)
        stamp()
        bk(125)
        rt(11.25)
    dot(12)

    goto(0, -270)
    write("Stare at the dot, "
          "then lean forward and back!",
          align="center",
          font=("Courier",14,"bold"))
    tracer(True)
    return "DONE!"

if __name__ == "__main__":
    msg = main()
    print(msg)
    mainloop()
