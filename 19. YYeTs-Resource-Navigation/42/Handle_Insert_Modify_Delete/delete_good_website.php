<?php 
    require_once('../verify.php');
    require_once('../../tool/MySQL_Helper.php');
    header('Content-Type: text/html; charset=utf-8');


    /* 处理"好站推荐管理"页面的 删除操作 */


    if( isset($_POST['type']) && isset($_POST['id']) ){

        $id = mysql_real_escape_string($_POST['id']);
        $type = mysql_real_escape_string($_POST['type']);

    }else{
        return;
    }




    $mysql_helper = new MySQLHelper();
    $sql = "delete from good_website where type='$type' and id='$id' ";


    $status_number = $mysql_helper->excute_dml($sql);
        // 如果没有成功，就返回0;
        // 执行成功并且有行受到影响, 返回1
        // 表示执行成功但是没有行受到影响, 返回2



    echo $status_number;
    $mysql_helper->close_connect();




?>