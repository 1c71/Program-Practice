from Tkinter import *

class KeyDemo ( Frame ):
    
    def __init__( self ):
        ''' 创建2个Label, 并绑定键盘事件 '''

        Frame.__init__( self )
        # 调用基类的构造函数，它会为整个应用程序创建一个顶级组件，并初始化Frame。

        self.pack( expand = YES, fill = BOTH )
        # pack方法将组件放入父容器, 参数fill指定组件应占多大空间

        # 参数fill, 可选值有 X(所有可用的水平空间),  Y(所有可用的垂直空间),
        # BOTH(同时包括水平和垂直空间),  以及NONE(默认值-不占任何额外空间)

        # 参数expand指定子组件是否应该占用父组件中任何多余的空间(即未被其他组件占用的空间)
        # 可选值有 YES(扩充以占据多余空间) 或NO(不进行扩充)

        # keystroke - 按键
        self.master.title( " Keystroke Events " )

        self.master.geometry( "350x100" )
        # geometry方法配置以像素为单位, 指定顶级组件的长度和宽度



        self.message1 = StringVar()
        self.line1 = Label( self, textvariable = self.message1 )
        self.message1.set( "Type and key or shift" )
        self.line1.pack()


        self.message2 = StringVar()
        self.line2 = Label( self, textvariable = self.message2 )
        self.message2.set( "" )
        self.line2.pack()

	# 按下任意键时
        self.master.bind( "<KeyPress>", self.keyPressed )
	
	# 松开任意键时
        self.master.bind( "<KeyRelease>", self.keyReleased )
        
	# 按下左shift键盘时
        self.master.bind( "<KeyPress-Shift_L>", self.shiftPressed )

	# 松开左shift键盘时
        self.master.bind( "<KeyRelease-Shift_L>", self.shiftReleased )
	# 注意, 并不是所有系统都能区分 左右 Shift 键

    def keyPressed( self, event ):
        self.message1.set( "Key pressed: " + event.char )
        self.message2.set( "This key is not left shift" )
	# 这个键不是左shift键


    def keyReleased( self, event ):
        self.message1.set( "Key released: " + event.char )
        self.message2.set( "This key is not left shift" )


    def shiftPressed( self, event ):
        self.message1.set( "Shift pressed" )
        self.message2.set( "This key is left shift" )   
        

    def shiftReleased( self, event ):
        self.message1.set( "Shift Released" )
        self.message2.set( "This key is left shift" )     




def main():
    KeyDemo().mainloop()


if __name__ == "__main__":
    main()
