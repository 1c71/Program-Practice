<?php
class search_model extends CI_Model {

    public function __construct()
    {
            parent::__construct();
    }

    function search($name)
    {
    	$sql = "SELECT * FROM demand where name LIKE '%$name%' order by time desc";

    	$r = $this->db->query($sql);
    	if($r){
    		return $r->result_array();
    	}else{
    		return false;
    	}

    }

}