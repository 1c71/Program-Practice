<?php

class front extends CI_Controller {

    function __construct() {
        parent::__construct();
    }
    
	// localhost/dianzi/front
	public function index()
	{

		if(isset($_SESSION['account_id'])){
			
		}
		// echo 'aasdasdadsd';

		// $this->load->model('xx_model');
		// $this->model->xxx('');

    	$meta = array(
    			'meta_title' => '采芯网',
    			'meta_description' => ''
    	);
    	$this->load->view ('common_head',$meta);
		// $this->load->view('index', $data);
		$this->load->view('index');

	}







}
