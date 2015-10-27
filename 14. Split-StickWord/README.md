## 中文:

<br>
__1. 程序会给字幕文件分词.__  因为网上下载的英文字幕文件里经常有各种各样烦人的连词  
比如:  whatis, howthey, thereare  .....
分词是依据 split.txt 来分词的  

split.txt 里面的格式是这样的:  

    thepart
    the part

    putthis
    put this




<br>
__2. 程序会把 \' 替换成 '__. 因为有些字幕里经常会有:<br>

    \N
    don\'t
    shouldn\'t
    we\'ve  
    they\'re  
    you\'ll 
    let\'s

<br>
输出会是:

    \N
    don't
    shouldn't
    we've  
    they're  
    you'll 
    let's


<br>
__3. 如果句号后面有字母, 程序会给它加个空格__<br>
input:

    do you know....that thing?

output:
    
    do you know.... that thing?

input:

    wow.is awesome

output:
    
    wow. is awesome



<br>



__4. 如果数字前面或后面有字符, 会加上个空格__<br>
 
input:
    
    i have900cm

output:

    i have 900 cm

input:

    he have200 pound?

output:

    he have 200 pound?


<br>
__5. 程序会自动检测是否有错位, 所以你不用担心自己多打了一个单词导致全错位了__<br>
程序循环的时候是2个2个的从split.txt里面拿单词的.<br>
 
假设split.txt里有:
    
    aaa

    firstquestion
    first question

    heis
    he is

程序会直接报错停止运行, 告诉你 aaa--firstquestion 错了, 你再去split.txt里面修复这个问题.

<br>
<br>
### 用法:
1. 下载程序
1. 把字幕文件拖到 exe/Split_Word.exe 上面即可




<br>
### 目录说明:

* __Python_SourceCode/__ <br>
里面放的是Python源代码 <br>
你可以把这个目录删掉...对你没用..(除非你是程序猿)  


* __exe/__  
把Python源代码编译成exe的结果





<br>
### 其他说明:

* __分词完成后会覆盖原文件__
* 字幕文件的存放路径中不要有中文名, 不然无法运行
* split.txt 文件里面存放的是替换单词, 替换的时候会忽略大小写, 统一替换成第2个单词

__举几个例子. 如果 split.text 文件里有__:
    
    wehave
    we have

[例1]:

    WEHAVE

[例1]会替换成:

    we have


[例2]:

    We Have

[例2]会替换成:

    we have

<br>
[例3]:
    
    wEhAvE

[例3]会替换成:
    
    we have

<br>
__再假设 split.text 文件里有__:
    
    HEIS
    he is

[例1]:
    
    HEIS

[例1]会替换成:
    
    he is


[例2]:
    
    heis

[例2]会替换成:
    
    he is







<br>
### 程序说明:
代码用的是 [Python3](http://www.python.org/download/releases/3.3.1/)<br />
以及扩展库 [pysubs](https://github.com/tigr42/pysubs)<br />

split.txt这个文件存的是分词列表, 格式是: <br />

    whenthey
    when they

    helpof
    help of

    thedevelopment
    the development

    toexploit
    to exploit

    theway
    the way

    youcan
    you can

    # 井号开头的内容会被当作注释, 不会影响程序的执行. 比如这一行
    # 单词之间不一定要有回车隔开, 就算不隔开也不影响程序.. 隔开只是为了美观


你可以根据需要来修改..


<br />
***
有问题可以来新浪微博给我留言: [@糖醋陈皮](http://www.weibo.com/2004104451/profile?rightmod=1&wvr=5&mod=personnumber)  

当然你也可以开一个issue, 如果你有Github帐号的话

<br><br><br><br><br><br>



## English



### Description:

<br>
__1. Program will split english word__  
because if you download subtitle from internet, always have some word combine together<br>
Example:<br>

    whatis, howthey, thereare  etc..


<br>
__2. replace \' with '__  
because have some subtitle file is like this:<br>

    \N
    don\'t
    shouldn\'t
    we\'ve  
    they\'re  
    you\'ll 
    let\'s

<br>
Output:

    \N
    don't
    shouldn't
    we've  
    they're  
    you'll 
    let's 



<br>
__3. If behind '.' is a char. add a black behind the '.'__ <br>
Example<br>

input:

    do you know....that thing?

output:
    
    do you know.... that thing?

input:

    wow.is awesome

output:
    
    wow. is awesome




<br>


__4. If number with non-number char. We add a blank__<br>
Example<br>

input:
    
    i have900cm

output:

    i have 900 cm

input:

    he have200 pound?

output:

    he have 200 pound?




<br>
__5. Program will check Dislocation, you don't need worry about, you Careless input some word__  
Program get word from split.txt, everytime take two word  
 
Assum split.txt have:
    
    aaa

    firstquestion
    first question

    heis
    he is

<br>
Program just stop, and tell you  
"aaa--firstquestion Wrong, please fix that"  




<br>
<br>
### Usage:
1. drag subtitle file on exe/Split_Word.exe



<br>
### FAQ:
* __Program will Overwrite the original file__
* in subtitle file path. don't have chinese, or Japanese or something weird Character. Program will can not run
* split.txt  Storage replace english word. and will Ignore case.

few example. if split.text have:
    
    wehave
    we have

input:

    WEHAVE

replace with:

    we have


input:

    We Have

replace with:

    we have


input:
    
    wEhAvE

replace with:
    
    we have


<br>
### Program explain:
Program written by [Python3](http://www.python.org/download/releases/3.3.1/)<br />
and module [pysubs](https://github.com/tigr42/pysubs) <br />

split.txt  is for split word. the format like this: <br />

    whenthey
    when they

    helpof
    help of

    thedevelopment
    the development

    toexploit
    to exploit

    theway
    the way

    youcan
    you can

    # in this file. 
    # anyline start with #, will not process.. just like code comment


If you want, You can modify this file.

<br />
If you have suggestions. Or you want report bug  <br />
you can come [HERE](https://github.com/1c7/Split_StickWord/issues/1)  <br />
Thank you~


<br />
<br />



