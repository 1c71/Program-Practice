<?php
class my_offer_model extends CI_Model {

        public function __construct()
        {
                // Call the CI_Model constructor
                parent::__construct();
        }

    function get(){
    	$sql = "SELECT 
        `demand`.`name` AS `demand_stuff`,
        `demand`.`how_many` AS `demand_number`,
        `demand`.`price` AS `demand_price`,

        `report_price`.`id` AS `offer_id`,
        `report_price`.`price` AS `offer_price`,
        `report_price`.`how_many` AS `offer_number`,
        `report_price`.`time` AS `offer_time`
        FROM 
        `report_price`
        LEFT JOIN `demand` 
        ON `demand`.`id` = `report_price`.`demand_id`
        ORDER BY `report_price`.offer_time desc";

    	$r = $this->db->query($sql);
    	if($r){
    		return $r->result_array();
    	}else{
    		return false;
    	}

    }

}