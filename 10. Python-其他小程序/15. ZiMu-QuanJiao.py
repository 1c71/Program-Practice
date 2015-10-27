'''

双击运行后, 程序会把所有以(done)开头的srt字幕文件,
里的全角符号换成半角

此程序需要和 Translate_Whole_SubtitleFile.py 配合使用.
因为 Translate_Whole_SubtitleFile.py 在翻译完字幕后
会保存到新文件里, 而且新文件的文件名会多一个(done)

'''

# encoding=utf-8
import glob
import pysubs



filename_list = glob.glob("(done)*.srt")

for filename in filename_list:
    subs = pysubs.load(filename, encoding='utf-8')
    for line in subs:
        line.text = line.text.replace('，', ', ')
        line.text = line.text.replace('。', '. ')
        line.text = line.text.replace('！', '! ')
        line.text = line.text.replace('’', "'")
        line.text = line.text.replace('：', ': ')
        line.text = line.text.replace('？', '? ')
    subs.save(filename)


print("done")
input()
