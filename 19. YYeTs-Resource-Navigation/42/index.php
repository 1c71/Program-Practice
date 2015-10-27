<?php 

session_start();

// 如果已经登录   就跳转到后台. 没必要再登录一次
if (isset($_SESSION['admin']) && $_SESSION['admin'] == 1){
    header("Location: real_back.php");
    return;
}

?>

<!DOCTYPE html>
<html>
<head>
    <meta http-equiv="content-type" content="html/text; charset=utf-8;" />
    <title>你发现了神秘的后台</title>

    <link href="../css/reset.css" rel="stylesheet">
    <link href="../css/index.css" rel="stylesheet">
    <link href="../css/bootstrap.min.css" rel="stylesheet">
    <link href="../css/bootstrap-responsive.min.css" rel="stylesheet">

    <!-- Le HTML5 shim, for IE6-8 support of HTML5 elements -->
    <!--[if lt IE 9]>
      <script src="http://html5shim.googlecode.com/svn/trunk/html5.js"></script>
    <![endif]-->

    <style type="text/css">
        body{
            padding-top: 30px;
        }
    </style>
</head>
<body>




<div class="container">
    <div class="span4 offset4">


        <!-- ==登录表单开始== -->
        <form class="form-signin" action="Handle_Login.php" method="post">
            <h2 class="form-signin-heading">请登录</h2>
            <input name="un" id="username" type="text" class="input-block-level" placeholder="用户名">
            <input name="pw" id="password" type="password" class="input-block-level" placeholder="密码">
            <!--                 
                <label class="checkbox">
                    <input type="checkbox" value="remember-me"> 记住俺
                </label> 
            -->
            <button id="unique-login-button"  class="btn btn-large btn-primary" type="submit">
                我登~
            </button>
        </form>
        <!-- ==登录表单结束== -->




        <!-- 这是个错误提示框. 当用户名或密码没有填上的时候就弹这个. -->
        <div class="alert alert-error" style="display:none"> 
            <a class="close" onclick="$('.alert').hide()">×</a>

            <div id="error_message">
                <!-- 
                    错误信息默认为空, 让JS动态填充就行了. 
                    如果第一次错误, 就显示 "你忘记填用户名或者密码了"
                    第二次错误, 就显示 "你忘记填用户名或者密码了(2)" ...以此类推
                 -->
            </div>  
            
        </div>
        <!-- 错误提示框结束. -->



    </div>
</div> <!-- /container -->














<!-- =================== 载入必要的脚本 ======================= -->
<script src="../js/jquery-1.9.1.min.js"></script>
<script src="../js/bootstrap.min.js"></script>


<script type="text/javascript">
$(function(){

    var count_error = 0;    /* 负责计数错误次数 */


    /*
        点击登录按钮后, 判断用户名和密码框是否为空, 空就提示错误. 
    */
    $('#unique-login-button').click(function(){


        if ( $('#username').val()=="" || $('#password').val()=="" ){
            
            count_error = count_error + 1;

            if (count_error == 1){
                $('#error_message').html('你忘记填用户名或者密码了');
            }
            else if(count_error > 30){     /* 错误次数大于30次就很有可能就是闲着蛋疼了. */
                window.location.href = "http://www.google.com";   /* 把丫扔到google去 */
                /* 
                    如果别人要暴力破解的话会看一下源码, 然后发现你的表单是提交到Handle_Login.php
                    然后就不断构造请求直接提交数据给 Handle_Login.php
                    所以在这里防止暴力破解是没用滴..
                */
            }
            else{
                $('#error_message').html( '你忘记填用户名或者密码了('+count_error+')' );
            }
            

            $('.alert').show();     /* 显示提示框 */
            return false;   /* 这样就不会提交了 */
        }



    });




});
</script>



    
</body>
</html>