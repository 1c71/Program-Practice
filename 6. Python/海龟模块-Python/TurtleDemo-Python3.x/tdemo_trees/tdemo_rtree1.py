#!/usr/bin/python
"""      turtle-example-suite:

            tdemo_rtree1.py

Displays a 'breadth-first-tree' - in contrast
to the classical Logo tree drawing programs,
which use a depth-first-algorithm.

Uses turtle-cloning: At each branching point the
current turtle is cloned. 
"""
from turtle import Turtle, Screen
from time import clock

screen = Screen()

def tree(plist, l, a, f):
    """ plist is list of turtles
    l is length of branch
    a is half of the angle between 2 branches
    f is factor by which branch is shortened
    from level to level.
    """
    for p in plist:
        p.forward(l)
    if l > 5:
        lst = []
        for p in plist:
            q = p.clone()
            p.left(a)
            q.right(a)
            lst.append(p)
            lst.append(q)
        tree(lst, l*f, a, f)
    
def maketree():
    p = Turtle(shape="triangle", visible=False)
    p.setundobuffer(None)
    p.fillcolor("green")
    p.shapesize(0.4)
    p.speed(0)
    p.left(90)
    p.penup()
    p.backward(210)
    p.pendown()
    tree([p], 200, 65, 0.6375)

def main():
    screen.tracer(30,0)
    a=clock()
    maketree()
    b=clock()
    screen.tracer(True)
    for t in screen.turtles():
        t.showturtle()
    print(len(screen.turtles()))
    return "done: {0:.2f} sec.".format(b-a)

if __name__ == "__main__":
    msg = main()
    print(msg)
    screen.mainloop()
