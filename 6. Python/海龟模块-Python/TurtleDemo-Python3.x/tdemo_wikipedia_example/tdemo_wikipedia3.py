"""       turtle-example-suite:

           tdemo_wikipedia3.py

This is the third of a series of 4 examples
inspired by the Wikipedia article on turtle
graphics. (See example wikipedia1 for URLs)

It gives an alternate implementation:
First we create (ne-1) (i.e. 35 in this
example) copies of our first turtle p.
Then we let them perform their steps in
parallel.

Version without cloning using the turtles()
method of TurtleScreen
"""
from turtle import Screen, Turtle, mainloop
from time import clock

def create_turtles(ne):
    for i in range(ne):
        t=Turtle()
        t.ht()
        t.speed(0)
        t.seth(i*360.0/ne)
        t.width(3)
    return s.turtles()

def mn_eck(ne,sz):
    #create ne turtles
    myturtles = create_turtles(ne)
    for i in range(ne):
        c = abs(ne/2.0-i)/(ne*.7)
        # let alle those turtles make
        # a step in parallel:
        for t in myturtles:
            t.rt(360./ne)
            t.pencolor(1-c,0,c)
            t.fd(sz)

def main():
    global s
    at = clock()
    s = Screen()
    s.bgcolor("black")
    s.tracer(36, 0)
    mn_eck(36,19)
    et = clock()
    return "Laufzeit: {0:.3f} sec".format(et-at)

if __name__ == '__main__':
    msg = main()
    print(msg)
    mainloop()


## on my desktop machine: approx. 1.65 sec.
## on my laptop: approx. 1.1 sec
