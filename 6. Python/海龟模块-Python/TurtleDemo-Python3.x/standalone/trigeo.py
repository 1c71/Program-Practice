"""       turtle-example-suite:

   standalone application: trigeo.py

Implementation of a find of Kirby Urner:

See: pdf_animation_by_ron_resch.pdf at
http://www.4dsolutions.net/presentations/

This version is an exact replica of the
obove pdf animation. During the animation
the six central triangles get temporarily
obscured by the outer ones.

The version in the tdemo_suite differs
slightly from this one in that these six
triangles are the upmost and thus remain
visible.
"""

from turtle import Turtle, Screen, Vec2D, mainloop
import math

A = 50.  # adjust this to your needs

SHS = A / 20
SF = 1.0
DSF = 1.0038582416
e = Vec2D(3**.5/2, 0.5)

def dsin(angle):
    return math.sin(angle*math.pi/180)

def lines(l):
    for i in range(6):
        d.fd(l)
        d.bk(l)
        d.left(60)   

class TriTurtle(Turtle):
    def __init__(self, c, r, tritype):
        Turtle.__init__(self, shape="triangle")
        self.c = c
        self.r = r
        self.speed(0)
        self.pencolor(0,0,0)
        if tritype == 1:
            self.basecolor = (1.0, 0.80392, 0.0)
            self.f = -1
            self.left(30)
        else:
            self.basecolor = (0.43137, 0.43137, 1.0)
            self.f = 1
            self.left(90)
        self.fillcolor(self.basecolor)
        self.pu()
        self.goto(c*A, r*A*3**.5/3)
        self.shapesize(SHS, SHS, 1)
        self.D = self.distance(0,0)
        self.e = (1/self.D)*self.pos()
    def setturn(self, phi):
        self.goto(SF*self.D*dsin(90-phi)*self.e)
        self.settiltangle(phi*self.f)
        self.shapesize(SHS*SF)
        if abs(self.c) + abs(self.r) > 2:
            self.fillcolor([x + (1-x)*phi/360 for x in self.basecolor])
            bc = phi/360.
            self.pencolor(bc, bc, bc)
            

s = Screen()
s.reset()
s.tracer(0)
d = Turtle(visible=False)
lines(500)

triangles = []
for c in range(-5,6,2):
    triangles.append(TriTurtle(c, 1, 1))
    triangles.append(TriTurtle(c, -1, 2))
for c in range(-4,5,2):
    triangles.append(TriTurtle(c, 2, 2))
    triangles.append(TriTurtle(c, -2, 1))
    triangles.append(TriTurtle(c, -4, 2))
    triangles.append(TriTurtle(c, 4, 1))
for c in range(-3,4,2):
    triangles.append(TriTurtle(c, 5, 2))
    triangles.append(TriTurtle(c, -5, 1))
    triangles.append(TriTurtle(c, -7, 2))
    triangles.append(TriTurtle(c, 7, 1))
for c in range(-2,3,2):
    triangles.append(TriTurtle(c, 8, 2))
    triangles.append(TriTurtle(c, -8, 1))
s.tracer(1)
                     
for phi in range(1,361):
    SF = SF*DSF
    s.tracer(0)
    for t in triangles:
        t.setturn(phi)
    s.tracer(1)
    
mainloop()
