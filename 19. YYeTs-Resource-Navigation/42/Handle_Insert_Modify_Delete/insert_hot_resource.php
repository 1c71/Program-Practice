<?php 
    require_once('../verify.php');
    require_once('../../tool/MySQL_Helper.php');
    header('Content-Type: text/html; charset=utf-8');


    /* 处理"热门资源管理"页面的 插入操作 */



    if( isset($_POST['type']) && isset($_POST['ijson']) ){
        $type = mysql_real_escape_string($_POST['type']);
        $txt = $_POST['ijson'];  //现在只是字符串而已.

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

        $sort = $value->{'sort'};
        $name = urldecode($value->{'name'});
        $link = urldecode($value->{'link'});

        $sql = "insert into hot_resource (type,sort,name,link) values('$type',$sort,'$name','$link');";


        $number = $mysql_helper->excute_dml($sql);
        // 如果没有成功，就返回0;
        // 执行成功并且有行受到影响, 返回1
        // 表示执行成功但是没有行受到影响, 返回2

        //我们这里啥也不返回.. 如果的确有需要的话可以做一个数组什么的.. push $number就行

    }


// foreach就是循环嘛. 下面这句echo在foreach语句之外
// 所以它实际干的是返回foreach最后一次操作时候赋值的$number
echo $number;


$mysql_helper->close_connect();




?>