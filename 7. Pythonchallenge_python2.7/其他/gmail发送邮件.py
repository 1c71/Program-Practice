import smtplib  
from email.Message import Message  
from time import sleep  
  
smtpserver = 'smtp.gmail.com'  
username = 'guokrfans@gmail.com'  
password = 'thisgmail'

from_addr = 'lorerrr@gmail.com'  
to_addr = '1003211008@qq.com'  
#cc_addr = 'huzhenwei@csdn.net'  #抄送
  
  
message = Message()  
message['Subject'] = 'Mail Subject'    #邮件标题   
message['From'] = from_addr   
message['To'] = to_addr   
#message['Cc'] = cc_addr   
message.set_payload('mail content')    #邮件正文   
msg = message.as_string()  
  
  
sm = smtplib.SMTP(smtpserver, port=587, timeout=20)  
sm.set_debuglevel(1)                   #开启debug模式   
sm.ehlo()  
sm.starttls()                          #使用安全连接   
sm.ehlo()  
sm.login(username, password)  
sm.sendmail(from_addr, to_addr, msg)  
sleep(5)                               #避免邮件没有发送完成就调用了quit()   
sm.quit()  
