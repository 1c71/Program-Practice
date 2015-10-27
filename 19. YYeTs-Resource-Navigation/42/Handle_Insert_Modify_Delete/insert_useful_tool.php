<?php 
    require_once('../verify.php');
    require_once('../../tool/MySQL_Helper.php'); 
    
    /* 这个文件负责接收post请求. 并插入新数据. 不是用来直接访问的. */




    //注意, 接收到的全是string. 

    if ( isset($_POST['json_sort']) ){   // 如果post里有这个键.
        $sort = $_POST['json_sort'];    // 接数据
        $sort = intval($sort);  //如果转换失败. $sort会为0
    }else{
        // 如果json_sort 从 post 里拿不到. 应该就是直接访问了这个页面.
        // 为了避免显示不友好的报错信息. 我们跳转到首页去.
        header("Location: ../../index.php");
        return;
    }


    if (isset($_POST['json_name'])){
        $name = $_POST['json_name'];
        if(!is_numeric($name)){     
        //is_numeric判断变量是否是数字, 或者是数字字符串. 是的话就返回true.
            $name = mysql_real_escape_string($name);
        }
        
    }

    if (isset($_POST['json_intro'])){
        $intro = $_POST['json_intro'];
        if(!is_numeric($intro)){
            $intro = mysql_real_escape_string($intro);
        }
    }

    if (isset($_POST['json_imglink'])){
        $imglink = $_POST['json_imglink'];
        if(!is_numeric($imglink)){
            $intro = mysql_real_escape_string($imglink);
        }
    }

    if (isset($_POST['json_link'])){
        $link = $_POST['json_link'];
        if(!is_numeric($link)){
            $intro = mysql_real_escape_string($link);
        }
    }



$mysql_helper = new MySQLHelper();
$sql = "insert into useful_tool (sort, name, intro, imglink, link) values($sort, '$name', '$intro', '$imglink', '$link')";
//echo $sql;

$status = $mysql_helper->excute_dml($sql);
// 如果没有成功，就返回0;
// 执行成功并且有行受到影响, 返回1
// 表示执行成功但是没有行受到影响, 返回2
// MySQLHelper类是属于 tool/MySQL_Helper.php 文件的. 请参阅里面的返回代码.


$id = mysql_insert_id();
// 拿到上一步insert操作所插入的数据的id

// 将[状态代码]和[刚插入的数据的id]弄成一个数组.
$json = Array('status'=>$status, 'id'=>$id);


// ====JSON编码后 输出数据=====
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