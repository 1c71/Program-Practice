


CREATE DATABASE `salad-idea` DEFAULT CHARSET='UTF8'


-- 模板
CREATE TABLE XX(
	id int unsigned auto_increment,
	xxx varchar(100),
	primary key(id)
)DEFAULT CHARSET='UTF8';



CREATE TABLE demand(
	id int unsigned auto_increment,
	name TEXT,
	how_many int unsigned COMMENT '数量',
	price float COMMENT '价格',
	time timestamp DEFAULT now() COMMENT '时间',
	note varchar(500) COMMENT '备注',
	primary key(id)
)DEFAULT CHARSET='UTF8';



CREATE TABLE report_price(
	id int unsigned auto_increment,
	demand_id int unsigned,
	how_many int unsigned COMMENT '数量',
	price float COMMENT '价格',
	time timestamp DEFAULT now() COMMENT '货期',
	offer_time timestamp DEFAULT now() COMMENT '提交这个报价的时间',
	note TEXT COMMENT '备注',
	primary key(id)
)DEFAULT CHARSET='UTF8';


CREATE TABLE account(
	accound_id int unsigned auto_increment,
	name varchar(200),
	email varchar(200),
	password  varchar(100),
	createTime timestamp DEFAULT now() COMMENT '注册时间',
	account_type tinyint unsigned COMMENT '0:需求方, 1:供给方',
	primary key(accound_id)
)DEFAULT CHARSET='UTF8';


-- 需求方
INSERT INTO account(name, email, password, account_type) VALUES('羊化腾', '1@haha.com', 'admin', 0);

-- 供给方
INSERT INTO account(name, email, password, account_type) VALUES('西瓜化腾', '2@haha.com', 'admin', 1);
INSERT INTO account(name, email, password, account_type) VALUES('苹果化腾', '3@haha.com', 'admin', 1);
INSERT INTO account(name, email, password, account_type) VALUES('胡萝卜化腾', '4@haha.com', 'admin', 1);












