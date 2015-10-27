<?php 
    require_once('../verify.php');
    require_once('../../tool/MySQL_Helper.php'); 
    
    /* "好站推荐管理" 的插入命令. */



    //注意, 接收到的全是string. 

    if ( isset($_POST['type']) && isset($_POST['sort']) && isset($_POST['name']) && isset($_POST['intro'])&& isset($_POST['link']) ){
        
        $type = mysql_real_escape_string($_POST['type']);

        $sort = $_POST['sort'];    // 接数据
        $sort = intval($sort);  //如果转换失败. $sort会为0

        $name = mysql_real_escape_string($_POST['name']);
        $intro = mysql_real_escape_string($_POST['intro']);
        $link = mysql_real_escape_string($_POST['link']);

    }else{
        header("Location: ../../index.php");
        return;
    }




$mysql_helper = new MySQLHelper();
$sql = "insert into good_website (type, sort, name, intro, link) values('$type', $sort, '$name', '$intro', '$link')";


$status = $mysql_helper->excute_dml($sql);
// 如果没有成功，就返回0;
// 执行成功并且有行受到影响, 返回1
// 表示执行成功但是没有行受到影响, 返回2
// MySQLHelper类是属于 tool/MySQL_Helper.php 文件的. 请参阅里面的返回代码.


$id = mysql_insert_id();
// 拿到上一步insert操作所插入的数据的id

// 将[状态代码]和[刚插入的数据的id]弄成一个数组.
$json = Array('good_website_insert_status'=>$status, 'nsert_id'=>$id);


// ====JSON编码后 输出数据=====
header('Content-type:text/json');   // 加了这个header之后, 前端的js就可以直接取, 而不用先JSON.parse一次
echo json_encode($json);



$mysql_helper->close_connect();






// ====备注=====================================


// ==== mysql_real_escape_string ====
// mysql_real_escape_string 转义 SQL 语句中使用的字符串中的特殊字符.
// 并且它接收到数字会出错.



// ==== intval ====
// 如果第一个碰到的字符就是字母. 直接转换失败. 转换失败会返回 0
// echo intval('zasasf13f13f');  // 返回0

// 如果第一个碰到的字符是数字. 那么直到碰到字母之前的数字都会被返回.
// echo intval('33a99');   // 返回33

// 正常的转换:
// echo intval('88');   // 返回88


?>