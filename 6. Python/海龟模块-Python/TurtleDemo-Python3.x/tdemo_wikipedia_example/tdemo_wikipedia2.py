"""      turtle-example-suite:

          tdemo_wikipedia2.py

This is the second of a series of 4 examples
inspired by the Wikipedia article on turtle
graphics. (See example wikipedia1 for URLs)

To the plain transcription of the
corresponding Logo code I added the lines:

        c = abs(ne/2.0-i)/(ne*.7)
        pencolor(1-c,0,c)

in n_eck. They change the colors or the
circle segments.

"""
from turtle import *
from time import clock

def n_eck(ne,sz):
    for i in range(ne):
        rt(360./ne)
        # blue component of color it i-th
        # segment:
        c = abs(ne/2.0-i)/(ne*.7)
        pencolor(1-c,0,c)
        fd(sz)

def mn_eck(ne, sz):
    for i in range(ne):
        rt(360./ne)
        n_eck(ne, sz)

def main():
    mode("logo")
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


## on my desktop machine: approx. 1.2 sec.
