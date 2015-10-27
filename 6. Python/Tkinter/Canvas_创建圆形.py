from Tkinter import *

canvas_width = 190
canvas_height =150

master = Tk()

w = Canvas(master, 
           width=canvas_width, 
           height=canvas_height)
w.pack()

w.create_oval(50,10,100,200)
# 位置是50,10  宽和高是100,200

mainloop()
