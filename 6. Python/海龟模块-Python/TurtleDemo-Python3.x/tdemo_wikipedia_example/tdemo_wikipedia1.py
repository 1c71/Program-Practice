"""      turtle-example-suite:

          tdemo_wikipedia1.py

This is the first of a series of 4 examples
inspired by the Wikipedia article on turtle
graphics:

http://en.wikipedia.org/wiki/Turtle_graphics
http://en.wikipedia.org/wiki/Image:Remi_turtlegrafik.png

It's a plain transcription of the
corresponding Logo code.

"""
from turtle import *
from time import clock

def n_eck(ne,sz):
    for i in range(ne):
        rt(360./ne)
        fd(sz)

def mn_eck(ne, sz):
    for i in range(ne):
        rt(360./ne)
        n_eck(ne, sz)
        
def main():
    #mode("logo")
    speed(0)
    hideturtle()
    bgcolor("black")
    pencolor("red")
    pensize(3)

    tracer(36,0)

    at = clock()
    mn_eck(36,20)
    et = clock()
    return "Laufzeit: {0:.3f} sec".format(et-at)

if __name__ == '__main__':
    msg = main()
    print(msg)
    mainloop()

# on my desktop machine: approx. 0.3 sec.
