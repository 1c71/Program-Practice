<?php

class login_model extends CI_Model {

    function __construct() {
        parent::__construct();
    }

    function check_login($email, $password){

    	$data = array(
    		'email' => $email,
    		'password' => $password
    	);
    	$this->db->where($data); 
    	$query = $this->db->get('account');
    	if($query->num_rows() > 0){

    		$result = $query->result();
    		// var_dump($result);

			$_SESSION['name'] = $result[0]->name;
			$_SESSION['email'] = $result[0]->email;
			$_SESSION['account_type'] = $result[0]->account_type;
			$_SESSION['accound_id'] = $result[0]->accound_id;

    		return true;
    
    	}else{
    		return false;
    	}

    }

}