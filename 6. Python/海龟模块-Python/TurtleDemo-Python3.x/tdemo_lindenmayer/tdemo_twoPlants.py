#!/usr/bin/python
"""       turtle-example-suite:

            tdemo_plants.py

Lindenmayer systems, named after the biologist
Aristid Lindenmayer, are formal grammars used
to model the growth of plants and many more
patterns (see example indianDesigns).

For more information see:
http://en.wikipedia.org/wiki/Lindenmayer_system

Here are two examples produced in parallel by
Lindenmayer generators

"""
####################################
# Mini Lindenmayer tool -
# this time a bit more sophisticated
####################################

from turtle import Turtle, Screen

def replace( seq, replacementRules, n ):
    for i in range(n):
        newseq = ""
        for element in seq:
            newseq += replacementRules.get(element,element)
        seq = newseq  
    return seq

def lindenmayer(turtle,
                axiom = "",
                replacementRules = {},
                depth = 1,
                step = 5,
                angle = 90,
                startpos = (0,-120),
                startdir = 90,
                updating = 20):
    turtle.step, turtle.angle = step, angle
    drawing = replace(axiom, replacementRules, depth)
    Screen().tracer(updating)
    turtle.start(startpos, startdir)
    return turtle.draw(drawing, turtle.standardRules()) 
    

class LPen(Turtle):
    def __init__(self):
        Turtle.__init__(self)
        self.speed(0)
        self.hideturtle()
        self.tstack = []
        
    def start(self, startpos, startdir):
        self.up()
        self.goto(startpos)
        self.left(startdir)
        self.down()

    def draw( self, commands, rules):
        i = 0
        for c in commands:
            try:
                rules[c]()
            except:
                pass
            # We turn it into a generator!                
            yield 1

    ################################
    # Standardrules
    ################################

    def r(self):
        self.right(self.angle)

    def l(self):
        self.left(self.angle)

    def f(self):
        self.up()
        self.forward(self.step)

    def F(self):
        self.down()
        self.forward(self.step)

    def turn(self):
        self.left(180)

    def save(self):
        self.tstack.append( (self.pos(), self.heading()) )

    def load(self):
        position, richtung = self.tstack.pop()
        self.up()
        self.goto(position)
        self.setheading(richtung)

    def standardRules(self):
        return {"-":self.l, "+":self.r, "F": self.F, "f":self.f,
                "|": self.turn, "[":self.save, "]":self.load}

# 2 examples for Lindenmayer plants:
herb = {
         "axiom" : "G",
         "replacementRules" : { "G" : "GFX[+G][-G]",
                                "X" : "X[-FFF][+FFF]FX" },
         "depth" : 5,
         "step" : 6.75,
         "angle" : 180.0/7,
         "startpos" : (-135, -192),
         "startdir" : 90
       }

bush = {
         "axiom" : "F",
         "replacementRules" : { "F" : "FF+[+F-F-F]-[-F+F+F]" },
         "depth" : 3,
         "step" : 13.5,
         "angle" : 180.0/8,
         "startpos" : (90, -192),
         "startdir" : 90,
       }


def main():
    l1 = lindenmayer(LPen(), **herb)
    l2 = lindenmayer(LPen(), **bush)
    done = 0
    while done < 2:
        done = 0
        for l in l1, l2:
            try:
                next(l)
            except StopIteration:
                done += 1
    Screen().tracer(True)
    return "Done!"
    

if __name__ == '__main__':
    msg = main()
    print(msg)
    Screen().mainloop()
