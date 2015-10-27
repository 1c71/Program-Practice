#!/usr/bin/python
"""        turtle-example-suite:

      tdemo_sun_and_inner_planets.py

Gravitational system simulation using the
approximation method from Feynman-lectures,
Vol.1, p.9-8, using turtlegraphics

This example uses real phyisical data of
our planetary system: simulates the four
inner planets orbiting around the sun.

Demonstrates the use of (user defined)
worldcoordinates.
"""
from turtle import Screen, Turtle, Shape, Vec2D

AE = 1.5e11
# masses
mS = 2.e30
mE = 6.e24
mME = 3.3e23
mVE = 4.869e24
mMA = 6.419e23

G = 6.67e-11
# radii of the orbits
rE = 1.5e11
perihelME = .307*AE  # orbit is fairly eccentric
rVE = 0.732*AE
rMA = 1.524*AE
# velocities
vE = 3.e4
perihelvME = 5.9e4
vVE = 3.502e4
vMA = 2.413e4
DT = 10800
# half width of user coordinate system (in meters)
hfw =  2.5e11 

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
    s.setup(800, 600, 50, 50)
    s.screensize(750, 550)
    createPlanetShape()
    ## setup gravitational system
    s.setworldcoordinates(-hfw*4/3, -hfw, hfw*4/3, hfw)
    gs = GravSys()
    sun = Star(mS, Vec2D(0.,0.), Vec2D(0.,0.), gs, "circle")
    sun.color("yellow")
    sun.turtlesize(1.8)
    sun.pu()
    earth = Star(mE, Vec2D(rE,0.), Vec2D(0.,vE), gs, "planet")
    earth.pencolor("green")
    earth.shapesize(0.8)
    mercury = Star(mME, Vec2D(0., perihelME), Vec2D(-perihelvME, 0),
                                                        gs, "planet")
    mercury.pencolor("blue")
    mercury.shapesize(0.5)
    venus = Star(mVE, Vec2D(-rVE, 0.), Vec2D(0., -vVE), gs, "planet")
    venus.pencolor("blue")
    venus.shapesize(0.65)
    mars = Star(mMA, Vec2D(0., -rMA), Vec2D(vMA, 0.), gs, "planet")
    mars.pencolor("blue")
    mars.shapesize(0.45)
    gs.init()
    gs.start()
    return "Done!"

if __name__ == '__main__':
    msg = main()
    print(msg)
    Screen().mainloop()

