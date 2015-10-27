#!/usr/bin/python
"""     turtlegraphics-example-suite:

             tdemo_forest.py

Displays a 'forest' of 3 'breadth-first-trees'
similar to the one from example tree.
For further remarks see xtx_tree.py

This example is a 'breadth-first'-rewrite of
a Logo program written by Erich Neuwirth. See:
http://homepage.univie.ac.at/erich.neuwirth/
"""
from turtle import Turtle, Screen
from random import randrange
from time import clock

def symRandom(n):
    return randrange(-n,n+1)

def randomize( branchlist, angledist, sizedist ):
    return [ (angle+symRandom(angledist),
              sizefactor*1.01**symRandom(sizedist))
                     for angle, sizefactor in branchlist ]

def randomfd( t, distance, parts, angledist ):
    for i in range(parts):
        t.left(symRandom(angledist))
        t.forward( (1.0 * distance)/parts )

def tree(tlist, size, level, widthfactor, branchlists, angledist=10, sizedist=5):
    # benutzt Liste von turtles und Liste von Zweiglisten,
    # fuer jede turtle eine!
    if level > 0:
        lst = []
        brs = []
        for t, branchlist in list(zip(tlist,branchlists)):
            t.pensize( size * widthfactor )
            t.pencolor( 255 - (180 - 11 * level + symRandom(15)),
                        180 - 11 * level + symRandom(15),
                        0 )
            t.pendown()
            randomfd(t, size, level, angledist )
            yield 1
            for angle, sizefactor in branchlist:
                t.left(angle)
                lst.append(t.clone())
                brs.append(randomize(branchlist, angledist, sizedist))
                t.right(angle)
        for x in tree(lst, size*sizefactor, level-1, widthfactor, brs,
                      angledist, sizedist):
            yield None


def start(t,x,y):
    t.reset()
    t.speed(0)
    t.hideturtle()
    t.left(90)
    t.penup()
    t.setpos(x,y)
    t.pendown()

def doit1(level, pen):
    pen.hideturtle()
    start(pen, -10, -218)
    t = tree( [pen], 80, level, 0.1, [[ (45,0.69), (0,0.65), (-45,0.71) ]] )
    return t

def doit2(level, pen):
    pen.hideturtle()
    start(pen, -135, -80)
    t = tree( [pen], 120, level, 0.1, [[ (45,0.69), (-45,0.71) ]] )
    return t

def doit3(level, pen):
    pen.hideturtle()
    start(pen, 190, -90)
    t = tree( [pen], 100, level, 0.1, [[ (45,0.7), (0,0.72), (-45,0.65) ]] )
    return t

def doit4(level, pen):
    pen.hideturtle()
    start(pen, -270, -250)
    t = tree( [pen], 60, level, 0.1, [[ (55,0.75), (0,0.73), (-35,0.62) ]] )
    return t

def doit5(level, pen):
    pen.hideturtle()
    start(pen, 265, -280)
    t = tree( [pen], 100, level, 0.1, [[ (10,0.62), (5,0.80), (-10,0.72) ]] )
    return t

# Hier 3 Baumgeneratoren:
def main():
    global screen
    screen = Screen()
    screen.colormode(255)
    p = Turtle()
    p.ht()
    screen.tracer(75,0)
    u = doit1(6, Turtle(undobuffersize=1))
    s = doit2(7, Turtle(undobuffersize=1))
    t = doit3(5, Turtle(undobuffersize=1))
    v = doit4(6, Turtle(undobuffersize=1))
    w = doit5(5, Turtle(undobuffersize=1))
    a = clock()
    while True:
        done = 0
        for b in u,s,t,v,w:
            try:
                next(b)
            except:
                done += 1
        if done == 5:
            break

    screen.tracer(1,10)
    b = clock()
    return "runtime: {0:.2f} sec.".format(b-a)

if __name__ == '__main__':
    msg = main()
    print(msg)
    screen.mainloop()
