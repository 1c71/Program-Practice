<?php 
    require_once('../tool/MySQL_Helper.php');
?>
<!DOCTYPE html>
<html>
<head>
    <title>热门资源</title>

    <link rel="stylesheet"  href="../css/reset.css">
    <link rel="stylesheet" type="text/css" href="../css/bootstrap.min.css">
    <link rel="stylesheet" type="text/css" href="../css/bootstrap-responsive.min.css">

    <style type="text/css">
        body{
            margin-top: 10px;
        }
        table thead{
            text-align: center;
        }

        table tr td{
            padding-left: 10px;
            /* td 用不了margin */
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
            <li class="active"><a href="#lA" data-toggle="tab">电影</a></li>
            <li class=""><a href="#lB" data-toggle="tab">美剧</a></li>
            <li class=""><a href="#lC" data-toggle="tab">日韩剧</a></li>
            <li class=""><a href="#lD" data-toggle="tab">动漫</a></li>
            <li class=""><a href="#lE" data-toggle="tab">国产剧</a></li>
            <li class=""><a href="#lF" data-toggle="tab">游戏</a></li>
        </ul>

        <div class="tab-content">

            <!-- 电影 -->
            <div class="tab-pane active" id="lA">
                10个电影热门
                <br>
                <br>
                <table id="movie_table" type="movie">
                    <?php 
                        output_ten_tr('movie');
                    ?>
                </table>
                <button type="button" id="movie_btn" class="btn btn-success" style="margin-left:10px;margin-top:10px;">
                    <i class="icon-ok"></i> &nbsp; 提交修改
                </button>
            </div>

            <!-- 美剧 -->
            <div class="tab-pane" id="lB">
                10个美剧热门
                <br>
                <br>
                <table id="am_tv_table" type="am_tv">
                    <?php 
                        output_ten_tr('am_tv');
                    ?>
                </table>
                <button type="button" id="am_tv_btn" class="btn btn-success" style="margin-left:10px;margin-top:10px;">
                    <i class="icon-ok"></i> &nbsp; 提交修改
                </button>
            </div>

            <!-- 日韩剧 -->
            <div class="tab-pane" id="lC">
                10个日韩剧热门
                <br>
                <br>
                <table id="jk_tv_table" type="jk_tv">
                    <?php 
                        output_ten_tr('jk_tv');
                    ?>
                </table>
                <button type="button" id="jk_tv_btn" class="btn btn-success" style="margin-left:10px;margin-top:10px;">
                    <i class="icon-ok"></i> &nbsp; 提交修改
                </button>
            </div>




            <!-- 动漫 -->
            <div class="tab-pane" id="lD">
                10个动漫热门
                <br>
                <br>
                <table id="ct_table" type="ct">
                    <?php 
                        output_ten_tr('ct');
                    ?>
                </table>
                <button type="button" id="ct_btn" class="btn btn-success" style="margin-left:10px;margin-top:10px;">
                    <i class="icon-ok"></i> &nbsp; 提交修改
                </button>
            </div>




            <!-- 国产剧 -->
            <div class="tab-pane" id="lE">
                10个国产剧热门
                <br>
                <br>
                <table id="china_table" type="china">
                    <?php 
                        output_ten_tr('china');
                    ?>
                </table>
                <button type="button" id="china_btn" class="btn btn-success" style="margin-left:10px;margin-top:10px;">
                    <i class="icon-ok"></i> &nbsp; 提交修改
                </button>
            </div>




            <!-- 游戏 -->
            <div class="tab-pane" id="lF">
                10个游戏热门
                <br>
                <br>
                <table id="game_table" type="game">
                    <?php 
                        output_ten_tr('game');
                    ?>
                </table>
                <button type="button" id="game_btn" class="btn btn-success" style="margin-left:10px;margin-top:10px;">
                    <i class="icon-ok"></i> &nbsp; 提交修改
                </button>
            </div>



        </div>
    </div>
</div>









<!--   ======== JS 代码 =============== -->


    <script src="../js/jquery-1.9.1.min.js"></script>
    <script src="../js/bootstrap.min.js"></script>
    <script type="text/javascript">
    $(function(){


        // 清空按钮点击后清空那一行
        $('a.clear').click(function(){
            $(this).closest('tr').find('input').each(function(){
                $(this).val('');
            });
            $(this).closest('tr').attr('modify','true');
            $(this).closest('td').text("需要点击[提交修改]后才能保存, 如果想撤销可刷新页面.")
        });



        // 任何一个 input 如果被修改后
        $('table input').bind("keydown", function(){     //change事件在焦点离开输入框的时候才触发. 所以我们不用change事件

            //取父type属性
            var type = $(this).closest('tr').attr('type');    

            // 如果修改的是 modify 就给它的父 tr 加一个 modify=true 属性.
            if(type === 'modify'){
                $(this).closest('tr').attr('modify','true');
            }
            // 如果修改的是 insert 就给它的父 tr 加一个 insert=true 属性.
            else if(type === 'insert'){
                $(this).closest('tr').attr('insert','true');
            }

        });







        // "电影" 的提交按钮
        $('#movie_btn').click(function(){
            var id = $('#movie_btn').closest('div').find('table').attr('id');
            // 拿到最近的div下的table的id  拿到的id的类型是string
            // 去看看上面HTML的结构你就懂了.
            get_tableID_dosomething(id);
        });



        //美剧的提交按钮
        $('#am_tv_btn').click(function(){
            var id = $('#am_tv_btn').closest('div').find('table').attr('id');
            get_tableID_dosomething(id);
        });


        //日韩剧的提交按钮
        $('#jk_tv_btn').click(function(){
            var id = $('#jk_tv_btn').closest('div').find('table').attr('id');
            get_tableID_dosomething(id);
        });


        //动漫的提交按钮
        $('#ct_btn').click(function(){
            var id = $('#ct_btn').closest('div').find('table').attr('id');
            get_tableID_dosomething(id);
        });


        //国产剧的提交按钮
        $('#china_btn').click(function(){
            var id = $('#china_btn').closest('div').find('table').attr('id');
            get_tableID_dosomething(id);
        });


        //游戏的提交按钮
        $('#game_btn').click(function(){
            var id = $('#game_btn').closest('div').find('table').attr('id');
            get_tableID_dosomething(id);
        });



















// 不要问我为什么给函数取这个名字...
function get_tableID_dosomething(id){

    var table_id = id;       //另外拿个变量存一下参数.


// 思路
// 1. 根据拿到的表格id. 对整个表格的每个tr进行循环
// 2. 取这个 tr 的type
// 如果type == modify:
    // 取对应表格里的对应行的数据.(那3个input)
    // 如果全是空, 那就是删除操作. 把这个tr的id用ajax发给 delete_hot_resource.php
    // 如果某个域不为空. 那么就是修改操作. 把这3个input的数据打包.. 
    // 把数据发给 modify_hot_resource.php


// 如果type == insert:
    // 取对应表格里的对应行的数据..打个包
    // ajax 发出去.



    
    var modify_obj = {};
    var insert_obj = {};
    // 这俩存数据用的. 不能写在each里. 这样的话each外面的ajax相关操作是取不到值的.


    $('#'+table_id+' tbody tr').each(function(index){


        var type = $(this).attr('type');    
        //取tr的type属性

        if(type === 'modify'){  // 如果值为modify. 说明这一行是从数据库取的, 几乎都是修改操作.(如果这行tr的全部input都清空, 那就是删除操作)
            
            var was_modify = $(this).attr('modify');    
            //取这个tr的modify属性..还记得前面我们写过这样的代码: 当一个tr里的Input被修改后, 这个tr的modify属性会被设置为true.
            
            if(was_modify){

                console.log('执行到modify_flag了')
                $(this).closest('table').attr('modify_flag',"true");     
                // 如果这个tr里面的值的确被修改过了. 给这个tr的父table加一个modify_flag属性. 后面发ajax的时候需要用到它来判断的.
                // 后面还会有类似的操作. 后面的就不打注释了.


                var tr_id = $(this).attr('id');
                // 拿到tr的id属性

                
                var m_sort = $(this).find("input[name='sort']").val();
                // 拿"排序"    m mean modify

                
                var m_name = $(this).find("input[name='name']").val(); 
                // 拿"标题"                           

                
                var m_link = $(this).find("input[name='link']").val();                                
                // 拿"链接地址"


                // 如果这3样都是为空, 那么其实就是个[删除]操作.
                if(m_sort=="" && m_name=="" && m_link==""){

                    $.ajax({
                        type: "POST",
                        url: 'Handle_Insert_Modify_Delete/delete_hot_resource.php',
                        data: {'id':tr_id},
                    }).done(function(d_r){
                        location.reload();      //刷新
                    });

                    $(this).closest('table').attr('modify_flag',"false");
                    return;
                }

                
                modify_obj[tr_id] = {};
                modify_obj[tr_id]['id'] = tr_id;
                modify_obj[tr_id]['sort'] = m_sort;
                modify_obj[tr_id]['name'] = m_name;
                modify_obj[tr_id]['link'] = m_link;

            }
        
        }else if(type === 'insert'){

            var was_insert = $(this).attr('insert');    //取type属性
            
            if(was_insert){

                $(this).closest('table').attr('insert_flag',"true");

                var i_sort = $(this).find("input[name='sort']").val();
                // 拿"排序"


                if(!i_sort){
                    alert('排序不能为空~');
                    $(this).closest('table').attr('insert_flag',"false");
                    console.log('排序不能为空~1111');
                    return;
                }


                // 如果排序不是数字, 我们就把这个改为false, 这样后面就不会发ajax了。
                if(isNaN(i_sort)){
                    alert('排序必须是数字');
                    $(this).closest('table').attr('insert_flag',"false");
                    return;
                }else{
                    $(this).closest('table').attr('insert_flag',"true");
                }

                
                var i_name = $(this).find("input[name='name']").val();
                // 拿"标题"                        

                
                var i_link = $(this).find("input[name='link']").val(); 
                // 拿"链接地址"                              
                

                insert_obj[index] = {};
                insert_obj[index]['sort'] = i_sort;
                insert_obj[index]['name'] = i_name;
                insert_obj[index]['link'] = i_link;

            }
        }

    }); 
    // ==== tr的each结尾 =====







    // ===== 该发ajax请求了 =======


    var m_f = $('#'+table_id).attr('modify_flag');
    // m_f 是字符串类型
    //console.log(m_f);

    var i_f = $('#'+table_id).attr('insert_flag');
    // i_f 也是字符串类型
    //console.log(i_f);


    // http://stackoverflow.com/questions/1318076/jquery-hasattr-checking-to-see-if-there-is-an-attribute-on-an-element
    // For some browsers, `attr` is undefined; for others,
    // `attr` is false.  Check for both.
    if(typeof m_f !== 'undefined' && m_f !== false && m_f !== 'false'){   // 通过这个来判断页面上究竟有没有修改过某个input 
        var modify_data = JSON.stringify(modify_obj);
        var table_type = $('#'+table_id).attr('type');        //拿table的type属性.
        var m_json = {'type':table_type, 'mjson':modify_data};
        
        $.ajax({
            type: "POST",
            url: 'Handle_Insert_Modify_Delete/modify_hot_resource.php',
            data: m_json,
            beforeSend: function(){
                // 换一下图标.
                $('#'+table_id).closest('div').find('button i').replaceWith('<img src="../img/wait.gif" width="18px">');
            }
        }).done(function(m_r){

            // 成功了再换回来
            if(m_r == '1' || m_r == '2'){
                $('#'+table_id).closest('div').find('button img').replaceWith('<i class="icon-ok"></i>');
            }else{
                $('#'+table_id).closest('div').find('button img').replaceWith('修改出错');
            }

        });
    }

    if(typeof i_f !== 'undefined' && i_f !== false && i_f !== 'false'){   // 同理
        
        console.log('会执行到insert这里吗');
        var insert_data = JSON.stringify(insert_obj);
        var table_type = $('#'+table_id).attr('type');        //拿table的type属性.
        var i_json = {'type':table_type, 'ijson':insert_data};

        $.ajax({
            type: "POST",
            url: 'Handle_Insert_Modify_Delete/insert_hot_resource.php',
            data: i_json,
            beforeSend: function(){
                // 换一下图标.
                $('#'+table_id).closest('div').find('button i').replaceWith('<img src="../img/wait.gif" width="18px">');
            }
        }).done(function(i_r){

            // 成功了再换回来
            if(i_r == '1'){
                $('#'+table_id).closest('div').find('button img').replaceWith('<i class="icon-ok"></i>');
            }else{
                $('#'+table_id).closest('div').find('button').html('修改出错');
                $('#'+table_id).closest('div').find('button').attr('class','btn btn-warning');
            }

        });
    }





}











    });
    </script>
</body>
</html>







<?php 

/*

电影/美剧/日韩剧/动漫/国产剧/游戏
公用的函数.

根据类型名 从数据库里面取数据.
因为是10个热门. 所以循环10次.
拿得到数据就输出[数据]. 拿不到数据就输出[空输入框]

*/


function output_ten_tr($type){

        $mysql_helper = new MySQLHelper();
        $sql_command = "select * from  hot_resource  where type='$type' order by sort;";

        $resource = $mysql_helper->excute_dql($sql_command);
            echo "<thead>";
            echo "<td>排序</td> <td>名称</td> <td>链接地址</td>";
            echo "</thead>";

            for($n=0; $n<10; $n++){
                if($row = mysql_fetch_assoc($resource)){
                    echo "<tr id=".$row['id']." type='modify' >";   // 注意这里的type
                        echo "<td> <input type='text' name='sort' class='input-mini' value=".$row['sort']."> </td> ";
                        echo "<td> <input type='text' name='name' class='input-medium' value=".$row['name']."> </td> ";
                        echo "<td> <input type='text' name='link' class='input-xlarge' value=".$row['link']."> </td> ";
                        echo "<td> <a href='#' class='clear'> 清空 </a> </td>";
                    echo "</tr>";                 
                }else{
                    echo "<tr type='insert'>";
                        echo "<td> <input type='text' name='sort' class='input-mini'> </td> ";
                        echo "<td> <input type='text' name='name' class='input-medium'> </td> ";
                        echo "<td> <input type='text' name='link' class='input-xlarge'> </td> ";
                    echo "</tr>";                
                }
                // tr的type是用于点击 "提交修改" 后用来判断的.
            }

        mysql_free_result($resource);
        $mysql_helper->close_connect();

}







?>