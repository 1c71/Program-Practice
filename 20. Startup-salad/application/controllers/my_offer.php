<?php

class my_offer extends CI_Controller {

    function __construct() {
        parent::__construct();
    }

	// localhost/dianzi/my_offer
	public function index()
	{	
		// echo 'my offer';



		$this->load->model('my_offer_model');
		$r = $this->my_offer_model->get();
		// var_dump($r);

		$data['offer'] = $r;

    	$meta = array(
    			'meta_title' => '我的报价 -- 采芯网',
    			'meta_description' => ''
    	);
    	$this->load->view ('common_head',$meta);
		$this->load->view('my_offer', $data);


	}







}
