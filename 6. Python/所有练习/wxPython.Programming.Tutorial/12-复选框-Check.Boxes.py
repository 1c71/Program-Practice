import wx

class bucky(wx.Frame):
     
    def __init__(self, parent, id):
        wx.Frame.__init__(self, parent, id, 'Frame aka window', size=(300,200))
        panel = wx.Panel(self)
        
        # 创建复选框

        # 
        wx.CheckBox(panel, -1, "Apples", (20,30), (160,-1))
        wx.CheckBox(panel, -1, "Banana", (20,50), (160,-1))
        wx.CheckBox(panel, -1, "Orange", (20,70), (160,-1))
        wx.CheckBox(panel, -1, "Roast Beef", (20,90), (160,-1))


        
  

if __name__ == "__main__" :
     app = wx.PySimpleApp()
     frame = bucky(parent=None, id=-1)
     frame.Show()
     app.MainLoop()















          
