from Tkinter import *
import Pmw
import sys


class MenuBarDemo( Frame ):
    

    def __init__( self ):
        
        Frame.__init__( self )
        Pmw.initialise()
        self.pack( expand = YES, fill = BOTH )
        self.master.title( "MenuBar Demo" )
        self.master.geometry( "500x200" )
        
        self.myBalloon = Pmw.Balloon( self )
        # 创建了myBalloon, 这是一个Pmw Balloon组件
        
        self.choices = Pmw.MenuBar( self, balloon = self.myBalloon )
        # 创建了一个MenuBar, 名为choices. balloon选项指定将一个Balloon组件与菜单项连接到一起.

        self.choices.pack( fill = X )


	# 添加 文件 菜单和菜单项
        self.choices.addmenu( "File", "Exit" )
        # 第一个参数是菜单名称, 第二个参数是鼠标悬浮在上面的时候显示的title
        self.choices.addmenuitem( "File", "command",
                                  command=self.closeDemo,
                                  label="Exit" )
        # 调用addmenuitem方法,在File菜单里插入一个command菜单项.
        # 该方法需要2个参数: 菜单项所属菜单的名称, 以及菜单项的类型.
        # 方法的 关键字参数label指定了菜单项的文本, 关键字参数command指定了菜单项的回调方法.



	# 添加 格式 菜单和菜单项
        self.choices.addmenu( "Format", "Change font/color" )
        
        self.choices.addcascademenu( "Format", "Color" )
        # addcascademenu方法, 在现有菜单中添加一个子菜单.
        # 该方法需要2个参数: 子菜单所属的菜单名称, 以及子菜单的文本
        
        self.choices.addmenuitem( "Format", "separator" )
        # 添加了一个separator菜单, 这个菜单实际是一条横线, 用于分隔Color和Font这2个子菜单

        self.choices.addcascademenu( "Format", "Font" )


#tips1: 菜单项按照他们添加的顺序出现. 因此, 务必按正确顺序添加.
#tips2: 菜单通常按照添加的顺序从左到右排列



	# 添加元素到 格式/颜色 菜单
        colors = [ "Black","Blue","Red","Green" ]
        # 定义一个颜色选项列表

        self.selectedColor = StringVar()
        self.selectedColor.set( colors[0] )
        # 创建了一个StringVar对象(名为selectedColor), 并初始化成颜色列表的第一个元素
        


        for item in colors:
            self.choices.addmenuitem( "Color", "radiobutton",
                                      label = item,
                                      command = self.changeColor,
                                      variable = self.selectedColor )

        # 针对颜色列表中的每一项, 都为Color子菜单添加一个radiobutton菜单项
        # 注意, 所有radiobutton菜单项都共享同一个回调方法(changeColor),和同一个变量(selectedColor)
        # 一旦用户选择一个菜单项, selectedColor的值就会变成该项的文本值
        # selectedColor变量是同一组内所有radiobutton菜单项共用的

        

	# 添加元素到 格式/字体 菜单
        fonts = [ "Times","Courier","Helvetica" ]
        self.selectedFont = StringVar()
        self.selectedFont.set( fonts[ 0 ] )


        for item in fonts:
            self.choices.addmenuitem( "Font", "radiobutton",
                                      label = item,
                                      command = self.changeFont,
                                      variable = self.selectedFont )


	# 添加 水平线 到 字体菜单
        self.choices.addmenuitem( "Font", "separator" )


        self.boldOn = BooleanVar()
        self.choices.addmenuitem( "Font", "checkbutton",
                                  label = "Bold",
                                  command = self.changeFont,
                                  variable = self.boldOn )
        # 用户选择该选项，则BooleanVar的值会变成1, 否则为0
	

        self.italicOn = BooleanVar()
        self.choices.addmenuitem ( "Font", "checkbutton",
                                   label="Italic",
                                   command = self.changeFont,
                                   variable = self.italicOn )




        self.display = Canvas( self, bg = "white")
        # 创建一个画布组件,名为display,有一个白色背景
        # Canvas会显示一个 “画布项目”, 它实际上是一个可在Canvas组件上描绘的对象(比如字符串或形状)


        
        self.display.pack( expand = YES, fill = BOTH )

        self.sampleText = self.display.create_text( 250, 100,
                                                    text = "Sample Text",
                                                    font = "Times 48" )
        # create_text方法可创建一个画布文本项目. 该方法在display上描绘文本"Sample Text"



    def changeColor( self ):

        self.display.itemconfig( self.sampleText,fill = self.selectedColor.get() )
 
    # 如果用户选择了一个Color 菜单项, changeColor 方法会配饰 sampleText,
    # 使用 selectedColor 的值对 sampleText 进行填充(上色)处理. 
    # itemconfig方法对Canvas上的项目进行配置. 通过指定fill选项,可以将sampleText的颜色设置为所选颜色.


        
       
    def changeFont( self ):

        newFont = self.selectedFont.get() + " 48"
        
        if self.boldOn.get():
            newFont += " bold"

        if self.italicOn.get():
            newFont += " italic"

        self.display.itemconfig( self.sampleText, font = newFont )



    def closeDemo( self ):
        sys.exit()






def main():
    MenuBarDemo().mainloop()

if __name__ == "__main__":
    main()

    
