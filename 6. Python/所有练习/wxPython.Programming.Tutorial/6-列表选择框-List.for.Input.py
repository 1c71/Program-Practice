import wx

class bucky(wx.Frame):
     
    def __init__(self, parent, id):
        wx.Frame.__init__(self, parent, id, 'Frame aka window', size=(300,200))
        panel = wx.Panel(self)
        
        # 创建列表选择框

        # 第2个参数是问题，第3个参数是标题值，第4个参数是列表可选项
        box = wx.SingleChoiceDialog(None,'Whats you fav food?', "Title",
                                    ['Banana',
                                     'Beef',
                                     'suagar',
                                     'chicken'
                                     ])

        # 只有2个选项，OK和cancel
        # 如果用户点击了按钮，并且是个OK按钮
        if box.ShowModal() == wx.ID_OK:
            answer = box.GetStringSelection()

        # answer会获得选择了的值
         





if __name__ == "__main__" :
     app = wx.PySimpleApp()
     frame = bucky(parent=None, id=-1)
     frame.Show()
     app.MainLoop()

















          
