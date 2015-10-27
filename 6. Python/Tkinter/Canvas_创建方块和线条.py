from Tkinter import *

master = Tk()

w = Canvas(master, width=200, height=100)
w.pack()

w.create_rectangle(50, 20, 150, 80, fill="#476042")
# 方块的位置是(50,20),宽高是(150,80)

w.create_line(0, 0, 50, 20, fill="#476042", width=3)
#线的起始点是(0,0) 终点是(50,20)

mainloop()
