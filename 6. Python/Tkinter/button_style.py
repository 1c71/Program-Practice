import Tkinter
import ttk

root = Tkinter.Tk()

ttk.Style().configure("TButton", padding=10, relief="flat",
   background="#f96")

btn = ttk.Button(text="Sample", style="TButton")
btn.pack()

root.mainloop()
