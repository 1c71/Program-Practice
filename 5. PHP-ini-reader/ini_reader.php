<?php 


// 这个函数读取一个ini文件, 弄成php的 key=>value 数组
// 成功: 返回 key=>value 数组.

function get_ini_file($file_name){


    $file_content = file_get_contents($file_name);  // 读取ini文件存到一个字符串中.
    $line_array = explode("\r\n", $file_content);  // 按换行拆开,放到数组中.
    $ini_items = array(); 


    foreach($line_array as $line){    // 循环数组, 每个都放到$item里

        $item_array = explode("=", $line);  // 按照 = 号分割

        if( isset($item_array[0]) && isset($item_array[1]) ){

        	$k = trim($item_array[0]);
        	$v = trim($item_array[1]);
        	// 去空格

            $ini_items[$k] = $v;	
            // 存成key=>value.
        }
        
    }

    return $ini_items;
}



 ?>