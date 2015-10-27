import wx

class bucky(wx.Frame):
     
    def __init__(self, parent, id):
        wx.Frame.__init__(self, parent, id, 'Frame aka window', size=(300,200))
        panel = wx.Panel(self)
        
        # 创建选择列表框

        # 创建列表对象
        mylist = ["beef","tuna","cocnuts","more beef","cereal","chicken","apple"]

        # 创建列表框
        # wx.LB_SINGLE意思是你只能选择一个
        # 第三个参数是位置，第四个参数是宽高
        cunt = wx.ListBox(panel, -1, (20,20), (180,80), mylist, wx.LB_SINGLE )

        #默认选择第四个元素(元素是从0开始计算的)
        cunt.SetSelection(3)
        
  

if __name__ == "__main__" :
     app = wx.PySimpleApp()
     frame = bucky(parent=None, id=-1)
     frame.Show()
     app.MainLoop()















          
