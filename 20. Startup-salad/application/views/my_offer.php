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
        <h2>我的报价</h2>
      </div>
    </div><!-- /.container -->



<!-- <div class="bs-example" data-example-id="hoverable-table">
    <table class="table table-hover">
      <thead>
        <tr>
          <th>提交日期</th>
          <th>型号</th>
          <th>数量</th>
          <th>目标价</th>
          <th>状态</th>
        </tr>
      </thead>
      <tbody>

			<tr>
	          <th scope="row">我的报价1</th>
	          <td>123123123123</td>
	          <td>413413413</td>
	          <td>2312312312</td>
	          <td>暂时无人报价, 已有X人看过</td>
	        </tr>  



      </tbody>
    </table>
  </div>

 -->
	<style>
		.one_offer{
			
			width: 60%;
			margin: 0 auto;
			border-radius: 8px;
			color: white;
			margin-bottom: 90px;
		}
		.offer_title_ONE{
			text-align: center;
			font-size: 16px;
			height: 50px;
			line-height: 50px;
			background-color: #2ecc71;
			    border-top-left-radius: 12px;
			        border-top-right-radius: 12px;
		}
		.offer_title_TWO{
			display: flex;
			height: 40px;
			line-height: 40px;
			/*border-bottom: 1px solid black;*/
			/*border-left: 1px solid black;*/
			/*border-right: 1px solid black;*/
			background-color: #f96;
			/*color: black;*/
		}

		.need{
			/*background-color: #f99;*/
			/*display: inline-block;*/
			text-align: center;
			width: 50%;
			font-size: 20px;
			border-right: 1px solid #ebebeb;
			font-weight: bold;
		}

		.offer{
			/*background-color: #f96;*/

			/*display: inline-block;*/
			text-align: center;
			width: 50%;
			font-size: 20px;
			font-weight: bold;
		}
		.offer_title_THREE{
			display: flex;
						    border-bottom-left-radius: 12px;
			        border-bottom-right-radius: 12px;
		}
		.offer_title_THREE .left, .offer_title_THREE .right{
			width: 50%;
		}

		.offer_title_THREE .left{
			/*background-color: blue;*/
			text-align: center;
			border-right: 1px solid #ebebeb;
			background-color: #f96;
			/*color: black;*/

		}

		.offer_title_THREE .left div{
			margin-top: 16px;
			margin-bottom: 16px;

		}

		.offer_title_THREE .right{
			/*background-color: black;*/
			text-align: center;
			background-color: #f96;
			/*color: black;*/
		}

		.offer_title_THREE .right div{
			margin-top: 16px;
			margin-bottom: 16px;
		}
		.cancal_offer{
			width: 20%;
			background-color: #e74c3c;
			margin: 0 auto;
			text-align: center;
			height: 30px;
			line-height: 30px;
			/*border-radius: 6px;*/
			border-bottom-left-radius:  12px;
			border-bottom-right-radius:  12px;
		}
	</style>




	<?php foreach ($offer as $index => $one_offer): ?>\



	<div class='one_offer'>
		<div class='offer_title_ONE'>报价 <?php echo $index+1; ?></div>
		<div class='offer_title_TWO'>
			<div class='need'>需求</div>
			<div class='offer'>报价</div>
		</div>
		<div class='offer_title_THREE'>
			<div class='left'>
				<div>型号:  <?php echo $one_offer['demand_stuff'] ?></div>
				<div>数量:  <?php echo $one_offer['demand_number'] ?></div>
				<div>目标价:  <?php echo $one_offer['demand_price'] ?></div>
			</div>
			<div class='right'>
				<div>型号:  <?php echo $one_offer['demand_stuff'] ?></div>
				<div>数量:   <?php echo $one_offer['offer_number'] ?></div>
				<div>价格:   <?php echo $one_offer['offer_price'] ?></div>				
			</div>
		</div>
		<div class='cancal_offer'>取消报价</div>
	</div>


	<?php endforeach; ?>





<!-- 
<div class="bs-example" data-example-id="hoverable-table">
    <table class="table table-hover">
      <thead>
        <tr>
          <th> </th>
          <th> </th>
          <th>我的报价1</th>
          <th> </th>
          <th> </th>
        </tr>
      </thead>
      <tbody>
			<tr>
	          <th scope="row">需求</th>
	          <td>我的报价</td>
	        </tr>  



			<tr>
	          <th scope="row">我的报价1</th>
	          <td>123123123123</td>
	          <td>413413413</td>
	          <td>2312312312</td>
	          <td>暂时无人报价, 已有X人看过</td>
	        </tr>  



      </tbody>
    </table>
  </div>

 -->





















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
