<?php 

    require_once('../verify.php');
    require_once('../../tool/MySQL_Helper.php');
    header('Content-Type: text/html; charset=utf-8');


    /* 处理"好站推荐管理"的 更新(或者说修改)操作 */


    if( isset($_POST['json'])){
        $json_text = $_POST['json'];
    }else{
        return;
    }

    $json = json_decode($json_text); 
    // $json 现在是 object
    // echo gettype($json);        


    //var_dump($json);
    // 你可以去掉注释看看格式. 可以在chrome的Network里看响应. 不要用echo 
    // JS 用 encodeURIComponent 编码中文.. 然后PHP用 urldecode 来解码是没有问题的.
    // 但是Chrome的preview页面却会显示乱码. 不要担心.



$mysql_helper = new MySQLHelper();

$has_error = 0;

    foreach($json as $key=>$value){

        $type = $value->{'type'};
        $id = $value->{'id'};
        $sort = $value->{'sort'};
        $name = $value->{'name'};
        $intro = $value->{'intro'};
        $link = $value->{'link'};

        $sql = "update good_website set sort=$sort, name='$name', intro='$intro', link='$link' where type='$type' and id=$id;";


        $number = $mysql_helper->excute_dml($sql);
        // 如果没有成功，就返回0;
        // 执行成功并且有行受到影响, 返回1
        // 表示执行成功但是没有行受到影响, 返回2

        // 每执行完一条语句就判断一下是否成功.
        // 如果失败, 就把$has_error设为1
        if($number == 0){
            $has_error = 1;
        }


    }


    // 如果$has_error == 1 会进入if分支
    // 一般来讲都是进入else分支.
    if($has_error){
        echo "something error in modify_good_website.php";
    }else{
        echo "all success";
    }


$mysql_helper->close_connect();




?>