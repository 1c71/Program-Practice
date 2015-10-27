"""       turtle-example-suite:

           tdemo_illusion_2.py

A simple drawing suitable as a beginner's
programming example.

Diagonals moving away from the center create
an illusion of depth, which makes the parallel
horizontal lines seem to bend in the center.

Inspired by NetLogo's model of optical
illusions.
"""
from turtle import *

def main():
    tracer(False)
    ht()
    speed(0)
    pensize(2)
    lt(90)
    for i in range(30):
        pu()
        bk(500)
        pd()
        fd(1000)
        pu()
        bk(500)
        lt(6)
    dot(60)

    pensize(16)
    fd(53)
    rt(90)
    bk(400)
    pd()
    fd(800)
    pu()
    bk(400)
    lt(90)
    bk(106)
    rt(90)
    bk(400)
    pd()
    fd(800)
    pu()
    bk(400)
    lt(90)
    fd(330)
    pencolor("red")
    write("Are the thick lines parallel?",
          align="center",
          font=("Courier",24,"bold"))
    tracer(True)
    return "DONE!"

if __name__ == "__main__":
    msg = main()
    print(msg)
    mainloop()
