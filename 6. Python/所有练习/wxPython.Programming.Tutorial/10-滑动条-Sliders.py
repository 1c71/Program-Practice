import wx

class bucky(wx.Frame):
     
    def __init__(self, parent, id):
        wx.Frame.__init__(self, parent, id, 'Frame aka window', size=(300,400))
        panel = wx.Panel(self)

        # 滑动条

        
        
        # 第3个参数是默认值,第4个参数最小值,第5个参数是最大值
        slider = wx.Slider(panel, -1, 50, 1, 100, pos=(20,30), size=(250,-1),
                           style=wx.SL_AUTOTICKS | wx.SL_LABELS)

        slider.SetTickFreq(5,1)
        # 每距离5做一个标记，1不知道什么意思

  

if __name__ == "__main__" :
     app = wx.PySimpleApp()
     frame = bucky(parent=None, id=-1)
     frame.Show()
     app.MainLoop()















          
