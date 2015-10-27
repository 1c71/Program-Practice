# Button
# 8. 3. 2007
# Gregor Lingl

from turtle import Turtle

class Button(Turtle):
    def __init__(self, picfile, action):
        Turtle.__init__(self)
        self.getscreen().register_shape(picfile)
        self.shape(picfile)
        def _action(x,y):
            action()
        self.onclick(_action)
        self.pu()
        self.speed(0)
