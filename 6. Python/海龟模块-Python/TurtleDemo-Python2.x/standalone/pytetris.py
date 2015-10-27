"""       turtle-example-suite:

   standalone application: pytetris.py

Author: Gregor Lingl
Version: 0.9

Needs some streamlining,
but you can play it already!
"""

from turtle import Screen, Turtle, Vec2D, mainloop
from random import randint
from time import sleep, time # clock

COLUMNS = 8
ROWS = 20
BLOCKWIDTH = 35

BRICKS_ = { 1: ("red",    ((0,-1), (1,-1), (0,0), (1,0))),
            2: ("blue",   ((-1,0), (0,0), (1,0), (2,0))),
            3: ("green",  ((-1,0), (0,0), (1,0), (0,-1))),
            4: ("orange", ((0,-1), (0,0), (1,0), (1,1))),
            5: ("yellow", ((1,-1), (0,0), (1,0), (0,1))),
            6: ("magenta",((-1,0), (0,0), (1,0), (-1,-1))),
            7: ("cyan",   ((-1,0), (0,0), (1,0), (1,-1)))
          }

class TetrisBoard(object):
    def __init__(self, cols, rows):
        self.cols, self.rows = cols, rows
        self.screen = Screen()
        self.screen.screensize(BLOCKWIDTH*cols-50, BLOCKWIDTH*rows-50)
        self.screen.setup(BLOCKWIDTH*cols+12, BLOCKWIDTH*rows+12)
        self.screen.title("Turtle Tetris")
        self.screen.bgcolor("black")
        self.writer = Turtle()
        self.writer.ht()        
        self.label = None
        self.grid = {}
        self.screen.tracer(False)
        for row in range(rows):
            for col in range(cols):
                self.grid[(col, row)] = TetrisTurtle(col, row)
        self.screen.tracer(True)
        self.brick = TetrisBrick(self)
        self.result = 0
        self.LEVEL = 0.6
        self.keybuffer = KeyBuffer(self.screen,
                            ["Right", "Left", "Up", "Down", "space", "Escape"])
        self.reset()
        self.screen.listen()
        self.t1 = time()
        
    def reset(self):
        self.result = 0
        self.LEVEL = 0.600
        self.screen.tracer(False)
        self.writer.clear()
        if self.label:
            self.writer.clearstamp(self.label)
        for x in range(COLUMNS):
            for y in range(ROWS):
                self.grid[(x,y)].fillcolor("")
        self.screen.tracer(True)
        self.state = "NEWBRICK"
        
    def blink(self, y, n=1):
        for _ in range(n):
            for color in ("white", "black"):
                self.screen.tracer(False)
                for x in range(COLUMNS):
                    self.grid[(x,y)].pencolor(color)
                    sleep(self.LEVEL/10.0)
                self.screen.tracer(True)
            
    def display_result(self):
        tb = self
        tb.writer.color("white", "gray20")
        tb.writer.shape("square")
        tb.writer.shapesize(5, 15)
        tb.writer.goto(-4 ,0)
        self.label = tb.writer.stamp()
        tb.writer.goto(-2,3)
        tb.writer.write(str(tb.result) + " rows!",
                        align="center", font = ("Courier", 24, "bold") )
        tb.writer.goto(-2,-22)
        tb.writer.write("New game : <spacebar>",
                        align="center", font = ("Courier", 16, "bold") )
        tb.writer.goto(-2,-42)
        tb.writer.write("Quit : <escape>",
                        align="center", font = ("Courier", 16, "bold") )
        
    def getcolor(self, col, row):
        return self.grid[(col, row)].fillcolor()
    def setcolor(self, col, row, color):
        return self.grid[(col, row)].fillcolor(color)
    def rowfree(self, row):
        return not any([self.getcolor(col, row) for col in range(COLUMNS)])
    def rowfull(self, row):
        return all([self.getcolor(col, row) for col in range(COLUMNS)])

    def cleanup(self, shp):
        try:
            ymax = max([y for (x,y) in shp])
        except ValueError:
            self.state = "FINIS"
            return
        currenty = ymax
        while currenty > 0:
            if self.rowfull(currenty):
                self.blink(currenty, 2)
                self.result += 1
                if self.result == 8:
                    self.LEVEL = 0.4
                elif self.result == 20:
                    self.LEVEL = 0.25
                y = currenty
                while True:
                    self.screen.tracer(False)
                    for c in range(COLUMNS):
                        self.setcolor(c, y, self.getcolor(c, y-1))
                    self.screen.tracer(True)
                    if self.rowfree(y):
                        break
                    else:
                        y -= 1
            else:
                currenty -= 1
        tetris.state = "NEWBRICK"

    def run(self):
        tb = self
        b = self.brick
        ### actions to be done unconditionally
        if tb.state == "NEWBRICK":
            if b.reset():
                self.t1 = time()
                tb.state = "FALL"
            else:
                tb.state = "FINIS"
        t2 = time()
        if tb.state == "FALL" and t2 - self.t1 > self.LEVEL:
            b.down()
            b.apply("Step")
            self.t1 = t2
        ### actions bound to key events
        key = self.keybuffer.getkey()
        if key:
            if tb.state == "FALL":
                if key == "Left":
                    b.shiftleft()
                elif key == "Right":
                    b.shiftright()
                elif key == "Down":
                    b.drop()
                    tb.state = "CLEANUP"
                elif key == "Up":
                    b.turn()
                elif key == "space":
                    tb.state = "BREAK"
                b.apply(key)
            elif tb.state == "BREAK":
                if key == "space":
                    tb.state = "FALL"
            elif tb.state == "ADE":
                if key == "space":
                    tb.reset()
                    tb.state = "NEWBRICK"
                elif key == "Escape":
                    tb.screen.bye()
                
        if tb.state == "CLEANUP":
            tb.cleanup(b.shape1)
        if tb.state == "FINIS":
            tb.display_result()
            tb.state = "ADE"
        self.screen.ontimer(self.run, 100)    

class KeyBuffer(object):
    def __init__(self, board, used_keys):
        self.board = board
        for key in used_keys:
            self.board.onkey(lambda x=key: self.add(x), key)
        self.buffer = []
    def add(self, key):
        self.buffer.append(key)
    def getkey(self):
        if self.buffer:
            return self.buffer.pop(0)
        else:
            return None

class TetrisTurtle(Turtle):
    def __init__(self, col, row):
        Turtle.__init__(self)
        self.speed(0)
        self.pu()
        self.shape("square")
        self.color("black", "")
        self.shapesize((BLOCKWIDTH-1)/20., (BLOCKWIDTH-1)/20., 1)
        self.goto(-COLUMNS*BLOCKWIDTH/2+14+col*BLOCKWIDTH, ROWS*BLOCKWIDTH/2 - 14 - row*BLOCKWIDTH)

class TetrisBrick(object):
    def __init__(self, board):
        self.board = board
        self.brick_type = None
        self.index = 0
        self.shape1 = ()
        self.shape2 = ()
        self.checked = True
    def reset(self):
        data = BRICKS_[randint(1,7)]
        self.color = data[0]
        self.shapetype = [Vec2D(*x) for x in data[1]]
        self.pos = Vec2D(COLUMNS//2-1, 1) 
        if self.check(self.pos, self.shapetype):
            self.board.state = "FALL"
            self.shape1 = [self.pos + x for x in self.shapetype]
            self.apply(None)
            return True
        else:
            self.board.state = "FINIS"
            self.shape1 = ()
            return False
    def turn(self):
        newshape = [(-y,x) for (x,y) in self.shapetype]
        if self.check(self.pos, newshape):
            self.shapetype = newshape
    def shiftright(self):
        newpos = self.pos + Vec2D(1,0)
        if self.check(newpos, self.shapetype):
            self.pos = newpos 
    def shiftleft(self):
        newpos = self.pos + Vec2D(-1,0)
        if self.check(newpos, self.shapetype):
            self.pos = newpos 
    def down(self):
        newpos = self.pos + Vec2D(0,1)
        if self.check(newpos, self.shapetype):
            self.pos = newpos
        else:
            pass
    def drop(self):
        pos = self.pos
        falling = True
        while falling:
            pos = pos + Vec2D(0,1)
            falling = self.check(pos, self.shapetype)
        self.pos = pos + Vec2D(0,-1)
            
    def apply(self, ev):
        self.shape2 = [self.pos + x for x in self.shapetype]            
        self.board.screen.tracer(False)
        for x, y in self.shape1:
            self.board.setcolor(x, y, "")            
        for x, y in self.shape2:
            self.board.setcolor(x, y, self.color)
        self.board.screen.tracer(True)
        self.shape1 = self.shape2
        if ev == "Step":
            if not self.checked:
                self.board.cleanup(self.shape1)    
                if self.board.state != "FINIS":
                    self.shape1 = ()
                    self.reset()
    def check(self, pos, shp):
        ok = True
        brickpos = [pos + x for x in shp]
        for c in brickpos:
            if c not in self.board.grid:
                self.checked = False
                return False
            if c not in self.shape1 and self.board.getcolor(*c):
                self.checked = False
                return False
        self.checked = True
        return True

if __name__ == "__main__":
    tetris = TetrisBoard(COLUMNS, ROWS)
    tetris.run()
    mainloop()

