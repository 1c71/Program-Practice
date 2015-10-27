from Tkinter import *
from tkMessageBox import *

class PlainAndFancy( Frame ):

    def __init__(self):
        '''创建2个按钮, 打包并绑定事件'''

        Frame.__init__(self)
        self.pack( expand = YES, fill = BOTH )
        self.master.title( "Buttons" )

	# 创建一个文本按钮
        self.plainButton = Button(self, text = "plain Button",
                                  command = self.pressedPlain )
        self.plainButton.bind("<Enter>",self.rolloverEnter)
        self.plainButton.bind("<Leave>",self.rolloverLeave)
        self.plainButton.pack(side = LEFT, padx=5, pady=5) 

	# 创建一个图片按钮
        self.myImage = PhotoImage(file = "a.gif")
        self.fancyButton = Button(self,image = self.myImage,
                                  command = self.pressedFancy)
        self.fancyButton.bind("<Enter>",self.rolloverEnter)
        self.fancyButton.bind("<Leave>",self.rolloverLeave)
        self.fancyButton.pack(side = LEFT, padx=5,pady=5)

    
    def pressedPlain( self ):
        showinfo( "Message","you pressed : plain button" )

    def pressedFancy( self ):
        showinfo( "Message","you pressed : Fancy button" )

    def rolloverEnter( self, event ):
        event.widget.config( relief = GROOVE )

    def rolloverLeave( self, event ):
        event.widget.config( relief = RAISED )


def main():
    PlainAndFancy().mainloop()


if __name__ == "__main__":
    main()
