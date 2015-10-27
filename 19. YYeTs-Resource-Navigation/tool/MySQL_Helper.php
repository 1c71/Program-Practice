<?php 
	/*
		这是一个mysql工具类，作用是完成对mysql的各种操作
	*/


	class MySQLHelper {

			public  $conn;				//连接名
			public  $host="localhost";  //主机名
			public  $dbname="yyets_resource";	//数据库名
			public  $username="root";	//数据库用户名
			public  $password="";		//数据库密码


			/* 实例化这个类的时候就连接数据库了 */
			public function __construct(){
				$this->conn=mysql_connect($this->host,$this->username,$this->password);
				if(!$this->conn){
					die("连接失败".mysql_error());		
				}
				mysql_select_db($this->dbname,$this->conn);
				mysql_query("set names utf8");
			}


			/* 数据查询语言 dql  负责查询操作. 也就是select相关操作的*/
			public function excute_dql($sql){
				$res = mysql_query($sql,$this->conn) or die(mysql_error());
				return $res;
			}

			/* 数据操纵语言 dml  负责 插入, 更新, 删除 相关操作 */
			public function excute_dml($sql){
					
				$b=mysql_query($sql,$this->conn) or die(mysql_error());
				if(!$b){
					return 0; //如果没有成功，就返回0;
				}else{

					// mysql_affected_rows 返回前一次 MySQL 操作所影响的记录行数。
					if(mysql_affected_rows($this->conn)>0){
				 		return 1;  //执行成功并且有行受到影响, 返回1
					}else{
				 		return 2;  //表示执行成功但是没有行受到影响, 返回2
				 	}

				}



			}


			/* 关闭链接 */
			public function close_connect(){
				if(!empty($this->conn)){ //如果这个连接还是有效的，那么我们可以关闭
					mysql_close($this->conn);
				}
			}




	}





 ?>