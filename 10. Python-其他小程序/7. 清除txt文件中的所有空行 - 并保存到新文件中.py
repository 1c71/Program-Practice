# 程序去除txt文件中的所有空行后, 保存到新文件里 (原文件不会被修改)
# 新文件的名字是 (clear)-原文件名
# a.txt 清理后的新文件会是: (clear)-a.txt




file_name = "large-file.txt"   # 请修改这里为你要清除空格的txt文件名





















# ---- ---- ---- ---- ---- ---- ---- ---- 
# 后面这部分用户不用修改.




old = open(file_name, "r")
# r = ready

new = open('(clear)-'+file_name, "w")
# w = write






try:
    while True:
        line = old.readline()
        # 读取一行
        # readline()方法在读到文件末尾后会返回一个空字符串


        if line == '':
            break
        # 为空就是到达文件末尾了, 我们退出循环


        if line.replace(' ', '') == '\n': 
           continue
        # 如果去掉所有空格后只剩一个\n, 说明这是个空行, 我们跳过这个空行


        new.write(line)
        # 写到新文件里去
finally:
    old.close()
    # 关闭原文件
    new.close()
    # 关闭新文件














