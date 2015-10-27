<?php

class ajax extends CI_Controller {

    function __construct() {
        parent::__construct();
    }


	public function login()
	{

		$email = $this->input->get('email');
		$password = $this->input->get('password');

		$this->load->model('login_model');
		$status = $this->login_model->check_login($email, $password);

		if($status){
			echo '1';
		}else{
			echo '0';
		}

    		


	}







}
