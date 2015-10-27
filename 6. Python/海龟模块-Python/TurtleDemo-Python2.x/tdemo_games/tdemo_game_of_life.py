from turtle import Turtle, Screen
import time

try:
    import psyco
    from psyco.classes import *
    psyco.full()
    print ("PSYCO -- SUPER!!")
except:
    print ("-- psyco not installed - reduced performance --")
    print ("-- Download psyco at http://psyco.sourceforge.net/ --")

MARG_X = 2
MARG_Y = 8
MAX_X = 80
MAX_Y = 57
SQUARE_WIDTH = 10
FREEROWS = 3
DM = 10

screen = Screen()

def coords(col, row):
	return ((-MAX_X/2. + col)*SQUARE_WIDTH + MARG_X,
                ((-MAX_Y+ FREEROWS)/2. + row )*SQUARE_WIDTH + MARG_Y)

def cellindices(x, y):
    return (int(round((x-MARG_X)/SQUARE_WIDTH + MAX_X/2.)),
            int(round((y-MARG_Y)/SQUARE_WIDTH + (MAX_Y- FREEROWS)/2. )) )

class Patch(Turtle):
    def __init__(self, col, row):
        Turtle.__init__(self, shape="square", visible=False)
        self.pu()
        self.goto(coords(col, row))
        self.color("black")
        self.shapesize((SQUARE_WIDTH-2)/20.0)
        
class Game(object):

    NBADDR = ((-1,-1),(-1,0),(-1,1),(0,-1),(0,1),(1,-1),(1,0),(1,1))
    
    def __init__(self):
        screen.tracer(False)
        screen.setup(width=MAX_X*SQUARE_WIDTH + DM,
                     height = (MAX_Y+FREEROWS)*SQUARE_WIDTH + DM,
                     startx = -20,
                     starty = 20)
        screen.screensize(MAX_X*SQUARE_WIDTH + DM - 50,
                          (MAX_Y+FREEROWS)*SQUARE_WIDTH + DM -50)
        self.designer = Turtle(visible=False)
        starttime = time.clock()
        self.messagero = Turtle(visible=False)
        self.messagero.penup()
        self.messagero.pencolor("blue")
        self.messagero.goto(0, -(MAX_Y+FREEROWS)*SQUARE_WIDTH/2+6)
        self.message("Please wait a moment!")
        self.designer.pencolor("gray90")
        for c in range(MAX_X+1):
            self.line((-MAX_X/2. -.5 + c)*SQUARE_WIDTH + MARG_X, 
                      ((-MAX_Y + FREEROWS)/2. -.5 + 0)*SQUARE_WIDTH + MARG_Y,
                      (-MAX_X/2. -.5 + c)*SQUARE_WIDTH + MARG_X,
                      ((-MAX_Y + FREEROWS)/2. -.5 + MAX_Y)*SQUARE_WIDTH + MARG_Y)
        for r in range(MAX_Y+1):
            self.line((-MAX_X/2. -.5 + 0)*SQUARE_WIDTH + MARG_X, 
                      ((-MAX_Y + FREEROWS)/2. -.5 + r)*SQUARE_WIDTH + MARG_Y,
                      (-MAX_X/2. -.5 + MAX_X)*SQUARE_WIDTH + MARG_X,
                      ((-MAX_Y + FREEROWS)/2. -.5 + r)*SQUARE_WIDTH + MARG_Y)
        screen.update()
        self.patches = {}
        for r in range(MAX_Y):
            for c in range(MAX_X):
                self.patches[(c, r)] = Patch(c, r)

        self.state = set([(41,33), (42,33), (43,34), (42,32), (42,34)])
        for cell in self.state:
            self.patches[cell].showturtle()
        self.newstate = None

        stoptime = time.clock()
        print(stoptime - starttime)
        screen.update()
        screen.onkey(self.run, "space")
        screen.onkey(screen.bye, "Escape")
        screen.onkey(self.clear, "c")
        screen.listen()
        screen.onclick(self.toggle)
        self.message("spacebar:start/pause | left click:toggle cell | c:clear"
                     " | escape:quit")

    def message(self, txt):
        self.messagero.clear()
        self.messagero.write(txt, align="center", font=("Courier", 14, "bold"))
        

    def line(self, x1, y1, x2, y2):
        self.designer.penup()
        self.designer.goto(x1, y1)
        self.designer.pendown()
        self.designer.goto(x2, y2)

    def calcnext(self):
        cd = {}
        for (x,y) in self.state:
            for dx, dy in Game.NBADDR:
                xx, yy = x+dx, y+dy
                cd[(xx,yy)] = cd.get((xx,yy), 0) + 1
            cd[(x,y)] = cd.get((x,y), 0) + 10
        td = []
        for c in cd:
            if cd[c] not in [3, 12, 13]:
                td.append(c)
        for c in td: del cd[c]
        return set(cd.keys())

    def update_display(self):
        screen.tracer(False)
        for cell in self.newstate - self.state:
            try:
                self.patches[cell].showturtle()
            except:
                pass
        for cell in self.state - self.newstate:
            try:
                self.patches[cell].hideturtle()
            except:
                pass
        screen.tracer(True)

    def clear(self):
        self.newstate = set()
        self.update_display()
        self.state = set()

    def toggle(self, x, y):
        cell = cellindices(x, y)
        self.newstate = self.state.copy()
        if cell in self.newstate:
            self.newstate.discard(cell)
        else:
            self.newstate.add(cell)
        self.update_display()
        self.state = self.newstate
         
    def run(self):
        starttime = time.clock()
        anzahl_generationen = 0
        screen.onkey(self.stop, "space")
        self.RUNNING = True
        while self.RUNNING:
            self.newstate = self.calcnext()
            self.update_display()
            self.state = self.newstate
            anzahl_generationen +=1
        stoptime = time.clock()
        t = stoptime - starttime
        print(anzahl_generationen, t, anzahl_generationen/t)

    def stop(self):
        self.RUNNING = False
        screen.onkey(self.run, "space")

def main():
    game=Game()
    return "EVENTLOOP"
    

if __name__ == "__main__":
    msg = main()
    print(msg)
    screen.mainloop()
