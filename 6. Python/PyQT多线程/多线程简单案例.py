import sys,time
import thread

def a():    
    for i in range(1,5):
        time.sleep(0.5)
        print "\nhello"
        time.sleep(1)
def b():
    for j in range(1,5):
        time.sleep(1)
        print "\nthen"        
        time.sleep(0.5)


thread.start_new_thread(a,())
thread.start_new_thread(b,())
