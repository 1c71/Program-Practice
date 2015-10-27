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

# MAX_X and MAX_Y must be odd
MAX_X = 79
MAX_Y = 57
SQUARE_WIDTH = 10 # must be even
FREEROWS = 3
WINHEIGHT = MAX_Y + FREEROWS
MARG_X = 2 + SQUARE_WIDTH//2   
MARG_Y = 8
DM = 10

screen = Screen()

def coords(col, row):
	return ((-MAX_X//2 + col)*SQUARE_WIDTH + MARG_X,
                ((-MAX_Y+ FREEROWS)//2  + row )*SQUARE_WIDTH + MARG_Y)

def cellindices(x, y):
    return ((x-MARG_X + (SQUARE_WIDTH-1)//2)//SQUARE_WIDTH + MAX_X//2 + 1,
            (y-MARG_Y + (SQUARE_WIDTH-1)//2)//SQUARE_WIDTH + (MAX_Y- FREEROWS)//2)

def calccolor(i):
    i = min(20, i)
    return (1.05-i/20., 0., i/20.-0.05)
    
def generate(state):
    NBADDR = ((-1,-1),(-1,0),(-1,1),(0,-1),(0,1),(1,-1),(1,0),(1,1))
    while True:
        yield state
        cd = {}
        for (x,y) in state:
            for dx, dy in NBADDR:
                xx, yy = x+dx, y+dy
                cd[(xx,yy)] = cd.get((xx,yy), 0) + 1
            cd[(x,y)] = cd.get((x,y), 0) + 10
        cells = [c for c in cd if cd[c] in (3,12,13)]
        state1 = {c:1 for c in cells if c not in state}
        for c in cells:
            if c in state:
                state1[c] = state[c]+1
        state = state1


class Patch(Turtle):
    def __init__(self, col, row):
        Turtle.__init__(self, shape="square", visible=False)
        self.pu()
        self.goto(coords(col, row))
        self.color("black")
        self.shapesize((SQUARE_WIDTH-2)/20.0)
        
        
class Game(object):

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
        w2 = SQUARE_WIDTH // 2
        for c in range(MAX_X+1):
            x1, y1 = coords(c,0)
            x2, y2 = coords(c, MAX_Y)
            x1, y1, y2 = x1 - w2, y1 - w2, y2 - w2
            self.line(x1, y1, x1, y2)
        for r in range(MAX_Y+1):
            x1, y1 = coords(0, r)
            x2, y2 = coords(MAX_X, r)
            x1, y1, x2 = x1 - w2, y1 - w2, x2 - w2
            self.line(x1, y1, x2, y1)
        screen.update()
        self.patches = {}
        for r in range(MAX_Y):
            for c in range(MAX_X):
                self.patches[(c, r)] = Patch(c, r)

        self.state = {(41,33):1, (42,33):1, (43,34):1,
                      (42,32):1, (42,34):1}
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

    def update_display(self):
        screen.tracer(False)
        for cell in self.state:
            if cell not in self.newstate:
                try:
                    self.patches[cell].hideturtle()
                except KeyError:
                    pass
        for cell in self.newstate:
            try:
                self.patches[cell].showturtle()
                self.patches[cell].color(calccolor(self.newstate[cell]))
            except KeyError:
                pass
        screen.tracer(True)

    def clear(self):
        self.newstate = {}
        self.update_display()
        self.state = {}

    def toggle(self, x, y):
        cell = cellindices(int(x), int(y))
        self.newstate = self.state.copy()
        if cell in self.newstate:
            del self.newstate[cell]
        else:
            self.newstate[cell] = 1
        self.update_display()
        self.state = self.newstate
         

    def run(self):
        starttime = time.clock()
        anzahl_generationen = 0
        screen.onkey(self.stop, "space")
        generation = generate(self.state)
        self.RUNNING = True
        while self.RUNNING:
            self.newstate = next(generation)
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
