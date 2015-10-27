#!/usr/bin/python
"""      turtle-example-suite:

        tdemo_tree2_generator.py

Displays a 'breadth-first-tree' - in contrast
to the classical Logo tree drawing programs,
which use a depth-first-algorithm.

Uses:
(1) Turtle-cloning: At each branching point the
current turtle is cloned. 
(2) a tree-generator, where the drawing is
quasi the side-effect, whereas the generator
always yields None. This allows for drawing
trees in parallel - sort of 'micro-threads'.

See: tdemo_2rtrees_generators.py
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
        yield p.forward(l)
    if l > 5:
        lst = []
        for p in plist:
            q = p.clone()
            p.left(a)
            q.right(a)
            lst.append(p)
            lst.append(q)
        for x in tree(lst, l*f, a, f):
            yield None
    
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
    for x in tree([p], 200, 65, 0.6375):
        pass

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
