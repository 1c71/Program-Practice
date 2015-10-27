<?php

class submit extends CI_Controller {

    function __construct() {
        parent::__construct();
    }

	// localhost/dianzi/submit
	public function index()
	{

		$name = $this->input->get('name');
		$number = $this->input->get('number');
		$price = $this->input->get('price');

		$this->load->model('new_demand_model');
		$status = $this->new_demand_model->new_demand($name, $number, $price);
		if($status){
			echo '1';
		}else{
			echo '0';
		}

	}







}
