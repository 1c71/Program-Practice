<?php 
    require_once('../verify.php');
    require_once('../../tool/MySQL_Helper.php');
    header('Content-Type: text/html; charset=utf-8');


    /* 处理"热门资源管理"页面的 更新操作~ */



    if( isset($_POST['type']) && isset($_POST['mjson']) ){
        $type = mysql_real_escape_string($_POST['type']);
        $txt = $_POST['mjson'];  //现在类型还是 string
    }else{
        return;
    }

    $json = json_decode($txt); 
    // $json 现在是 object
    // echo gettype($json);        


    //var_dump($json);
    // 你可以去掉注释看看格式. 可以在chrome的Network里看响应. 不要用echo 
    // JS 用 encodeURIComponent 编码中文.. 然后PHP用 urldecode 来解码是没有问题的.
    // 但是Chrome的preview页面却会显示乱码. 不要担心.


$mysql_helper = new MySQLHelper();


    foreach($json as $key=>$value){

        $id = $value->{'id'};
        $sort = $value->{'sort'};
        $name = urldecode($value->{'name'});
        $link = urldecode($value->{'link'});

        $sql = "update hot_resource set sort=$sort, name='$name',link='$link' where id=$id;";

        $number = $mysql_helper->excute_dml($sql);
        // 如果没有成功，就返回0;
        // 执行成功并且有行受到影响, 返回1
        // 表示执行成功但是没有行受到影响, 返回2

    }


// 当后台操作的时候.
// 有时候修改一个input, 那个tr就加上了modify. 保存修改后
// 再修改另一个的时候, 由于第一次修改的那个tr有modify属性，所以又发过来了. 但是数据是一样的. 所以excute_dml会返回2
// 所以$number一般会返回1或2.
echo $number;

$mysql_helper->close_connect();




?>