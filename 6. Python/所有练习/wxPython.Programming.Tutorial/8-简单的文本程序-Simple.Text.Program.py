import wx

class bucky(wx.Frame):
     
    def __init__(self, parent, id):
        wx.Frame.__init__(self, parent, id, 'Frame aka window', size=(300,200))
        panel = wx.Panel(self)
        
        # 让用户输入信息并显示到界面上
        
        test = wx.TextEntryDialog(None,"what you name?", 'Tile', 'enter name')

        # ShowModal() 千万要记得加括号，不加运行不起来
        if test.ShowModal()==wx.ID_OK:
            apples=test.GetValue()
    
        wx.StaticText(panel, -1, apples, (10,10))

  

if __name__ == "__main__" :
     app = wx.PySimpleApp()
     frame = bucky(parent=None, id=-1)
     frame.Show()
     app.MainLoop()















          
