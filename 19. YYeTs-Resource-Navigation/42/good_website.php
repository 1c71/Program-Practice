<?php 
    require_once('../tool/MySQL_Helper.php');
?>
<!DOCTYPE html>
<html>
<head>
    <title>好站推荐</title>

    <link rel="stylesheet"  href="../css/reset.css">
    <link rel="stylesheet" type="text/css" href="../css/bootstrap.min.css">
    <link rel="stylesheet" type="text/css" href="../css/bootstrap-responsive.min.css">
    <link rel="stylesheet"  href="css/back.css">


    <style type="text/css">
        body{
            margin-top: 10px;
        }


        .main{
            margin-left: 20px;
        }

    </style>
    
</head>
<body>


<div class="main">
    <div class="tabbable tabs-left ">

        <ul class="nav nav-tabs">
            <li class="active"><a href="#lA" data-toggle="tab">资源下载站</a></li>
            <li class=""><a href="#lB" data-toggle="tab">点播站</a></li>
            <li class=""><a href="#lC" data-toggle="tab">视频站</a></li>
            <li class=""><a href="#lD" data-toggle="tab">PT站</a></li>
            <li class=""><a href="#lE" data-toggle="tab">其他相关站</a></li>
            <li class=""><a href="#lF" data-toggle="tab">美图美女站</a></li>
        </ul>

        <div class="tab-content">

            <!-- 资源下载站 -->
            <div class="tab-pane active" id="lA" type='download'>   <!-- type属性在插入数据库的时候需要用到.  -->
                    <?php Recommend('download'); ?>
            </div>



            <!-- 点播站 -->
            <div class="tab-pane" id="lB" type='online'>
                    <?php Recommend('online'); ?>
            </div>

            <!-- 视频站 -->
            <div class="tab-pane" id="lC" type='video'>
                    <?php Recommend('video'); ?>
            </div>

            <!-- PT站 -->
            <div class="tab-pane" id="lD" type='pt'>
                    <?php Recommend('pt'); ?>
            </div>

            <!-- 其他相关站 -->
            <div class="tab-pane" id="lE" type='other'>
                    <?php Recommend('other'); ?>
            </div>

            <!-- 美图美女站 -->
            <div class="tab-pane" id='lF' type='girl'>
                    <?php Recommend('girl'); ?>
            </div>


        </div>  <!-- .tab-content 结束 -->



    </div>  <!-- .tabbable tabs-left 结束 -->
</div>  <!-- .main 结束 -->







    <div id="good_new_form" class="new_box">

        <label for="g_sort"> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;排序 </label>
        <input type="text" name="g_sort" id="g_sort" class="input-mini">
        <br>

        <label for="g_name"> 网站名称 </label>
        <input type="text" name="g_name" id="g_name">
        <br>

        <label for="g_intro" > 网站简介 </label>
        <input type="text" name="g_intro" id="g_intro">
        <br>

        <label for="g_link"> 链接地址 </label>
        <input type="text" name="g_link" id="g_link">
        <br>

        <button id="yes" type="button"> 确定  </button>
        <button id="no" type="button">  取消  </button>
    </div>






<!-- ================= 引入一些库 ==================================== -->

<script type="text/javascript" src="../js/jquery-1.9.1.min.js"></script>
<script type="text/javascript" src="../js/bootstrap.min.js"></script>

<script type="text/javascript" src="../js/mootools-core-1.4.5-full-compat-yc.js"></script>
<script type="text/javascript" src="../js/mootools-more-1.4.0.1.js"></script>




<script type="text/javascript">
jQuery.noConflict();

(function($){


    // "添加新站" 点击后的那个表单. 默认不显示.
    $('#good_new_form').css('display','none');




    //  [添加新站]
    $('.good_new_btn').click(function(){
        var type = $(this).closest('div').attr('type');     // 拿到【添加新站】最近的div的type
        $('#good_new_form').toggle();           // 切换显示状态
        $('#good_new_form').attr('type',type);  // 给这个div表单加一个type属性, 值是最近的div的type
        // 这样做的话, 你在不同的tab下点击"添加新站"的时候, 那个表单就会有不同的type属性
        // 做插入数据库的时候需要用到.
        // 比如你点击 "资源下载站" --> 添加新站.
        // 这样 #good_new_form 的type属性就是 download
    });





    // "确定" 按钮 (100%是插入操作) (不要和"添加新站"混淆了.. 这个是浅蓝色表单的确定按钮)
    $('#yes').click(function(){

        // 1.拿type属性

        var type = $('#good_new_form').attr('type');



        // 2. 拿表单里的数据

        // “排序”
        var sort = $('#good_new_form').find("#g_sort").val();

        // “网站名称”
        var name = $('#good_new_form').find("#g_name").val();

        // “网站简介”
        var intro = $('#good_new_form').find("#g_intro").val();

        // “拿链接地址”
        var link = $('#good_new_form').find("#g_link").val();


        // 如果都是空..
        if(sort == '' && name == '' && intro == '' && link == ''){
            alert('你坑我呢~');
            return;
        }




        // 3. 发ajax请求. 把数据插入数据库

        var insert_data = {'type':type, 'sort':sort, 'name':name, 'intro':intro, 'link':link};

        $.ajax({ 
            type: "POST",
            data: insert_data,
            url: 'Handle_Insert_Modify_Delete/insert_good_website.php'
        }).done(function(i_r){

            if(i_r['good_website_insert_status'] == 1){

                // 清空一下表单
                $('#good_new_form input').each(function(){
                    $(this).val('');
                });

                location.reload();
            }

        }); 
        // ajax 结束



    });
    // "确定" 结束











    // "取消" 按钮 
    $('#no').click(function(){

        // 1.隐藏表单
        $('#good_new_form').css('display','none');


        // 2.清空所有input 
        $('#good_new_form input').each(function(){
            $(this).val("");
        });

    });


    // 【修复无法聚焦问题】
    // 因为我们把这个 div 用 mootools 变成可拖动的了.
    // 但是这时点击 input 就无法获得焦点了.. 就是说你没有办法输入东西
    // 我们用下面的代码来修复这个问题.
    $('#good_new_form input').click(function(){
        $(this).focus();
    });




    // 切换tab的时候把表单隐藏掉.
    $('.nav-tabs').click(function(){
        $('#good_new_form').css('display','none');
    });






    // ==== '删除' ====
    $('div.tab-pane a').click(function(){

        // 1. 拿type
        var del_type = $(this).closest('tr').attr('type');

        // 2. 拿id
        var del_id = $(this).closest('tr').attr('id');


        // 3. 打个包
        var del_data = {'type':del_type, 'id':del_id};


        // 4. 发ajax
        $.ajax({ 
            type: "POST",
            data: del_data,
            url: 'Handle_Insert_Modify_Delete/delete_good_website.php'
        }).done(function(d_r){

            // 判断是否删除成功.
            if(d_r == '1'){
                $('tr#'+del_id).remove();   // 把那个tr删了.
            }

        }); 
        // ajax 结束


        // 5. 洗洗睡了


    }); 
    // 删除 结束
    



    // "提交修改"

    $('.good_save_change').click(function(){


        var type = $(this).closest('div.tab-pane').attr('type');     
        // 拿到“提交修改”按钮 的最近的class为tab-pane的div的 type

        var need_send = false;   
        // 因为我们的tr each和ajax是分开的. 所以不管each有没有拿到数据. ajax都会发出去 
        // 这没必要. 所以我们利用这个变量来控制ajax

        




        /* 
            我们的HTML的结构是这样的

            <div>
                button-添加新站
                table-数据
                button-提交修改
            </div>

        */

        // 所以....
        // 1. 找"提交修改"按钮的最近的div下的 table 下的 tr   然后我们循环每个tr
        // 2. 根据modify属性判断是否被修改过
        // 3. 对于修改过的tr, 我们取它的id, 以及4个input里面的值. 
        // 4. 然后ajax发给modify_good_website.php


        var all_modify_data = {};       //存数据.


        // [1] 
        $(this).closest('div').find('table tr').each(function(each_index){

            // [2]
            var modify = $(this).attr('modify');

            if(modify){     



                // 拿type
                var type = $(this).closest('tr').attr('type');


                // 拿id
                var id = $(this).closest('tr').attr('id');


                // “排序”
                var sort = $(this).find("input[name='sort']").val();

                // “网站名称”
                var name = $(this).find("input[name='name']").val();

                // “网站简介”
                var intro = $(this).find("input[name='intro']").val();


                // “拿链接地址”
                var link = $(this).find("input[name='link']").val();


                // 打个包. 实际上这个each_index在后台是不会用到的.
                // 后台我们只是对每个 "键值对" 循环, 把"值"里面的东西拼成sql语句然后执行而已.
                all_modify_data[each_index] = {};
                all_modify_data[each_index]['type'] = type;
                all_modify_data[each_index]['id'] = id;
                all_modify_data[each_index]['sort'] = sort;
                all_modify_data[each_index]['name'] = name;
                all_modify_data[each_index]['intro'] = intro;
                all_modify_data[each_index]['link'] = link;


                need_send = true;

            } // if modify 结束

        });  // each 结束


        // console.log(all_modify_data);return;    
        // 你要是觉得有点晕的话可以把注释去掉看看格式
        // 后面加个return是为了不发ajax请求


        if(need_send){

            // 这里转换成json格式
            var md = JSON.stringify(all_modify_data);
            console.log(md);
            var json = {'json': md};


            // [4]
            $.ajax({ 
                type: "POST",
                data: json,
                url: 'Handle_Insert_Modify_Delete/modify_good_website.php',
                beforeSend: function(){
                    // 发请求的时候换一下图标.
                    $('.good_save_change i').replaceWith('<img src="../img/wait.gif" width="18px">');
                }

            }).done(function(m_r){

                // 成功了再换回来
                if(m_r == "all success"){
                    $('.good_save_change img').replaceWith('<i class="icon-ok"></i>');
                }else{
                    $('.good_save_change img').replaceWith('修改出错');
                }
                

            });    


        }








    });
    // "提交修改" 结束



    // 给所有 class 为 resource_table 的 table. 添加一个事件
    // 当里面的某行tr被修改后, 就给丫加上一个modify=true属性
    // "提交修改"按钮点击后的数据库修改操作, 会需要用到这个属性来判断哪些行被修改过了.
    $('table.resource_table tr').keydown(function(){
        $(this).attr('modify','true');
    });








})(jQuery);
// ---- jQuery 代码结束 ---- 







// ---- Mootools代码 ----
(function($){

    window.addEvent('domready', function(){

        new Drag.Move($('good_new_form'));

    });



})(document.id);
// ---- Mootools代码 结束 ----



// 更多信息可查阅:
// http://stackoverflow.com/questions/2810399/jquery-and-mootools-conflict



</script>












</body>
</html>




<?php 

    /* [好站推荐]和[热门资源]差不多. 也是一段代码复用好几次..这里写成函数*/
    // Recommend -- 推荐
    function Recommend($type){
        $mysql_helper = new MySQLHelper();
        $sql_command = "select * from good_website where type='$type' order by sort;";

        $res = $mysql_helper->excute_dql($sql_command);

            echo   '<button type="button" class="btn btn-info btn-small good_new_btn" style="margin-left:10px;margin-bottom:10px;">';
            echo        '添加新站';
            echo   '</button>';

            echo  '<table class="resource_table">';
            echo  '<thead> ';
            echo      '<td>排序</td> <td>网站名称(8个字以内)</td> <td>网站简介(十个字以内)</td> <td>链接地址</td>'; 
            echo  '</thead>';
            while($row = mysql_fetch_assoc($res)){
                echo "<tr type=".$row['type']." id=".$row['id'].">";
                // id 用于删除操作. type用于插入操作.
                    echo "<td> <input type='text' name='sort' class='input-mini' value='{$row['sort']}'> </td> ";
                    echo "<td> <input type='text' name='name' class='input-medium' value='{$row['name']}''> </td> ";
                    echo "<td> <input type='text' name='intro' class='input-medium' value='{$row['intro']}'> </td> ";
                    echo "<td> <input type='text' name='link' class='input-xlarge' value='{$row['link']}'> </td> ";
                    // 这些input的name属性用于取值.
                    echo "<td> <a href='javascript:void(0)'>删除</a> </td> ";
                echo "</tr>";  
            }

            echo '</table>';
            echo '<button type="button" class="btn btn-success good_save_change" style="margin-left:10px;margin-top:10px;">';
            // class good_save_change 是给jQuery用的. 其他的是bootstrap的样式
            echo     '<i class="icon-ok"></i> &nbsp; 提交修改';
            echo '</button>';

        mysql_free_result($res);
        $mysql_helper->close_connect();      
    }









?>