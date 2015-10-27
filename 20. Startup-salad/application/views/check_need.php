<!DOCTYPE html>
<html lang="zh-CN">
  <head>
    <meta charset="utf-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <!-- 上述3个meta标签*必须*放在最前面，任何其他内容都*必须*跟随其后！ -->
    <meta name="description" content="">
    <meta name="author" content="">
    <!-- <link rel="icon" href="../../favicon.ico"> -->

    <title>搜索 -- 采芯网</title>

    <link href="common/css/bootstrap.min.css" rel="stylesheet">
	<link rel="stylesheet" href="common/css/font-awesome.min.css">
	<!-- <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/font-awesome/4.4.0/css/font-awesome.min.css"> -->

    <style>


body {
  padding-top: 50px;
}
.starter-template {
  padding: 30px 15px;
  text-align: center;
}



		#navbar{
			float: right;
		}
		#top{
			color: black !important;
			/*background-color: #3498db !important;*/
			border-color: #080808;
		}
		#middle{
			/*height:616px; */
			background-color:#f96;
		}
		#middle-text{
			    position: absolute;
    top: 50%;
    left: 50%;
    width: 210px;
    height: 46px;
    text-align: center;
    margin-left: -110px;
    margin-top: -23px;
		}
		#bottom{
			height:616px; 
			/*background-color:#f96;	*/
			display: -webkit-flex;
			display: flex;
		}
		#bottom-left{
			background-color: #f99;
			-webkit-flex: 1;
			flex: 1;

		}
		#bottom-right{
			background-color: #f96;
			-webkit-flex: 1;
          	flex: 1;
		}
		#line{
			height: 1px;
			background-color: #f99;
		}

		.top-text{
/* 			-webkit-align-items: center;
          align-items: center;
  			-webkit-justify-content: center;
          justify-content: center; */
          text-align: center;
          margin-top: 50px;
          font-size: 22px;
		}

		.round{
			height: 90px;
			width: 90px;
			background-color: #e74c3c;
			border-radius: 50%;
			margin-left: 43.5%;
			margin-top: 20px;
		}
		.top-name{
          text-align: center;
          margin-top: 20px;
          font-size: 19px;			
		}
		.about{
			margin-top: 40px;
			margin-left: 29%;
		}
		.about div{
			margin-top: 20px;
			font-size: 18px;
		}
    .search_result_table{
      margin-top: 30px;
    }

    /* 载入提示  */
    #hey_im_loading{
        margin-top: 80px;
    }



    #nothing{
        margin-top: 80px;
    }

    .time, .name, .number, .price, .status, .report_price{
          line-height: 51px !important; 
    }
    thead th{
      text-align: center;
    }
    tbody th, td{
      text-align: center;
    } 
    </style>
  </head>

  <body>

    <nav id='top' class="navbar navbar-inverse navbar-fixed-top">
      <div class="container">
        <div class="navbar-header">
          <button type="button" class="navbar-toggle collapsed" data-toggle="collapse" data-target="#navbar" aria-expanded="false" aria-controls="navbar">
            <span class="sr-only">Toggle navigation</span>
            <span class="icon-bar"></span>
            <span class="icon-bar"></span>
            <span class="icon-bar"></span>
          </button>
          <a class="navbar-brand" href="/dianzi/">采芯网</a>
        </div>
        <div id="navbar" class="collapse navbar-collapse">
          <ul class="nav navbar-nav">
            <li><a href="#">登陆</a></li>
            <!-- <li class="active"><a href="#">登陆</a></li> -->
            <li><a href="#about">注册</a></li>
          </ul>
        </div><!--/.nav-collapse -->
      </div>
    </nav>


    <div class="container">

      <div class="starter-template">
        <h2>搜索所有需求</h2>
      </div>

    </div><!-- /.container -->


    <!-- 搜索框 -->
    <div class="container" style='text-align:center; '>

      <div class="input-group" style="width: 500px; margin-left: 28%;">
        <input id='name' type="text" class="form-control" placeholder="元器件名">
        <span class="input-group-btn">
          <button id="search" class="btn btn-default" type="button">搜索</button>
        </span>
      </div><!-- /input-group -->


    </div><!-- /.container -->


  <!--  正在载入的提示 -->
  <div id='hey_im_loading'style='text-align:center; display:none;'>
    <i class="fa fa-spinner fa-spin fa-3x"></i>
  </div>

  <div id='nothing' style='text-align:center; display:none;'>
    <h3>没, 真没找着...</h3>
  </div>

<!--  结果表格  -->
<div class="search_result_table" data-example-id="hoverable-table" style='display:none;'>
    <table class="table table-hover">
      <thead>
        <tr>
          <th>型号</th>
          <th>数量</th>
          <th>目标价</th>
          <!-- <th>提交时间</th> -->
          <th>是否报价</th>
        </tr>
      </thead>
      <tbody>
	        <tr class='haha_one_row' style='display:none;'>
            <td class='name'>名字</td>
            <td class='number'>数量</td>
            <td class='price'>价格</td>

	          <!-- <td class='time'>时间</td> -->
            <td class='report_price'>
              <button type="button" class="btn btn-success" data-toggle="modal" data-target="#myModal">
                我要报价
              </button>
            </td>

	        </tr>  
      </tbody>
    </table>
  </div>






<!-- 提示框！！！！！！！！！！！！ -->
<div class="modal fade" id="myModal" tabindex="-1" role="dialog" aria-labelledby="myModalLabel">
  <div class="modal-dialog" role="document">
    <div class="modal-content">
      <div class="modal-header">
        <button type="button" class="close" data-dismiss="modal" aria-label="Close"><span aria-hidden="true">&times;</span></button>
        <h4 class="modal-title" id="myModalLabel">报价</h4>
      </div>
      <div class="modal-body">
        <div class="input-group">
		  
		  <input id="number" type="text" class="form-control" placeholder='数量'>
		  <input id="price" type="text" class="form-control" placeholder='价格(单价)'>
      <input id="goods_date" type="text" class="form-control" placeholder='货期(请填写年-月-日, 如 2015-10-18)'>
      <input id="note" type="text" class="form-control" placeholder='备注(可留空)'>
		</div>
	
      </div>
      <!-- <div class="modal-footer" style='text-align:center;'> -->
      <div class="modal-footer" style='text-align:left;'>
      <!-- <div class="modal-footer"> -->
        <!-- <button type="button" class="btn btn-default" data-dismiss="modal">Close</button> -->
        <button id="new_report_price" type="button" class="btn btn-success">报价</button>
      </div>
    </div>
  </div>
</div>






    <!-- Bootstrap core JavaScript
    ================================================== -->
    <!-- Placed at the end of the document so the pages load faster -->
    <script src="common/js/jquery-2.1.3.min.js"></script>
    <script src="common/js/bootstrap.min.js"></script>


	<script>
    var demand_id_for_ajax = null;
    // 那篇需求的 ID


    // "搜索" 的点击事件
		$('#search').click(function(){
			var name = $('#name').val();

      // var save = $(this).html();

      $('#nothing').hide();  // 隐藏没有结果的提示
      $('.search_result_table').hide(); // 隐藏表格
      $('#hey_im_loading').show();
      // 显示提交中按钮


			// ajax
			$.ajax({
				url:'search',
				data:{
					'name': name,
				},
        dataType : 'json',
        context : this
			}).done(function(r){
        console.log(r);


        $('#hey_im_loading').hide();


        if(jQuery.isEmptyObject(r)){

          $('#nothing').show();

        }else{
          var the_table =  $('.search_result_table'); // 拿到表格
          the_table.show(); // 显示表格


          // 清掉之前的结果
          the_table.find('.haha_one_row:visible').each(function(){
            $(this).remove();
          });

          [].forEach.call(r, function(one){

            var demand_id = one.id;
            var time = one.time;
            var name = one.name;
            var how_many = one.how_many;
            var price = one.price;

            var new_row = the_table.find('.haha_one_row').first().clone(); // 复制新行
            new_row.show(); // 显示新行
            new_row.attr('demand_id', demand_id);
            new_row.find('.time').text(time);
            new_row.find('.name').text(name);
            new_row.find('.number').text(how_many);
            new_row.find('.price').text(price);


            // 表格里的 "我要报价" 点击事件
            new_row.find('.report_price button').click(function(){
                demand_id_for_ajax = $(this).closest('tr').attr('demand_id');
                console.log(demand_id_for_ajax);




            });


            $('.search_result_table table tbody').append(new_row); // 加到表里            
          });

        }

			});


			// 根据结果响应
		});


    // 弹出框里的 "报价"的点击事件
    $('#new_report_price').click(function(){
      // var demand_id = $('#number').val();
      var number = $('#number').val();
      var price = $('#price').val();
      var goods_date = $('#goods_date').val();
      var note = $('#note').val();
      if(note == ''){
        console.log('备注是空');
      }
      // console.log(number);
      // console.log(price);
      // console.log(goods_date);
      // console.log(note);
      // return;


      var save = $(this).html();

      $(this).html('<i class="fa fa-spinner fa-spin"></i>');
      // 显示提交中按钮


      // ajax
      $.ajax({
        url:'report_price',
        data:{
          'demand_id': demand_id_for_ajax,
          'number': number,
          'price': price,
          'goods_date': goods_date,
          'note': note
        },
        context:this
      }).done(function(r){
          if(r == '1'){
            // 成功
            $(this).html(save);
          window.location = "./my_offer";
          }








      });



    });





	</script>











  </body>
</html>
