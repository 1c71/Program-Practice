from Tkinter import *
import Pmw

class CopyTextWindow( Frame ):
    
    def __init__(self):
        Frame.__init__( self )
        Pmw.initialise()
        self.pack( expand = YES,fill = BOTH )
        self.master.title( "ScrooledText Demo" )

        self.text1 = Pmw.ScrolledText( self,
                                       text_width=25,
                                       text_height=12,
                                       text_wrap=WORD,
                                       hscrollmode="static",
                                       vscrollmode = "static" )
	# 创建了一个25列,12行的text子组件. text_wrap选项决定了过长的文本是否自动换行.
	# 如果被设为NONE(默认值), 就不显示超过限制的文本, 只显示组件宽度范围内的文本
	# 设为CHAR, 会以字符为最小单位进行断行
	# 设为WORD, 则以单词为最小单位进行断行(即只在制表符和空格等空白字符处进行断行)

        self.text1.pack( side=LEFT, expand=YES, fill = BOTH,
                         padx = 5,
                         pady = 5 )


        self.copyButton = Button( self, text= "Copy >>>",
                                  command = self.copyText )
	# 绑定了回调方法copyText, 单击按钮会被触发

        self.copyButton.pack( side = LEFT, padx = 5,pady = 5 )


        self.text2 = Pmw.ScrolledText( self,
                                      text_state = DISABLED,
                                      text_width =25,
                                      text_height= 12,
                                      text_wrap = WORD,
                                      hscrollmode = "static",
                                      vscrollmode="static" )
	# text_state选项设为DISABLED, 它禁止insert和delete调用, 使得这个文本区域不可编辑

        self.text2.pack( side = LEFT,
                         expand = YES,
                         fill=BOTH,
                         padx=5,
                         pady=5 )

    
    def copyText(self):
        self.text2.settext( self.text1.get( SEL_FIRST, SEL_LAST) )
	# settext方法删除组件中的当前文本, 再插入作为一个参数由方法接收的文本.
	# 如果用户没有选定文本, 会产生一个TelError异常.
	# 调用get方法获得text1中选定的文本.
	# 这个范围开始于选定文本的起始处(SEL_FIRST), 终止于选定文本的结束处(SEL_LAST)


def main():
    CopyTextWindow().mainloop()

if __name__  == "__main__":
    main()
