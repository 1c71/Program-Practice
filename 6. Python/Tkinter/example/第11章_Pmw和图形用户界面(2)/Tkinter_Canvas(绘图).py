
from Tkinter import *

class PaintBox( Frame ):


     def __init__( self ):

          Frame.__init__( self )
          self.pack( expand = YES, fill = BOTH )
          self.master.title( "A simple Paint program" )
          self.master.geometry( "300x150" ) 
          

          self.message = Label( self,
                                text = "Drag the mouse to draw" )
          self.message.pack( side = BOTTOM )


          self.myCanvas = Canvas( self )
          self.myCanvas.pack( expand = YES,fill = BOTH )

          self.myCanvas.bind("<B1-Motion>", self.paint)
          # <B1-Motion>千万不要忘记2个尖括号, 不然起不了作用, 血的教训啊...


     def paint( self, event ):
          
          x1, y1 = (event.x - 4),(event.y - 4)
          x2, y2 = (event.x + 4),(event.y + 4)
          self.myCanvas.create_oval(x1,y1,x2,y2, fill="black")
          # create_oval方法创建名为oval(椭圆)的一种"画布项目",
          # 它的半径是4,填充颜色为black,而且在当前鼠标位置居中




def main():
     PaintBox().mainloop()

if __name__ == "__main__":
     main()































