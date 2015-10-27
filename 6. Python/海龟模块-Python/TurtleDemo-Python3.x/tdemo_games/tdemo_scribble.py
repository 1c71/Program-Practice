"""       turtle-example-suite:

           tdemo_scribble.py

Another very rudimentary paint program

- use left mouse button to move turtle
  (by clicking) or to drag it drawing.
- middle mouse button to toggle fill-state
  (watch fillindicator)
- colorbuttons: left button sets pe>>> ================================ RESTART ================================
ncolor,
  right button sets fillcolor
- keys 123456789 set pensize
- spacebar clears drawing
- press backspace to undo recent drawing
  steps.
 -------------------------------------------
                Try to draw!
 -------------------------------------------
          To exit press STOP button
 -------------------------------------------
"""
from turtle import *
import sys
sys.setrecursionlimit(20000)

class ColorButton(Turtle):
    def __init__(self, col, x, y):
        Turtle.__init__(self)
        self.pu(); self.goto(x, y)
        self.color(col)
        self.shape("square")
        self.onclick(self.setpencolor)
        self.onclick(self.setfillcolor, 3)
    def setpencolor(self, x, y):
        pencolor(self.pencolor())
    def setfillcolor(self, x, y):
        fillcolor(self.pencolor())

def jump(x,y):
    if x > -350:
        pu(); goto(x,y); pd()

def fill_switch():
    while True:
        fillindicator.fillcolor("red")
        yield begin_fill()
        fillindicator.fillcolor("")
        yield end_fill()   

def toggle_fill(x, y):
    next(fs)

def main():
    global fs, fillindicator
    setup(800, 600, -20, 20)
    reset()
    shape("circle")
    shapesize(0.5)
    speed(0)
    fs = fill_switch() 

    ondrag(goto)
    onscreenclick(jump)
    onscreenclick(toggle_fill, 2)
    for c in "123456789":
        def setpensize(s=int(c)):
            pensize(s)
            shapesize(outline=s)
        onkey(setpensize, c)
    onkey(clear, "space")
    onkeypress(undo, "BackSpace")

    tracer(False)
    ColorButton("yellow", -365, 90)
    ColorButton("orange", -365, 60)
    ColorButton("red", -365, 30)
    ColorButton("violet", -365, 0)
    ColorButton("blue", -365, -30)
    ColorButton("green", -365, -60)
    ColorButton("black", -365, -90)
    fillindicator = Turtle(shape="circle")
    fillindicator.pu()
    fillindicator.goto(-365, -180)
    fillindicator.color("black", "")
    tracer(True)
    listen()
    return "DONE!"

if __name__ == "__main__":
    msg = main()
    print(msg)
    mainloop()
