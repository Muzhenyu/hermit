-- MySQL dump 10.13  Distrib 5.7.27, for Linux (x86_64)
--
-- Host: localhost    Database: groupwork
-- ------------------------------------------------------
-- Server version	5.7.27-0ubuntu0.18.04.1

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `areas`
--

DROP TABLE IF EXISTS `areas`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `areas` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(50) NOT NULL,
  `pid_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `areas_pid_id_534d967d_fk_areas_id` (`pid_id`),
  CONSTRAINT `areas_pid_id_534d967d_fk_areas_id` FOREIGN KEY (`pid_id`) REFERENCES `areas` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=330185207 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `areas`
--

LOCK TABLES `areas` WRITE;
/*!40000 ALTER TABLE `areas` DISABLE KEYS */;
INSERT INTO `areas` VALUES (330102,'上城区',NULL),(330103,'下城区',NULL),(330104,'江干区',NULL),(330105,'拱墅区',NULL),(330106,'西湖区',NULL),(330108,'滨江区',NULL),(330109,'萧山区',NULL),(330110,'余杭区',NULL),(330122,'桐庐县',NULL),(330127,'淳安县',NULL),(330182,'建德市',NULL),(330183,'富阳市',NULL),(330185,'临安市',NULL),(330102001,'清波街道',330102),(330102003,'湖滨街道',330102),(330102004,'小营街道',330102),(330102008,'南星街道',330102),(330102009,'紫阳街道',330102),(330102010,'望江街道',330102),(330103001,'长庆街道',330103),(330103002,'武林街道',330103),(330103003,'天水街道',330103),(330103005,'潮鸣街道',330103),(330103006,'朝晖街道',330103),(330103007,'文晖街道',330103),(330103008,'东新街道',330103),(330103009,'石桥街道',330103),(330104005,'凯旋街道',330104),(330104006,'采荷街道',330104),(330104007,'闸弄口街道',330104),(330104008,'四季青街道',330104),(330104009,'白杨街道',330104),(330104010,'下沙街道',330104),(330104102,'彭埠镇',330104),(330104103,'笕桥镇',330104),(330104104,'丁桥镇',330104),(330104105,'九堡镇',330104),(330105001,'米市巷街道',330105),(330105002,'湖墅街道',330105),(330105003,'小河街道',330105),(330105004,'和睦街道',330105),(330105005,'拱宸桥街道',330105),(330105007,'大关街道',330105),(330105008,'上塘街道',330105),(330105102,'康桥镇',330105),(330105103,'半山镇',330105),(330105104,'祥符镇',330105),(330106002,'北山街道',330106),(330106003,'灵隐街道',330106),(330106004,'西溪街道',330106),(330106005,'翠苑街道',330106),(330106006,'文新街道',330106),(330106007,'古荡街道',330106),(330106008,'西湖街道',330106),(330106103,'留下镇',330106),(330106104,'转塘镇',330106),(330106105,'袁浦镇',330106),(330106106,'龙坞镇',330106),(330106109,'三墩镇',330106),(330106202,'周浦乡',330106),(330106203,'蒋村乡',330106),(330108001,'西兴街道',330108),(330108002,'长河街道',330108),(330108003,'浦沿街道',330108),(330109001,'城厢街道',330109),(330109002,'北干街道',330109),(330109003,'蜀山街道',330109),(330109004,'新塘街道',330109),(330109100,'楼塔镇',330109),(330109101,'河上镇',330109),(330109102,'戴村镇',330109),(330109103,'浦阳镇',330109),(330109104,'进化镇',330109),(330109105,'临浦镇',330109),(330109106,'义桥镇',330109),(330109107,'所前镇',330109),(330109108,'衙前镇',330109),(330109109,'闻堰镇',330109),(330109110,'宁围镇',330109),(330109111,'新街镇',330109),(330109112,'坎山镇',330109),(330109113,'瓜沥镇',330109),(330109114,'党山镇',330109),(330109115,'益农镇',330109),(330109116,'靖江镇',330109),(330109117,'南阳镇',330109),(330109118,'义蓬镇',330109),(330109119,'河庄镇',330109),(330109120,'党湾镇',330109),(330109121,'新湾镇',330109),(330109401,'萧山经济开发区',330109),(330109501,'围垦区',330109),(330110001,'临平街道',330110),(330110002,'南苑街道',330110),(330110003,'东湖街道',330110),(330110004,'星桥街道',330110),(330110100,'乔司镇',330110),(330110101,'运河镇',330110),(330110102,'塘栖镇',330110),(330110103,'崇贤镇',330110),(330110104,'仁和镇',330110),(330110105,'良渚镇',330110),(330110106,'闲林镇',330110),(330110107,'仓前镇',330110),(330110108,'余杭镇',330110),(330110109,'径山镇',330110),(330110110,'瓶窑镇',330110),(330110111,'鸬鸟镇',330110),(330110112,'百丈镇',330110),(330110113,'黄湖镇',330110),(330110200,'中泰乡',330110),(330122001,'桐君街道',330122),(330122002,'旧县街道',330122),(330122101,'富春江镇',330122),(330122102,'横村镇',330122),(330122107,'凤川镇',330122),(330122109,'分水镇',330122),(330122110,'瑶琳镇',330122),(330122112,'百江镇',330122),(330122113,'江南镇',330122),(330122201,'莪山畲族自治乡',330122),(330122202,'钟山乡',330122),(330122204,'新合乡',330122),(330122210,'合村乡',330122),(330127100,'千岛湖镇',330127),(330127101,'文昌镇',330127),(330127102,'石林镇',330127),(330127103,'临岐镇',330127),(330127104,'威坪镇',330127),(330127106,'姜家镇',330127),(330127107,'梓桐镇',330127),(330127108,'汾口镇',330127),(330127109,'中洲镇',330127),(330127110,'大墅镇',330127),(330127111,'枫树岭镇',330127),(330127200,'里商乡',330127),(330127201,'金峰乡',330127),(330127202,'富文乡',330127),(330127203,'左口乡',330127),(330127205,'屏门乡',330127),(330127206,'瑶山乡',330127),(330127208,'王阜乡',330127),(330127210,'宋村乡',330127),(330127211,'鸠坑乡',330127),(330127212,'浪川乡',330127),(330127214,'界首乡',330127),(330127216,'安阳乡',330127),(330182001,'新安江街道',330182),(330182002,'洋溪街道',330182),(330182003,'更楼街道',330182),(330182101,'莲花镇',330182),(330182102,'乾潭镇',330182),(330182104,'梅城镇',330182),(330182105,'杨村桥镇',330182),(330182106,'下涯镇',330182),(330182107,'大洋镇',330182),(330182108,'三都镇',330182),(330182109,'寿昌镇',330182),(330182110,'航头镇',330182),(330182111,'大慈岩镇',330182),(330182112,'大同镇',330182),(330182113,'李家镇',330182),(330182202,'钦堂乡',330182),(330183001,'富春街道',330183),(330183002,'春江街道',330183),(330183003,'东洲街道',330183),(330183004,'鹿山街道',330183),(330183100,'万市镇',330183),(330183101,'洞桥镇',330183),(330183102,'新登镇',330183),(330183103,'渌渚镇',330183),(330183104,'胥口镇',330183),(330183105,'永昌镇',330183),(330183106,'大源镇',330183),(330183107,'灵桥镇',330183),(330183108,'里山镇',330183),(330183109,'常绿镇',330183),(330183110,'场口镇',330183),(330183111,'常安镇',330183),(330183112,'龙门镇',330183),(330183113,'高桥镇',330183),(330183114,'受降镇',330183),(330183200,'新桐乡',330183),(330183201,'上官乡',330183),(330183202,'渔山乡',330183),(330183204,'环山乡',330183),(330183205,'湖源乡',330183),(330183206,'春建乡',330183),(330185001,'锦城街道',330185),(330185002,'玲珑街道',330185),(330185003,'青山湖街道',330185),(330185004,'上甘街道',330185),(330185100,'三口镇',330185),(330185101,'横畈镇',330185),(330185102,'高虹镇',330185),(330185103,'太湖源镇',330185),(330185104,'於潜镇',330185),(330185105,'藻溪镇',330185),(330185106,'太阳镇',330185),(330185107,'潜川镇',330185),(330185108,'昌化镇',330185),(330185109,'河桥镇',330185),(330185110,'龙岗镇',330185),(330185111,'湍口镇',330185),(330185112,'清凉峰镇',330185),(330185113,'岛石镇',330185),(330185114,'大峡谷镇',330185),(330185200,'板桥乡',330185),(330185201,'西天目乡',330185),(330185202,'千洪乡',330185),(330185203,'横路乡',330185),(330185204,'乐平乡',330185),(330185205,'马啸乡',330185),(330185206,'新桥乡',330185);
/*!40000 ALTER TABLE `areas` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_group`
--

DROP TABLE IF EXISTS `auth_group`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_group` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(80) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_group`
--

LOCK TABLES `auth_group` WRITE;
/*!40000 ALTER TABLE `auth_group` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_group` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_group_permissions`
--

DROP TABLE IF EXISTS `auth_group_permissions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_group_permissions` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `group_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  KEY `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_group_permissions`
--

LOCK TABLES `auth_group_permissions` WRITE;
/*!40000 ALTER TABLE `auth_group_permissions` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_group_permissions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_permission`
--

DROP TABLE IF EXISTS `auth_permission`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_permission` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `content_type_id` int(11) NOT NULL,
  `codename` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`),
  CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=55 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_permission`
--

LOCK TABLES `auth_permission` WRITE;
/*!40000 ALTER TABLE `auth_permission` DISABLE KEYS */;
INSERT INTO `auth_permission` VALUES (1,'Can add log entry',1,'add_logentry'),(2,'Can change log entry',1,'change_logentry'),(3,'Can delete log entry',1,'delete_logentry'),(4,'Can add permission',2,'add_permission'),(5,'Can change permission',2,'change_permission'),(6,'Can delete permission',2,'delete_permission'),(7,'Can add group',3,'add_group'),(8,'Can change group',3,'change_group'),(9,'Can delete group',3,'delete_group'),(10,'Can add content type',4,'add_contenttype'),(11,'Can change content type',4,'change_contenttype'),(12,'Can delete content type',4,'delete_contenttype'),(13,'Can add session',5,'add_session'),(14,'Can change session',5,'change_session'),(15,'Can delete session',5,'delete_session'),(16,'Can add user',6,'add_user'),(17,'Can change user',6,'change_user'),(18,'Can delete user',6,'delete_user'),(19,'Can add User_address',7,'add_address'),(20,'Can change User_address',7,'change_address'),(21,'Can delete User_address',7,'delete_address'),(22,'Can add collect_library',8,'add_collect_library'),(23,'Can change collect_library',8,'change_collect_library'),(24,'Can delete collect_library',8,'delete_collect_library'),(25,'Can add areas',9,'add_areas'),(26,'Can change areas',9,'change_areas'),(27,'Can delete areas',9,'delete_areas'),(28,'Can add Token',10,'add_token'),(29,'Can change Token',10,'change_token'),(30,'Can delete Token',10,'delete_token'),(31,'Can add library',11,'add_library'),(32,'Can change library',11,'change_library'),(33,'Can delete library',11,'delete_library'),(34,'Can add user',12,'add_libraryuser'),(35,'Can change user',12,'change_libraryuser'),(36,'Can delete user',12,'delete_libraryuser'),(37,'Can add usercomment',13,'add_usercomment'),(38,'Can change usercomment',13,'change_usercomment'),(39,'Can delete usercomment',13,'delete_usercomment'),(40,'Can add lib type',14,'add_libtype'),(41,'Can change lib type',14,'change_libtype'),(42,'Can delete lib type',14,'delete_libtype'),(43,'Can add imglist',15,'add_imglist'),(44,'Can change imglist',15,'change_imglist'),(45,'Can delete imglist',15,'delete_imglist'),(46,'Can add library_detail_info_page_model',16,'add_library_detail_info_page_model'),(47,'Can change library_detail_info_page_model',16,'change_library_detail_info_page_model'),(48,'Can delete library_detail_info_page_model',16,'delete_library_detail_info_page_model'),(49,'Can add imgsave',17,'add_imgsave'),(50,'Can change imgsave',17,'change_imgsave'),(51,'Can delete imgsave',17,'delete_imgsave'),(52,'Can add explore_time',18,'add_explore_time'),(53,'Can change explore_time',18,'change_explore_time'),(54,'Can delete explore_time',18,'delete_explore_time');
/*!40000 ALTER TABLE `auth_permission` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `authtoken_token`
--

DROP TABLE IF EXISTS `authtoken_token`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `authtoken_token` (
  `key` varchar(40) NOT NULL,
  `created` datetime(6) NOT NULL,
  `user_id` int(11) NOT NULL,
  PRIMARY KEY (`key`),
  UNIQUE KEY `user_id` (`user_id`),
  CONSTRAINT `authtoken_token_user_id_35299eff_fk_user_user_id` FOREIGN KEY (`user_id`) REFERENCES `gw_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `authtoken_token`
--

LOCK TABLES `authtoken_token` WRITE;
/*!40000 ALTER TABLE `authtoken_token` DISABLE KEYS */;
/*!40000 ALTER TABLE `authtoken_token` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_admin_log`
--

DROP TABLE IF EXISTS `django_admin_log`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_admin_log` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint(5) unsigned NOT NULL,
  `change_message` longtext NOT NULL,
  `content_type_id` int(11) DEFAULT NULL,
  `user_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `django_admin_log_content_type_id_c4bce8eb_fk_django_co` (`content_type_id`),
  KEY `django_admin_log_user_id_c564eba6_fk_user_user_id` (`user_id`),
  CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  CONSTRAINT `django_admin_log_user_id_c564eba6_fk_user_user_id` FOREIGN KEY (`user_id`) REFERENCES `gw_user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=38 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_admin_log`
--

LOCK TABLES `django_admin_log` WRITE;
/*!40000 ALTER TABLE `django_admin_log` DISABLE KEYS */;
INSERT INTO `django_admin_log` VALUES (1,'2019-08-07 06:14:32.076797','1','libType object',1,'[{\"added\": {}}]',14,1),(2,'2019-08-07 06:39:35.412351','1','libType object',2,'[{\"changed\": {\"fields\": [\"type_name\", \"type_description\"]}}]',14,1),(3,'2019-08-07 06:39:58.297651','2','libType object',1,'[{\"added\": {}}]',14,1),(4,'2019-08-07 06:52:37.801287','1','shuwu',3,'',11,1),(5,'2019-08-08 05:58:13.449971','1','imgsave object',1,'[{\"added\": {}}]',17,1),(6,'2019-08-08 05:59:19.751330','1','library_detail_info_page_model object',1,'[{\"added\": {}}]',16,1),(7,'2019-08-08 06:17:58.644376','4','baidushuwu',3,'',11,1),(8,'2019-08-08 06:45:08.380851','5','sdaxzcsad',3,'',11,1),(9,'2019-08-08 08:26:26.912846','6','shuwudada',3,'',11,1),(10,'2019-08-08 09:04:31.652998','7','czsdawxzdwad',3,'',11,1),(11,'2019-08-09 07:02:51.180283','1','Usercomment object',3,'',13,1),(12,'2019-08-09 07:06:58.900890','4','Usercomment object',3,'',13,1),(13,'2019-08-09 07:07:07.227148','5','Usercomment object',3,'',13,1),(14,'2019-08-09 07:07:11.042025','3','Usercomment object',3,'',13,1),(15,'2019-08-09 07:07:17.381365','2','Usercomment object',3,'',13,1),(16,'2019-08-09 07:09:05.472862','1','library_detail_info_page_model object',2,'[{\"changed\": {\"fields\": [\"page_model\"]}}]',16,1),(17,'2019-08-09 07:09:51.749260','8','xdawdsadw',3,'',11,1),(18,'2019-08-09 07:09:59.271160','3','shuwuda',3,'',11,1),(19,'2019-08-09 07:10:04.792981','2','shuwu',3,'',11,1),(20,'2019-08-09 07:26:56.832039','1','library_detail_info_page_model object',2,'[{\"changed\": {\"fields\": [\"page_model\"]}}]',16,1),(21,'2019-08-09 07:48:46.283079','10','shuwudsa',3,'',11,1),(22,'2019-08-09 07:48:51.809994','9','网易蜗牛读书馆',3,'',11,1),(23,'2019-08-12 11:19:19.746559','1','explore_time object',3,'',18,1),(24,'2019-08-13 03:02:13.668557','1','library_detail_info_page_model object',2,'[{\"changed\": {\"fields\": [\"page_model\"]}}]',16,1),(25,'2019-08-13 07:06:02.709231','1','library_detail_info_page_model object',2,'[{\"changed\": {\"fields\": [\"page_model\"]}}]',16,1),(26,'2019-08-13 08:52:35.589466','2','explore_time object',2,'[{\"changed\": {\"fields\": [\"explore_data_time\"]}}]',18,1),(27,'2019-08-13 08:52:49.000386','3','explore_time object',2,'[{\"changed\": {\"fields\": [\"explore_data_time\"]}}]',18,1),(28,'2019-08-14 02:07:09.377562','2','imgsave object',1,'[{\"added\": {}}]',17,1),(29,'2019-08-14 02:09:28.451317','16','muzhenyu1',2,'[{\"changed\": {\"fields\": [\"img_url\"]}}]',6,1),(30,'2019-08-14 02:09:35.926104','15','13806782813',2,'[{\"changed\": {\"fields\": [\"img_url\"]}}]',6,1),(31,'2019-08-14 02:09:43.488361','14','shu18291124520',2,'[{\"changed\": {\"fields\": [\"img_url\"]}}]',6,1),(32,'2019-08-14 02:09:54.585814','13','lvbu89757',2,'[{\"changed\": {\"fields\": [\"img_url\"]}}]',6,1),(33,'2019-08-14 02:10:10.540272','5','Mzy1009m',2,'[{\"changed\": {\"fields\": [\"img_url\"]}}]',6,1),(34,'2019-08-19 06:56:13.113557','70','explore_time object',1,'[{\"added\": {}}]',18,1),(35,'2019-08-19 07:03:27.688627','3','imgsave object',1,'[{\"added\": {}}]',17,1),(36,'2019-08-20 01:03:39.677503','1','library_detail_info_page_model object',2,'[{\"changed\": {\"fields\": [\"page_model\"]}}]',16,1),(37,'2019-08-20 12:13:21.534709','4','imgsave object',1,'[{\"added\": {}}]',17,1);
/*!40000 ALTER TABLE `django_admin_log` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_content_type`
--

DROP TABLE IF EXISTS `django_content_type`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_content_type` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`)
) ENGINE=InnoDB AUTO_INCREMENT=19 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_content_type`
--

LOCK TABLES `django_content_type` WRITE;
/*!40000 ALTER TABLE `django_content_type` DISABLE KEYS */;
INSERT INTO `django_content_type` VALUES (1,'admin','logentry'),(9,'areas','areas'),(3,'auth','group'),(2,'auth','permission'),(10,'authtoken','token'),(4,'contenttypes','contenttype'),(18,'libraries','explore_time'),(15,'libraries','imglist'),(17,'libraries','imgsave'),(11,'libraries','library'),(12,'libraries','libraryuser'),(16,'libraries','library_detail_info_page_model'),(14,'libraries','libtype'),(13,'libraries','usercomment'),(5,'sessions','session'),(7,'user','address'),(8,'user','collect_library'),(6,'user','user');
/*!40000 ALTER TABLE `django_content_type` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_migrations`
--

DROP TABLE IF EXISTS `django_migrations`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_migrations` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=74 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_migrations`
--

LOCK TABLES `django_migrations` WRITE;
/*!40000 ALTER TABLE `django_migrations` DISABLE KEYS */;
INSERT INTO `django_migrations` VALUES (1,'contenttypes','0001_initial','2019-08-07 06:12:03.915036'),(2,'contenttypes','0002_remove_content_type_name','2019-08-07 06:12:03.961356'),(3,'auth','0001_initial','2019-08-07 06:12:04.082248'),(4,'auth','0002_alter_permission_name_max_length','2019-08-07 06:12:04.109404'),(5,'auth','0003_alter_user_email_max_length','2019-08-07 06:12:04.124464'),(6,'auth','0004_alter_user_username_opts','2019-08-07 06:12:04.139766'),(7,'auth','0005_alter_user_last_login_null','2019-08-07 06:12:04.190610'),(8,'auth','0006_require_contenttypes_0002','2019-08-07 06:12:04.194565'),(9,'auth','0007_alter_validators_add_error_messages','2019-08-07 06:12:04.209849'),(10,'auth','0008_alter_user_username_max_length','2019-08-07 06:12:04.223171'),(11,'user','0001_initial','2019-08-07 06:12:04.388670'),(12,'admin','0001_initial','2019-08-07 06:12:04.460162'),(13,'admin','0002_logentry_remove_auto_add','2019-08-07 06:12:04.486350'),(14,'areas','0001_initial','2019-08-07 06:12:04.523106'),(15,'authtoken','0001_initial','2019-08-07 06:12:04.577569'),(16,'authtoken','0002_auto_20160226_1747','2019-08-07 06:12:04.659629'),(17,'user','0002_user_phone','2019-08-07 06:12:04.699807'),(18,'user','0003_auto_20190627_0626','2019-08-07 06:12:04.745692'),(19,'user','0004_user_active_email','2019-08-07 06:12:04.789319'),(20,'user','0005_address','2019-08-07 06:12:04.894568'),(21,'user','0006_image','2019-08-07 06:12:04.907575'),(22,'user','0007_auto_20190706_0311','2019-08-07 06:12:05.064965'),(23,'user','0008_address','2019-08-07 06:12:05.175886'),(24,'user','0009_auto_20190708_0633','2019-08-07 06:12:05.298569'),(25,'user','0010_auto_20190708_0635','2019-08-07 06:12:05.320699'),(26,'user','0011_auto_20190708_0649','2019-08-07 06:12:05.392951'),(27,'user','0012_auto_20190708_0654','2019-08-07 06:12:05.492239'),(28,'user','0013_auto_20190708_1134','2019-08-07 06:12:05.520461'),(29,'user','0014_library','2019-08-07 06:12:05.542266'),(30,'user','0015_auto_20190724_1121','2019-08-07 06:12:05.609807'),(31,'libraries','0001_initial','2019-08-07 06:12:05.625735'),(32,'libraries','0002_delete_librariesinfo','2019-08-07 06:12:05.637525'),(33,'libraries','0003_library','2019-08-07 06:12:05.722569'),(34,'libraries','0004_auto_20190708_1120','2019-08-07 06:12:05.744621'),(35,'libraries','0005_auto_20190708_1125','2019-08-07 06:12:05.762321'),(36,'user','0016_library_library','2019-08-07 06:12:05.825757'),(37,'user','0017_library_library_img','2019-08-07 06:12:05.889560'),(38,'user','0018_remove_library_library_img','2019-08-07 06:12:05.935596'),(39,'user','0019_auto_20190725_0657','2019-08-07 06:12:05.988429'),(40,'user','0020_auto_20190725_0700','2019-08-07 06:12:06.044619'),(41,'user','0021_auto_20190725_0724','2019-08-07 06:12:06.171374'),(42,'user','0022_remove_user_library','2019-08-07 06:12:06.218404'),(43,'user','0023_user_library','2019-08-07 06:12:06.280663'),(44,'user','0024_remove_user_library','2019-08-07 06:12:06.327602'),(45,'user','0025_user_library','2019-08-07 06:12:06.388740'),(46,'user','0026_remove_user_library','2019-08-07 06:12:06.441369'),(47,'user','0027_user_library','2019-08-07 06:12:06.509683'),(48,'user','0028_auto_20190725_0808','2019-08-07 06:12:06.564728'),(49,'user','0029_remove_user_library','2019-08-07 06:12:06.612623'),(50,'user','0030_collect_library','2019-08-07 06:12:06.688545'),(51,'user','0031_auto_20190730_1034','2019-08-07 06:12:06.736067'),(52,'libraries','0006_library_user_collect','2019-08-07 06:12:06.762632'),(53,'libraries','0007_libraryuser','2019-08-07 06:12:06.827584'),(54,'libraries','0008_auto_20190802_0353','2019-08-07 06:12:07.076930'),(55,'libraries','0009_libraryuser_is_library','2019-08-07 06:12:07.119209'),(56,'libraries','0010_remove_libraryuser_is_library','2019-08-07 06:12:07.155606'),(57,'libraries','0011_auto_20190802_1029','2019-08-07 06:12:07.188966'),(58,'libraries','0012_auto_20190802_1050','2019-08-07 06:12:07.266827'),(59,'libraries','0013_auto_20190802_1214','2019-08-07 06:12:07.298943'),(60,'libraries','0014_auto_20190805_0718','2019-08-07 06:12:07.389000'),(61,'libraries','0015_auto_20190807_0611','2019-08-07 06:12:07.483163'),(62,'sessions','0001_initial','2019-08-07 06:12:07.519866'),(63,'user','0032_user_is_library','2019-08-07 06:12:07.566268'),(64,'user','0033_auto_20190803_0401','2019-08-07 06:12:07.704238'),(65,'libraries','0016_auto_20190808_0152','2019-08-08 01:52:35.731774'),(66,'libraries','0017_auto_20190808_0201','2019-08-08 02:01:04.920345'),(67,'libraries','0018_library_page_mode_id','2019-08-08 03:46:40.039286'),(68,'libraries','0019_imgsave','2019-08-08 05:55:47.522739'),(69,'libraries','0020_auto_20190809_0557','2019-08-09 05:57:23.182793'),(70,'libraries','0021_auto_20190809_0706','2019-08-09 07:06:44.115043'),(71,'libraries','0022_library_explore_time','2019-08-12 10:18:40.203819'),(72,'libraries','0023_auto_20190812_1106','2019-08-12 11:06:12.766948'),(73,'user','0034_auto_20190814_0208','2019-08-14 02:08:48.550694');
/*!40000 ALTER TABLE `django_migrations` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_session`
--

DROP TABLE IF EXISTS `django_session`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime(6) NOT NULL,
  PRIMARY KEY (`session_key`),
  KEY `django_session_expire_date_a5c62663` (`expire_date`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_session`
--

LOCK TABLES `django_session` WRITE;
/*!40000 ALTER TABLE `django_session` DISABLE KEYS */;
/*!40000 ALTER TABLE `django_session` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `gw_user`
--

DROP TABLE IF EXISTS `gw_user`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `gw_user` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `password` varchar(128) NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(150) NOT NULL,
  `first_name` varchar(30) NOT NULL,
  `last_name` varchar(30) NOT NULL,
  `email` varchar(254) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL,
  `phone` varchar(11) NOT NULL,
  `active_email` tinyint(1) NOT NULL,
  `img_url` varchar(100) NOT NULL,
  `is_library` tinyint(1) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`),
  UNIQUE KEY `phone` (`phone`)
) ENGINE=InnoDB AUTO_INCREMENT=17 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `gw_user`
--

LOCK TABLES `gw_user` WRITE;
/*!40000 ALTER TABLE `gw_user` DISABLE KEYS */;
INSERT INTO `gw_user` VALUES (1,'pbkdf2_sha256$36000$pDqpSvMVbTpn$w05eQ3FCcxMbO/v3MSjJnDtnRYukXMtVhJyJedVKHgQ=','2019-08-07 06:14:20.841649',1,'muzhenyu','','','lvbu89757@163.com',1,1,'2019-08-07 06:14:04.064939','',0,'',0),(5,'shu18291124520',NULL,0,'Mzy1009m','','','lvbu89757@163.com',0,1,'2019-08-08 01:00:47.000000','13806782811',0,'group1/M00/00/02/wKjTiV1TbM2AZB2bAAANkt5fqtM4440190',0),(13,'shu18291124520',NULL,0,'lvbu89757','','','lvbu89757@163.com',0,1,'2019-08-09 07:50:04.000000','13806782813',0,'group1/M00/00/02/wKjTiV1TbM2AZB2bAAANkt5fqtM4440190',1),(14,'shu18291124520',NULL,0,'shu18291124520','','','lvbu89757@163.com',0,1,'2019-08-09 07:55:48.000000','13806782812',0,'group1/M00/00/02/wKjTiV1TbM2AZB2bAAANkt5fqtM4440190',1),(15,'shu18291124520',NULL,0,'13806782813','','','lvbu89757@163.com',0,1,'2019-08-09 08:29:19.000000','13806782810',0,'group1/M00/00/02/wKjTiV1TbM2AZB2bAAANkt5fqtM4440190',0),(16,'shu18291124520',NULL,0,'muzhenyu1','','','lvbu89757@163.com',0,1,'2019-08-09 11:04:22.000000','13806782800',0,'group1/M00/00/02/wKjTiV1TbM2AZB2bAAANkt5fqtM4440190',1);
/*!40000 ALTER TABLE `gw_user` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `gw_user_groups`
--

DROP TABLE IF EXISTS `gw_user_groups`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `gw_user_groups` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `group_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `user_user_groups_user_id_group_id_bb60391f_uniq` (`user_id`,`group_id`),
  KEY `user_user_groups_group_id_c57f13c0_fk_auth_group_id` (`group_id`),
  CONSTRAINT `user_user_groups_group_id_c57f13c0_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  CONSTRAINT `user_user_groups_user_id_13f9a20d_fk_user_user_id` FOREIGN KEY (`user_id`) REFERENCES `gw_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `gw_user_groups`
--

LOCK TABLES `gw_user_groups` WRITE;
/*!40000 ALTER TABLE `gw_user_groups` DISABLE KEYS */;
/*!40000 ALTER TABLE `gw_user_groups` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `gw_user_user_permissions`
--

DROP TABLE IF EXISTS `gw_user_user_permissions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `gw_user_user_permissions` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `user_user_user_permissions_user_id_permission_id_64f4d5b8_uniq` (`user_id`,`permission_id`),
  KEY `user_user_user_permi_permission_id_ce49d4de_fk_auth_perm` (`permission_id`),
  CONSTRAINT `user_user_user_permi_permission_id_ce49d4de_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `user_user_user_permissions_user_id_31782f58_fk_user_user_id` FOREIGN KEY (`user_id`) REFERENCES `gw_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `gw_user_user_permissions`
--

LOCK TABLES `gw_user_user_permissions` WRITE;
/*!40000 ALTER TABLE `gw_user_user_permissions` DISABLE KEYS */;
/*!40000 ALTER TABLE `gw_user_user_permissions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `hermit_user_address`
--

DROP TABLE IF EXISTS `hermit_user_address`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `hermit_user_address` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `is_delete` tinyint(1) NOT NULL,
  `user_id` int(11) NOT NULL,
  `district_id` int(11) NOT NULL,
  `street_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `shanghui_user_address_user_id_a2c9a008_fk_gw_user_id` (`user_id`),
  KEY `hermit_user_address_district_id_9991aedc_fk_areas_id` (`district_id`),
  KEY `hermit_user_address_street_id_35627983_fk_areas_id` (`street_id`),
  CONSTRAINT `hermit_user_address_district_id_9991aedc_fk_areas_id` FOREIGN KEY (`district_id`) REFERENCES `areas` (`id`),
  CONSTRAINT `hermit_user_address_street_id_35627983_fk_areas_id` FOREIGN KEY (`street_id`) REFERENCES `areas` (`id`),
  CONSTRAINT `shanghui_user_address_user_id_a2c9a008_fk_gw_user_id` FOREIGN KEY (`user_id`) REFERENCES `gw_user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `hermit_user_address`
--

LOCK TABLES `hermit_user_address` WRITE;
/*!40000 ALTER TABLE `hermit_user_address` DISABLE KEYS */;
INSERT INTO `hermit_user_address` VALUES (1,0,15,330103,330103003);
/*!40000 ALTER TABLE `hermit_user_address` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `libraries`
--

DROP TABLE IF EXISTS `libraries`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `libraries` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(20) NOT NULL,
  `grade` double NOT NULL,
  `lib_commit` varchar(300) NOT NULL,
  `district_id` int(11) NOT NULL,
  `street_id` int(11) NOT NULL,
  `lib_img_url` varchar(100) DEFAULT NULL,
  `lib_license_url` varchar(100) NOT NULL,
  `detail_address` varchar(200) NOT NULL,
  `price` double NOT NULL,
  `type` int(11) DEFAULT NULL,
  `lib_info_url` varchar(100) NOT NULL,
  `page_mode_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`),
  KEY `libraries_library_district_id_bba16c32_fk_areas_id` (`district_id`),
  KEY `libraries_library_street_id_1541fde1_fk_areas_id` (`street_id`),
  CONSTRAINT `libraries_library_district_id_bba16c32_fk_areas_id` FOREIGN KEY (`district_id`) REFERENCES `areas` (`id`),
  CONSTRAINT `libraries_library_street_id_1541fde1_fk_areas_id` FOREIGN KEY (`street_id`) REFERENCES `areas` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=14 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `libraries`
--

LOCK TABLES `libraries` WRITE;
/*!40000 ALTER TABLE `libraries` DISABLE KEYS */;
INSERT INTO `libraries` VALUES (11,'shuwu',7.5,'xzdwadwa',330102,330102004,'group1/M00/00/02/wKjTh11NJlSAD1ysAAcWIldZHGQ1028646','group1/M00/00/02/wKjTh11NJlSAdMqSAAAfDlg7vfw9083693','sadwadwa',0,1,'shuwu.html',1),(12,'dadsadw',8,'xczwadw',330105,330105004,'group1/M00/00/02/wKjTh11NJyaAT81XAAAfDlg7vfw7742383','group1/M00/00/02/wKjTh11NJyaAWfh6AAcWIldZHGQ5697562','cxzdsad',60,1,'dadsadw.html',1),(13,'muzhenyu',0,'xzccawd',330105,330105008,'group1/M00/00/02/wKjTh11NU4WAHqIlAAX8eOFewpM1240600','group1/M00/00/02/wKjTh11NU4WARoQXAAClwxE36W80435674','ncagjuuihda',40,2,'muzhenyu.html',1);
/*!40000 ALTER TABLE `libraries` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `libraries_explore_time`
--

DROP TABLE IF EXISTS `libraries_explore_time`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `libraries_explore_time` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `library_id` int(11) NOT NULL,
  `explore_data_time` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=90 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `libraries_explore_time`
--

LOCK TABLES `libraries_explore_time` WRITE;
/*!40000 ALTER TABLE `libraries_explore_time` DISABLE KEYS */;
INSERT INTO `libraries_explore_time` VALUES (2,12,'2019-09-10 02:48:36.000000'),(3,12,'2019-07-17 02:49:03.000000'),(4,12,'2019-08-13 02:52:41.840105'),(5,12,'2019-08-13 02:52:56.208340'),(6,12,'2019-08-13 02:55:41.793459'),(7,12,'2019-08-13 02:56:47.081446'),(8,12,'2019-08-13 03:06:09.455644'),(9,12,'2019-08-13 03:06:43.997008'),(10,12,'2019-08-13 03:08:33.562380'),(11,12,'2019-08-13 03:12:17.656066'),(12,11,'2019-08-13 07:06:31.901687'),(13,11,'2019-08-13 07:06:39.200949'),(14,11,'2019-08-13 07:07:08.780811'),(15,12,'2019-08-13 07:07:21.126065'),(16,13,'2019-08-13 07:07:31.946566'),(17,11,'2019-08-13 07:08:28.401076'),(18,13,'2019-08-13 07:08:42.817578'),(19,12,'2019-08-13 07:08:55.081081'),(20,13,'2019-08-13 07:09:02.237301'),(21,11,'2019-08-13 07:09:30.368426'),(22,13,'2019-08-13 07:09:41.167551'),(23,13,'2019-08-13 07:09:43.981026'),(24,13,'2019-08-13 07:41:26.368620'),(25,13,'2019-08-13 07:42:39.630533'),(26,13,'2019-08-13 07:43:19.524300'),(27,13,'2019-08-13 07:43:59.937956'),(28,13,'2019-08-13 07:44:55.158899'),(29,11,'2019-08-13 08:44:11.491481'),(30,11,'2019-08-13 11:18:38.786992'),(31,11,'2019-08-13 11:19:34.605054'),(32,11,'2019-08-13 11:29:54.794676'),(33,11,'2019-08-13 11:31:06.576156'),(34,11,'2019-08-13 11:33:08.926072'),(35,11,'2019-08-13 11:34:38.308016'),(36,11,'2019-08-13 11:37:26.729453'),(37,11,'2019-08-13 11:41:35.785082'),(38,11,'2019-08-13 11:44:40.961408'),(39,11,'2019-08-13 11:46:30.243484'),(40,11,'2019-08-13 11:46:55.991661'),(41,11,'2019-08-13 11:49:00.969193'),(42,11,'2019-08-13 11:52:20.895893'),(43,11,'2019-08-13 11:53:08.386836'),(44,11,'2019-08-13 11:53:44.162369'),(45,11,'2019-08-13 11:57:59.633632'),(46,11,'2019-08-13 11:59:06.837049'),(47,11,'2019-08-13 12:01:33.510473'),(48,11,'2019-08-13 12:01:51.371652'),(49,11,'2019-08-13 12:02:46.499692'),(50,11,'2019-08-13 12:05:24.013380'),(51,11,'2019-08-13 12:05:44.610290'),(52,11,'2019-08-13 12:10:11.774666'),(53,11,'2019-08-13 12:10:33.578169'),(54,11,'2019-08-13 12:12:13.313046'),(55,11,'2019-08-13 12:15:12.687212'),(56,11,'2019-08-13 12:15:29.201559'),(57,11,'2019-08-13 12:19:41.684411'),(58,11,'2019-08-13 12:20:09.891400'),(59,11,'2019-08-13 12:22:49.123675'),(60,11,'2019-08-13 12:23:15.911588'),(61,11,'2019-08-13 12:23:47.730339'),(62,11,'2019-08-13 12:24:41.837768'),(63,11,'2019-08-13 12:26:22.504828'),(64,11,'2019-08-13 12:30:21.537227'),(65,11,'2019-08-13 12:30:47.380393'),(66,11,'2019-08-14 00:33:08.510924'),(67,11,'2019-08-14 07:00:17.389794'),(68,11,'2019-08-14 07:00:54.597445'),(69,11,'2019-08-14 07:02:37.827457'),(70,3,'2019-08-19 06:56:12.000000'),(71,11,'2019-08-19 06:57:16.540904'),(72,12,'2019-08-20 00:50:01.716282'),(73,12,'2019-08-20 00:50:12.339448'),(74,12,'2019-08-20 00:53:04.223254'),(75,12,'2019-08-20 00:53:56.950482'),(76,12,'2019-08-20 00:56:20.716392'),(77,12,'2019-08-20 00:58:50.578360'),(78,12,'2019-08-20 00:59:11.102962'),(79,12,'2019-08-20 01:00:02.923995'),(80,12,'2019-08-20 01:00:57.161578'),(81,12,'2019-08-20 01:01:38.457407'),(82,12,'2019-08-20 01:06:05.143885'),(83,11,'2019-08-20 01:06:09.998705'),(84,11,'2019-08-20 01:06:14.855911'),(85,13,'2019-08-20 01:06:19.926685'),(86,12,'2019-08-20 01:09:21.636597'),(87,13,'2019-08-20 01:09:26.889714'),(88,12,'2019-08-20 01:44:46.356894'),(89,12,'2019-08-20 01:46:56.074124');
/*!40000 ALTER TABLE `libraries_explore_time` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `libraries_imglist`
--

DROP TABLE IF EXISTS `libraries_imglist`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `libraries_imglist` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `library_id` int(11) NOT NULL,
  `img_url` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `libraries_imglist`
--

LOCK TABLES `libraries_imglist` WRITE;
/*!40000 ALTER TABLE `libraries_imglist` DISABLE KEYS */;
/*!40000 ALTER TABLE `libraries_imglist` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `libraries_imgsave`
--

DROP TABLE IF EXISTS `libraries_imgsave`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `libraries_imgsave` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `img` varchar(100) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `libraries_imgsave`
--

LOCK TABLES `libraries_imgsave` WRITE;
/*!40000 ALTER TABLE `libraries_imgsave` DISABLE KEYS */;
INSERT INTO `libraries_imgsave` VALUES (1,'group1/M00/00/01/wKjTh11LufWAYBh2AAX8eOFewpM5627474'),(2,'group1/M00/00/02/wKjTiV1TbM2AZB2bAAANkt5fqtM4440190'),(3,'group1/M00/00/02/wKjTiV1aSb-APFkRAAcWIldZHGQ0475051'),(4,'group1/M00/00/02/wKjTil1b4-GAItaJAAcWIldZHGQ7368633');
/*!40000 ALTER TABLE `libraries_imgsave` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `libraries_library_detail_info_page_model`
--

DROP TABLE IF EXISTS `libraries_library_detail_info_page_model`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `libraries_library_detail_info_page_model` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `page_model_views_url` varchar(100) NOT NULL,
  `page_model` varchar(100) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `libraries_library_detail_info_page_model`
--

LOCK TABLES `libraries_library_detail_info_page_model` WRITE;
/*!40000 ALTER TABLE `libraries_library_detail_info_page_model` DISABLE KEYS */;
INSERT INTO `libraries_library_detail_info_page_model` VALUES (1,'group1/M00/00/01/wKjTh11LufWAYBh2AAX8eOFewpM5627474','group1/M00/00/02/wKjTiV1bRuuAeu1DAAGjzURk3eY3352437');
/*!40000 ALTER TABLE `libraries_library_detail_info_page_model` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `libraries_libraryuser`
--

DROP TABLE IF EXISTS `libraries_libraryuser`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `libraries_libraryuser` (
  `user_ptr_id` int(11) NOT NULL,
  `own_library_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`user_ptr_id`),
  UNIQUE KEY `own_library_id` (`own_library_id`),
  CONSTRAINT `libraries_libraryuser_own_library_id_377b24f5_fk_libraries_id` FOREIGN KEY (`own_library_id`) REFERENCES `libraries` (`id`),
  CONSTRAINT `libraries_libraryuser_user_ptr_id_c749761e_fk_gw_user_id` FOREIGN KEY (`user_ptr_id`) REFERENCES `gw_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `libraries_libraryuser`
--

LOCK TABLES `libraries_libraryuser` WRITE;
/*!40000 ALTER TABLE `libraries_libraryuser` DISABLE KEYS */;
INSERT INTO `libraries_libraryuser` VALUES (13,11),(14,12),(16,13);
/*!40000 ALTER TABLE `libraries_libraryuser` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `libraries_libtype`
--

DROP TABLE IF EXISTS `libraries_libtype`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `libraries_libtype` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `type_name` varchar(15) NOT NULL,
  `type_description` varchar(200) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `type_name` (`type_name`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `libraries_libtype`
--

LOCK TABLES `libraries_libtype` WRITE;
/*!40000 ALTER TABLE `libraries_libtype` DISABLE KEYS */;
INSERT INTO `libraries_libtype` VALUES (1,'娱乐书屋','有娱乐气氛的书店'),(2,'专业书店','非常专业的书店');
/*!40000 ALTER TABLE `libraries_libtype` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `libraries_usercomment`
--

DROP TABLE IF EXISTS `libraries_usercomment`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `libraries_usercomment` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `library_id` int(11) NOT NULL,
  `user_id` int(11) NOT NULL,
  `User_comment` varchar(500) NOT NULL,
  `User_grade` int(11) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=9 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `libraries_usercomment`
--

LOCK TABLES `libraries_usercomment` WRITE;
/*!40000 ALTER TABLE `libraries_usercomment` DISABLE KEYS */;
INSERT INTO `libraries_usercomment` VALUES (6,12,16,'xdwadwadw',8),(7,11,13,'sadwafedwa',7),(8,11,13,'dawdwafsadwadwa',8);
/*!40000 ALTER TABLE `libraries_usercomment` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `user_collect_library`
--

DROP TABLE IF EXISTS `user_collect_library`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `user_collect_library` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `library_id` int(11) NOT NULL,
  `user_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `user_collect_library_library_id_4f897974_fk_libraries_id` (`library_id`),
  KEY `user_collect_library_user_id_6874324e_fk_gw_user_id` (`user_id`),
  CONSTRAINT `user_collect_library_library_id_4f897974_fk_libraries_id` FOREIGN KEY (`library_id`) REFERENCES `libraries` (`id`),
  CONSTRAINT `user_collect_library_user_id_6874324e_fk_gw_user_id` FOREIGN KEY (`user_id`) REFERENCES `gw_user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=16 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `user_collect_library`
--

LOCK TABLES `user_collect_library` WRITE;
/*!40000 ALTER TABLE `user_collect_library` DISABLE KEYS */;
INSERT INTO `user_collect_library` VALUES (13,11,15),(14,12,16),(15,12,13);
/*!40000 ALTER TABLE `user_collect_library` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2019-08-26  8:53:30
