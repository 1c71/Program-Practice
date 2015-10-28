# 習題 17: 更多的檔案操作
# 在命令行运行的时候需要接收2个参数，
# 第1个参数是 准备复制的文件名，第2个参数是 准备接收这些数据的文件

from_file, to_file = ARGV
script = $0

indata = File.open(from_file).read()
  # 现在indata里面都是准备复制文件的数据

puts " 即将进行的操作是把 #{from_file} 的内容复制到 #{to_file} 里去 "
puts "  按下回车键继续, 按下CTRL-C终止. "
STDIN.gets
puts "----------------------------------------------------------------"

output = File.open(to_file, 'w')
output.write(indata)

puts "   事情都干完了..文件数据复制成功.. 啊哈哈哈哈~~~ "

output.close()
