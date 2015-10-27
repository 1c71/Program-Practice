from Tkinter import *

class PopupMenuDemo( Frame ):

     def __init__( self ):

          Frame.__init__( self )
          self.pack( expand = YES, fill = BOTH )
          self.master.title( "Popup Menu Demo" )
          self.master.geometry( "300x200" )


          self.frame1 = Frame( self, bg="white" )
	  # Frame构造函数的bg选项指定了Frame背景色的一个字符串.

          self.frame1.pack( expand = YES, fill = BOTH )

          
	  
          self.menu = Menu( self.frame1,tearoff=0 )
	  # 创建了一个Tkinter的Menu组件, 名为menu
	  # tearoff选项设置为0, 会删除默认情况下作为 Menu 的第一项使用的虚线分隔符


          colors = [ "White","Blue","Yellow","Red" ]
          self.selectedColor = StringVar()
          self.selectedColor.set( colors[0] )


          for item in colors:
               self.menu.add_radiobutton(label = item,
                                         variable = self.selectedColor,
                                         command = self.changeBackgroundColor)

	  # 针对颜色列表的每一项, 为Menu添加相应的 radiobutton 菜单项
	  # 每个radiobutton都有相同的回调方法(changeBackgroundColor),和相同的变量(selectedColor)
          # 经过测试,选项的顺序不重要, variable选项和command选项可以互换位置.
	  

          self.frame1.bind( "<Button-3>",self.popUpMenu )
	  # 将popUpMenu方法绑定在frame1上发生的鼠标右键事件



     def popUpMenu( self, event ):
          self.menu.post( event.x_root, event.y_root )
	  # 调用menu的post方法, 从而在指定位置显示一个Menu
	  # post方法接收2个参数, 他们指定了顶级组件上的菜单显示位置.
	  # 事件属性 x_root 和 y_root 对应事件触发时鼠标指针的坐标.



     def changeBackgroundColor( self ):
          self.frame1.config( bg = self.selectedColor.get() )
     
     # 一旦选择某个radiobutton菜单项, 就会执行changeBackgroundColor方法.
     # 这个方法调用frame1的config方法, 将新的bg指定为selectedColor的值
     



def main():
     PopupMenuDemo().mainloop()

if __name__ == "__main__":
     main()
