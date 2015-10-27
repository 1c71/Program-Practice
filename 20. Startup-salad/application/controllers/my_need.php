<?php

class my_need extends CI_Controller {

    function __construct() {
        parent::__construct();
    }
    
	// localhost/dianzi/my_need
	public function index()
	{

		// echo 'aasdasdadsd';

		$this->load->model('my_need_model');
		$r = $this->my_need_model->get();
		// var_dump($r);

		$data['need'] = $r;
		$this->load->view('my_need', $data);

	}







}
