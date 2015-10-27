import pygtk
    6   pygtk.require('2.0')
    7   import gtk
    8   import operator
    9   import time
   10   import string
   11
   12   class DrawingAreaExample:
   13       def __init__(self):
   14           window = gtk.Window(gtk.WINDOW_TOPLEVEL)
   15           window.set_title("Drawing Area Example")
   16           window.connect("destroy", lambda w: gtk.main_quit())
   17           self.area = gtk.DrawingArea()
   18           self.area.set_size_request(400, 300)
   19           self.pangolayout = self.area.create_pango_layout("")
   20           self.sw = gtk.ScrolledWindow()
   21           self.sw.add_with_viewport(self.area)
   22           self.table = gtk.Table(2,2)
   23           self.hruler = gtk.HRuler()
   24           self.vruler = gtk.VRuler()
   25           self.hruler.set_range(0, 400, 0, 400)
   26           self.vruler.set_range(0, 300, 0, 300)
   27           self.table.attach(self.hruler, 1, 2, 0, 1, yoptions=0)
   28           self.table.attach(self.vruler, 0, 1, 1, 2, xoptions=0)
   29           self.table.attach(self.sw, 1, 2, 1, 2)
   30           window.add(self.table)
   31           self.area.set_events(gtk.gdk.POINTER_MOTION_MASK |
   32                                gtk.gdk.POINTER_MOTION_HINT_MASK )
   33           self.area.connect("expose-event", self.area_expose_cb)
   34           def motion_notify(ruler, event):
   35               return ruler.emit("motion_notify_event", event)
   36           self.area.connect_object("motion_notify_event", motion_notify,
   37                                    self.hruler)
   38           self.area.connect_object("motion_notify_event", motion_notify,
   39                                    self.vruler)
   40           self.hadj = self.sw.get_hadjustment()
   41           self.vadj = self.sw.get_vadjustment()
   42           def val_cb(adj, ruler, horiz):
   43               if horiz:
   44                   span = self.sw.get_allocation()[3]
   45               else:
   46                   span = self.sw.get_allocation()[2]
   47               l,u,p,m = ruler.get_range()
   48               v = adj.value
   49               ruler.set_range(v, v+span, p, m)
   50               while gtk.events_pending():
   51                   gtk.main_iteration()
   52           self.hadj.connect('value-changed', val_cb, self.hruler, True)
   53           self.vadj.connect('value-changed', val_cb, self.vruler, False)
   54           def size_allocate_cb(wid, allocation):
   55               x, y, w, h = allocation
   56               l,u,p,m = self.hruler.get_range()
   57               m = max(m, w)
   58               self.hruler.set_range(l, l+w, p, m)
   59               l,u,p,m = self.vruler.get_range()
   60               m = max(m, h)
   61               self.vruler.set_range(l, l+h, p, m)
   62           self.sw.connect('size-allocate', size_allocate_cb)
   63           self.area.show()
   64           self.hruler.show()
   65           self.vruler.show()
   66           self.sw.show()
   67           self.table.show()
   68           window.show()
   69
   70       def area_expose_cb(self, area, event):
   71           self.style = self.area.get_style()
   72           self.gc = self.style.fg_gc[gtk.STATE_NORMAL]
   73           self.draw_point(10,10)
   74           self.draw_points(110, 10)
   75           self.draw_line(210, 10)
   76           self.draw_lines(310, 10)
   77           self.draw_segments(10, 100)
   78           self.draw_rectangles(110, 100)
   79           self.draw_arcs(210, 100)
   80           self.draw_pixmap(310, 100)
   81           self.draw_polygon(10, 200)
   82           self.draw_rgb_image(110, 200)
   83           return True
   84
   85       def draw_point(self, x, y):
   86           self.area.window.draw_point(self.gc, x+30, y+30)
   87           self.pangolayout.set_text("Point")
   88           self.area.window.draw_layout(self.gc, x+5, y+50, self.pangolayout)
   89           return
   90
   91       def draw_points(self, x, y):
   92           points = [(x+10,y+10), (x+10,y), (x+40,y+30),
   93                     (x+30,y+10), (x+50,y+10)]
   94           self.area.window.draw_points(self.gc, points)
   95           self.pangolayout.set_text("Points")
   96           self.area.window.draw_layout(self.gc, x+5, y+50, self.pangolayout)
   97           return
   98
   99       def draw_line(self, x, y):
  100           self.area.window.draw_line(self.gc, x+10, y+10, x+20, y+30)
  101           self.pangolayout.set_text("Line")
  102           self.area.window.draw_layout(self.gc, x+5, y+50, self.pangolayout)
  103           return
  104
  105       def draw_lines(self, x, y):
  106           points = [(x+10,y+10), (x+10,y), (x+40,y+30),
  107                     (x+30,y+10), (x+50,y+10)]
  108           self.area.window.draw_lines(self.gc, points)
  109           self.pangolayout.set_text("Lines")
  110           self.area.window.draw_layout(self.gc, x+5, y+50, self.pangolayout)
  111           return
  112
  113       def draw_segments(self, x, y):
  114           segments = ((x+20,y+10, x+20,y+70), (x+60,y+10, x+60,y+70),
  115               (x+10,y+30 , x+70,y+30), (x+10, y+50 , x+70, y+50))
  116           self.area.window.draw_segments(self.gc, segments)
  117           self.pangolayout.set_text("Segments")
  118           self.area.window.draw_layout(self.gc, x+5, y+80, self.pangolayout)
  119           return
  120
  121       def draw_rectangles(self, x, y):
  122           self.area.window.draw_rectangle(self.gc, False, x, y, 80, 70)
  123           self.area.window.draw_rectangle(self.gc, True, x+10, y+10, 20, 20)
  124           self.area.window.draw_rectangle(self.gc, True, x+50, y+10, 20, 20)
  125           self.area.window.draw_rectangle(self.gc, True, x+20, y+50, 40, 10)
  126           self.pangolayout.set_text("Rectangles")
  127           self.area.window.draw_layout(self.gc, x+5, y+80, self.pangolayout)
  128           return
  129
  130       def draw_arcs(self, x, y):
  131           self.area.window.draw_arc(self.gc, False, x+10, y, 70, 70,
  132                                     0, 360*64)
  133           self.area.window.draw_arc(self.gc, True, x+30, y+20, 10, 10,
  134                                     0, 360*64)
  135           self.area.window.draw_arc(self.gc, True, x+50, y+20, 10, 10,
  136                                     0, 360*64)
  137           self.area.window.draw_arc(self.gc, True, x+30, y+10, 30, 50,
  138                                     210*64, 120*64)
  139           self.pangolayout.set_text("Arcs")
  140           self.area.window.draw_layout(self.gc, x+5, y+80, self.pangolayout)
  141           return
  142
  143       def draw_pixmap(self, x, y):
  144           pixmap, mask = gtk.gdk.pixmap_create_from_xpm(
  145               self.area.window, self.style.bg[gtk.STATE_NORMAL], "gtk.xpm")
  146
  147           self.area.window.draw_drawable(self.gc, pixmap, 0, 0, x+15, y+25,
  148                                          -1, -1)
  149           self.pangolayout.set_text("Pixmap")
  150           self.area.window.draw_layout(self.gc, x+5, y+80, self.pangolayout)
  151           return
  152
  153       def draw_polygon(self, x, y):
  154           points = [(x+10,y+60), (x+10,y+20), (x+40,y+70),
  155                     (x+30,y+30), (x+50,y+40)]
  156           self.area.window.draw_polygon(self.gc, True, points)
  157           self.pangolayout.set_text("Polygon")
  158           self.area.window.draw_layout(self.gc, x+5, y+80, self.pangolayout)
  159           return
  160
  161       def draw_rgb_image(self, x, y):
  162           b = 80*3*80*['\0']
  163           for i in range(80):
  164               for j in range(80):
  165                   b[3*80*i+3*j] = chr(255-3*i)
  166                   b[3*80*i+3*j+1] = chr(255-3*abs(i-j))
  167                   b[3*80*i+3*j+2] = chr(255-3*j)
  168           buff = string.join(b, '')
  169           self.area.window.draw_rgb_image(self.gc, x, y, 80, 80,
  170                                    gtk.gdk.RGB_DITHER_NONE, buff, 80*3)
  171           self.pangolayout.set_text("RGB Image")
  172           self.area.window.draw_layout(self.gc, x+5, y+80, self.pangolayout)
  173           return
  174
  175   def main():
  176       gtk.main()
  177       return 0
  178
  179   if __name__ == "__main__":
  180       DrawingAreaExample()
  181       main()
