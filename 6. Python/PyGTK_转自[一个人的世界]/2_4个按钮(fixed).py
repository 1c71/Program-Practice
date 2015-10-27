import pygtk
pygtk.require('2.0')
import gtk
class FixedLC:
    def __init__(self):
        self.window = gtk.Window(gtk.WINDOW_TOPLEVEL)
        self.window.set_title("Fixed Layout Container")
        self.window.set_size_request(300,250)
        self.window.set_position(gtk.WIN_POS_CENTER)
        btn1 = gtk.Button("Button1")
        btn2 = gtk.Button("Button2")
        btn3 = gtk.Button("Button3")
        btn4 = gtk.Button(stock = gtk.STOCK_CLOSE)
        btn2.set_sensitive(False)
        btn3.set_size_request(80,40)
        fixed = gtk.Fixed()
        fixed.put(btn1, 30, 30)
        fixed.put(btn2, 150, 30)
        fixed.put(btn3, 30, 130)
        fixed.put(btn4, 150, 130)
        btn4.connect("clicked", gtk.main_quit)
        self.window.connect("destroy", gtk.main_quit)
        self.window.add(fixed)
        self.window.show_all()
    def main(self):
        gtk.main()
if __name__ == "__main__":
    fixedLC = FixedLC()
    fixedLC.main()
