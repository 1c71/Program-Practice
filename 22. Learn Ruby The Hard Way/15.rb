# œ∞Ã‚15 ∂¡»°µµ∞∏

filename = ARGV.first

txt = File.open(filename)

puts "ready to read file name is : #{filename}"
puts txt.read()


puts "Type the filename again: "
file_again = STDIN.gets.chomp()
txt_again = File.open(file_again)

puts txt_again.read()




