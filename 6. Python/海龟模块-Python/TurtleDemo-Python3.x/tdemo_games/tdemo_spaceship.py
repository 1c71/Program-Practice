#!/usr/bin/python
"""       turtle-example-suite:

           tdemo_spaceship.py

How does rocket propulsion work?
Play this game to learn about it.

The keys:

<space> starts a new game

Arrow-Keys:
<up> exerts a force (for a moment) and so
     accelerates spaceship in direction of
     its heading
<left>,<right> turns spaceship by 10 degrees

If the canvas has lost the focus, click into
it!

   Press STOP to exit the program!
   ===============================

Remark: this is a rather old script;
a rewrite possibly  on OOP basis
would make it clearer and/or cleaner.
"""
from turtle import *
from time import clock

FORCE_UNIT = 0.1  # change this to fine-tune
                  # control of the spaceship
                  # on your machine

smallfont  = ("Courier", 12, "bold")
normalfont = ("Courier", 18, "normal")
boldfont   = ("Courier", 18, "bold")

def scenery():
    global target
    designer.ht()
    designer.speed(0)
    designer.pu()
    designer.lt(180)
    designer.fd(240)
    designer.lt(90)
    designer.pensize(10)
    designer.pencolor("blue")
    designer.circle(120, 15)
    designer.pd()
    designer.circle(120, 330)
    designer.pu()
    designer.circle(120, 15)
    designer.lt(90)
    designer.fd(120)
    designer.dot(20, "yellow")
    target = designer.pos()

# spaceship is the "anonymous" turtle
def start():
    global vx, vy
    vx, vy = 0.0, 0.0
    reset()
    ht()
    speed(0)
    pensize(7)
    color("red", "orange")
    pu()
    fd(120)
    pd()
    lt(90)
    st()
    # hint for the player
    writer.reset()
    writer.ht()
    writer.speed(0)
    writer.up()
    writer.goto(-307,-220)
    writer.write('Move "spaceship" to yellow dot using up/left/right-arrow-keys!',
                 font = ("Courier", 12, "bold") )

def turnleft():
    lt(10)

def turnright():
    rt(10)

def rueckstoss():
    global vx, vy
    from math import sin, cos, pi
    alpha = heading() * pi / 180.0
    vx += FORCE_UNIT * cos(alpha)
    vy += FORCE_UNIT * sin(alpha)

def steps():
    global result
    x,y=pos()
    setpos(x+vx, y+vy)
    if (110 < distance(target) < 135 and
          8 < towards(0,0) < 352):
        result = "CRASH!" 
    elif distance(target) > 450:
        result = "ESCAPED!"
    elif distance(target) < 15:
        result = "SUCCESS!"
    if not result:
        ontimer(steps)
    
def go():
    global result
    result = None
    # Ein Spiel!
    startzeit = clock()
    steps()
    # ouptut result!
    writer.goto(-305,-200)
    writer.pencolor("red")
    writer.write(result, font=boldfont, move=1)
    if result == "SUCCESS!":
        zeit = clock() - startzeit
        writer.write(" (%2.2f s)" % zeit, font=boldfont, move=1)
    writer.pencolor("black")
    writer.write(" New game: spacebar", font=normalfont)

def spiel():
    if result:  # i.e. if game over
        start()
        go()

def main():
    global designer, writer
    designer = Turtle()
    writer = Turtle()
    tracer(1,0)

    global result
    onkey(turnleft,"Left")
    onkey(turnright,"Right")
    onkey(rueckstoss, "Up")
    onkey(spiel, "space")
    #onscreenclick(listen)
    listen()
    result = "start"
    scenery()
    ontimer(spiel,500)
    delay(5)
    # a moment please to ...
    return "EVENTLOOP"

if __name__ == '__main__':
    msg = main()
    print(msg)
    mainloop()
