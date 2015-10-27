from Tkinter import *
import Pmw

class ImageSelection( Frame ):
    
    def __init__( self, images ):
        
        Frame.__init__( self )
        Pmw.initialise()
        self.pack( expand = YES, fill=BOTH )
        self.master.title( "select an image" )

        self.photos = []

        for item in images:
            self.photos.append( PhotoImage (file=item) )

        self.listBox = Pmw.ScrolledListBox(self,items=images,
                                           listbox_height=3,
                                           vscrollmode="static",
                                           selectioncommand = self.switchImage)
	
        self.listBox.pack( side=LEFT, expand=YES, fill=BOTH, padx=5, pady=5 )

        self.display = Label( self, image=self.photos[ 0 ] )
        self.display.pack( padx=5,pady=5 )


    def switchImage( self ) :     
        chosenPicture = self.listBox.curselection()

        if chosenPicture:
            choice = int( chosenPicture[0] )
            self.display.config( image = self.photos[choice] )



def main():
    images = ["1.gif","2.gif","3.gif","4.gif"]
    ImageSelection(images).mainloop()

if __name__ == "__main__":
    main()
