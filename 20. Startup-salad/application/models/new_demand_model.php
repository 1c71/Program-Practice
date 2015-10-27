<?php
class new_demand_model extends CI_Model {

        public function __construct()
        {
                // Call the CI_Model constructor
                parent::__construct();
        }

    function new_demand($name, $number, $price){
    	$sql = "INSERT INTO demand(name, how_many, price) VALUES('$name', '$number', '$price')";

    	$r = $this->db->query($sql);
    	if($r){
    		return true;
    	}else{
    		return false;
    	}

    }

}