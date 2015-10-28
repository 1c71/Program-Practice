# 習題 14: 提示和傳遞

user = ARGV.first    
#如果在命令行执行的时候在名字后面还给了一个参数，这个名字就是user的值

prompt = '> '
#设置用户提示符，在每一个提示输出的地方都会摆在前头

puts "Hi #{user}, I'm the #{$0} script."

# #{$0} 会输出文件路径和文件名, 测试#{$1}和#{$2}没反应

puts "I'd like to ask you a few questions."
puts "Do you like me #{user}?"
print prompt
likes = STDIN.gets.chomp()

puts "Where do you live #{user}?"
print prompt
lives = STDIN.gets.chomp()

puts "What kind of computer do you have?"
print prompt
computer = STDIN.gets.chomp()

puts <<MESSAGE
Alright, so you said #{likes} about liking me.
You live in #{lives}.  Not sure where that is.
And you have a #{computer} computer.  Nice.
MESSAGE

=begin
同時必須注意的是，我們也用了 STDIN.gets 取代了 gets。
這是因為如果有東西在 ARGV 裡，標準的gets會認為將第一個參數當成檔案而嘗試從裡面讀東西。
在要從使用者的輸入（如stdin）讀取資料的情況下我們必須明確地使用 STDIN.gets。
=end