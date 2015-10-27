import wx

if __name__ == "__main__" :
     app = wx.PySimpleApp()


     names = ["buckly","lucky","sarch","ahaha","morning"]

     modal = wx.SingleChoiceDialog(None, "Whats ur name", "title here", names)

     if modal.ShowModal() == wx.ID_OK:
         print "you name is %s\n" % modal.GetStringSelection()
     modal.Destroy()

     # 选择列表对象框

















          
