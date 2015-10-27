--
-- MySQL 5.5.24
-- Mon, 25 Mar 2013 02:53:35 +0000
--

CREATE DATABASE `yyets_resource` DEFAULT CHARSET utf8;

USE `yyets_resource`;

CREATE TABLE `good_website` (
   `id` int(11) not null auto_increment,
   `type` varchar(20),
   `sort` smallint(6) default '0',
   `name` varchar(30),
   `intro` varchar(30),
   `link` varchar(200),
   PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 AUTO_INCREMENT=82;

INSERT INTO `good_website` (`id`, `type`, `sort`, `name`, `intro`, `link`) VALUES ('13', 'download', '1', '人人影视', '海外影视翻译下载站', 'http://yyets.com/');
INSERT INTO `good_website` (`id`, `type`, `sort`, `name`, `intro`, `link`) VALUES ('14', 'pt', '0', 'CHDBits', '国内著名高清PT站', 'http://chdbits.org/login.php');
INSERT INTO `good_website` (`id`, `type`, `sort`, `name`, `intro`, `link`) VALUES ('16', 'online', '1', '一一影视', '影视点播站', 'http://www.yiyi.cc/');
INSERT INTO `good_website` (`id`, `type`, `sort`, `name`, `intro`, `link`) VALUES ('17', 'video', '0', '优酷', '中国最大视频站', 'http://www.youku.com/');
INSERT INTO `good_website` (`id`, `type`, `sort`, `name`, `intro`, `link`) VALUES ('18', 'other', '2', '时光网', '最新上映电影资讯网站', 'http://www.mtime.com/');
INSERT INTO `good_website` (`id`, `type`, `sort`, `name`, `intro`, `link`) VALUES ('25', 'online', '0', '宇宙点播网', '影视点播站', 'http://www.abcze.com/');
INSERT INTO `good_website` (`id`, `type`, `sort`, `name`, `intro`, `link`) VALUES ('27', 'girl', '1', '18P2P', '最大的美女网站', '哈哈');
INSERT INTO `good_website` (`id`, `type`, `sort`, `name`, `intro`, `link`) VALUES ('28', 'other', '1', '射手网', '最大的影视字幕下载站', 'http://www.shooter.cn/');
INSERT INTO `good_website` (`id`, `type`, `sort`, `name`, `intro`, `link`) VALUES ('29', 'other', '3', 'TLF字幕站', '电影字幕比较多', 'http://sub.eastgame.org/');
INSERT INTO `good_website` (`id`, `type`, `sort`, `name`, `intro`, `link`) VALUES ('30', 'download', '2', 'EZTV', '美剧片源下载站', 'http://eztv.it/');
INSERT INTO `good_website` (`id`, `type`, `sort`, `name`, `intro`, `link`) VALUES ('31', 'download', '4', 'KickassTorrents', '各种类型资源下载站', 'http://kat.ph/');
INSERT INTO `good_website` (`id`, `type`, `sort`, `name`, `intro`, `link`) VALUES ('32', 'download', '3', 'TV Underground', '美剧片源下载站', '');
INSERT INTO `good_website` (`id`, `type`, `sort`, `name`, `intro`, `link`) VALUES ('33', 'download', '5', '海盗美剧', '美剧，电影下载站', 'http://www.hdmeiju.com/main.php');
INSERT INTO `good_website` (`id`, `type`, `sort`, `name`, `intro`, `link`) VALUES ('34', 'download', '6', 'Public3D', '高清电影3D版下载站', 'http://public3d.se/');
INSERT INTO `good_website` (`id`, `type`, `sort`, `name`, `intro`, `link`) VALUES ('35', 'download', '7', '宇宙影视', '最新海外影视下载点播', '123');
INSERT INTO `good_website` (`id`, `type`, `sort`, `name`, `intro`, `link`) VALUES ('36', 'download', '8', '丫丫下载站', '影视下载站，可求档', '');
INSERT INTO `good_website` (`id`, `type`, `sort`, `name`, `intro`, `link`) VALUES ('37', 'download', '9', '电影天堂', '电影下载站', '');
INSERT INTO `good_website` (`id`, `type`, `sort`, `name`, `intro`, `link`) VALUES ('38', 'download', '10', '追新番', '日剧，动漫下载站', '');
INSERT INTO `good_website` (`id`, `type`, `sort`, `name`, `intro`, `link`) VALUES ('39', 'download', '11', '极影动漫', '国内著名动漫下载站', '');
INSERT INTO `good_website` (`id`, `type`, `sort`, `name`, `intro`, `link`) VALUES ('40', 'download', '12', '每天美剧', '最新影视翻译版下载', '');
INSERT INTO `good_website` (`id`, `type`, `sort`, `name`, `intro`, `link`) VALUES ('42', 'download', '14', 'OABT下载站', '最新海外影视下载站', '');
INSERT INTO `good_website` (`id`, `type`, `sort`, `name`, `intro`, `link`) VALUES ('44', 'download', '16', '天天美剧2', '片源下载站', '');
INSERT INTO `good_website` (`id`, `type`, `sort`, `name`, `intro`, `link`) VALUES ('45', 'online', '2', '比特动漫', '在线动漫点播站', 'http://www.bityx.com/');
INSERT INTO `good_website` (`id`, `type`, `sort`, `name`, `intro`, `link`) VALUES ('46', 'online', '3', 'PPS', '在线影视点播', 'http://www.pps.tv/');
INSERT INTO `good_website` (`id`, `type`, `sort`, `name`, `intro`, `link`) VALUES ('47', 'online', '5', '迅雷看看', '在线影视点播', 'http://www.kankan.com/');
INSERT INTO `good_website` (`id`, `type`, `sort`, `name`, `intro`, `link`) VALUES ('48', 'online', '0', '百度影音点播站', '海外影视高质量点播', '');
INSERT INTO `good_website` (`id`, `type`, `sort`, `name`, `intro`, `link`) VALUES ('49', 'online', '0', '奇热视频', '影视点播站', 'http://www.qire123.com/');
INSERT INTO `good_website` (`id`, `type`, `sort`, `name`, `intro`, `link`) VALUES ('50', 'online', '0', 'PPTV', '在线点播', 'http://www.pptv.com/');
INSERT INTO `good_website` (`id`, `type`, `sort`, `name`, `intro`, `link`) VALUES ('51', 'online', '0', '风行', '在线点播观看', 'http://www.funshion.com/?ta=4');
INSERT INTO `good_website` (`id`, `type`, `sort`, `name`, `intro`, `link`) VALUES ('53', 'video', '2', '六间房', '在线歌唱视频站', 'http://www.6.cn/');
INSERT INTO `good_website` (`id`, `type`, `sort`, `name`, `intro`, `link`) VALUES ('54', 'video', '3', 'hulu', '美国电视剧在线站', 'http://www.hulu.com/');
INSERT INTO `good_website` (`id`, `type`, `sort`, `name`, `intro`, `link`) VALUES ('55', 'video', '4', '网易视频', '最大特点是公开课', 'http://v.163.com/');
INSERT INTO `good_website` (`id`, `type`, `sort`, `name`, `intro`, `link`) VALUES ('56', 'video', '5', '土豆', '中国第二大视频站', 'http://www.tudou.com/');
INSERT INTO `good_website` (`id`, `type`, `sort`, `name`, `intro`, `link`) VALUES ('57', 'video', '6', '爱奇艺', '百度旗下的视频站', 'http://www.iqiyi.com/');
INSERT INTO `good_website` (`id`, `type`, `sort`, `name`, `intro`, `link`) VALUES ('58', 'video', '7', '乐视网', '国产版权最多的视频站', 'http://www.letv.com/');
INSERT INTO `good_website` (`id`, `type`, `sort`, `name`, `intro`, `link`) VALUES ('59', 'video', '8', 'YouTube', '自备梯子', 'http://www.youtube.com/');
INSERT INTO `good_website` (`id`, `type`, `sort`, `name`, `intro`, `link`) VALUES ('60', 'video', '9', '中国网络电视 CNTV', '央视旗下在线视频站', 'http://www.cntv.cn/');
INSERT INTO `good_website` (`id`, `type`, `sort`, `name`, `intro`, `link`) VALUES ('61', 'video', '10', '酷六网', '在线视频站', 'http://www.ku6.com/');
INSERT INTO `good_website` (`id`, `type`, `sort`, `name`, `intro`, `link`) VALUES ('62', 'video', '11', '新浪视频', '在线视频站', 'http://video.sina.com.cn/');
INSERT INTO `good_website` (`id`, `type`, `sort`, `name`, `intro`, `link`) VALUES ('63', 'video', '12', '音悦台', '音乐在线站', 'http://www.yinyuetai.com/');
INSERT INTO `good_website` (`id`, `type`, `sort`, `name`, `intro`, `link`) VALUES ('64', 'video', '13', '腾讯视频', '视频站', 'http://v.qq.com/');
INSERT INTO `good_website` (`id`, `type`, `sort`, `name`, `intro`, `link`) VALUES ('65', 'video', '1', '搜狐视频', '正版最多的视频站', 'http://tv.sohu.com/');
INSERT INTO `good_website` (`id`, `type`, `sort`, `name`, `intro`, `link`) VALUES ('66', 'pt', '1', 'TTG', '国内PT站', 'http://ttg.im/login.php?returnto=');
INSERT INTO `good_website` (`id`, `type`, `sort`, `name`, `intro`, `link`) VALUES ('67', 'pt', '2', 'TVT', '国外著名美剧PT站', '');
INSERT INTO `good_website` (`id`, `type`, `sort`, `name`, `intro`, `link`) VALUES ('68', 'pt', '3', 'SCC', '国外著名0DAY资源PT站', '');
INSERT INTO `good_website` (`id`, `type`, `sort`, `name`, `intro`, `link`) VALUES ('69', 'pt', '4', 'BITMETV', '国外著名美剧PT站', '');
INSERT INTO `good_website` (`id`, `type`, `sort`, `name`, `intro`, `link`) VALUES ('70', 'pt', '5', 'HDR', 'MYsilu的PT站', 'http://hdroad.org/login.php?returnto=%2F');
INSERT INTO `good_website` (`id`, `type`, `sort`, `name`, `intro`, `link`) VALUES ('71', 'pt', '6', 'HDBits', '国外著名高清影视PT站', 'http://hdbits.cn/login.php');
INSERT INTO `good_website` (`id`, `type`, `sort`, `name`, `intro`, `link`) VALUES ('72', 'other', '4', '伊甸园字幕组', '著名美剧字幕组', 'http://bbs.sfile2012.com/');
INSERT INTO `good_website` (`id`, `type`, `sort`, `name`, `intro`, `link`) VALUES ('73', 'other', '5', '破烂熊字幕组', '著名美剧字幕组', 'http://www.ragbear.com/');
INSERT INTO `good_website` (`id`, `type`, `sort`, `name`, `intro`, `link`) VALUES ('74', 'other', '6', '人人影视字幕站', '人人影视原创翻译字幕', 'http://www.yyets.com/php/subtitle/');
INSERT INTO `good_website` (`id`, `type`, `sort`, `name`, `intro`, `link`) VALUES ('75', 'other', '7', '网票网', '在线购买电影票的网站', 'http://www.wangpiao.com/');
INSERT INTO `good_website` (`id`, `type`, `sort`, `name`, `intro`, `link`) VALUES ('76', 'other', '8', 'Addic7ed字幕站', '美剧英文字幕站', 'http://www.addic7ed.com/');
INSERT INTO `good_website` (`id`, `type`, `sort`, `name`, `intro`, `link`) VALUES ('77', 'other', '9', '风软字幕组', '著名美剧字幕组', 'http://www.1000fr.net/forum-46-1.html');
INSERT INTO `good_website` (`id`, `type`, `sort`, `name`, `intro`, `link`) VALUES ('78', 'other', '10', '深影字幕组', '海外影视字幕组', 'http://shinybbs.com/');
INSERT INTO `good_website` (`id`, `type`, `sort`, `name`, `intro`, `link`) VALUES ('79', 'other', '11', '猪猪日剧字幕组', '著名日剧字幕组', 'http://www.subpig.net/');
INSERT INTO `good_website` (`id`, `type`, `sort`, `name`, `intro`, `link`) VALUES ('80', 'other', '12', '漫游字幕组', '著名动漫字幕组', 'http://bt.ktxp.com/team-131-1.html');
INSERT INTO `good_website` (`id`, `type`, `sort`, `name`, `intro`, `link`) VALUES ('81', 'other', '13', '法国字幕组', '法国美剧字幕组', '');

CREATE TABLE `hot_resource` (
   `id` int(11) not null auto_increment,
   `type` varchar(20),
   `sort` smallint(6),
   `name` varchar(100),
   `link` varchar(200),
   PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 AUTO_INCREMENT=104;

INSERT INTO `hot_resource` (`id`, `type`, `sort`, `name`, `link`) VALUES ('1', 'movie', '5', '遗忘星球', 'http://baike.baidu.com/view/28733.htm');
INSERT INTO `hot_resource` (`id`, `type`, `sort`, `name`, `link`) VALUES ('2', 'movie', '8', '西游·降魔篇', 'http://baike.baidu.com/view/9632495.htm');
INSERT INTO `hot_resource` (`id`, `type`, `sort`, `name`, `link`) VALUES ('14', 'movie', '4', '特种部队：全面反击', 'hahaha');
INSERT INTO `hot_resource` (`id`, `type`, `sort`, `name`, `link`) VALUES ('15', 'am_tv', '3', '猫鼠游戏', 'http://www.baidu.com');
INSERT INTO `hot_resource` (`id`, `type`, `sort`, `name`, `link`) VALUES ('16', 'am_tv', '4', '生活大爆炸', 'http://www.baidu.com');
INSERT INTO `hot_resource` (`id`, `type`, `sort`, `name`, `link`) VALUES ('17', 'jk_tv', '3', '城市猎人', 'http://www.baidu.com');
INSERT INTO `hot_resource` (`id`, `type`, `sort`, `name`, `link`) VALUES ('18', 'jk_tv', '4', '膝盖道士', 'http://www.baidu.com');
INSERT INTO `hot_resource` (`id`, `type`, `sort`, `name`, `link`) VALUES ('19', 'ct', '3', '喜洋洋与灰太狼', 'http://www.baidu.com');
INSERT INTO `hot_resource` (`id`, `type`, `sort`, `name`, `link`) VALUES ('20', 'ct', '1', '海绵宝宝', ' http://www.baidu.com ');
INSERT INTO `hot_resource` (`id`, `type`, `sort`, `name`, `link`) VALUES ('21', 'ct', '1', '飞出个未来', ' http://www.baidu.com ');
INSERT INTO `hot_resource` (`id`, `type`, `sort`, `name`, `link`) VALUES ('22', 'china', '1', '阳光的快乐生活', 'http://www.baidu.com');
INSERT INTO `hot_resource` (`id`, `type`, `sort`, `name`, `link`) VALUES ('23', ' china ', '60', '垃圾电视剧', ' http://www.baidu.com ');
INSERT INTO `hot_resource` (`id`, `type`, `sort`, `name`, `link`) VALUES ('24', 'game', '4', '无主之地2', 'http://www.baidu.com');
INSERT INTO `hot_resource` (`id`, `type`, `sort`, `name`, `link`) VALUES ('25', ' game ', '7', '愤怒的小鸟', ' http://www.baidu.com ');
INSERT INTO `hot_resource` (`id`, `type`, `sort`, `name`, `link`) VALUES ('31', 'game', '3', '真三国无双9', '你猜');
INSERT INTO `hot_resource` (`id`, `type`, `sort`, `name`, `link`) VALUES ('32', 'game', '1', '侠盗飞车', '3');
INSERT INTO `hot_resource` (`id`, `type`, `sort`, `name`, `link`) VALUES ('33', 'game', '5', '假三国无双2', 'www.google.com');
INSERT INTO `hot_resource` (`id`, `type`, `sort`, `name`, `link`) VALUES ('37', 'game', '2', '吃豆人', '很好');
INSERT INTO `hot_resource` (`id`, `type`, `sort`, `name`, `link`) VALUES ('58', 'game', '2', '超级玛丽', '2');
INSERT INTO `hot_resource` (`id`, `type`, `sort`, `name`, `link`) VALUES ('60', 'movie', '1', '钢铁侠3', '哈哈');
INSERT INTO `hot_resource` (`id`, `type`, `sort`, `name`, `link`) VALUES ('61', 'movie', '2', '金刚狼2', '嗯嗯');
INSERT INTO `hot_resource` (`id`, `type`, `sort`, `name`, `link`) VALUES ('62', 'movie', '3', '星际迷航', '哈哈');
INSERT INTO `hot_resource` (`id`, `type`, `sort`, `name`, `link`) VALUES ('63', 'am_tv', '1', '吸血鬼日记', 'www.hhhhh.com');
INSERT INTO `hot_resource` (`id`, `type`, `sort`, `name`, `link`) VALUES ('64', 'am_tv', '2', '老友记', '哈哈');
INSERT INTO `hot_resource` (`id`, `type`, `sort`, `name`, `link`) VALUES ('65', 'movie', '6', '虎胆龙威5', '2');
INSERT INTO `hot_resource` (`id`, `type`, `sort`, `name`, `link`) VALUES ('66', 'movie', '7', '霍比特人：意外之旅', '2');
INSERT INTO `hot_resource` (`id`, `type`, `sort`, `name`, `link`) VALUES ('67', 'movie', '9', '巨人捕手杰克 ', '2');
INSERT INTO `hot_resource` (`id`, `type`, `sort`, `name`, `link`) VALUES ('68', 'am_tv', '5', '美少女的谎言', '1');
INSERT INTO `hot_resource` (`id`, `type`, `sort`, `name`, `link`) VALUES ('69', 'am_tv', '6', '尼基塔', '2');
INSERT INTO `hot_resource` (`id`, `type`, `sort`, `name`, `link`) VALUES ('70', 'am_tv', '7', '冰与火之歌：权力的游戏', '3');
INSERT INTO `hot_resource` (`id`, `type`, `sort`, `name`, `link`) VALUES ('71', 'am_tv', '8', '好汉两个半', '4');
INSERT INTO `hot_resource` (`id`, `type`, `sort`, `name`, `link`) VALUES ('72', 'am_tv', '9', '老爸老妈的浪漫史', '5');
INSERT INTO `hot_resource` (`id`, `type`, `sort`, `name`, `link`) VALUES ('73', 'am_tv', '10', '破产姐妹', '6');
INSERT INTO `hot_resource` (`id`, `type`, `sort`, `name`, `link`) VALUES ('74', 'ct', '4', '火影忍者', '2');
INSERT INTO `hot_resource` (`id`, `type`, `sort`, `name`, `link`) VALUES ('75', 'ct', '5', '海贼王', '3');
INSERT INTO `hot_resource` (`id`, `type`, `sort`, `name`, `link`) VALUES ('76', 'ct', '6', '黑背漫画', '7');
INSERT INTO `hot_resource` (`id`, `type`, `sort`, `name`, `link`) VALUES ('77', 'ct', '7', '十万个冷笑话', '8');
INSERT INTO `hot_resource` (`id`, `type`, `sort`, `name`, `link`) VALUES ('78', 'ct', '8', '名侦探柯南', '9');
INSERT INTO `hot_resource` (`id`, `type`, `sort`, `name`, `link`) VALUES ('79', 'ct', '9', '猫和老鼠', '18');
INSERT INTO `hot_resource` (`id`, `type`, `sort`, `name`, `link`) VALUES ('80', 'ct', '10', '老鼠和猫', '');
INSERT INTO `hot_resource` (`id`, `type`, `sort`, `name`, `link`) VALUES ('81', 'china', '2', '我是特种兵', '2');
INSERT INTO `hot_resource` (`id`, `type`, `sort`, `name`, `link`) VALUES ('82', 'china', '3', '青春期撞上更年期 第2部', '3');
INSERT INTO `hot_resource` (`id`, `type`, `sort`, `name`, `link`) VALUES ('83', 'china', '4', '非凡英雄', '4');
INSERT INTO `hot_resource` (`id`, `type`, `sort`, `name`, `link`) VALUES ('84', 'china', '5', '隋唐演义', '');
INSERT INTO `hot_resource` (`id`, `type`, `sort`, `name`, `link`) VALUES ('85', 'china', '6', '笑傲江湖 霍建华TV版', '');
INSERT INTO `hot_resource` (`id`, `type`, `sort`, `name`, `link`) VALUES ('86', 'china', '7', '爱情公寓 TV版 第3季', '');
INSERT INTO `hot_resource` (`id`, `type`, `sort`, `name`, `link`) VALUES ('87', 'china', '8', '同福客栈', '');
INSERT INTO `hot_resource` (`id`, `type`, `sort`, `name`, `link`) VALUES ('88', 'china', '9', '放着我来', '');
INSERT INTO `hot_resource` (`id`, `type`, `sort`, `name`, `link`) VALUES ('89', 'china', '10', '一起来看什么雨', '');
INSERT INTO `hot_resource` (`id`, `type`, `sort`, `name`, `link`) VALUES ('90', 'game', '6', '英雄使命', '');
INSERT INTO `hot_resource` (`id`, `type`, `sort`, `name`, `link`) VALUES ('91', 'game', '7', '糖果竞速', '');
INSERT INTO `hot_resource` (`id`, `type`, `sort`, `name`, `link`) VALUES ('92', 'game', '8', '快手阿修', '');
INSERT INTO `hot_resource` (`id`, `type`, `sort`, `name`, `link`) VALUES ('93', 'game', '10', '风之旅者', '');
INSERT INTO `hot_resource` (`id`, `type`, `sort`, `name`, `link`) VALUES ('94', 'jk_tv', '5', '傻瓜妈妈', '');
INSERT INTO `hot_resource` (`id`, `type`, `sort`, `name`, `link`) VALUES ('95', 'jk_tv', '7', '假如明天来临', '');
INSERT INTO `hot_resource` (`id`, `type`, `sort`, `name`, `link`) VALUES ('96', 'jk_tv', '9', '随便编一个名字好了', '');
INSERT INTO `hot_resource` (`id`, `type`, `sort`, `name`, `link`) VALUES ('97', 'jk_tv', '12', '比如这样', '');
INSERT INTO `hot_resource` (`id`, `type`, `sort`, `name`, `link`) VALUES ('98', 'jk_tv', '13', '再这样', '');
INSERT INTO `hot_resource` (`id`, `type`, `sort`, `name`, `link`) VALUES ('99', 'jk_tv', '14', '嗯', '');
INSERT INTO `hot_resource` (`id`, `type`, `sort`, `name`, `link`) VALUES ('100', 'jk_tv', '15', '思密达', '');
INSERT INTO `hot_resource` (`id`, `type`, `sort`, `name`, `link`) VALUES ('101', 'jk_tv', '16', '123', '');
INSERT INTO `hot_resource` (`id`, `type`, `sort`, `name`, `link`) VALUES ('103', 'movie', '10', '巴拉拉啦啦啦', 'http:2b.com');

CREATE TABLE `knowledge_share` (
   `id` int(11) not null auto_increment,
   `sort` smallint(6),
   `title` varchar(75),
   `link` varchar(200),
   PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 AUTO_INCREMENT=14;

INSERT INTO `knowledge_share` (`id`, `sort`, `title`, `link`) VALUES ('3', '5', '美剧，电影的资源播出和发布时间详解', 'http://www.123.com');
INSERT INTO `knowledge_share` (`id`, `sort`, `title`, `link`) VALUES ('4', '2', '如何压制字幕？', 'http://www.hao123.com');
INSERT INTO `knowledge_share` (`id`, `sort`, `title`, `link`) VALUES ('11', '1', '字幕翻译软件介绍', 'http://www.222.com');
INSERT INTO `knowledge_share` (`id`, `sort`, `title`, `link`) VALUES ('12', '3', '字幕文件格式之间有什么不同？', 'http://www.zhihu.com');
INSERT INTO `knowledge_share` (`id`, `sort`, `title`, `link`) VALUES ('13', '4', '视频格式详解', 'http://www.baidu.com');

CREATE TABLE `useful_tool` (
   `id` int(11) not null auto_increment,
   `sort` smallint(6),
   `name` varchar(60) not null,
   `intro` varchar(90),
   `imglink` varchar(200),
   `link` varchar(200) not null,
   PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 AUTO_INCREMENT=7;

INSERT INTO `useful_tool` (`id`, `sort`, `name`, `intro`, `imglink`, `link`) VALUES ('1', '1', '迅雷', '好用的下载工具', 'http://dl.xunlei.com/img/icon/36_xl.png', 'http://dl.xunlei.com/xl7.html');
INSERT INTO `useful_tool` (`id`, `sort`, `name`, `intro`, `imglink`, `link`) VALUES ('2', '3', '百度影音', '高质量在线点播的播放器', 'http://t11.baidu.com/it/u=3100026709,425211555&fm=58', 'http://player.baidu.com/');
INSERT INTO `useful_tool` (`id`, `sort`, `name`, `intro`, `imglink`, `link`) VALUES ('3', '5', '小红伞', '德国的免费杀毒软件', 'http://www.avira.com/images/content/avira-antivirus.png', 'http://www.avira.com/zh-tw/for-home');
INSERT INTO `useful_tool` (`id`, `sort`, `name`, `intro`, `imglink`, `link`) VALUES ('4', '7', '火狐', '强大安全的浏览器', 'http://t10.baidu.com/it/u=2748679902,1639824998&fm=58', 'http://firefox.com.cn/');
INSERT INTO `useful_tool` (`id`, `sort`, `name`, `intro`, `imglink`, `link`) VALUES ('5', '9', '快车', '老牌下载软件', 'http://www.flashget.com/cn/images/logo.jpg', 'http://www.flashget.com/cn/');
INSERT INTO `useful_tool` (`id`, `sort`, `name`, `intro`, `imglink`, `link`) VALUES ('6', '13', 'QQ旋风', '腾讯旗下的下载软件，很强大', 'http://xf.qq.com/xf4/xf/images/logo.png', 'http://xf.qq.com/');