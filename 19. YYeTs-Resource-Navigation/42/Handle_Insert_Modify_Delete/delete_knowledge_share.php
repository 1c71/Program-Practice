<?php 
    require_once('../verify.php');
    require_once('../../tool/MySQL_Helper.php');


    /* 处理"知识讲解"页面的删除请求 */


    if (isset($_POST['id'])){
        $id = $_POST['id'];
        $id = intval($id);      // 转成数字
        
        // 如果是数字或数字字符串. is_numberic会返回true. 这里取反了.
        // 如果不是数字, 才会进入下面这个分支.
        if(!is_numeric($id)){   
            echo "not number";
            return;
        }
    }




    $mysql_helper = new MySQLHelper();
    $sql = "delete from  knowledge_share  where id = $id";
    //echo $sql;

    $number = $mysql_helper->excute_dml($sql);
    // 如果没有成功，就返回0;
    // 执行成功并且有行受到影响, 返回1
    // 表示执行成功但是没有行受到影响, 返回2

    echo $number;

    $mysql_helper->close_connect();

?>
