<?php 
class Blog_model extends CI_Model {


        public function __construct()
        {
                // Call the CI_Model constructor
                parent::__construct();
        }

        public function xx()
        {
                $query = $this->db->query('select * from demand');
                return $query->result();
        }



}

 ?>