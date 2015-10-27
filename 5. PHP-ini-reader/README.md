
##### 这个是用php读取ini文件的例子.  供学习用.

<br> 
<strong>ini_reader.php</strong> <br>
里面定义了一个 get_ini_file() 函数 (里面就这一个函数)  <br>
它可以读取ini配置文件.  <br>

<br>
__get_ini_file() 函数说明__:

    $数组 = get_ini_file($文件名);


<br>

---


### 栗子:


test.ini:

	autostart = false
	font_size = 12
	font_color = red
	草地 = 绿的

<br>
test.php:

	<?php 

		require_once('ini_reader.php');

		$ini_items = get_ini_file('test.ini');

		echo $ini_items['font_color'];
		echo '<br>';
		echo $ini_items['草地'];

	?>

<br>
输出:

	red
	绿的
    
    
    
    
<br>
<br>
<br>
<br>
<br>
