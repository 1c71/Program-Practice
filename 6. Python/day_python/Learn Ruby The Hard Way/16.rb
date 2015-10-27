# 習題 16: 讀寫檔案

filename = ARGV.first
script = $0

puts " 准备清空数据的文件名是:#{filename}."
puts " 如果你不想这么做，请按下 CTRL-C (^C). "
puts " 如果确认清空请按下回车 "

print "? "
STDIN.gets

puts "正在打开文件..."
target = File.open(filename, 'w')

puts "正在清空这个文件...再见!"
target.truncate(1)

puts " 请你输入三行文字 "

print "第一行: "; line1 = STDIN.gets.chomp()
print "第二行: "; line2 = STDIN.gets.chomp()
print "第三行: "; line3 = STDIN.gets.chomp()

puts "我准备把这些写进文件里"

target.write(line1)
target.write("\n")
target.write(line2)
target.write("\n")
target.write(line3)
target.write("\n")

puts " 写入完毕，文件关闭成功！ "
target.close()