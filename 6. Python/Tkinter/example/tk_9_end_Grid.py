from Tkinter import *

class GridDemo ( Frame ):
    
    def __init__( self ):
	
        Frame.__init__( self )
	# Frame 构造函数, 允许基类执行在添加组件之前需要的初始化操作.

        self.master.title( "Grid Demo" )
        self.master.rowconfigure( 0, weight = 1 )
        self.master.columnconfigure( 0, weight = 1 )
        self.grid( sticky = W+E+N+S )

        self.text1 = Text( self, width = 15, height = 5 )

        self.text1.grid( rowspan=3, sticky=W+E+N-S )
        self.text1.insert(INSERT, "Text1")

        self.button1 = Button( self, text = "Button 1", width=25 )
        self.button1.grid( row=0, column=1, columnspan=2, sticky=W+E+N+S )

        self.button2 = Button( self, text = "Button 2" )
        self.button2.grid( row=1, column=1, sticky=W+E+N+S )
   
        self.button3 = Button( self, text = "Button 3" )
        self.button3.grid( row=1, column=1, sticky=W+E+N+S )

        self.button4 = Button( self, text = "Button 4" )
        self.button4.grid( row=2, column=1, columnspan=2, sticky=W+E+N+S )

        self.entry = Entry(self)
        self.entry.grid( row=3, columnspan=2, sticky=W+E+N+S )
        self.entry.insert( INSERT, "Entry" )

        self.text2 = Text(self, width=2, height=2 )
        self.text2.grid(row=3,column=2,sticky=W+E+N+S)
        self.text2.insert( INSERT, "Text2" )

        self.rowconfigure(1,weight=1)
        self.columnconfigure(1,weight=1)


def main():
    GridDemo().mainloop()


if __name__ == "__main__":
    main()
