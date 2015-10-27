<?php 
    require_once('../verify.php');
    require_once('../../tool/MySQL_Helper.php');


    /* 负责处理删除请求, 然后把数据从数据库中删除. */


    if (isset($_GET['id'])){
        $id = $_GET['id'];
        $id = intval($id);      // 转成数字
        if(!is_numeric($id)){   // 如果是数字或数字字符串. is_numberic会返回true. 这里取反了.
            echo "not number";
            return;
        }
    }




$mysql_helper = new MySQLHelper();
$sql = "delete from  useful_tool  where id = $id";
//echo $sql;

$number = $mysql_helper->excute_dml($sql);
// 如果没有成功，就返回0;
// 执行成功并且有行受到影响, 返回1
// 表示执行成功但是没有行受到影响, 返回2

echo $number;
$mysql_helper->close_connect();




?>