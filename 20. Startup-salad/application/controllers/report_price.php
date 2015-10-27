<?php

class report_price extends CI_Controller {

    function __construct() {
        parent::__construct();
    }

	// localhost/dianzi/report_price
	public function index()
	{

		$demand_id = $this->input->get('demand_id'); // 数量
		$number = $this->input->get('number'); // 数量
		$price = $this->input->get('price'); // 价格
		$goods_date = $this->input->get('goods_date'); //货期
		$note = $this->input->get('note'); // 备注
		// var_dump($demand_id);
		// var_dump($number);
		// var_dump($price);
		// var_dump($goods_date);
		// var_dump($note);

		$this->load->model('report_price_model');
		$status = $this->report_price_model->report_price($demand_id, $number, $price, $goods_date, $note);
		// 返回成功或失败

		if($status){
			echo '1';
		}else{
			echo '0';
		}


	}







}
