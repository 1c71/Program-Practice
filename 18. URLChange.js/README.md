打算写个英文版文档，过阵子写..
### URLChange.js

<br/>
#### 这库是干嘛的？
操作 URL 里的 GET 参数的  
能:  
1. 获得一个 get 参数的值   
2. 增加/修改一个 get 参数(参数已存在就覆盖，不存在就添加)  
3. 删除一个 get 参数   
4. 清空所有 get 参数   
5. 判断某参数是否存在  

<br/>
#### 为什么写这库?
之前在 DrinknLink 工作的时候，有个需求是用户搜索酒吧的的时候，可能需要分享酒吧搜索结果。  
那么我们就得改 URL ，修改 GET 参数。不然没法做到分享功能。  
网上没找到类似的库，就自己写了。然后觉得别人可能也用得着。就干脆放出来。  
如果你发现已经有类似的东西请告诉我。  

<br/>
#### 用法举例
    <!DOCTYPE HTML>
	<html>
		<head></head>
		<body>
			<script type="text/javascript" src="URLChange-min.js"></script>
			<script>
			
				var newURL = addORchangeURLParameter('hello', 'world', "http://localhost/Example.html");
				console.log(newURL);
				// http://localhost/Example.html?hello=world

			</script>
		</body>
	</html>



<br/>
## 文档

### 说明
这些函数只是接收一个 URL 字符串，处理。然后__返回新的 URL 字符串__。  

要把新 URL 改动到地址栏，你得自己这样写：

    if (typeof(history.pushState) == 'function'){
		var newURL = addORchangeURLParameter('hello', 'world', window.location.href);
		// window.location.href 是当前网址
		window.history.pushState("", "", newURL);
	}

解释：先是判断这个函数能不能用，能用才执行。如果不判断直接用。就报错停住了。

### 目录
1. addORchangeURLParameter 添加或修改
2. getParameterFromURL     获得参数值
3. removeParameterFromURL  删参数
4. clearParameterFromURL   清空所有参数
5. thereAreParameterInURL  判断参数是否存在

<br/>
#### addORchangeURLParameter(paramName, paramValue, URL)
添加 URL 参数。如果同名的参数存在就覆盖。
 
<br/>
如果参数不存在, 添加:  

	addORchangeURLParameter('name', 'obama', 'http://localhost/newteamwork/')
		http://localhost/newteamwork/?name=obama


如果参数存在, 则修改值:


	addORchangeURLParameter('name', 'obama', 'http://localhost/newteamwork/?name=handsomejack')
	http://localhost/newteamwork/?name=obama

	addORchangeURLParameter('name', 'obama', 'http://localhost/newteamwork/?name=handsomejack&age=19')
	http://localhost/newteamwork/?name=obama&age=19

	addORchangeURLParameter('name', 'obama', 'http://localhost/newteamwork/?Category=2,4,6,1')
	http://localhost/newteamwork/?Category=2,4,6,1&name=obama



<br/>
#### getParameterFromURL(parameter_name, URL)
取指定 URL 参数的值

	getParameterFromURL('aa', 'http://localhost/newteamwork/?aa=bb');
	bb

	getParameterFromURL('haha', 'http://localhost/newteamwork/?aa=bb&haha=lol');
	lol

如果一个参数也没有  

		getParameterFromURL('aa', 'http://localhost/newteamwork/');
		false

如果有参数, 但是你要的参数不存在

		getParameterFromURL('jj', 'http://localhost/newteamwork/?aa=bb');
		false


<br/>
#### removeParameterFromURL(parameter_name, URL) {
从 URL 里删除指定的参数

		removeParameterFromURL('aa', 'http://localhost/newteamwork/');
		false	

		removeParameterFromURL('aa', 'http://localhost/newteamwork/?aa=bb');
		http://localhost/newteamwork/

		removeParameterFromURL('aa', 'http://localhost/newteamwork/?aa=bb&cc=dd&ee=ff');
		http://localhost/newteamwork/?cc=dd&ee=ff

		removeParameterFromURL('cc', 'http://localhost/newteamwork/?aa=bb&cc=dd&ee=ff');
		http://localhost/newteamwork/?aa=bb&ee=ff

		removeParameterFromURL('ee', 'http://localhost/newteamwork/?aa=bb&cc=dd&ee=ff');
		http://localhost/newteamwork/?aa=bb&cc=dd

		removeParameterFromURL('asdasdasdasd', 'http://localhost/newteamwork/?aa=bb&cc=dd&ee=ff');
		http://localhost/newteamwork/?aa=bb&cc=dd&ee=ff



<br/>
#### clearParameterFromURL(URL)
清空所有参数


		clearParameterFromURL('http://localhost/newteamwork/');
		http://localhost/newteamwork/

		clearParameterFromURL(http://localhost/newteamwork/?aa=bb&cc=dd&ee=ff');
		http://localhost/newteamwork/


<br/>
#### thereAreParameterInURL(URL)

判断 URL 是否有某参数，有就 True 没有就 False

		thereAreParameterInURL('http://localhost/newteamwork/');
		false

		thereAreParameterInURL('http://localhost/newteamwork/?aa=bb');
		true

		thereAreParameterInURL('http://localhost/newteamwork/?aa=bb&cc=dd&ee=ff');
		true


---

<br/>
<br/>
#### 其他说明
欢迎 fork & pull request.  
欢迎提 issue。   

