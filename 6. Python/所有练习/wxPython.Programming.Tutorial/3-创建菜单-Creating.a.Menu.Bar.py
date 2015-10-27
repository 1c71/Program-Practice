import wx

class bucky(wx.Frame):
     
    def __init__(self, parent, id):
        wx.Frame.__init__(self, parent, id, 'Frame aka window', size=(300,200))
        panel = wx.Panel(self)

        # 创建状态条
        status = self.CreateStatusBar()
        
        # 创建菜单条对象
        menubar = wx.MenuBar()
        
        # 创建了两个菜单列表(可以往里添加多个选项,看下面代码) 对象
        first = wx.Menu()
        second = wx.Menu()

        # 给菜单项 添加id ,名字, 状态栏说明
        first.Append(wx.NewId(),"New Window","This is a new window")
        first.Append(wx.NewId(),"Open...","Will Open a new Window")

        # 把菜单条添加菜单项 ，并且给个名字
        menubar.Append(first,"File")
        menubar.Append(second,"Edit")

        # 
        self.SetMenuBar(menubar)

        


if __name__ == "__main__" :
     app = wx.PySimpleApp()
     frame = bucky(parent=None, id=-1)
     frame.Show()
     app.MainLoop()

















          
