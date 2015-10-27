<?php 

require_once('ini_reader.php');
// 引入


$ini_items = get_ini_file('test.ini');
// 使用函数, 获得 key=>value 数组.


echo $ini_items['font_color'];
echo '<br>';
echo $ini_items['草地'];


?>