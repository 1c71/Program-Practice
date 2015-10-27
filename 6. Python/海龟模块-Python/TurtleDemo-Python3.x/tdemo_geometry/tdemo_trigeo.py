"""       turtle-example-suite:

           tdemo_trigeo.py

Implementation of a find of Kirby Urner:

See: pdf_animation_by_ron_resch.pdf at
http://www.4dsolutions.net/presentations/

This version differs slightly from the
original in that the central three triangles
are the upmost, so *they* remain visible
during the animation.
"""

from turtle import Turtle, Screen, Vec2D
import math

def dsin(angle):
    return math.sin(angle*math.pi/180)

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
            

def main():
    global d, SHS, SF, A
    A = 42 # answer to the ultimate question ... (you know)
    SHS = A / 20.
    SF = 1.0
    DSF = 1.0038582416
    s = Screen()
    s.setup(800, 600)
    s.reset()
    s.tracer(0)
    d = Turtle(visible=False)
    for i in range(6):
        d.fd(500)
        d.bk(500)
        d.left(60)   

    triangles = []
    for c in range(-5,6,2):
        if abs(c) != 1:
            triangles.append(TriTurtle(c, 1, 1))
            triangles.append(TriTurtle(c, -1, 2))
    for c in range(-4,5,2):
        if c != 0:
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
    for c in (-1, 1):
        triangles.append(TriTurtle(c, 1, 1))
        triangles.append(TriTurtle(c, -1, 2))
    triangles.append(TriTurtle(0, 2, 2))
    triangles.append(TriTurtle(0, -2, 1))
    s.tracer(1)
                         
    for phi in range(1,361):
        SF = SF*DSF
        s.tracer(0)
        for t in triangles:
            t.setturn(phi)
        s.tracer(1)
    return "DONE!"

if __name__ == "__main__":
    msg = main()
    print(msg)
    Screen().mainloop()
