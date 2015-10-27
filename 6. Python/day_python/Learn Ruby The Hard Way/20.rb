input_file = ARGV[0]

# 定义一个输出文件全部内容的函数
def print_all(f)
  puts f.read()
  puts " "
end

# 这个函数将文件指针指向开头
def rewind(f)
  f.seek(0, IO::SEEK_SET)
end

=begin
io.seek(offset,whence)

offset应以整数指定位置
whence指定应该如何解释offset这个值
IO::SEEK_SET  将文件指针移动到offset所指定的位置处
=end

def print_a_line(line_count, f)
  puts "#{line_count} #{f.readline()}"
end

current_file = File.open(input_file)

puts "首先，让我们输出整个文件内容: "
puts # a blank line

# 使用这个函数输出文件里的全部信息
print_all(current_file)

puts "Now let's rewind, kind of like a tape."

# 将文件指针移动到文件开头
rewind(current_file)

puts "输出3行 :"

current_line = 1
print_a_line(current_line, current_file)

current_line = current_line + 1
print_a_line(current_line, current_file)

current_line = current_line + 1
print_a_line(current_line, current_file)

# 没有控制读取几行，都是按照顺序1，2，3行读取，只是前面加了一个行号而已。





