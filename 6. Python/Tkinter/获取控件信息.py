import Tkinter
import ttk



root = Tkinter.Tk()
print root.winfo_width()
print root.winfo_x() # 控件x坐标
print root.winfo_y() # 控件y坐标
print root.winfo_screenwidth()   # 返回屏幕宽度
print root.winfo_screenheight()  # 返回屏幕高度
print root.winfo_screenmmheight()# 应该是root的高度
print root.winfo_name() # 返回名字
print root.winfo_parent()

print root.winfo_class()
# 返回这个控件的window class name

print root.winfo_exists()
# 控件存在则返回True or 1

print root.winfo_geometry();
# 字符串形式返回控件的宽x高+X+Y

print root.winfo_id()
# Return identifier ID for this widget.
# 返回控件的标识符ID。(每次运行都不一样，不知道为什么)


a = ttk.Notebook(height=100,width=200)
a.pack()

print a.winfo_rootx()
# 返回控件左上角相对于根组件的x坐标

root.mainloop()

