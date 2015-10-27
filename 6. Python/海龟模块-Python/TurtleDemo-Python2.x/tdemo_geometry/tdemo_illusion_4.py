"""       turtle-example-suite:

           tdemo_illusion_4.py

A simple drawing suitable as a beginner's
programming example.

Relative sizes of other circles skew the
perception of the middle circles, creating
an illusion of difference in size.

Inspired by NetLogo's model of optical
illusions.
"""

from turtle import *


def circlepattern(r1, d, r2):
    dot(2*r1)
    left(30)
    R = r1 + d + r2
    for i in range(6):
        fd(R)
        dot(2*r2)
        bk(R)
        left(60)
    right(30)

def main():
    bgcolor("black")
    ht()
    pu()
    color("white")

    tracer(False)
    bk(200)
    circlepattern(36, 3, 16)
    fd(300)
    circlepattern(36, 20, 56)

    goto(0, -270)
    pencolor("white")
    write("Which inner circle is bigger?",
          align="center",
          font=("Courier",14,"bold"))
    tracer(True)

    return "DONE!"

if __name__ == '__main__':
    msg = main()
    print(msg)
    mainloop()    
