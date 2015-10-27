<?php

class search_need extends CI_Controller {

    function __construct() {
        parent::__construct();
    }
    
	// localhost/dianzi/check_need
	public function index()
	{

		// echo 'aasdasdadsd';

		$this->load->model('check_need_model');
		$r = $this->check_need_model->get();
		// // var_dump($r);

		$data['need'] = $r;
		$this->load->view('check_need', $data);

	}







}
