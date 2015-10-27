<?php 
    require_once('../verify.php');
    require_once('../../tool/MySQL_Helper.php');
    header('Content-Type: text/html; charset=utf-8');


    /* 处理"热门资源管理"页面的 删除操作 */



    if( isset($_POST['id'])){
        $id = mysql_real_escape_string($_POST['id']);
    }else{
        return;
    }



$mysql_helper = new MySQLHelper();



$sql = "delete from hot_resource where id='$id'";


$number = $mysql_helper->excute_dml($sql);
    // 如果没有成功，就返回0;
    // 执行成功并且有行受到影响, 返回1
    // 表示执行成功但是没有行受到影响, 返回2

    //我们这里啥也不返回.. 如果的确有需要的话可以做一个数组什么的.. push $number就行

echo $number;
$mysql_helper->close_connect();




?>