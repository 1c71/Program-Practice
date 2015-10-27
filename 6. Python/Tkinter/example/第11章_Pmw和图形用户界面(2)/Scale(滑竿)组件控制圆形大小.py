from Tkinter import *

class ScaleDemo( Frame ):

     def __init__(self):

          Frame.__init__(self)
          self.pack( expand = YES, fill = BOTH )
          self.master.title("Scale Demo")
          self.master.geometry( "220x270" )



          self.control = Scale( self, from_ = 0, to = 200,
                                orient=HORIZONTAL, command=self.updateCircle)
          # orient选项(HORIZONTAL或VERTICAL)决定了新的Scale实例的方向.
          # from_和to选项指定了最小值和最大值
          # 回调方法是updateCircle.移动滑块改变数值时,就会执行这个方法

          self.control.pack(side=BOTTOM,fill=X)
          self.control.set(10)
          # 将control设为10,所以程序启动时, 直径为10的一个圆会出现在屏幕上.


          self.display = Canvas( self, bg="white" )
          self.display.pack( expand = YES, fill=BOTH )



     # 拖动滑块时, 会执行updateCircle方法. 回调方法的参数是Scale的当前值(表示成一个字符串)
     def updateCircle(self, scaleValue ):

          end = int(scaleValue)+10
          # 转换成整数值,再+10

          self.display.delete("circle")
          # delete方法先删除旧的圆. 需要取得1个参数,
          # 可能是一个"item handle",也可能是一个"tag"
          # item handle是用于对新描绘项目进行标识的整数值
          # 而tag是可在创建时连接到画布项目的一个名称.

     
          self.display.create_oval(10,10,end,end,
                                   fill="red",
                                   tags="circle")

          # 想要把tag和画布项目连接到一起, 应向项目的create方法的tags选项传递一个字符串值

          #create_oval方法描绘一个椭圆,坐标是10,10,end,end. fill选项为"red".

          # 注意,Canvas的create_item方法负责创建具体的画布项目,其中item要替换成具体的项目名称,
          # 比如, arc, line, oval, rectangele, polygon, image, bitmap, text和window
          

def main():
     ScaleDemo().mainloop()

if __name__ == "__main__":
     main()




















