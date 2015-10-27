
    <style>
		#navbar{
			float: right;
		}
		body {
			padding-top: 50px;
		}
/*		.starter-template {
			padding: 40px 15px;
			text-align: center;
		}*/
		#top{
			color: black !important;
			/*background-color: #3498db !important;*/
			border-color: #080808;
		}
		#middle{
			height:616px; 
			/*background-color:#f96;*/
			background-size: cover;
			background-repeat: no-repeat;
			/*background-image: url('common/img/1.png');*/
			/*background-image: url('common/img/2.png');*/
			background-image: url('common/img/3.png');
			/*background-image: url('common/img/4.png');*/
			/*background-image: url('common/img/5.png');*/
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
    background-color: #f79238;
    border: none;
		}
		#bottom{
			height:616px; 
			/*background-color:#f96;	*/
			display: -webkit-flex;
			display: flex;
			font-family: "微软雅黑";
		}
		#bottom-left{
			/*background-color: #808080;*/
			/*background-color: #C2C2C2;*/

			-webkit-flex: 1;
			flex: 1;
			/*color:white;*/
			border-right: 10px solid #f99;

		}
		#bottom-left:hover{
	/*background-color: #808080;*/



		}
		#bottom-right{
			/*background-color: #00B0AE;*/
			-webkit-flex: 1;
          	flex: 1;
          	/*color:white;*/
		}
		#bottom-right:hover{
	/*background-color: #808080;*/


		}



		#line{
			height: 1px;
			background-color: #ffd3d3;
		}

		.top-text{
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
		#red-dot{
			width: 20px;
			font-size: 16px;
			display: inline-block;

			border-radius: 50%;
			background-color: #e74c3c;

			text-align: center;
			color: white;
			margin-left: 17px;
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
          <a class="navbar-brand" href="">采芯网 (电子器件采购平台)</a>
        </div>
        <div id="navbar" class="collapse navbar-collapse">
          <ul class="nav navbar-nav">
          	<!-- ===============================这里===================================== -->
          	<?php /*if(isset($_SESSION['name'])):*/ ?>
          	<?php if(false): ?>

				<li role="presentation" class="dropdown" style='background-color:#2980b9; '>
				<a id="drop6" href="" class="dropdown-toggle" data-toggle="dropdown" role="button" 
				aria-haspopup="true" aria-expanded="false" style='color:white;'>
	            	<?php
	            		if($_SESSION['account_type'] == '1'){
	            			echo '(需求方) ';
	            		}else{
	            			echo '(供给方) ';
	            		}
	            		echo $_SESSION['name']; 
	            	?>
				<span class="caret"></span>
				</a>
					<ul id="menu3" class="dropdown-menu" aria-labelledby="drop6">

					<li role="separator" class="divider"></li>
					<li><a href="./logout">退出登陆</a></li>
					</ul>
				</li>

				<li style='background-color:#3498db; '>
					<a href="" style='color:white;'>我的需求<div id='red-dot'>3</div></a>
				</li>



			<?php else: ?>
	            <li><a href="./login">登陆</a></li>
	            <!-- <li class="active"><a href="#">登陆</a></li> -->
	            <li><a href="">注册</a></li>
          	<?php endif; ?>
          </ul>
        </div><!--/.nav-collapse -->
      </div>
    </nav>


	<!-- 中间 -->
	<div id='middle' style=''>
	<!-- <div id='middle-text'>采芯网</div> -->
	
<!-- Button trigger modal -->
<button type="button" id='middle-text' class="btn btn-success btn-lg" data-toggle="modal" data-target="#myModal">
  发布元器件需求
</button>
	</div>

<!-- <div id="line"></div> -->



<!--     <div class="container">

      <div class="starter-template">
        <h2>采芯网是一个电子元器件采购平台，使用方法如下</h2>
        <p class="lead">Use this document as a way to quickly start any new project.<br> All you get is this text and a mostly barebones HTML document.</p>
      </div>

    </div>

 -->



	<!-- 下面 -->
	<div id='bottom' style=''>
		<div id="bottom-left">
			<div class='top-text'>(需求方)</div>
			<!-- <div class='round'></div> -->
			<!-- <img class="round" src="data:image/gif;base64,R0lGODlhAQABAIAAAHd3dwAAACH5BAAAAAAALAAAAAABAAEAAAICRAEAOw==" alt="Generic placeholder image" width="140" height="140"> -->
			<div class='top-name'>工厂 / 企业</div>
			<div class='about'>
				<div>1. 提出电子元器件的需求</div>
				<div>2. 业内人员会查看您的需求, 帮助你寻找资源</div>
				<div>3. 业内人员找到资源后给您报价</div>
				<div>4. 质量/价格满意, 达成交易!</div>
				<div>5. 平台会为你提供诸多保障</div>
			</div>
		</div>
		<div id="bottom-right">
			<div class='top-text'>(提供方)</div>
			<!-- <img class="round" src="data:image/gif;base64,R0lGODlhAQABAIAAAHd3dwAAACH5BAAAAAAALAAAAAABAAEAAAICRAEAOw==" alt="Generic placeholder image" width="140" height="140"> -->
			
			<div class='top-name'>业内人员</div>
			<div class='about'>
				<div>1. 查看别人的采购需求, 找到相应物料</div>
				<div>2. 在平台报价</div>
				<div>3. 客户满意, 达成交易!</div>
				<!-- <div>4. xxxxxx</div> -->
			</div>	
		</div>
	</div>


	<!-- ===================---------------------------========================== -->
<!-- 	<div id='bottom' style=''>
	<div id="bottom-left">
		<div class='top-text'>(需求方)</div>
		<div class='round'></div>
		<img class="round" src="data:image/gif;base64,R0lGODlhAQABAIAAAHd3dwAAACH5BAAAAAAALAAAAAABAAEAAAICRAEAOw==" alt="Generic placeholder image" width="140" height="140">
		<div class='top-name'>工厂 / 企业</div>
		<div class='about'>
			<div>1. 提出电子元器件的需求</div>
			<div>2. 业内人员会查看您的需求, 帮助你寻找资源</div>
			<div>3. 业内人员找到资源后给您报价</div>
			<div>4. 质量/价格满意, 达成交易!</div>
			<div>5. 平台会为你提供诸多保障</div>
		</div>
	</div>
	<div id="bottom-right">
		<div class='top-text'>(提供方)</div>
		<img class="round" src="data:image/gif;base64,R0lGODlhAQABAIAAAHd3dwAAACH5BAAAAAAALAAAAAABAAEAAAICRAEAOw==" alt="Generic placeholder image" width="140" height="140">
		
		<div class='top-name'>业内人员</div>
		<div class='about'>
			<div>1. 查看别人的采购需求, 找到相应物料</div>
			<div>2. 在平台报价</div>
			<div>3. 客户满意, 达成交易!</div>
			<div>4. xxxxxx</div>
		</div>	
	</div>
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


			var save = $(this).html();

			$(this).html('<i class="fa fa-spinner fa-spin"></i>');
			// 显示提交中按钮


			// ajax
			$.ajax({
				url:'submit',
				data:{
					'name': name,
					'number': number,
					'price': price
				},
				context:this
			}).done(function(r){
				if(r == '1'){
					// 成功
					$(this).html(save);
					window.location = "./my_need";
				}
			});


			// 根据结果响应
		});










	</script>











  </body>
</html>
