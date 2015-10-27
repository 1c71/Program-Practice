### 程序说明:
程序用于翻译字幕文件  <br />
程序会用谷歌翻译把 英文字幕 变成 中英双语字幕    格式是:  中 \N 英 <br />
( \N 在 Aegisub 这个字幕编辑软件里是换行的意思 )

<br>
翻译好后会保存到新文件, 而不是覆盖原文件. <br />
原字幕文件: test.srt <br>
新字幕文件: (done)test.srt <br>


<br />
### 使用方法:
1. 下载并解压.
1. 用 __English-Chinese/__ 里面的东西就行, 其他的都可以删了.
1. 把字幕文件拖到 English-Chinese/Translate_Subtitle.exe 上面.
1. 泡杯喝的等一下吧. 待会就好了.


<br />
### 常见问题:
* 字幕文件可以是中文名, 但是字幕文件的路径中不要有中文字符, 不然无法运行.
* 如果某行字幕里面有中文字符, 那么会跳过那一行, 不翻译.


<br />
### Python 源代码说明 (如果你是普通用户那么不用看这里, 如果你是程序员倒可以看看):
程序用的是[Python3.3](http://www.python.org/download/releases/3.3.1/) <br />

并且用到了以下扩展库:<br />
[Pysubs库](https://pypi.python.org/pypi/pysubs/) -- 用于解析字幕文件(只能装在py3上) <br />
[Requests库](http://cn.python-requests.org/en/latest/user/install.html#install) -- 用于发送请求 <br />


<br />
### 有建议或问题或意见
可以去新浪微博找我 [@糖醋陈皮](http://www.weibo.com/u/2004104451/home?wvr=5#_rnd1387527321573) <br />

也可以开个github issue. <br />
