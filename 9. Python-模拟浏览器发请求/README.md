
#### 这里的例子都是用Python的网络库来模拟浏览器请求
检验方法: 把 浏览器发出去的http头 和 程序发出去的http头比对即可..  
只要弄的一模一样 服务器就分不出来了    

<br>
#### Output-All-Request-Header.php  
这个文件输出所有的 http 请求头  


<br>
#### 具体解释:
这里的程序都是访问Output-All-Request-Header.php, 然后输出内容.. <br>
因为这个文件输出所有http请求头, 所以我们能知道程序发的究竟是什么请求头 <br>

<br>
#### 用法:
用的时候记得把php文件放apache里运行...  <br>
Output-All-Request-Header.php里有个函数只能在apache下运行   <br>





