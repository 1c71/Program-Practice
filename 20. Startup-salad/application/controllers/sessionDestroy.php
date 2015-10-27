<?php	


class sessionDestroy extends CI_Controller{

	function index(){
		session_destroy();
		echo "session destroy done";
	}
	
}

 