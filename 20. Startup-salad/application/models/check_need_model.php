<?php
class check_need_model extends CI_Model {

    public function __construct()
    {
            parent::__construct();
    }

    function get()
    {
    	$sql = "SELECT * FROM demand";

    	$r = $this->db->query($sql);
    	if($r){
    		return $r->result_array();
    	}else{
    		return false;
    	}

    }

}