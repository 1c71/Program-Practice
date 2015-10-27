from Tkinter import *

class MouseLocation ( Frame ):
    
    def __init__( self ):
        '''创建一个Label, 打包并绑定鼠标事件 '''

        Frame.__init__( self )
        # 调用基类的构造函数，它会为整个应用程序创建一个顶级组件，并初始化Frame。

        self.pack( expand = YES, fill = BOTH )
        # pack方法将组件放入父容器, 参数fill指定组件应占多大空间

        # 参数fill, 可选值有 X(所有可用的水平空间),  Y(所有可用的垂直空间),
        # BOTH(同时包括水平和垂直空间),  以及NONE(默认值-不占任何额外空间)

        # 参数expand指定子组件是否应该占用父组件中任何多余的空间(即未被其他组件占用的空间)
        # 可选值有 YES(扩充以占据多余空间) 或NO(不进行扩充)

        
        self.master.title( "Demonstrating Mouse Events" )

        self.master.geometry( "274x100" )
        # geometry方法配置以像素为单位, 指定顶级组件的长度和宽度



	
        self.mousePosition = StringVar()    # 显示鼠标位置
        self.mousePosition.set( "Mouse outside window" )
        self.positionLabel = Label( self, textvariable = self.mousePosition)
        self.positionLabel.pack( side = BOTTOM )


        self.bind( "<Button-1>", self.buttonPressed )
        # 鼠标左键被按下

        self.bind( "<ButtonRelease-1>", self.buttonReleased )
        # 鼠标左键松开
        
        self.bind( "<Enter>", self.enteredWindow )
        #鼠标指针进入组件上方
        
        self.bind( "<Leave>", self.exitedWindow )
        #鼠标指针离开组件上方
        
        self.bind( "<B1-Motion>", self.mouseDragged )
        #按住左键的同时，鼠标移动


    # 一些拼接字符串的函数
    def buttonPressed( self, event ):
        self.mousePosition.set( "Pressed at [ "
                                + str( event.x )
                                + ", "
                                + str( event.y )
                                + " ]" )

    def buttonReleased( self, event ):
        self.mousePosition.set("Released at [ "
                               + str( event.x )
                               + ", "
                               + str( event.y )
                               + " ]" )


    def enteredWindow( self, event ):
        self.mousePosition.set( "Mouse in window" )


    def exitedWindow( self, event ):
        self.mousePosition.set( "Mouse outside window " )


    def mouseDragged( self, event ):
        self.mousePosition.set("Dragged at [ "
                               + str( event.x )
                               + ", "
                               + str( event.y )
                               + " ]" )
        

def main():
    MouseLocation().mainloop()


if __name__ == "__main__":
    main()
