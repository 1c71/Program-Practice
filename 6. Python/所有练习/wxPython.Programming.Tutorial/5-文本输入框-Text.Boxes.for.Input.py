import wx

class bucky(wx.Frame):
     
    def __init__(self, parent, id):
        wx.Frame.__init__(self, parent, id, 'Frame aka window', size=(300,200))
        panel = wx.Panel(self)
        # 演示如何创建一个文本输入框
        
        # 第1个参数是parent, none代表独立存在
        box = wx.TextEntryDialog(None, "whats you name", "Title", "defalut text")
        # 第2个参数是问题, 第3个参数是标题, 第4个参数是输入框里的默认值

        if box.ShowModal() == wx.ID_OK:
            answer = box.GetValue()



if __name__ == "__main__" :
     app = wx.PySimpleApp()
     frame = bucky(parent=None, id=-1)
     frame.Show()
     app.MainLoop()

















          
