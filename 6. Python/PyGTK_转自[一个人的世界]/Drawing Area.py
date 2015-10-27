import pygtk
pygtk.require('2.0')
import gtk

class DrawingArea:
    def __init__(self):
        window = gtk.Window()
        window.set_default_size(380, 220)
           
        self.drawingarea = gtk.DrawingArea()
        self.pangolayout = self.drawingarea.create_pango_layout("")
        
        window.connect("destroy", lambda w: gtk.main_quit())
        self.drawingarea.connect("expose-event", self.area_expose_cb)
        
        window.add(self.drawingarea)
        window.show_all()

    def area_expose_cb(self, area, event):
        self.style = self.drawingarea.get_style()
        self.gc = self.style.fg_gc[gtk.STATE_NORMAL]
        self.draw_point(10,10)
        self.draw_points(110, 10)
        self.draw_line(210, 10)
        self.draw_lines(310, 10)
        self.draw_segments(10, 110)
        self.draw_rectangles(110, 110)
        self.draw_arcs(210, 110)
        self.draw_polygon(310, 110)

    def draw_point(self, x, y):
        self.drawingarea.window.draw_point(self.gc, x+30, y+30)
        self.pangolayout.set_text("Point")
        self.drawingarea.window.draw_layout(self.gc, x+5, y+50, self.pangolayout)

    def draw_points(self, x, y):
        points = [(x+10,y+10), (x+10,y), (x+40,y+30), (x+30,y+10), (x+50,y+10)]
        self.drawingarea.window.draw_points(self.gc, points)
        self.pangolayout.set_text("Points")
        self.drawingarea.window.draw_layout(self.gc, x+5, y+50, self.pangolayout)

    def draw_line(self, x, y):
        self.drawingarea.window.draw_line(self.gc, x+10, y+10, x+20, y+30)
        self.pangolayout.set_text("Line")
        self.drawingarea.window.draw_layout(self.gc, x+5, y+50, self.pangolayout)

    def draw_lines(self, x, y):
        points = [(x+10,y+10), (x+10,y), (x+40,y+30), (x+30,y+10), (x+50,y+10)]
        self.drawingarea.window.draw_lines(self.gc, points)
        self.pangolayout.set_text("Lines")
        self.drawingarea.window.draw_layout(self.gc, x+5, y+50, self.pangolayout)

    def draw_segments(self, x, y):
        segments = ((x+20,y+10, x+20,y+70), (x+60,y+10, x+60,y+70), (x+10,y+30 , x+70,y+30), (x+10, y+50 , x+70, y+50))
        self.drawingarea.window.draw_segments(self.gc, segments)
        self.pangolayout.set_text("Segments")
        self.drawingarea.window.draw_layout(self.gc, x+5, y+80, self.pangolayout)

    def draw_rectangles(self, x, y):
        self.drawingarea.window.draw_rectangle(self.gc, False, x, y, 80, 70)
        self.drawingarea.window.draw_rectangle(self.gc, True, x+10, y+10, 20, 20)
        self.drawingarea.window.draw_rectangle(self.gc, True, x+50, y+10, 20, 20)
        self.drawingarea.window.draw_rectangle(self.gc, True, x+20, y+50, 40, 10)
        self.pangolayout.set_text("Rectangles")
        self.drawingarea.window.draw_layout(self.gc, x+5, y+80, self.pangolayout)

    def draw_arcs(self, x, y):
        self.drawingarea.window.draw_arc(self.gc, False, x+10, y, 70, 70, 0, 360*64)
        self.drawingarea.window.draw_arc(self.gc, True, x+30, y+20, 10, 10, 0, 360*64)
        self.drawingarea.window.draw_arc(self.gc, True, x+50, y+20, 10, 10, 0, 360*64)
        self.drawingarea.window.draw_arc(self.gc, True, x+30, y+10, 30, 50, 210*64, 120*64)
        self.pangolayout.set_text("Arcs")
        self.drawingarea.window.draw_layout(self.gc, x+5, y+80, self.pangolayout)

    def draw_polygon(self, x, y):
        points = [(x+10,y+60), (x+10,y+20), (x+40,y+70), (x+30,y+30), (x+50,y+40)]
        self.drawingarea.window.draw_polygon(self.gc, True, points)
        self.pangolayout.set_text("Polygon")
        self.drawingarea.window.draw_layout(self.gc, x+5, y+80, self.pangolayout)

DrawingArea()
gtk.main()
