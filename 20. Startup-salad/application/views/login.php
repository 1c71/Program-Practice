<?php 
  $this->load->view('common_head'); 
?>
    <style>
body {
  padding-top: 40px;
  padding-bottom: 40px;
  background-color: #eee;
}

.form-signin {
  max-width: 330px;
  padding: 15px;
  margin: 0 auto;
}
.form-signin .form-signin-heading,
.form-signin .checkbox {
  margin-bottom: 10px;
}
.form-signin .checkbox {
  font-weight: normal;
}
.form-signin .form-control {
  position: relative;
  height: auto;
  -webkit-box-sizing: border-box;
     -moz-box-sizing: border-box;
          box-sizing: border-box;
  padding: 10px;
  font-size: 16px;
}
.form-signin .form-control:focus {
  z-index: 2;
}
.form-signin input[type="email"] {
  margin-bottom: -1px;
  border-bottom-right-radius: 0;
  border-bottom-left-radius: 0;
}
.form-signin input[type="password"] {
  margin-bottom: 10px;
  border-top-left-radius: 0;
  border-top-right-radius: 0;
}
    </style>


  </head>

  <body>

    <div class="container">

      <form class="form-signin">
        <h2 class="form-signin-heading">欢迎登陆采芯网</h2>
        <label for="inputEmail" class="sr-only">邮件地址</label>
        <input type="text" id="inputEmail" class="form-control" placeholder="您的邮件地址" required autofocus>
        <label for="inputPassword" class="sr-only">密码</label>
        <input type="password" id="inputPassword" class="form-control" placeholder="密码" required>
        <div class="checkbox">
          <label>
            <input type="checkbox" value="remember-me"> 记住我
          </label>
        </div>
        <button id='login_haha'class="btn btn-lg btn-primary btn-block" type="">登陆</button>
      </form>

    </div> <!-- /container -->

  </body>
      <!-- Placed at the end of the document so the pages load faster -->
    <script src="common/js/jquery-2.1.3.min.js"></script>
    <script src="common/js/bootstrap.min.js"></script>
  <script>

  $('#login_haha').click(function(){
      var email = $('#inputEmail').val();
      var password = $('#inputPassword').val();

      console.log(email);
      console.log(password);


      var save = $(this).html();

      $(this).html('<i class="fa fa-spinner fa-spin fa-2x"></i>');
      // 显示提交中按钮


      // ajax
      $.ajax({
        url:'ajax/login',
        data:{
          'email': email,
          'password': password
        },
        context:this
      }).done(function(r){
          $(this).html(save);

        if(r == '1'){
          // 成功
          $(this).html(save);
          window.location = "http://localhost/dianzi/";
          // 跳回首页

          // TODO , 登陆成功!!
        }
      });


      return false;
  });
  </script>



</html>
