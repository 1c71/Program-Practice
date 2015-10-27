<?php

class search extends CI_Controller {

    function __construct() {
        parent::__construct();
    }

	// localhost/dianzi/search
	public function index()
	{

		$name = $this->input->get('name');


		$this->load->model('search_model');
		$status = $this->search_model->search($name);
		echo json_encode($status);


	}







}
