#!/usr/bin/python
"""        turtle-example-suite:

          tdemo_sun_earth_moon.py

Gravitational system simulation using the
approximation method from Feynman-lectures,
Vol. 1, p.9-8, using turtlegraphics

This example uses real phyisical data of
our planetary system: simulates the moon
orbiting the earth orbiting around the sun.

Demonstrates the use of worldcoordinates,
fixing the earth in the center of the
coordinate system.

The sun is not shown because the distance of
the earth from the sun is about 500 times
larger than the distance between earth and moon.
(But it's position can be concluded from
observing the bright side of the moon (and the
earth).

This simulation shows, that the orbit of the
moon is convex (in contrast to the artificial
example tdemo_plante_with_moon.py) because the
gravitational force exerted on the moon by the
sun is always greater that that exerted by
the earth.
"""
from turtle import Screen, Turtle, Shape, Vec2D
from time import sleep

mS = 2.e30
mE = 6.e24
mM = 7.35e22

G = 6.67e-11
rE = 1.5e11
rM = 3.85e8

vE = 3.e4
vM = 1.e3
DT = 7200

fx = 1.2e10
fy = fx * 3/4

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
            p = self.planets[1].pos()  #earth
            v = self.planets[1].vel
            d = (0.92*fy/abs(v))*v
            x, y = p - d
            s.setworldcoordinates(x-fx,y-fy,
                                  x+fx,y+fy)
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
    s.setworldcoordinates(-3.e11, -2.25e11, 3.e11, 2.25e11)
    gs = GravSys()
    sun = Star(mS, Vec2D(0.,0.), Vec2D(0.,0.), gs, "circle")
    sun.color("yellow")
    sun.turtlesize(1.8)
    sun.pu()
    earth = Star(mE, Vec2D(rE,0.), Vec2D(0.,vE), gs, "planet")
    earth.pencolor("green")
    earth.shapesize(0.8)
    moon = Star(mM, Vec2D(rE+rM,0.), Vec2D(0.,vE+vM), gs, "planet")
    moon.pencolor("blue")
    moon.shapesize(0.5)
    gs.init()
    gs.start()
    return "Done!"

if __name__ == '__main__':
    msg = main()
    print(msg)
    s.mainloop()

