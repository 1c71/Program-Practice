#!/usr/bin/python
"""       turtle-example-suite:

            tdemo_rhombi.py

Constructs an aperiodic penrose-tiling,
consisting of two types of rhombi, thin and
fat ones, by the method of inflation in six steps.

For more information see:
 http://en.wikipedia.org/wiki/Penrose_tiling
"""

from turtle import *
from time import clock, sleep

f = (5**0.5-1)/2.0   # (sqrt(5)-1)/2 -- goldener Schnitt

def fat(l):
    lt(36)
    fd(l)
    rt(72)
    fd(l)
    rt(108)
    fd(l)
    rt(72)
    fd(l)
    rt(144)
    
def skinny(l):    
    lt(72)
    fd(l)
    rt(144)
    fd(l)
    rt(36)
    fd(l)
    rt(144)
    fd(l)
    rt(108)

def inflatefat(l, n):
    if n == 0:
        px, py = pos()
        h, x, y = int(heading()), round(px,3), round(py,3)
        tiledict[(h,x,y)] = True
        return
    fl = f * l
    lt(216)
    bk(l)
    inflatefat(fl, n-1)
    lt(108)
    inflateskinny(fl, n-1)
    fd(l)
    rt(144)
    inflatefat(fl, n-1)
    lt(216)
    bk(l)
    inflateskinny(fl, n-1)
    lt(108)
    inflatefat(fl, n-1)
    fd(l)
    rt(144)

def inflateskinny(l, n):
    if n == 0:
        px, py = pos()
        h, x, y = int(heading()), round(px,3), round(py,3)
        tiledict[(h,x,y)] = False
        return
    fl = f * l
    lt(252)
    bk(l)
    inflatefat(fl, n-1)
    lt(216)
    bk(l)
    inflateskinny(fl, n-1)
    lt(144)
    inflateskinny(fl, n-1)
    fd(l)
    rt(144)
    inflatefat(fl, n-1)
    fd(l)
    rt(108)

def draw(l, n, th=2):
    clear()
    l = l * f**n
    turtlesize(l/100.0, l/100.0, th)    
    for k in tiledict:
        h, x, y = k
        setpos(x, y)
        setheading(h)
        if tiledict[k]:
            shape("fat")
            color("black", "green")
        else:
            shape("skinny")
            color("black", "red")
        stamp()

def makeshapes():
    tracer(0)
    begin_poly()
    fat(100)
    end_poly()
    addshape("fat", get_poly())
    begin_poly()
    skinny(100)
    end_poly()
    addshape("skinny", get_poly())
    tracer(1)

def rsun(l, n):
    for i in range(5):
        inflatefat(l, n)
        lt(72)

def start():
    #winsize(800, 800)
    reset()
    ht()
    pu()
    makeshapes()
    resizemode("user")
    
def test(l=300, n=4, fun=rsun, startpos=(0,0), th=2):
    global tiledict
    goto(startpos)
    setheading(0)
    tiledict = {}
    a = clock()
    tracer(0)
    fun(l, n)
    b = clock()
    draw(l, n, th)
    tracer(1)
    c = clock()
    print("Rechnen:   %7.4f s" % (b - a))
    print("Zeichnen:  %7.4f s" % (c - b))
    print("Insgesamt: %7.4f s" % (c - a))
    nk = len([x for x in tiledict if tiledict[x]])
    nd = len([x for x in tiledict if not tiledict[x]])
    print("%d dicke und %d schmale Rhomben = zusammen %d Teile." % (nk, nd, nk+nd))

def demo(fun=rsun):
    start()
    for i in range(7):
        test(200, i, fun)
        if i < 5:
            sleep(2-i*0.2)

def main():
    #title("Demo: Penrose-Parkettierung mit Rhomben.")
    mode("logo")
    demo()
    pencolor("black")
    goto(0,-370)
    write("Please wait for some 15 seconds ...",
          align="center", font=('Courier', 24, 'bold'))
    test(450, 6)
    return "Done!"

if __name__ == "__main__":
    msg = main()
    print(msg)
    mainloop()
