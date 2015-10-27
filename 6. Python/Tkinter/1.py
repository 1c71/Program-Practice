from Tkinter import *       

class Application(Frame):              
    def __init__(self, master=None):
        Frame.__init__(self, master)   
        self.grid()
        # 必须要这一行才能显示到屏幕上
        self.createWidgets()

    def createWidgets(self):
        self.quitButton = Button ( self, text='Quit',
            command=self.quit )        
        self.quitButton.grid()
        # 把这个按钮放到屏幕上

app = Application()                    
app.master.title("Sample application") 
app.mainloop()      
