<?php 
/* 这个文件负责处理后台登录的 用户名和密码验证. */


/* ===========接受表单发来的用户名和密码========== */
$un = $_POST['un'];
$pw = $_POST['pw'];


/* ===========如果用户名或密码的其中一个为空, 那也就不用处理了, 直接跳回去============ */
if($un=="" or $pw==""){
    header("Location: index.html");
    return;
}

/* =============俩都不为空的话那我们就验证用户名密码是否正确==================== */


// 下面代码只是做了  [验证] [设session] [跳转]  这3件事情而已
// 死密码写在这里了. 可自行更改.

if($un == "yyets" and $pw == "superadmin"){

    session_start();
    $_SESSION["admin"] = true;      
    // 设为true之后, 实际上当你在 $_SESSION 取值的时候, 值会是1      

    //  保存一天
    $lifeTime = 24 * 3600;
    setcookie(session_name(), session_id(), time() + $lifeTime, "/");

    // 跳转
    header("Location: real_back.php");
    return;

}
else{
    // 密码不对的话也不弄什么友好的错误显示了..直接跳回登录页
    header("Location: index.html");
    return;

}














?>