<!DOCTYPE html>
<html lang="zh-CN">
  <head>
    <meta charset="utf-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <meta name="description" content="">


    <title>我的需求 -- 采芯网</title>

    <link href="common/css/bootstrap.min.css" rel="stylesheet">
	<link rel="stylesheet" href="common/css/font-awesome.min.css">

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
        <h2>我的需求</h2>
        <!-- <p class="lead">Use this document as a way to quickly start any new project.<br> All you get is this text and a mostly barebones HTML document.</p> -->
      </div>

    </div><!-- /.container -->






<div class="bs-example" data-example-id="hoverable-table">
    <table class="table table-hover">
      <thead>
        <tr>
          <th>型号</th>
          <th>数量</th>
          <th>目标价</th>
          <th>状态</th>
          <!-- <th>需求提交日期</th> -->
        </tr>
      </thead>
      <tbody>
      	<?php foreach ($need as $key => $value): ?>
	        <tr>
	          
	          <td style='color:blue;'><?php echo $value['name']; ?></td>
	          <td><?php echo $value['how_many']; ?></td>
	          <td><?php echo $value['price']; ?></td>
	          <td>暂时无人报价</td>
	          <!-- <td><?php echo $value['time']; ?></td> -->
	        </tr>  
      	<?php endforeach; ?>

      </tbody>
    </table>
  </div>






























<!-- Modal -->
<div class="modal fade" id="myModal" tabindex="-1" role="dialog" aria-labelledby="myModalLabel">
  <div class="modal-dialog" role="document">
    <div class="modal-content">
      <div class="modal-header">
        <button type="button" class="close" data-dismiss="modal" aria-label="Close"><span aria-hidden="true">&times;</span></button>
        <h4 class="modal-title" id="myModalLabel">发布元器件需求</h4>
      </div>
      <div class="modal-body">
        <div class="input-group">
		  <input id="name" type="text" class="form-control" placeholder='元器件名'>
		  <input id="number" type="text" class="form-control" placeholder='数量'>
		  <input id="price" type="text" class="form-control" placeholder='目标价格'>
		</div>
	
      </div>
      <!-- <div class="modal-footer" style='text-align:center;'> -->
      <div class="modal-footer" style='text-align:left;'>
      <!-- <div class="modal-footer"> -->
        <!-- <button type="button" class="btn btn-default" data-dismiss="modal">Close</button> -->
        <button id="new_demand" type="button" class="btn btn-primary">发布</button>
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
		$('#new_demand').click(function(){
			var name = $('#name').val();
			var number = $('#number').val();
			var price = $('#price').val();
			console.log(name);
			console.log(number);
			console.log(price);




			$(this).html('<i class="fa fa-spinner fa-spin"></i>');
			// 显示提交中按钮


			// ajax
			$.ajax({
				url:'submit',
				data:{
					'name': name,
					'number': number,
					'price': price
				}
			}).done(function(r){
				if(r == '1'){
					// 成功

					console.log('asdasdsd');
				}
			});


			// 根据结果响应
		});










	</script>











  </body>
</html>
