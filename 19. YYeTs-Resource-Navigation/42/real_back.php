<?php  
    require_once('verify.php');
    // require会在引入之后马上执行. require_once()一样. 只不过是它会检测是否重复包含该文件而已.
    // 这个文件里的内容是用 SESSION 验证是否登录. 没有登录就跳回登录页
?>
<!DOCTYPE html>
<html>
<head>
    <title>后台</title>
    <meta http-equiv="content-type" content="html/text; charset=utf-8;">
    <link rel="stylesheet"  href="../css/reset.css">
    <link rel="stylesheet" type="text/css" href="../css/bootstrap.min.css">
    <link rel="stylesheet" type="text/css" href="../css/bootstrap-responsive.min.css">


    <style type="text/css">
        body{
            height: 100%;   
            /* iframe即使设置了100%之后，实际高度是150px. 要把body设置为100%, iframe才会真正100% */
        }

        /* 后台页头的导航部分. 比如热门资源管理, 好站推荐管理 */
        #top{
            background-color: #e0e0e0;
        }

        #top ul{
            list-style: none;
        }

        #top ul li{
            display: inline-block;
            margin-left: 20px;
            margin-top: 5px;
            margin-bottom: 5px;
        }

        /* 热门资源管理距离左边的外边距 */
        #top ul li:first-child{
            margin-left: 96px;
        }

        #top ul li a{
            text-align: center;
            display: inline-block;

            width: 120px;
            height: 20px;

            color: #2c2c2c;
            font-size: 14px;
            font-weight: bold;
            text-decoration: none;  
            
            padding-top: 5px;
            padding-bottom: 5px;

            height: 24px;
            line-height: 24px;



        }


        #top ul li a:hover{
            color: white;
            background-color: #0096ff;
        }




        /* 当顶部灰色框里的任意一个链接被点击后的"选中"样式 */
        .nav_Click{
            color: white  !important;
            background-color: #0096ff;
        }

    </style>
</head>
<body>

    <div id="top">
        <ul>
            <li> <a href="hot_resource.php" target="main">热门资源管理</a> </li>
            <li> <a href="good_website.php" target="main">好站推荐管理</a></li>
            <li> <a href="knowledge_share.php" target="main">知识讲解管理</a> </li>
            <li> <a href="useful_tool.php" target="main">实用工具管理</a> </li>
            <li> <a id='refresh' href="javascript:void(0);" >更新首页缓存</a> </li>
        </ul>
    </div>


    <iframe name="main" frameborder='0' style="width:100%; height:90%;" src="hot_resource.php">
    </iframe>
    <!-- height:90%; 就不会有滑动条了. -->


    <script src="../js/jquery-1.9.1.min.js"></script>
    <script type="text/javascript">
        $(function(){

            // 默认的第几个导航有  被选中样式
            $('#top a:eq(0)').not('#refresh').addClass('nav_Click');


            /* 当顶部灰色框里的任意一个链接被点击后. */
            $('#top a').not('#refresh').click(function(){

                /* 先移除掉所有元素的nav_Click类 */
                $('#top a').each(function(){
                    $(this).removeClass('nav_Click');
                });

                /* 给点击的元素加上nav_Click类 */
                $(this).addClass('nav_Click');
            });



            // "更新首页缓存"
            $('#refresh').click(function(){

                $.ajax({
                    url: '../index.php?refresh_cache=1'
                }).done(function(){
                    alert('收工！');
                });

            });



        });
    </script>
</body>
</html>