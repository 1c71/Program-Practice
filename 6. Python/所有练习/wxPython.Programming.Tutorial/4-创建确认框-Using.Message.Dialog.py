import wx

class bucky(wx.Frame):
     
    def __init__(self, parent, id):
        wx.Frame.__init__(self, parent, id, 'Frame aka window', size=(300,200))
        panel = wx.Panel(self)

        # 这一节会教你如何创建一个确认/取消选择框
        box = wx.MessageDialog(None,'today is monday?','Title',wx.YES_NO)
                                     # 这是问题        # 这是标题

        # ShowModal里是box的值
        answer = box.ShowModal()
        # 如果点击Yes ,answer里的值会是yes, 点击no值会是no
        box.Destroy()





if __name__ == "__main__" :
     app = wx.PySimpleApp()
     frame = bucky(parent=None, id=-1)
     frame.Show()
     app.MainLoop()

















          
