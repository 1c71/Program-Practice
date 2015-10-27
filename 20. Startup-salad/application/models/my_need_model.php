<?php
class my_need_model extends CI_Model {

        public function __construct()
        {
                // Call the CI_Model constructor
                parent::__construct();
        }

    function get(){
    	$sql = "SELECT * FROM demand ORDER BY time desc";

    	$r = $this->db->query($sql);
    	if($r){
    		return $r->result_array();
    	}else{
    		return false;
    	}

    }

}