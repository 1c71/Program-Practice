<?php 
    require_once('../tool/MySQL_Helper.php');
?>
<!DOCTYPE html>
<html lang="cn">
<html>
<head>
    <meta http-equiv="Content-Type" content="text/html; charset=utf-8">
    <title>实用工具管理(用于iframe, 标题一般看不到)</title>

    <link rel="stylesheet"  href="../css/reset.css">
    <link rel="stylesheet" type="text/css" href="../css/bootstrap.min.css">
    <link rel="stylesheet" type="text/css" href="../css/bootstrap-responsive.min.css">

    <link rel="stylesheet"  href="css/back.css">
    <style type="text/css">
        tr{
            padding-top: 10px;
        }

    </style>
    
</head>
<body>



    <button type="button" id="know_new_btn" class="btn btn-info btn-small" style="margin-left:10px;margin-bottom:10px;">
        添加新条目
    </button>


    <table class="resource_table">
        <thead> 
            <td>排序</td> <td>标题</td> <td>链接地址</td> 
        </thead>
        <!-- 一行就是一个tr -->
        <?php 
            $mysql_helper = new MySQLHelper();
            $sql_command = "select * from knowledge_share order by sort";

            $res_know = $mysql_helper->excute_dql($sql_command);

                while($row = mysql_fetch_assoc($res_know)){
                    echo "<tr id='{$row['id']}' >";
                        echo "<td> <input type='text' name='sort' class='input-mini' value=".$row['sort']."> </td> ";
                        echo "<td> <input type='text' name='title' class='input-xlarge' value=".$row['title']."> </td> ";
                        echo "<td> <input type='text' name='link' class='input-xxlarge' value=".$row['link']."> </td> ";
                        echo "<td> <a id='{$row['id']}'href='#'>删除</a> </td> ";
                    echo "</tr>";  
                }

            mysql_free_result($res_know);
            $mysql_helper->close_connect();
         ?>
    </table>


    <button type="button" id="know_save_change" class="btn btn-success" style="margin-left:10px;margin-top:10px;">
        <i class="icon-book"></i> &nbsp; 提交修改
    </button>


    <br>









    <div id="new_form" class="new_box">

        <!-- knowledge share 取了首字母k 做表单元素的id  -->
        <label for="k_sort"> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;排序 </label>
            <input type="text" name="k_sort" id="k_sort" class="input-mini">
        <br>

        <label for="k_name"> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;标题 </label>
            <input type="text" name="k_title" id="k_title">
        <br>


        <label for="k_link"> 链接地址 </label>
            <input type="text" name="k_link" id="k_link">
        <br>

        <button id="yes" type="button"> 确定  </button>
        <button id="no" type="button">  取消  </button>
    </div>



















<script src="../js/jquery-1.9.1.min.js"></script>
<script src="../js/bootstrap.min.js"></script>

<script type="text/javascript" src="../js/mootools-core-1.4.5-full-compat-yc.js"></script>
<script type="text/javascript" src="../js/mootools-more-1.4.0.1.js"></script>


<script type="text/javascript">

jQuery.noConflict();

(function($){



        // 【修复无法聚焦问题】
        // 因为我们把这个 div 用 mootools 变成可拖动的了.
        // 但是这时点击 input 就无法获得焦点了.. 就是说你没有办法输入东西
        // 我们用下面的代码来修复这个问题.
        $('#new_form input').click(function(){
            $(this).focus();
        });




        // 现在是测试, 表单默认先显示.
        $('#new_form').css('display','inline-block'); 


        // "添加新条目"
        $('#know_new_btn').click(function(){
            $('#new_form').toggle();
        });
            



        // "确定"
        $('#yes').click(function(){
            // 1. 拿数据
            // 2. 验证
            // 3. 构造数据. 发ajax请求
            // 4. 如果返回值是1, 代表成功. 我们构造一个tr元素插入到页面上. 这样体验更好. 否则的话就只能刷新才能看到效果了.

            // [1]
            var sort = $('#k_sort').val()||2;
            var title = $('#k_title').val();
            var link = $('#k_link').val();

            

            // [2]
            if(title==""){
                alert('标题必填');
                return;
            }

            if(link==""){
                alert('链接地址也必填');
                return;
            }


            // [3]
            var data = {'sort':sort,'title':title,'link':link};

            $.post("Handle_Insert_Modify_Delete/insert_knowledge_share.php", data)
            .done(function(r){
                var status = r['status'];
                var return_id = r['id'];

                // [4]
                if(status == 1){

                    var html = "<tr id="+ return_id +" >"+
                    "<td> <input type='text' name='name' class='input-mini' value="+sort+"> </td> " +
                    "<td> <input type='text' name='title' class='input-xlarge' value="+title+"> </td> " +
                    "<td> <input type='text' name='link' class='input-xxlarge' value="+link+"> </td> " +
                    "<td> <a id="+ return_id +" 'href='#'>删除</a> </td> " +
                    "</tr>";  

                    $('.resource_table tr:last').after(html);   //插入数据.
                }
            });

        }); 
        // "确定"结束   (因为函数有点长, 避免搞晕..)



        // "取消"
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



        var already_modify = false;     
        //用于判断页面上的信息(就是那些td里的input)是否被修改过. 当点击"提交修改"的时候需要用到.


        $('.resource_table input').keydown(function(){
            //$(this).closest('tr').css('background-color','red');  
            //你可以把上面这行注释去掉,然后你会发现当你修改一个input的时候,他的父tr的背景颜色会变成红色


            // 当某个input被修改后. 我们将他的父tr加一个modify属性.
            $(this).closest('tr').attr('modify','true');
            already_modify = true;
        });





        // "提交修改"
        $('#know_save_change').click(function(){
            // 1. 根据 already_modify 判断是否修改过页面上的 input. 如果没有, 啥也不干
            // 2. 循环每个tr, 找出被修改过的tr
            // 3. 取tr里面的3个td的值.
            // 4. ajax传给 modify_knowledge_share.php 它会负责修改的.


            // [1]
            if(already_modify){

                //这个空对象待会会存放那些修改过的数据
                var modify_obj = {};

                // [2]
                $('.resource_table tr').each(function(){

                    //如果有该属性, 说明这一行被修改过.
                    if($(this).attr('modify')){

                        // 拿到tr的id属性
                        var m_id = $(this).attr('id');

                        // 拿"排序"
                        var m_sort = $(this).find("input[name='sort']").val();

                        // 拿标题
                        var m_title = $(this).find("input[name='title']").val();

                        // 拿链接地址
                        var m_link = $(this).find("input[name='link']").val();

                        modify_obj[m_id] = {};

                        modify_obj[m_id]['id'] = m_id;
                        modify_obj[m_id]['sort'] = m_sort;


                        modify_obj[m_id]['title'] = encodeURIComponent(m_title); //以URL形式编码, 
                        modify_obj[m_id]['link'] = encodeURIComponent(m_link);   

                    }


                }); // 循环tr结束


                // console.log(modify_obj);
                // 你可以把注释去掉然后看看结构.


                // 转换成json格式了
                var modify_data = JSON.stringify(modify_obj);
                //console.log(modify_json);

                var json = {'json':modify_data};


                $.ajax({
                    type: "POST",
                    url: 'Handle_Insert_Modify_Delete/modify_knowledge_share.php',
                    data: json,
                    beforeSend: function(){
                        // 换一下图标.
                       $('#know_save_change i').replaceWith('<img src="../img/wait.gif" width="18px">');
                    }
                }).done(function(m){

                    // 成功了再换回来
                    if(m == '1' || m=='2'){
                        $('#know_save_change img').replaceWith('<i class="icon-ok"></i>');

                        $('.resource_table tr').each(function(){
                            $(this).removeAttr('modify')
                        });

                    }else{
                        $('#know_save_change').html('修改出错');
                        $('#know_save_change').attr('class','btn btn-warning');
                    }

                });










            }


        }); // "提交修改" 结束
        



        // '删除'
        $('.resource_table a').bind('click', function(){
            // 1. 拿id
            // 2. 发请求
            // 3. 如果返回值是1, 代表操作成功. 那么我们把那一行从页面上删除(tr标签和a标签有着相同的id)
            
            //[1]
            var id = $(this).attr('id');
            
            //[2]
            $.post('Handle_Insert_Modify_Delete/delete_knowledge_share.php', {'id':id})
            .done(function(r){
                //[3]
                if(r=='1'){
                    $('tr#'+id).remove();
                }
            });

        }); 


})(jQuery);
// ---- jQuery 代码结束 ---- 



// ---- Mootools代码 ----
(function($){

    window.addEvent('domready', function(){

        new Drag.Move($('new_form'));

    });


})(document.id);
// ---- Mootools代码 结束 ----



// 以这种方式写是为了 jQuery 和 MooTools 不冲突. 更多信息可查阅:
// http://stackoverflow.com/questions/2810399/jquery-and-mootools-conflict
// ~






</script>














</body>
</html>