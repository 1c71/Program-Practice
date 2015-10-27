import wx

class bucky(wx.Frame):
     
    def __init__(self, parent, id):
        wx.Frame.__init__(self, parent, id, 'Frame aka window', size=(300,200))
        panel = wx.Panel(self)
        
        # 微调控制项 就是有上下按钮的框，点击更改数字



        # 第3个参数不清楚是啥,, 第4个参数是位置, 第5个参数是高宽
        spinner = wx.SpinCtrl(panel, -1, "", (40,40), (190,-1) )
        
        # 范围是1~100
        spinner.SetRange(1,100)
        # 一开始的默认值是10
        spinner.SetValue(10)

        
  

if __name__ == "__main__" :
     app = wx.PySimpleApp()
     frame = bucky(parent=None, id=-1)
     frame.Show()
     app.MainLoop()















          
