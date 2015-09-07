/*
SQLyog Ultimate v12.09 (64 bit)
MySQL - 5.5.43-0ubuntu0.14.04.1 : Database - router04
*********************************************************************
*/

/*!40101 SET NAMES utf8 */;

/*!40101 SET SQL_MODE=''*/;

/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;
CREATE DATABASE /*!32312 IF NOT EXISTS*/`router04` /*!40100 DEFAULT CHARACTER SET utf8 */;

USE `router04`;

/*Table structure for table `model_paths` */

DROP TABLE IF EXISTS `model_paths`;

CREATE TABLE `model_paths` (
  `id` int(10) unsigned NOT NULL AUTO_INCREMENT,
  `model_name` varchar(255) NOT NULL,
  `server_name` varchar(255) NOT NULL,
  `host` varchar(255) NOT NULL DEFAULT '',
  `path` varchar(255) NOT NULL,
  `created_at` datetime DEFAULT NULL,
  `updated_at` datetime DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `model_name` (`model_name`)
) ENGINE=InnoDB AUTO_INCREMENT=50 DEFAULT CHARSET=utf8 ROW_FORMAT=DYNAMIC;

/*Data for the table `model_paths` */

insert  into `model_paths`(`id`,`model_name`,`server_name`,`host`,`path`,`created_at`,`updated_at`) values (1,'couriers','api_server','http://127.0.0.1:3329','/api/v2','2015-05-28 08:06:11','2015-06-01 07:25:52');
insert  into `model_paths`(`id`,`model_name`,`server_name`,`host`,`path`,`created_at`,`updated_at`) values (2,'orders','api_server','http://127.0.0.1:3329','/api/v2','2015-05-28 08:06:11','2015-06-01 07:25:52');
insert  into `model_paths`(`id`,`model_name`,`server_name`,`host`,`path`,`created_at`,`updated_at`) values (3,'cities','api_server','http://127.0.0.1:3329','/api/v2','2015-05-28 08:06:11','2015-06-01 07:25:52');
insert  into `model_paths`(`id`,`model_name`,`server_name`,`host`,`path`,`created_at`,`updated_at`) values (4,'service_categories','api_server','http://127.0.0.1:3329','/api/v2','2015-05-28 08:06:11','2015-06-01 07:25:52');
insert  into `model_paths`(`id`,`model_name`,`server_name`,`host`,`path`,`created_at`,`updated_at`) values (5,'supplier_goods','api_server','http://127.0.0.1:3329','/api/v2','2015-05-28 08:06:11','2015-06-01 07:25:52');
insert  into `model_paths`(`id`,`model_name`,`server_name`,`host`,`path`,`created_at`,`updated_at`) values (6,'service_goods','api_server','http://127.0.0.1:3329','/api/v2','2015-05-28 08:06:11','2015-06-01 07:25:52');
insert  into `model_paths`(`id`,`model_name`,`server_name`,`host`,`path`,`created_at`,`updated_at`) values (7,'delivery_fee_settings','api_server','http://127.0.0.1:3329','/api/v2','2015-05-28 08:06:11','2015-06-01 07:25:52');
insert  into `model_paths`(`id`,`model_name`,`server_name`,`host`,`path`,`created_at`,`updated_at`) values (8,'order_good_details','api_server','http://127.0.0.1:3329','/api/v2','2015-05-28 08:06:11','2015-06-01 07:25:52');
insert  into `model_paths`(`id`,`model_name`,`server_name`,`host`,`path`,`created_at`,`updated_at`) values (9,'trans_tasks','api_server','http://127.0.0.1:3329','/api/v2','2015-05-28 08:06:11','2015-06-01 07:25:52');
insert  into `model_paths`(`id`,`model_name`,`server_name`,`host`,`path`,`created_at`,`updated_at`) values (19,'order_tips','ops_server','http://ops06.edaixi.cn:81','/api/v1','2015-05-29 09:28:48','2015-08-18 08:08:54');
insert  into `model_paths`(`id`,`model_name`,`server_name`,`host`,`path`,`created_at`,`updated_at`) values (20,'yiwu_constants','api_server','http://127.0.0.1:3329','/api/v2','2015-06-10 01:55:32','2015-06-10 01:55:32');
insert  into `model_paths`(`id`,`model_name`,`server_name`,`host`,`path`,`created_at`,`updated_at`) values (21,'wash_prices','api_server','http://127.0.0.1:3329','/api/v2','2015-06-11 07:44:10','2015-06-11 07:44:10');
insert  into `model_paths`(`id`,`model_name`,`server_name`,`host`,`path`,`created_at`,`updated_at`) values (22,'fans','api_server','http://127.0.0.1:3329','/api/v2','2015-06-11 07:44:10','2015-06-11 07:44:10');
insert  into `model_paths`(`id`,`model_name`,`server_name`,`host`,`path`,`created_at`,`updated_at`) values (23,'addresses','api_server','http://127.0.0.1:3329','/api/v2','2015-06-18 02:47:42','2015-06-18 02:47:42');
insert  into `model_paths`(`id`,`model_name`,`server_name`,`host`,`path`,`created_at`,`updated_at`) values (24,'outlets','api_server','http://127.0.0.1:3329','/api/v2','2015-06-18 02:47:42','2015-06-18 02:47:42');
insert  into `model_paths`(`id`,`model_name`,`server_name`,`host`,`path`,`created_at`,`updated_at`) values (25,'areas','api_server','http://127.0.0.1:3329','/api/v2','2015-06-18 10:43:40','2015-06-18 10:43:40');
insert  into `model_paths`(`id`,`model_name`,`server_name`,`host`,`path`,`created_at`,`updated_at`) values (26,'extra_accounts','api_server','http://127.0.0.1:3329','/api/v2','2015-07-30 04:37:01','2015-07-30 04:37:01');
insert  into `model_paths`(`id`,`model_name`,`server_name`,`host`,`path`,`created_at`,`updated_at`) values (27,'outlet_rules','api_server','http://127.0.0.1:3329','/api/v2','2015-07-30 04:37:01','2015-07-30 04:37:01');
insert  into `model_paths`(`id`,`model_name`,`server_name`,`host`,`path`,`created_at`,`updated_at`) values (28,'outlet_order_cleanings','caiwu_server','http://caiwu06.edaixi.cn:81','/api/v1','2015-07-30 04:37:01','2015-08-31 09:13:36');
insert  into `model_paths`(`id`,`model_name`,`server_name`,`host`,`path`,`created_at`,`updated_at`) values (29,'outlet_order_cleaning_details','caiwu_server','http://caiwu06.edaixi.cn:81','/api/v1','2015-07-30 04:37:01','2015-08-31 09:13:36');
insert  into `model_paths`(`id`,`model_name`,`server_name`,`host`,`path`,`created_at`,`updated_at`) values (30,'outlet_capacities','api_server','http://127.0.0.1:3329','/api/v2','2015-08-17 06:48:26','2015-08-17 06:48:26');
insert  into `model_paths`(`id`,`model_name`,`server_name`,`host`,`path`,`created_at`,`updated_at`) values (31,'banners','ops_server','http://ops06.edaixi.cn:81','/api/v1','2015-08-17 06:49:44','2015-08-18 08:08:54');
insert  into `model_paths`(`id`,`model_name`,`server_name`,`host`,`path`,`created_at`,`updated_at`) values (34,'maps','ops_server','http://ops06.edaixi.cn:81','/api/v1','2015-08-18 08:08:54','2015-08-18 08:08:54');
insert  into `model_paths`(`id`,`model_name`,`server_name`,`host`,`path`,`created_at`,`updated_at`) values (35,'tips','ops_server','http://ops06.edaixi.cn:81','/api/v1','2015-08-20 09:30:14','2015-08-20 09:30:14');
insert  into `model_paths`(`id`,`model_name`,`server_name`,`host`,`path`,`created_at`,`updated_at`) values (36,'order_complaints','kefu_server','http://kefu06.edaixi.cn:81','/api/v2','2015-08-20 10:41:32','2015-08-20 10:41:32');
insert  into `model_paths`(`id`,`model_name`,`server_name`,`host`,`path`,`created_at`,`updated_at`) values (37,'courier_invitees','api_server','http://127.0.0.1:3329','/api/v2','2015-08-20 11:01:35','2015-08-20 11:01:35');
insert  into `model_paths`(`id`,`model_name`,`server_name`,`host`,`path`,`created_at`,`updated_at`) values (38,'trans_groups','api_server','http://127.0.0.1:3329','/api/v2','2015-08-20 11:01:35','2015-08-20 11:01:35');
insert  into `model_paths`(`id`,`model_name`,`server_name`,`host`,`path`,`created_at`,`updated_at`) values (39,'outlet_versions','ops_server','http://ops06.edaixi.cn:81','/api/v1','2015-08-27 07:56:03','2015-08-27 07:56:03');
insert  into `model_paths`(`id`,`model_name`,`server_name`,`host`,`path`,`created_at`,`updated_at`) values (40,'outlet_updates','ops_server','http://ops06.edaixi.cn:81','/api/v1','2015-08-27 07:56:03','2015-08-27 07:56:03');
insert  into `model_paths`(`id`,`model_name`,`server_name`,`host`,`path`,`created_at`,`updated_at`) values (41,'outlet_grays','ops_server','http://ops06.edaixi.cn:81','/api/v1','2015-08-27 07:56:03','2015-08-27 07:56:03');
insert  into `model_paths`(`id`,`model_name`,`server_name`,`host`,`path`,`created_at`,`updated_at`) values (44,'extra_cleaning_details','caiwu_server','http://caiwu06.edaixi.cn:81','/api/v1','2015-08-27 11:12:10','2015-08-27 11:12:10');
insert  into `model_paths`(`id`,`model_name`,`server_name`,`host`,`path`,`created_at`,`updated_at`) values (47,'comment_options','api_server','http://127.0.0.1:3329','/api/v2','2015-08-27 13:57:16','2015-08-27 13:57:16');

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;
