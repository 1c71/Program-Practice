<?php
class report_price_model extends CI_Model {

    public function __construct()
    {
            parent::__construct();
    }

    // 报价
    function report_price($demand_id, $number, $price, $goods_date, $note)
    {

    	$sql = "INSERT INTO report_price 
                (demand_id, how_many, price, time, note) 
                VALUES('$demand_id', '$number', '$price', '$goods_date', '$note')";


    	$r = $this->db->query($sql);
        if($r){
            return true;
        }else{
            return false;
        }

    }

}