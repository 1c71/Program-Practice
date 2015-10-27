#!/usr/bin/python
"""       turtle-example-suite:

       tdemo_planet_and_moon_2.py

Gravitational system simulation using the
approximation method from Feynman-lectures,
Vol. 1, p.9-8, using turtlegraphics.

Example: heavy central body, light planet,
very light moon!
Planet has an eccentric orbit, moon an
unstable orbit around the planet. Observe
the decay of the system due to sort of
tidal forces near the sun.

---------------------------------------------
Enlarge the turtleDemo window to full screen
and use scrollbars if necessary.
---------------------------------------------

You can hold the movement temporarily by
pressing the left mouse button with mouse
over the scrollbar of the canvas.

"""
from turtle import Shape, Turtle, Screen, mainloop, Vec2D as Vec
from time import sleep

G = 8

class GravSys(object):
    def __init__(self):
        self.planets = []
        self.t = 0
        self.dt = 0.01
    def init(self):
        for p in self.planets:
            p.init()
    def start(self):
        for i in range(10000):
            self.t += self.dt
            for p in self.planets:
                p.step()
            
class Star(Turtle):
    def __init__(self, m, x, v, gravSys, shape):
        Turtle.__init__(self, shape)
        self.penup()
        self.m = m
        self.setpos(x)
        self.v = v
        gravSys.planets.append(self)
        self.gravSys = gravSys
        self.resizemode("user")
        self.pendown()
    def init(self):
        dt = self.gravSys.dt
        self.a = self.acc()
        self.v = self.v + 0.5*dt*self.a
    def acc(self):
        a = Vec(0,0)
        for planet in self.gravSys.planets:
            if planet != self:
                v = planet.pos()-self.pos()
                a += (G*planet.m/abs(v)**3)*v
        return a
    def step(self):
        dt = self.gravSys.dt
        self.setpos(self.pos() + dt*self.v)
        if self.gravSys.planets.index(self) != 0:
            self.setheading(self.towards(self.gravSys.planets[0]))
        self.a = self.acc()
        self.v = self.v + dt*self.a


def main():
    ## create compound yellow/blue turtleshape for planets
    s = Screen()
    s.reset()
    s.tracer(0, 0)
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
    s.tracer(1,0)

    ## setup gravitational system
    gs = GravSys()
    sun = Star(1000000, Vec(-250,0), Vec(0,-0.35), gs, "circle")
    sun.color("yellow")
    sun.pensize(1.8)
    sun.pu()
    earth = Star(5000, Vec(450,0), Vec(0,70), gs, "planet")
    earth.pencolor("green")
    earth.shapesize(0.8)

    rm=12.0583
    vm=(8.0*5000/rm)**.5
    moon = Star(1, Vec(450+rm,0), Vec(0,70+vm), gs, "planet")
    moon.pencolor("blue")
    moon.shapesize(0.5)
    gs.init()
    gs.start()
    return "Done!"

if __name__ == '__main__':
    msg = main()
    print(msg)
    Screen().mainloop()
