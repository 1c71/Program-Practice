from Tkinter import *

class PackDemo ( Frame ):
    
    def __init__( self ):
        ''' 创建4个pack选项不同的按钮 '''
	
        Frame.__init__( self )
        self.master.title( "Packing Demo" )
        self.master.geometry( "600x250" )
        self.pack (expand = YES, fill = BOTH )
        
	
        self.button1 = Button( self, text = "Add Button",
                               command = self.addButton )
	# command参数指定了用户在选择按钮后要执行的事件处理程序
        self.button1.pack( side = TOP )
        # 按钮在最上, 保持原大小


        self.button2 = Button( self, text = " bt2 Expand = NO, fill = BOTH " )
        self.button2.pack( side = BOTTOM, fill = BOTH )
        #按钮在底部，占据XY方向上分配的全部空间
        

        self.button3 = Button( self, text = "bt3 Expand = YES, fill = X " )
        self.button3.pack( side = LEFT, expand = YES, fill = X )
        # 在左边,  组件会自动扩展, 填充容器中任何额外的空间。在X方向上


        self.button4 = Button( self, text = "bt4 Expand = YES, fill = Y " )
        self.button4.pack( side = RIGHT, expand = YES, fill = Y )
        # 在右侧， 组件会自动扩展, 填充容器中任何额外的空间。在Y方向上

    def addButton( self ):
        Button( self, text = "New Button" ).pack( pady=5 )

    
def main():
    PackDemo().mainloop()


if __name__ == "__main__":
    main()
