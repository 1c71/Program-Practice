#!/usr/bin/python
"""        turtle-example-suite:

            tdemo_sun_earth.py

Gravitational system simulation using the
approximation method from Feynman-lectures,
Vol. 1, p.9-8, using turtlegraphics

This example uses real phyisical data of
our planetary system: simulates the earth
orbiting around the sun.

Demonstrates the use of worldcoordinates,
fixing the earth in the center of the
coordinate system. So after every step of
the simulation the worldcoordinatesystem
has to be recalculated.

For another application of this technique
see: tdemo_sun_earth_moon.py .
"""
from turtle import Screen, Turtle, Shape, mainloop, Vec2D
from time import sleep

mS = 2.e30
mE = 6.e24
G = 6.67e-11
rE = 1.5e11
vE = 3.e4
DT = 10800

class GravSys(object):
    def __init__(self):
        self.planets = []
        self.dt = DT
    def init(self):
        for p in self.planets:
            p.init()
    def start(self):
        s.tracer(False)
        for i in range(10000):
            for p in self.planets:
                p.step()
            x,y = p.pos()
            s.setworldcoordinates(x-4.e11,y-3.e11,
                                  x+4.e11,y+3.e11)
            if i % 5 == 0:
                s.update()
            
class Star(Turtle):
    def __init__(self, m, x, v, gravSys, shape):
        Turtle.__init__(self, shape)
        gravSys.planets.append(self)
        self.gravSys = gravSys
        self.dt = self.gravSys.dt
        self.penup()
        self.m = m
        self.setpos(x)
        self.vel = v
        self.pendown()
    def init(self):
        self.vel = self.vel + 0.5*self.dt*self.acc()
    def acc(self):
        a = Vec2D(0,0)
        for planet in self.gravSys.planets:
            if planet != self:
                r = planet.pos()-self.pos()
                a += (G*planet.m/abs(r)**3)*r
        return a
    def step(self):
        self.setpos(self.pos() + self.dt*self.vel)
        if self != sun:
            self.setheading(self.towards(sun))
        self.vel = self.vel + self.dt*self.acc()

## create compound yellow/blue turtleshape for planets
## yellow semicircle will point towards the sun
def createPlanetShape():
    s.tracer(0,0)
    t = Turtle()
    t.ht()
    t.pu()
    t.fd(6)
    t.lt(90)
    t.begin_poly()
    t.circle(6, 180)
    t.end_poly()
    m1 = t.get_poly()
    t.begin_poly()
    t.circle(6,180)
    t.end_poly()
    m2 = t.get_poly()

    planetshape = Shape("compound")
    planetshape.addcomponent(m1,"orange")
    planetshape.addcomponent(m2,"blue")
    s.register_shape("planet", planetshape)
    s.tracer(True,0)
    

def main():
    global s, sun
    s = Screen()
    s.setup(800, 600)
    s.screensize(750, 550)
    createPlanetShape()
    ## setup gravitational system
    s.setworldcoordinates(-4.e11, -3.e11, 4.e11, 3.e11)
    gs = GravSys()
    sun = Star(mS, Vec2D(0.,0.), Vec2D(0.,0.), gs, "circle")
    sun.color("yellow")
    sun.turtlesize(1.2)
    sun.pu()
    earth = Star(mE, Vec2D(rE,0.), Vec2D(0.,vE), gs, "planet")
    earth.pencolor("green")
    gs.init()
    gs.start()
    return "Done!"

if __name__ == '__main__':
    msg = main()
    print(msg)
    mainloop()

