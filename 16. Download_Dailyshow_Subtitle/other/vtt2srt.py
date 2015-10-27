# 这个文件用于把 vtt 转成 srt, 后来觉得麻烦就用 Tampermonkey 做了，虽然这个 python 程序没啥用了，但我还是想留下来。
# 也许以后用的上呢，天知道。
# Envirment: Win7
# Python version: 3.2.5
# Author: github 1c7
# 2014-12-10



d = open("d.txt", encoding='utf-8')
content = d.read()
content = content.replace("position:15%", "")
content = content.replace("align:start", "")
content = content.replace("<b>", "")
content = content.replace("</b>", "")
content = content.replace("WEBVTT", "")
content = content.replace("&gt;", "")    # html, greater then 
content = content.replace("\ufeff", "")  # 解决gbk编码报错问题
content = content.replace("\u266a", "")  # 解决gbk编码报错问题



#########################################
#
#  00:00:04.438 --> 00:00:07.941
#  00:00:00,060 --> 00:00:01,270
#  下面这段代码，把时间轴里的句号换成逗号, 这样才是符合规则的srt文件.
#
#########################################

content_list = content.split("\n")

for index, item in enumerate(content_list):
    if "-->" in item:
        item = item.replace(".", ",")
        item = item.strip()
        content_list[index] = item
    else:
        content_list[index] = item.capitalize()
        # 首字母大写


#########################################
#
#  保存结果到 srt 文件里
#
#########################################
result = "\n".join(content_list)
srt = open("result.srt", 'w')
srt.write(result)
srt.close()