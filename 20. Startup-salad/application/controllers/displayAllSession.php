<?php	

// localhost/teamwork/test/displayAllSession
class displayAllSession extends CI_Controller{

	function index(){
		echo "<pre>";
		print_r($_SESSION);
		echo "</pre>";
	}
	
}

 