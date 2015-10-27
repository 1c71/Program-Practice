"""      turtle-example-suite:

        tdemo_recursive squares.py

This program draws a recursive pattern of
coloured squares, that have smaller squares
at their vertices. To each square size
belongs a different colour.

The squares are stamped, the larger ones
first, the smaller ones upon them.

Finally you see 5461 squares.
"""
from turtle import Turtle, Screen
from time import clock

colors = ["red", "green", "blue", "yellow",
          "cyan", "magenta", "gray60"]

def recsquare(l, f, colors):
    if not colors: return
    t.shapesize(l/20)
    t.color(colors[0])
    t.stamp()
    t.fd(l/2.0)
    t.lt(90)
    t.fd(l/2)
    t.lt(90)
    for _ in range(4):
        recsquare(l*f, f, colors[1:])
        t.fd(l)
        t.lt(90)
    t.rt(90)
    t.bk(l/2)
    t.rt(90)
    t.bk(l/2)
    if len(colors) == 5:
        s.update()

def main():
    global s, t
    s = Screen()
    s.bgcolor("gray10")
    t = Turtle(visible=False, shape="square")
    t.pu()
    t.speed(0)
    s.tracer(False)
    ta = clock()
    recsquare(256, 0.5, colors)
    tb = clock()
    return "{0:.2f}sec.".format(tb-ta)

if __name__ == "__main__":
    main()
    s.mainloop()
