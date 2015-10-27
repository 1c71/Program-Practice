#!/usr/bin/python
"""       turtle-example-suite:

            tdemo_planets.py

Gravitational system simulation using the
approximation method from Feynman-lectures,
Vol. 1, p.9-8, using turtlegraphics.

Example: heavy central body, light planet,
very light second planet! This one will be
deflected several times by the gravitational
force exerted by the first planet.

You can hold the movement temporarily by
pressing the left mouse button with mouse
on the scrollbar of the canvas.

"""
from turtle import Shape, Screen, Turtle, Vec2D

G = 8   # gravitational constant

class GravSys(object):
    def __init__(self):
        self.planets = []
        self.dt = 0.01
    def init(self):
        for planet in self.planets:
            planet.init()
    def start(self):
        for i in range(20000):
            for planet in self.planets:
                planet.step()
            Screen().update()
            
class Star(Turtle):
    def __init__(self, m, x, v, gravSys, shape):
        Turtle.__init__(self, shape)
        self.resizemode("user")
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
## yellow semicircle will always point towards the sun
def createPlanetShape():
    global s
    s = Screen()
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
    global sun
    createPlanetShape()
    ## setup gravitational system
    gs = GravSys()
    sun = Star(1000000, Vec2D(0,0), Vec2D(0,-3.5), gs, "circle")
    sun.color("yellow")
    sun.turtlesize(1.2)
    sun.pu()
    earth = Star(10000, Vec2D(100,0), Vec2D(0,350), gs, "planet")
    earth.pencolor("green")
    venus = Star(4, Vec2D(-80,0), Vec2D(0,-350), gs, "planet")
    venus.pencolor("blue")
    venus.turtlesize(0.7)
    Screen().tracer(False)
    gs.init()
    gs.start()
    return "Done!"

if __name__ == '__main__':
    msg = main()
    print(msg)
    mainloop()
