import pygtk
pygtk.require('2.0')
import gtk
class HBoxLC:
    def __init__(self):
        self.window = gtk.Window(gtk.WINDOW_TOPLEVEL)
        self.window.set_title("HBox Layout Container")
        self.window.set_size_request(300,250)
        self.window.set_position(gtk.WIN_POS_CENTER)
        self.window.connect("destroy", gtk.main_quit)
        hbox = gtk.HBox(False, 5)
        btn1 = gtk.Button("small")
        btn2 = gtk.Button("Big")
        btn2.set_size_request(200,150)
        hbox.add(btn1)
        hbox.add(btn2)
        self.window.add(hbox)
        self.window.show_all()
    def main(self):
        gtk.main()
if __name__ == "__main__":
    hbox = HBoxLC()
    hbox.main()
