from Tkinter import *

class CheckFont( Frame ):

    def __init__(self):
        ''' 创建1个Entry 和 2个Checkbuttons '''

        Frame.__init__(self)
        self.pack( expand = YES, fill = BOTH )
        self.master.title( "Checkbutton Demo" )

        self.frame1 = Frame( self )
        self.frame1.pack()

        self.text = Entry( self.frame1, width = 40, font = "Arial 10" )
        self.text.insert( INSERT, "Watch the font change" )
        self.text.pack( padx=5, pady=5 )
	
        self.frame2 = Frame( self )
        self.frame2.pack()

	# 创建布尔变量
        self.boldOn = BooleanVar()

	# 创建 "粗体" 复选框
        self.checkBold = Checkbutton( self.frame2, text="Bold",
                                      variable=self.boldOn,
                                      command = self.changeFont )
        self.checkBold.pack( side = LEFT, padx=5, pady=5 )

	# 创建布尔变量
        self.italicOn = BooleanVar()
	
	# 创建 "斜体" 复选框
        self.checkItalic = Checkbutton( self.frame2, text="Italic",
                                        variable=self.italicOn,
                                        command = self.changeFont )

        self.checkItalic.pack( side = LEFT, padx=5, pady=5 )
	
    def changeFont( self ):
        ''' 根据复选框改变字体 '''

        desiredFont = "Arial 10"

        if self.boldOn.get():
            desiredFont += " bold"

        if self.italicOn.get():
            desiredFont += " italic"

        self.text.config( font = desiredFont )



def main():
    CheckFont().mainloop()


if __name__ == "__main__":
    main()
