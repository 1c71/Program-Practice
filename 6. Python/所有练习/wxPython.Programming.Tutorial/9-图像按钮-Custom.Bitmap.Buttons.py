import wx

class bucky(wx.Frame):
     
    def __init__(self, parent, id):
        wx.Frame.__init__(self, parent, id, 'Frame aka window', size=(300,400))
        panel = wx.Panel(self)
        
        #

        #如果是bmp图，后面就应该写TYPE_BMP
        pic = wx.Image("9.jpg", wx.BITMAP_TYPE_JPEG).ConvertToBitmap()
        #创建了一个位图按钮
        self.button = wx.BitmapButton(panel, -1, pic, pos=(10,10))
        #给按钮绑定事件
        self.Bind=(wx.EVT_BUTTON, self.doMe, self.button)
        
        self.button.SetDefault()

    def doMe(self, event):
        self.Destroy()
        

  

if __name__ == "__main__" :
     app = wx.PySimpleApp()
     frame = bucky(parent=None, id=-1)
     frame.Show()
     app.MainLoop()















          
