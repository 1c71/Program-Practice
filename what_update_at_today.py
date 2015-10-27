'''
这个程序用于输出某目录下所有今天更新过的文件
注意是今天.


写这个程序是用于 FTP 更新文件，
比如你今天写了某个功能，改了大概7个文件，你自己不记得到底是哪几个文件。
那么用 FTP 更新服务器的时候就会浪费时间，比如少更新了一个文件结果报错。
或者多更新了一个文件结果导致了意想不到的错误。

这个程序输出哪些文件更新过，这样就可以只上传更新过的文件了。

Time: 2015-8-31
Version : Python 3
Author : Cheng Zheng (郑诚)


### 使用方法
1. 修改下面的 dir_path 路径
2. 执行即可, 你用 Python 自带 IDE 的 F5 或者命令行也行，随你



'''







dir_path = r"F:\Apache24\htdocs\forum_CI3"
# 文件夹路径
# 别删掉字符串前面的 r
# 我自己都没试过相对路径，你试试？
# 然后有什么问题 fork 改完。pull request 一下？(github)






how_many_days_ago = 0
# 这个一般不用改
# 这个配置代表是几天前

# 0 代表是今天 00:00:00 点之后
# 比如 how_many_days_ago = 0 而且现在是2015年9月1号下午4点
# 那么程序就会判断 2015-9-1 00:00:00 之后哪些文件更新了，然后输出出来
# 然后你就开心的去用 FTP 更新文件吧哈哈哈

# 1 代表是昨天 00:00:00 点之后，或者说是1天前
# 2 代表前天, 或者说是2天前


# how_many_days_ago 取值不要超过28，因为逻辑是求上个月，超过28就会有问题(假设2月份情况)
# 这里懒得改因为这个需求很少。本来这个就是写给自己用的，没必要考虑到健壮性然后写个半天。









# ======================= 程序开始， 这后面的不是配置，你不用改 =====================
# ======================= 除非改 bug 或者干啥的，那你随意 =========================

'''

程序整体思路：

1. 拿到 X 天前的 0 点时间

    
2. 拿到文件的时间

    
3. 如果文件的时间 大于 X 天的 0 点时间
    那说明文件那个时间点之后更新过
    那我们输出文件名

'''



import os
from datetime import datetime
from calendar import monthrange





def today():
    # 函数生成今天的 00:00:00
    # 比如现在是 2015-8-31 17:17:00
    # 那么生成是 2015-8-31 00:00:00
    year = datetime.now().strftime('%Y')
    month = datetime.now().strftime('%m') 
    day =  datetime.now().strftime('%d')

    year = int(year)
    month = int(month)
    day = int(day)

    date = datetime(year, month, day, 00)
    return date



# 以下判断天数够不够减, 然后获得一个合理的 datetime 对象.
# 假设, 今天是2015年9月1号
# how_many_days_ago = 0, 那么会获得 2015年9月1号 00:00:00
# how_many_days_ago = 2, 那正确的时间应该是 2015年9月1号 2 天前的 0 点，也就是 2015年8月30号 00:00:00
# (备注: 2015年8月份有31天)

day =  datetime.now().strftime('%d')
day = int(day)
if (day - how_many_days_ago <= 0 ):
    # 根据这个，判断是取上个月的时间还是这个月的时间
    year = datetime.now().strftime('%Y')  # 今年是哪年？
    month = datetime.now().strftime('%m')# 这个月是几月？
    last_month = int(month) - 1  # 上个月是几月？
    day_range_tuple = monthrange(int(year), last_month)  #上个月有多少号？ 返回元组比如(1,31)
    if (how_many_days_ago == 1):
        prev_month_last_day = day_range_tuple[1] # 获得上个月最后一天
    else:
        prev_month_last_day = day_range_tuple[1] - how_many_days_ago + 1
    prev_day_obj = datetime(int(year), last_month, prev_month_last_day, 00) # 生成上个月最后一天的对象
    print(prev_day_obj, '之后, 修改了如下文件 ')
else:
    prev_day_obj = today()
    print(prev_day_obj, '之后, 修改了如下文件 ')





'''
输出的例子

F:\Apache24\htdocs\forum_CI3\application\config\database.php
F:\Apache24\htdocs\forum_CI3\application\controllers\@test.php
F:\Apache24\htdocs\forum_CI3\application\controllers\reply.php
F:\Apache24\htdocs\forum_CI3\application\models\@Test_model.php
F:\Apache24\htdocs\forum_CI3\application\models\Reply_model.php
F:\Apache24\htdocs\forum_CI3\script\reply.js

'''



# 循环指定的目录
for root, dirs, files in os.walk(dir_path):
    for f in files:
        
        file_full_path = root, '\\', f
        # file_full_path 是个元组
        
        f_path = ''.join(file_full_path)
        # 转成字符串

        change_time = os.path.getmtime(f_path);
        # 获得修改时间
        # 例子:
        # 1438893092.0
        # 1440390334.8682745
        
        date = datetime.fromtimestamp(change_time)
        # 转成 datetime 对象
        
        if(date > prev_day_obj):
            print (f_path)

 






