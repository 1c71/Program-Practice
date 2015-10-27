import wx

class bucky(wx.Frame):
     
    def __init__(self, parent, id):
        wx.Frame.__init__(self, parent, id, 'Frame aka window', size=(300,200))
        panel = wx.Panel(self)
        
        
        #教你如何在界面上显示一段文本(静态文本)
        

        
        # 第3个参数是文本值, 第4个参数是x,y位置,这个例子中的意思是距离左边10,顶部50
        # 单位是像素。
        wx.StaticText(panel, -1, "this is static text", (10,30))

                                            #第5个参数(260,30)是文字的高宽,
                                            #如果你只想设置宽，让高保持原样
                                            #可以用-1, (260,-1)
        custom = wx.StaticText(panel, -1, "this is custom", (10,60), (260,30),
                                wx.ALIGN_CENTER)
                                #设置文本居中显示
                                
        # 设置文本颜色
        custom.SetForegroundColour('white')
        # 设置文本的背景颜色
        custom.SetBackgroundColour('blue')     




if __name__ == "__main__" :
     app = wx.PySimpleApp()
     frame = bucky(parent=None, id=-1)
     frame.Show()
     app.MainLoop()

















          
