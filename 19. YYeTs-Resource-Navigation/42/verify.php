<?php 
session_start();

// 拿不到SESSION里的值就 跳到登录页.
if (!$_SESSION['admin'] == 1){
    header("Location: index.html");
    return;
}
?>