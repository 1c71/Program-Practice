import smtplib
smtp = smtplib.SMTP() 
smtp.connect("smtp.qq.com", "25") 
smtp.login('[QQ邮箱]', '[QQ密码]') 
smtp.sendmail('[from@qq.com]',
              '[to@qq.com]',
              '[email content]') 
smtp.quit()
