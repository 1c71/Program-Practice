"""       turtle-example-suite:

           tdemo_tangram.py

Inspired by Pawel Boytchev's Elica-Logo
implementation of the tangram game.

Use left mouse button to drag, middle
and right mouse button clicks to turn tiles,
left button doubleclick to flip rhomboid.
"""
from turtle import Turtle, Screen, Vec2D 
from button import Button
import sys, random, time

from tangramdata import tangramdata
sys.setrecursionlimit(20000)
screen = Screen()
screen.tracer(False)
screen.mode("logo")
designer = Turtle(visible=False)
designer.pu()

startdata = tangramdata[0]
tangramdata = tangramdata[1:]
A = 198.0
a = A / 4.0
d = a * 2**.5

def makerhomboidshapes():
    designer.shape("square")
    designer.shapesize(5, 2.5)
    designer.shearfactor(-1)    # needs Python 3.1
    designer.tilt(90)
    screen.register_shape("rhomboid1", designer.get_shapepoly())
    designer.shearfactor(1)
    screen.register_shape("rhomboid2", designer.get_shapepoly())

class TStein(Turtle):
    def __init__(self, size, shape="arrow", clickable=True):
        Turtle.__init__(self)
        self.size = size
        self.pu()
        self.shape(shape)
        self.resizemode("user")
        self.turtlesize(size,size,3)
        self.clicktime = -1
        if clickable:
            self.onclick(self.turnleft, 2)
            self.onclick(self.turnright, 3)
            self.onclick(self.store, 1)
            self.ondrag(self.move, 1)
            self.onrelease(self.match, 1)
    def turnleft(self,x,y):
        self.lt(15)
        screen.update()
    def turnright(self,x,y):
        self.rt(15)
        screen.update()
    def store(self,x,y):
        self.clickpos = Vec2D(x,y)
    def move(self,x,y):
        neu = Vec2D(x,y)
        self.goto(self.pos() + (neu-self.clickpos))
        self.clickpos = neu
        screen.update()
    def place(self, x, y, h):
        self.goto(x,y)
        self.setheading(h)
    def match(self, x=None, y=None):
        matching = False
        for cand in STiles:
            if self.size == cand.size and self.shape() == cand.shape():
                if self.distance(cand) < 20:
                    i = STiles.index(cand)
                    if i < 5 and self.heading() == cand.heading():
                        matching = cand
                    elif (i in [0,1] and
                          STiles[0].distance(STiles[1])<5
                          and (self.heading()-cand.heading())%90==0):
                        matching = cand
                    elif (i in [3,4] and
                          STiles[3].distance(STiles[4])<5
                          and (self.heading()-cand.heading())%90==0):
                        matching = cand
                    elif i == 5 and (self.heading()-cand.heading())%90 == 0:
                        matching = cand
                    elif (i == 6 and self.flipped == cand.flipped and
                          (self.heading()-cand.heading())%180 == 0):
                        matching = cand
                    if matching:
                        self.setpos(cand.pos())
                        break
        screen.update()


class TRhomboid(TStein):
    def __init__(self, clickable=True):
        TStein.__init__(self, 1, shape="rhomboid1", clickable=clickable)
        self.flipped = False
        self.pu()
    def flip(self):
        if not self.flipped:
            self.shape("rhomboid2")
            self.flipped = True
        else:
            self.shape("rhomboid1")
            self.flipped = False
        screen.update()
    def store(self, x, y):
        clicktime = time.clock()
        if clicktime - self.clicktime < 0.4:
            self.flip()
            self.clicktime = -1
        else:
            self.clicktime = clicktime
        self.clickpos = Vec2D(x,y)
        
def init():
    global TTiles, STiles
    makerhomboidshapes()
    screen.bgcolor("gray10")
    STiles = [TStein(A/20., clickable=False),
              TStein(A/20., clickable=False),
              TStein(2*d/20., clickable=False),
              TStein(A/40., clickable=False),
              TStein(A/40., clickable=False),
              TStein(d/20., "square", clickable=False),
              TRhomboid(clickable=False)]
    TTiles = [TStein(A/20.),
              TStein(A/20.),
              TStein(2*d/20.),
              TStein(A/40.),
              TStein(A/40.),
              TStein(d/20., "square"),
              TRhomboid()]
    for s in STiles:
        s.color((1,1,0.9))
        s.turtlesize(s.size, s.size, 2)
        s.ht()
    screen.update()
    designer.goto(-390,-288)
    designer.pencolor("gray70")
    designer.write("Inspired by Pawel Boytchev's Elica-Logo implementation of the tangram game",
                   font=("Courier", 10, "bold"))
    nextBtn = Button("next.gif", resetgame)
    nextBtn.setpos(320,220)
    helpBtn = Button("help.gif", helpme)
    helpBtn.setpos(320,-220)

def resetTiles():
    c1, c2, c3 = random.random()/2, random.random()/2, random.random()/2
    arrangeTiles(startdata, TTiles)
    if TTiles[6].flipped:
        TTiles[6].flip()
    if STiles[6].flipped:
        STiles[6].flip()
    for i in range(7):
        TTiles[i].pencolor(c1, c2, c3) 
        TTiles[i].fillcolor(c1+random.random()/2, c2+random.random()/2, c3+random.random()/2) 

def arrangeTiles(data, tileset):
    flip = data[-1] == -1
    l = data[:7]
    for i in range(7):
        x,y,h = data[i]
        if i==6 and flip:
            tileset[6].flip()
        tileset[i].place(x, y, h)

def resetgame():
    data = random.choice(tangramdata)
    resetTiles()
    arrangeTiles(data, STiles)
    for t in TTiles+STiles: t.showturtle()
    screen.update()

def helpme():
    c = STiles[0].pencolor()
    x,y,s = STiles[0].turtlesize()
    for t in STiles:
        t.pencolor("black")
        t.turtlesize(t.size, t.size, 1)
    screen.update()
    time.sleep(0.5)
    screen.tracer(False)
    for t in STiles:
        t.pencolor(c)
        t.turtlesize(t.size, t.size, s)
    screen.update()

def main():    
    init()    
    resetgame()
    return "EVENTLOOP"

if __name__ == "__main__":
    msg = main()
    print(msg)
    screen.mainloop()
