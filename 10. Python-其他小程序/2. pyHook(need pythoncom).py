import pythoncom, pyHook 
# pythoncom == pywin32 它们是一码子事儿
# pyHook 目前只支持python2.7 (2013-7-2)
# 所以代码也必须在2.7下运行


def OnMouseEvent(event):
    # called when mouse events are received
    print 'MessageName:',event.MessageName
    print 'Message:',event.Message
    print 'Time:',event.Time
    print 'Window:',event.Window
    print 'WindowName:',event.WindowName
    print 'Position:',event.Position
    print 'Wheel:',event.Wheel
    print 'Injected:',event.Injected
    print '---'

# return True to pass the event to other handlers
    return True

# create a hook manager
hm = pyHook.HookManager()

# watch for all mouse events
hm.MouseAll = OnMouseEvent

# set the hook
hm.HookMouse()

# wait forever
pythoncom.PumpMessages()
