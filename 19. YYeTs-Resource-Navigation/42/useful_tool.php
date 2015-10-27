<?php 
    require_once('../tool/MySQL_Helper.php');
?>
<!DOCTYPE html>
<html lang="cn">
<html>
<head>
    <title>实用工具管理(用于iframe, 标题一般看不到)</title>
    <meta http-equiv="content-type" content="html/text; charset=utf-8;">

    <link rel="stylesheet"  href="../css/reset.css">
    <link rel="stylesheet" type="text/css" href="../css/bootstrap.min.css">
    <link rel="stylesheet" type="text/css" href="../css/bootstrap-responsive.min.css">
    <link rel="stylesheet"  href="css/back.css">
</head>
<body>



    <button id="tool_new_btn" type="button" class="btn btn-info btn-small" style="margin-left:10px;margin-bottom:10px;">
        添加新条目
    </button>


    <table class="resource_table">
        <thead> 
            <td>排序</td> <td>名称</td> <td>简介</td><td>图片地址</td> <td>链接地址</td> 
        </thead>
        <!-- <div style="height:20px;"></div> -->

        <!-- 一行就是一个tr -->
        <?php 

            $mysql_helper = new MySQLHelper();
            $sql_command = "select * from useful_tool order by sort";

            $res_tool = $mysql_helper->excute_dql($sql_command);

                while($row = mysql_fetch_assoc($res_tool)){
                    echo "<tr id={$row['id']}>";    //这里的id是用于让jQuery删除节点的.
                        echo "<td> <input type='text' name='sort' class='input-mini' value=".$row['sort']."> </td> ";
                        echo "<td> <input type='text' name='name' class='input-medium' value=".$row['name']."> </td> ";
                        echo "<td> <input type='text' name='intro' class='input-large' value=".$row['intro']."> </td> ";
                        echo "<td> <input type='text' name='imglink' class='input-large' value=".$row['imglink']."> </td> ";
                        echo "<td> <input type='text' name='link' class='input-xlarge' value=".$row['link']."> </td> ";
                        echo "<td> <a href='#' id={$row['id']}>删除</a> </td> ";
                        // 这里的 id 用于 点击"删除"后
                        // 用 ajax 把 a 标签里 id 的值, 发给delete_useful_tool.php
                        // 由它来删除掉数据.
                    echo "</tr>";  
                }

            mysql_free_result($res_tool);
            $mysql_helper->close_connect();
         ?>
    </table>



    <button type="button" id="tool_save_change" class="btn btn-success" style="margin-left:10px;margin-top:10px;">
        <i id="save_change_icon" class="icon-wrench"></i> &nbsp; 提交修改
    </button>

    <br>





    <div id="new_form" class="new_box" style="">

        <label for="f_sort"> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;排序 </label>
        <input type="text" name="f_sort" id="f_sort" class="input-mini">
        <br>

        <label for="f_name"> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;名称 </label>
        <input type="text" name="f_name" id="f_name">
        <br>

        <label for="f_intro" >&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;简介 </label>
        <input type="text" name="f_intro" id="f_intro">
        <br>

        <label for="f_imglink"> 图片地址 </label>
        <input type="text" name="f_imglink" id="f_imglink">
        <br>

        <label for="f_link"> 链接地址 </label>
        <input type="text" name="f_link" id="f_link">
        <br>

        <button id="yes" type="button"> 确定  </button>
        <button id="no" type="button">  取消  </button>
    </div>












<!-- ==============================脚本=========================================== -->


<script src="../js/jquery-1.9.1.min.js"></script>
<script src="../js/bootstrap.min.js"></script>

<script type="text/javascript" src="../js/mootools-core-1.4.5-full-compat-yc.js"></script>
<script type="text/javascript" src="../js/mootools-more-1.4.0.1.js"></script>






<script type="text/javascript">
jQuery.noConflict();

(function($){


    // ==== 点击 "删除" 后的处理函数 ====
    $('.resource_table tr td a').click(function(){
        var itemid = $(this).attr('id');
        //alert(itemid);   //你可以去掉这行注释测试一下.

        var send_data = {'id':itemid};

        $.ajax({
            url: "Handle_Insert_Modify_Delete/delete_useful_tool.php",
            data: send_data,
        }).done(function(r) {
            if(r==1){
                $('#'+itemid).remove();
            }
        });

    });


    // ==== "添加新条目"按钮点击后 ==== 
    $('#tool_new_btn').click(function(){
        // 显示表单
        //$('#new_form').css('display','inline-block');
        $('#new_form').toggle();
    });
        

    // 下面这句可以把  "新条目表单"  调成默认不显示
    // $('#new_form').css('display','none'); 





    // ==== 点击添加新条目的表单里的"确认"按钮后 ==== 
    $('#yes').click(function(){

        var sort = $('#f_sort').val()||1;      //排序可以为空
        var name = $('#f_name').val();         
        var intro = $('#f_intro').val()||1;     //介绍可以为空
        var imglink = $('#f_imglink').val()||1;     //图片链接可以为空
        var link = $('#f_link').val();

        //var imglink = $('#f_imglink').val()||1;  这种语法的意思是 如果取值为空的话 那么赋值为1


        // sort(排序)如果为空, 会被赋值为1. 
        // sort(排序)如果不为空sort必须为数字,
        if(isNaN(sort)){
            alert('排序必须是数字');
            return;
        }


        // name(名称) 不能为空
        if(name == ""){
            alert('名称不允许为空');
            return;
        }

        // link(链接地址) 不能为空
        if(link == ""){
            alert('链接地址不允许为空');
            return;        
        }



       // 发ajax请求
       $.ajax({
            type: "POST",
            url: "Handle_Insert_Modify_Delete/insert_useful_tool.php",
            dataType: "json",
            data: {
                'json_sort':sort, 
                'json_name':name, 
                'json_intro':intro, 
                'json_imglink':imglink,
                'json_link':link
            },    
            /*  
                加个前缀免得搞晕.
                传过去之前就自动拆开了 $_POST['json_sort'] 这样取就行了. 
            */
        }).done(function(msg) {

            //传回来的JSON数据直接取就行了 不用再做一次JSON.parse
            var status = msg['status'];
            var last_insert_id = msg['id'];

            // 返回1,代表成功, [我们现在再把数据动态插入到页面上] 
            // 如果不这么做的话. 就需要刷新才能看到刚插入的数据.
            if(status == 1){

                // 构造html数据
                var htmldata = "<tr id="+last_insert_id+">"+
                "<td> <input type='text' class='input-mini' value="+sort+"> </td> "+
                "<td> <input type='text' class='input-medium' value="+name+"> </td> "+
                "<td> <input type='text' class='input-medium' value="+intro+"> </td> "+
                "<td> <input type='text' class='input-xlarge' value="+imglink+"> </td> "+
                "<td> <input type='text' class='input-xlarge' value="+link+"> </td> "+
                "<td> <a href='#' id="+last_insert_id+">删除</a> </td> "+
                "</tr>";  

                //真正插入数据.
                $('.resource_table tr:last').after(htmldata);   


                // 清空所有输入框
                $('#new_form input').each(function(){
                    $(this).val("");
                });
            }
            
        });

    });



    // "取消" 按钮    跟 "知识讲解管理"" 页面 一样
    $('#no').click(function(){

        // 1.隐藏浅蓝色表单
        // 2.清空所有input 

        // [1]
        $('#new_form').css('display','none');

        // [2]
        $('#new_form input').each(function(){
            $(this).val("");
        });

    });





    // 【修复无法聚焦问题】
    // 因为我们把这个 div 用 mootools 变成可拖动的了.
    // 但是这时点击 input 就无法获得焦点了.. 就是说你没有办法输入东西
    // 我们用下面的代码来修复这个问题.
    $('#new_form input').click(function(){
        $(this).focus();
    });










    // ===== 有关 "提交修改" 的相关代码======
    // 这里的实现思路和 "知识讲解管理" 里面的 “提交修改” 是一样的



    var tool_modify = false;     

    $('.resource_table input').change(function(){
        // 当某个input被修改后. 我们将他的父tr加一个modify属性.
        $(this).closest('tr').attr('modify','true');
        tool_modify = true;
    });



    // "提交修改"
    $('#tool_save_change').click(function(){
        // 1. 根据 tool_modify 判断是否修改过页面上的 input. 如果没有, 啥也不干
        // 2. 循环每个tr 找出被修改过的tr
        // 3. 取tr里面的 5 个td的值.
        // 4. Ajax传给 modify_useful_tool.php


        // [1]
        if(tool_modify){


            //这个空对象待会会存放那些修改过的数据
            var tools_row = {};

            // [2]
            $('.resource_table tr').each(function(){

                //如果有该属性, 说明这一行被修改过.
                if($(this).attr('modify')){

                    // 拿到tr的id属性
                    var id = $(this).attr('id');

                    // “排序”
                    var sort = $(this).find("input[name='sort']").val();

                    // “名称”
                    var name = $(this).find("input[name='name']").val();

                    // “简介”
                    var intro = $(this).find("input[name='intro']").val();

                    // “图片链接”
                    var imglink = $(this).find("input[name='imglink']").val();

                    // “拿链接地址”
                    var link = $(this).find("input[name='link']").val();



                    // 我们确认一下 '排序' 里面填的值必须是数字
                    if(!parseInt(sort)){    // parseInt转换字母会返回NaN
                        alert('排序必须是个数字');
                    }
                    else{
                        sort = Math.ceil(sort);     // 不允许小数, 我们转换成整数
                    }


                    tools_row[id] = {};

                    tools_row[id]['id'] = id;
                    tools_row[id]['sort'] = sort;
                    tools_row[id]['name'] = encodeURIComponent(name);
                    tools_row[id]['intro'] = encodeURIComponent(intro);
                    tools_row[id]['imglink'] = encodeURIComponent(imglink);
                    tools_row[id]['link'] = encodeURIComponent(link);  


                }


            }); // 循环tr结束


            console.log(tools_row);


            // 转换成json格式了

            var tool_modify_data = JSON.stringify(tools_row);
            console.log(tool_modify_data);


            var json = {'json': tool_modify_data};


            $.ajax({ 
                type: "POST",
                data: json,
                url: 'Handle_Insert_Modify_Delete/modify_useful_tool.php',
                beforeSend: function(){
                    // 发请求的时候换一下图标.
                    $('#tool_save_change i').replaceWith('<img src="../img/wait.gif" width="18px">');
                }
            }).done(function(return_message){
                // 完成之后再换回来
                $('#tool_save_change img').replaceWith('<i id="save_change_icon" class="icon-wrench"></i>');


                // alert(return_message);
            });


        }


    }); 


    // ===== "提交修改"相关代码 结束 ======
    

})(jQuery);
// ---- jQuery 代码结束 ---- 






// ---- JS 代码 ----


// ---- JS 代码结束 ----





// ---- Mootools代码 ----
(function($){

    window.addEvent('domready', function(){

        new Drag.Move($('new_form'));

    });



})(document.id);
// ---- Mootools代码 结束 ----



// 以这种方式写是为了 jQuery 和 MooTools 不冲突. 更多信息可查阅:
// http://stackoverflow.com/questions/2810399/jquery-and-mootools-conflict

</script>



</body>
</html>