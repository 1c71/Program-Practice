

'''
程序生成一列数字放到文件中,
每个数字一行:
1
2
3
4
5
6
等等

'''
out = open('sequence.txt', 'w')

for one in range(0,100):
    print(one, file=out)

out.close()
 
# 在 Python3.3.0 能成功运行 
# 2.7不行
 
# 这会创建一个叫做a.txt的文件, 内容是'Hello Earth!', 屏幕上并不会有任何输出
