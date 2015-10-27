<?php 
    require_once('../verify.php');
    require_once('../../tool/MySQL_Helper.php');


    /* 处理"知识讲解管理"页面的 更改 */



    if(isset($_POST['json'])){
        $txt = $_POST['json'];  //现在只是字符串而已.
    }else{
        return;
    }


    // http://stackoverflow.com/questions/1389431/how-to-check-if-object-is-empty-in-php
    // json_decode   http://www.php.net/json_decode
    $json = json_decode($txt, true); 
    // $json 现在是 array了
    // echo gettype($json);        

    if(empty($json)){
        echo "空";
        return;
    }


    // var_dump($json); 
    
    // 你可以去掉注释看看格式. 可以在chrome的Network里看响应
    // JS 用 encodeURIComponent 编码中文.. 然后PHP用 urldecode 来解码是没有问题的.
    // 但是Chrome的preview页面却会显示乱码. 不要担心.




$mysql_helper = new MySQLHelper();


    foreach($json as $key=>$value){

        $id = $value['id'];
        $sort = $value['sort'];
        $title = urldecode($value['title']);
        $link = urldecode($value['link']);

        $sql = "update knowledge_share set sort='$sort', title='$title', link='$link' where id = $id;";


        $number = $mysql_helper->excute_dml($sql);
        // 如果没有成功，就返回0;
        // 执行成功并且有行受到影响, 返回1
        // 表示执行成功但是没有行受到影响, 返回2


    }

echo $number;


$mysql_helper->close_connect();

















?>
