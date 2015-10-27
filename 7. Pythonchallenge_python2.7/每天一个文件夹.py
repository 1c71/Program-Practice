import time
import os
# 写于2012-12-21 13:47

basePath = "F:\\work\\"  # 这些文件的根目录

thisYear = str(time.localtime()[0])  # 拿到当前年份
# print thisYear
# 2012

thisMonth = str(time.localtime()[1])  #拿到当前月份
# print thisMonth
# 12

thisDay = time.strftime("%Y-%m-%d", time.localtime())  #拿到指定格式的年月日
# print thisDay
# 2012-12-21


yearPath = basePath + thisYear  #拼路径
# print yearPath
# F:\work\2012


monthPath = basePath  + thisYear + '\\' +thisMonth  #还是拼路径
# print monthPath
# F:\work\2012\12


dayPath = basePath + thisYear + '\\' +thisMonth + '\\' + thisDay
# print dayPath
# F:\work\2012\12\2012-12-21



# 下面都是一些： 如果该文件不存在则创建该文件的代码
if not os.path.exists(basePath):
    os.mkdir(basePath)
    
if not os.path.exists(yearPath):
    os.mkdir(yearPath)
    
if not os.path.exists(monthPath):
    os.mkdir(monthPath)
    
if not os.path.exists(dayPath):
    os.mkdir(dayPath)

# 创建完文件夹之后打开该文件夹..
os.popen("explorer.exe" + " " + dayPath)
os.popen("exit")















