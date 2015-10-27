from Tkinter import *

# 大量注释都在笔记中，写在程序里太乱了.
class LabelDemo( Frame ):
     # LabelDemo类继承Frame类

     def __init__(self):
          Frame.__init__(self)
          # 调用基类的构造函数，它会为整个应用程序创建一个顶级组件，并初始化Frame。

          self.pack( expand = YES, fill = BOTH )
          self.master.title(" Labels ")


          self.Label1 = Label( self, text="Label with text" )
          self.Label1.pack()


          self.Label2 = Label( self,
                               text="Labels with text and a bitmap" )
          self.Label2.pack( side = LEFT )


          self.Label3 = Label( self, bitmap="warning")
          self.Label3.pack( side = LEFT )


def main():
     LabelDemo().mainloop()

if __name__ == "__main__":
     main()
