<?php
    // 有了这个文件MySQL操作会方便许多.
    require_once('tool/MySQL_Helper.php');


    // 定义静态首页的文件名
    $Homepage_filename = 'index.html';


    // 如果拿不到 refresh_cache, 我们就会进入if分支.
    // 以达到访问静态文件的效果.
    if(!isset($_GET['refresh_cache'])){

        // 如果文件存在就输出该文件并退出脚本. 不继续往下执行了.
        if(file_exists($Homepage_filename)){
            echo file_get_contents($Homepage_filename);
            exit;
        }

    }
    // 如果从 get 中拿到了 refresh_cache  我们就不会进入if分支.
    // 会接着往下执行   ob_start()  html   ob_get_contents()    file_put_contents()
    // 其实就达到了[刷新缓存]的效果.




    // 打开缓冲区.
    ob_start();

?>
<!DOCTYPE html>
<html>
<head>
    <meta http-equiv="X-UA-Compatible" content="IE=edge,chrome=1" />
    <meta http-equiv="content-type" content="html/text; charset=utf-8;" />
    <title>资源导航站 -- 人人影视</title>

    <link href="css/reset.css" rel="stylesheet">
    <link href="css/index.css" rel="stylesheet">
    <link href="css/bootstrap.min.css" rel="stylesheet">
    <link href="css/bootstrap-responsive.min.css" rel="stylesheet">

    <base target="_blank" />    <!-- 全是新标签页打开. -->


    <link rel="icon" href="favicon.ico" />

    <!-- Le HTML5 shim, for IE6-8 support of HTML5 elements -->
    <!--[if lt IE 9]>
      <script src="http://html5shim.googlecode.com/svn/trunk/html5.js"></script>
    <![endif]-->

</head>
<body>




<!-- =========最顶部的蓝色导航条 "设本页为主站"等等========= -->
<div id="Top_nav">
    
    <ul id="Top_left">
        
        <li id="big">
            <a id="Homepage" title="设为首页" href="javascript:" style="color: white;" >
                设本站为主页
            </a> 
        </li>
        
        <li>
            <a id="Favorite" title="收藏"  href="javascript:" style="color: white;">
                收藏本站
            </a> 
        </li>
        
        <li>
            <a href="javascript:void(0)" onclick="ToSN();" target="_blank" title="分享到新浪微博">
                分享到新浪微博
            </a>
            <script type="text/javascript">
                function ToSN(){
                    var sina = "http://service.weibo.com/share/share.php?url=http://www.baidu.com&title=人人影视旗下有资源导航站了~~&language=zh_cn ";
                    window.open(sina,'',"width=615, height=505, top=0, left=0, toolbar=no, menubar=no, scrollbars=no, location=yes, resizable=no, status=no");
                }
            </script>
        </li>
        
        <li> 
            <a href="javascript:void(0)" onclick="ToTX();"target="_blank" title="分享到腾讯微博">
                分享到腾讯微博
            </a>
            <script type="text/javascript">
                function ToTX(){
                    var _t = encodeURI(document.title);
                    var _url = encodeURIComponent(document.location);
                    var _pic = encodeURI('');//
                    var _site = '';//你的网站地址，可以留空
                    var _u = 'http://v.t.qq.com/share/share.php?url='+_url+'&appkey=&site='+_site+'&pic='+_pic+'&title='+_t;
                    window.open( _u,'','width=700, height=680, top=0, left=0, toolbar=no, menubar=no, scrollbars=no, location=yes, resizable=no, status=no' );
                }
            </script>
        </li>
    </ul>



    <ul id="Top_right">
        <li> <a href="#">论坛</a> </li>
        <li> <a href="#">意见反馈版</a> </li>
        <li> <a href="#">各站邀请码互助</a> </li>
        <li> <a href="#">推荐好站给我们</a> </li>
    </ul>
    
</div>
<!-- =========最顶部的蓝色导航条 结束========= -->





<!-- =================== 头部 开始 ======================= -->
<header class="container">
    <div class="row">

        <!-- LOGO -->
        <div class="span4" id="Logo">
            <img src="img/LOGO.png" onclick="javascript:void(0)">
        </div>

        <!-- 搜索框 -->
        <div class="span7" id="Search">
            <div id="baohan">   <!-- 有个div包着比较好定位 -->
                <ul id="Search_list">
                    <li>百度</li>
                    <li>谷歌</li>
                    <li>必应</li>
                    <li>人人影视</li>
                    <li>射手字幕</li>
                    <li>宇宙点播</li>
                    <li>优酷</li>
                </ul>
                <div id="text_and_button">
                    <input id="Search_text" type='text'>
                    <div id="Search_botton">搜索</div>
                </div>
            </div>
        </div><!-- id="Search" 结束 -->

    </div>
</header>
<!-- =================== 头部 结束 ======================= -->







<!-- ============ 主要内容-开始  "热门资源搜索","好站推荐"=============== -->

<div class="container">
    <div class="row">

        <div class="span8">


            <!-- "热门资源搜索" -->
            <div id="hot_resource" class="box">
                <div class="title">热门资源搜索</div>

                <ul class="ht_ul">
                    <li class="head_li">电影</li>
                    <?php  how_resource_data('movie'); ?>
                </ul>


                <ul class="ht_ul">
                    <li class="head_li">美剧</li>
                    <?php  how_resource_data('am_tv'); ?>
                </ul>

                <ul class="ht_ul">
                    <li class="head_li">日韩剧</li>
                    <?php  how_resource_data('jk_tv'); ?>
                </ul>

                <ul class="ht_ul">
                    <li class="head_li">动漫</li>
                    <?php  how_resource_data('ct');  ?>
                </ul>

                <ul class="ht_ul">
                    <li class="head_li">国产剧</li>
                    <?php  how_resource_data('china'); ?>
                </ul>

                <ul class="ht_ul">
                    <li class="head_li">游戏</li>
                    <?php  how_resource_data('game');  ?>
                </ul>


            </div>




            <!-- "好站推荐" -->
            <div class="title">好站推荐</div>   
                <!-- 这个是标题, 因为要设置内边距, 所以没办法只能移出来 -->
            <div id="good_website" class="box">

                <!-- 资源下载 -->
                <?php good_website_data('download'); ?>
                <br>

                <!-- 点播站 -->
                <?php good_website_data('online'); ?>
                <br>

                <!-- 视频站 -->
                <?php good_website_data('video'); ?>
                <br>

                <!-- pt -->
                <?php good_website_data('pt'); ?>
                <br>


                <!-- 其他相关 -->
                <?php good_website_data('other'); ?>
                <br>

                <!-- 美图美女站 -->
                <?php good_website_data('girl'); ?>
                <br>
        </div>
        <!-- "好站推荐"-结束 -->
        </div><!-- span8 结束 -->





            <div class="span4">

                <!-- "知识讲解" -->
                <div id="Knowledge" class="box">
                    <div class="title">知识讲解</div>
                    <ul>
                        <?php knowledge_share_data(); ?>
                    </ul>
                </div>




                <!-- "实用工具" 开始 -->
                <div class="title"> 
                    实用工具    <!-- 这就是那个标题. -->
                </div> 

                <div id="Tool" class="box">
                    <ul style="margin:0;">






                        <?php useful_tool_data(); ?>





                    </ul>

                </div>  <!-- id="Tool" 结束 -->
                <!-- "实用工具" 结束 -->

            </div>  <!-- span4结束 -->
    </div>
</div>  
<!-- ============= 主要内容-结束 =============== -->



























<!-- =================== 页尾 开始 ======================= -->
<footer>
    资源导航网址大全 zydh123.com
    <br>
    欢迎大家把优秀的资源分享网站地址告诉我们更新到本站导航去, 这里为你搜集优秀的资源分享网站
</footer>
<!-- =================== 页尾 结束 ======================= -->








<!-- 
    无法通过javascript或jQuery在新标签页直接打开一个网站.
    所以当点击搜索按钮的时: 
    1. 动态构造url(根据你选择的搜索引擎).
    2. 用 jQuery 修改这个a标签的href.
    3. 用 jQuery 来模拟点击这个a标签..就能达到新标签页面打开的效果.
-->
<a id="newtab1" href="http://www.baidu.com" target="_black" style="display:none;">
    asdasdasdasd
</a>








<!-- =================== 载入必要的脚本 ======================= -->


<script src="js/jquery-1.9.1.min.js"></script>
<!-- 你猜 -->

<script src="js/bootstrap.min.js"></script> 
<!-- bootstrap -->

<script src="js/set_homepage_fav_page.js"></script> 
<!-- 设为首页和收藏本页的函数 -->

<script src="js/jquery.browser.min.js"></script>  
<!--  
    这个jQuery插件用来判断浏览器和浏览器版本的. 
    http://jquery.thewikies.com/browser/          
-->





<!-- ============================================================================== -->

<script type="text/javascript">

jQuery.noConflict();

(function($){


    // 【设本站为首页】
    $('#Homepage').click(function(){

        // chrome 没法收藏也没法设主页. 我们特殊对待一下chrome~
        if($.browser.name == "chrome"){
            var homgpageurl = "http://support.google.com/chrome/bin/answer.py?hl=cn&hlrm=en&answer=95314";
            $('#Homepage').attr('href', homgpageurl);
            $('#Homepage')[0].click();
        }
        else{
            SetHomepage('http://www.zydh123.com/');
            // 这个函数在 set_homepage_fav_page.js 里           
        }
    });



    // 【收藏本站】
    $('#Favorite').click(function(){

        if($.browser.name == "chrome"){
            alert('谷歌浏览器请按 CTRL+D 来添加书签')
        }
        else{
            AddFavorite('http://www.zydh123.com/','资源导航站 -- 人人影视'); 
            // 这个函数也是在 set_homepage_fav_page.js           
        }

    });


    

    /* 默认是第一个, 也就是百度. 默认被选中.*/
    $('#Search_list li:first').addClass('Search_list_active');



    /* 这段代码负责 搜索引擎选择后的背景高亮 */
    $('#Search_list li').click(function(){
        $('#Search_list li').removeClass('Search_list_active');
        $(this).addClass('Search_list_active');

    });


    /* 这段负责 鼠标划过时候的高光效果 */
    $('#Search_list li').hover(
        function(){
            $(this).addClass('Search_list_hover');
        },
        function(){
            $(this).removeClass('Search_list_hover');
        }
    );






    /*    这段负责 "搜索按钮"按下后发生的事情. -- 1. 根据选择的搜索引擎构造url  2. 跳转         */
    $('#Search_botton').click(function(){

        var s_val = $('#Search_text').val();    /* 拿到输入框里的值 */


        if (s_val != ''){   /*不为空的话才搜索.*/
            $('#Search_list li').each(function(index){
                if ($(this).hasClass('Search_list_active')){
                    var engine_name = $(this).text();
                    //alert(engine_name);

                    var jump_url = 0;

                    switch(engine_name)
                    {
                        case "百度":
                            jump_url = "http://www.baidu.com/s?wd="+s_val;
                        break;
                        
                        case "谷歌":
                            jump_url = "http://www.google.com.tw/search?hl=zh-CN&q="+s_val;
                        break;
                        
                        case "必应":
                            jump_url = "http://www.bing.com/search?q="+s_val;
                        break;

                        case "人人影视":
                            jump_url = "http://www.yyets.com/php/search/index?keyword="+s_val;
                        break;

                        case "射手字幕":
                            jump_url = "http://www.shooter.cn/search/"+s_val;
                        break;

                        case "宇宙点播":
                            jump_url = "http://abcze.com/?s="+s_val;
                        break;

                        case "优酷":
                            jump_url = "http://www.soku.com/search_video/q_"+s_val;
                        break;
                        
                        default:
                        //n 与 case 1 和 case 2 不同时执行的代码
                    }

                    if(jump_url!=0){
                        $('#newtab1').attr('href', jump_url);
                        $('#newtab1')[0].click();        
                    }


                }
            });
        }

    });



    /* 负责 "搜索按钮"按下后的渐变变化 */
    $('#Search_botton').mousedown(function(){
        $('#Search_botton')
        .css("background-image","-webkit-linear-gradient(top, #cfcfcf, #f1f1f1)")
        .css("background-image","-moz-linear-gradient(top, #cfcfcf, #f1f1f1)")
        .css("background-image","linear-gradient(top, #cfcfcf, #f1f1f1)");
    });

    /* 负责 "搜索按钮"松开后的渐变颜色恢复 */
    $('#Search_botton').mouseup(function(){
        $('#Search_botton')
        .css("background-image","-webkit-linear-gradient(top, #f1f1f1, #cfcfcf)")
        .css("background-image","-moz-linear-gradient(top, #f1f1f1, #cfcfcf)")
        .css("background-image","linear-gradient(top, #f1f1f1, #cfcfcf)");
    });





})(jQuery);
// ---- jQuery 代码结束 ---- 


</script>



</body>
</html>

<?php //\__________________________________________________________________________/  ?>


<?php 
    // ====== 静态化 ====== 

    $html_content = ob_get_contents(); 

    file_put_contents($Homepage_filename, $html_content);
    // file_put_contents在文件不存在的时候就会创建, 文件存在的时候就会覆盖. 除非写上参数声明是追加.
    
?>









<?php

// 后面没有啥实际输出的内容了.. 都是php函数


/* =============== 热门资源搜索 ==============  */
    function how_resource_data($type){

 
        $mysql_helper = new MySQLHelper();
        $sql = "select * from hot_resource where type='$type' order by sort;";
        $ht = $mysql_helper->excute_dql($sql);

        while($row = mysql_fetch_assoc($ht)){
            echo '<li class="normal"> <a href="'.$row["link"].'">'.$row["name"].'</a> </li>';
        }


        mysql_free_result($ht);
        $mysql_helper->close_connect();     
    }







/* ===================== 好站推荐 ===================== */

    function good_website_data($type){

        switch ($type)
        {
        case 'download':
            $link_class = 'Link Blue_t';
            $desc_class = 'Description Blue_d';
            break;  
        case 'online':
            $link_class = 'Link Red_t';
            $desc_class = 'Description Red_d';
            break; 
        case 'video':
            $link_class = 'Link Green_t';
            $desc_class = 'Description Green_d';
            break; 
        case 'pt':
            $link_class = 'Link Yellow_t';
            $desc_class = 'Description Yellow_d';
            break; 
        case 'other':
            $link_class = 'Link DarkBlue_t';
            $desc_class = 'Description DarkBlue_d';
            break; 
        case 'girl':
            $link_class = 'Link DarkYellow_t';
            $desc_class = 'Description DarkYellow_d';
            break; 
        default:
            echo "error in function good_website_data.";
            return;
        }



        $mysql_helper = new MySQLHelper();
        $sql = "select * from good_website where type='$type' order by sort;";
        $resource_download = $mysql_helper->excute_dql($sql);

            while($row = mysql_fetch_assoc($resource_download)){
                echo "<div class='item'>";
                    echo "<div class='$link_class'> <a href=".$row["link"].">{$row["name"]}</a> </div>";
                    echo "<div class='$desc_class'>{$row['intro']}</div>";
                echo "</div>";
            }

        //释放资源和关闭连接
        mysql_free_result($resource_download);
        $mysql_helper->close_connect();
    }







/*  ======================== 知识讲解 ====================  */


    function knowledge_share_data(){

        $mysql_helper = new MySQLHelper();
        $sql = "select * from knowledge_share order by sort";
        $know = $mysql_helper->excute_dql($sql);

        while($row = mysql_fetch_assoc($know)){
            echo "<li> <a href='{$row['link']}'> {$row['title']} </a></li>";
        }

        mysql_free_result($know);
        $mysql_helper->close_connect();

    }





/*  ======================== 实用工具 ====================  */


    function useful_tool_data(){

        $mysql_helper = new MySQLHelper();
        $sql = "select * from useful_tool order by sort";
        $tool = $mysql_helper->excute_dql($sql);

            while($row = mysql_fetch_assoc($tool)){
                echo "<li>";

                    echo '<div class="left_item">';
                        echo '<img src="'.$row['imglink'].'" width="30px" height="30px">';
                    echo '</div>';
                            
                    echo "<div class='right_item'>";
                        echo "<div class='right_item_up'>";
                            echo "<a href={$row['link']}>{$row['name']}</a>";
                        echo "</div>";
                        echo "<div class='right_item_down'>";
                            echo $row['intro'];
                        echo "</div>";
                    echo "</div>";

                echo "</li>";
            }


        mysql_free_result($tool);
        $mysql_helper->close_connect();
    }



?>