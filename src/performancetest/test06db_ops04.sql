/*
SQLyog Ultimate v12.09 (64 bit)
MySQL - 5.5.43-0ubuntu0.14.04.1 : Database - ops04
*********************************************************************
*/

/*!40101 SET NAMES utf8 */;

/*!40101 SET SQL_MODE=''*/;

/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;
CREATE DATABASE /*!32312 IF NOT EXISTS*/`ops04` /*!40100 DEFAULT CHARACTER SET utf8 */;

USE `ops04`;

/*Table structure for table `banner_cities` */

DROP TABLE IF EXISTS `banner_cities`;

CREATE TABLE `banner_cities` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `city_name` varchar(255) DEFAULT NULL,
  `banner_id` int(11) DEFAULT NULL,
  `created_at` datetime DEFAULT NULL,
  `updated_at` datetime DEFAULT NULL,
  `serial_index` int(11) DEFAULT NULL,
  `city_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `index_banner_cities_on_city_name` (`city_name`),
  KEY `index_banner_cities_on_city_id_and_serial_index` (`city_id`,`serial_index`)
) ENGINE=InnoDB AUTO_INCREMENT=75 DEFAULT CHARSET=utf8 ROW_FORMAT=DYNAMIC;

/*Table structure for table `banners` */

DROP TABLE IF EXISTS `banners`;

CREATE TABLE `banners` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `description` varchar(255) DEFAULT NULL,
  `created_at` datetime DEFAULT NULL,
  `updated_at` datetime DEFAULT NULL,
  `ios_file_name` varchar(255) DEFAULT NULL,
  `ios_content_type` varchar(255) DEFAULT NULL,
  `ios_file_size` int(11) DEFAULT NULL,
  `ios_updated_at` datetime DEFAULT NULL,
  `is_active` tinyint(1) DEFAULT '1',
  `title` varchar(255) DEFAULT NULL,
  `banner_type` int(11) DEFAULT '0',
  `android_file_name` varchar(255) DEFAULT NULL,
  `android_content_type` varchar(255) DEFAULT NULL,
  `android_file_size` int(11) DEFAULT NULL,
  `android_updated_at` datetime DEFAULT NULL,
  `web_file_name` varchar(255) DEFAULT NULL,
  `web_content_type` varchar(255) DEFAULT NULL,
  `web_file_size` int(11) DEFAULT NULL,
  `web_updated_at` datetime DEFAULT NULL,
  `website` varchar(500) DEFAULT NULL,
  `website_type` int(11) DEFAULT NULL,
  `url_type` varchar(255) DEFAULT NULL,
  `inner_type` int(11) DEFAULT NULL,
  `inner_url` varchar(255) DEFAULT NULL,
  `inner_title` varchar(255) DEFAULT NULL,
  `tips` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `index_banners_on_is_active` (`is_active`)
) ENGINE=InnoDB AUTO_INCREMENT=107 DEFAULT CHARSET=utf8 ROW_FORMAT=DYNAMIC;

/*Table structure for table `city_in_charges` */

DROP TABLE IF EXISTS `city_in_charges`;

CREATE TABLE `city_in_charges` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `city_name` varchar(255) DEFAULT NULL,
  `worker_id` int(11) DEFAULT NULL,
  `created_at` datetime DEFAULT NULL,
  `updated_at` datetime DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `index_city_in_charges_on_worker_id` (`worker_id`)
) ENGINE=InnoDB AUTO_INCREMENT=71 DEFAULT CHARSET=utf8 ROW_FORMAT=DYNAMIC;

/*Table structure for table `city_lists` */

DROP TABLE IF EXISTS `city_lists`;

CREATE TABLE `city_lists` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `initial` varchar(255) DEFAULT NULL,
  `initials` varchar(255) DEFAULT NULL,
  `pinyin` varchar(255) DEFAULT NULL,
  `parent_id` int(11) DEFAULT NULL,
  `name` varchar(255) DEFAULT NULL,
  `zip_code` varchar(255) DEFAULT NULL,
  `gaode_code` varchar(255) DEFAULT NULL,
  `name_alias` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3166 DEFAULT CHARSET=utf8;

/*Table structure for table `maps` */

DROP TABLE IF EXISTS `maps`;

CREATE TABLE `maps` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `title` varchar(255) DEFAULT NULL,
  `description` varchar(255) DEFAULT NULL,
  `is_active` int(11) DEFAULT NULL,
  `city_id` int(11) DEFAULT NULL,
  `top_file_name` varchar(255) DEFAULT NULL,
  `top_content_type` varchar(255) DEFAULT NULL,
  `top_file_size` int(11) DEFAULT NULL,
  `top_updated_at` datetime DEFAULT NULL,
  `ios_file_name` varchar(255) DEFAULT NULL,
  `ios_content_type` varchar(255) DEFAULT NULL,
  `ios_file_size` int(11) DEFAULT NULL,
  `ios_updated_at` datetime DEFAULT NULL,
  `android_file_name` varchar(255) DEFAULT NULL,
  `android_content_type` varchar(255) DEFAULT NULL,
  `android_file_size` int(11) DEFAULT NULL,
  `android_updated_at` datetime DEFAULT NULL,
  `web_file_name` varchar(255) DEFAULT NULL,
  `web_content_type` varchar(255) DEFAULT NULL,
  `web_file_size` int(11) DEFAULT NULL,
  `web_updated_at` datetime DEFAULT NULL,
  `worker_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=9 DEFAULT CHARSET=utf8;

/*Table structure for table `mobile_template_cities` */

DROP TABLE IF EXISTS `mobile_template_cities`;

CREATE TABLE `mobile_template_cities` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `city_name` varchar(255) DEFAULT NULL,
  `mobile_template_id` int(11) DEFAULT NULL,
  `created_at` datetime DEFAULT NULL,
  `updated_at` datetime DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `index_mobile_template_cities_on_city_name` (`city_name`)
) ENGINE=InnoDB AUTO_INCREMENT=39 DEFAULT CHARSET=utf8 ROW_FORMAT=DYNAMIC;

/*Table structure for table `mobile_templates` */

DROP TABLE IF EXISTS `mobile_templates`;

CREATE TABLE `mobile_templates` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `title` varchar(255) DEFAULT NULL,
  `banner_ids` varchar(255) DEFAULT NULL,
  `func_button_ids` varchar(255) DEFAULT NULL,
  `is_active` tinyint(1) DEFAULT NULL,
  `created_at` datetime DEFAULT NULL,
  `updated_at` datetime DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=27 DEFAULT CHARSET=utf8 ROW_FORMAT=DYNAMIC;

/*Table structure for table `order_tips` */

DROP TABLE IF EXISTS `order_tips`;

CREATE TABLE `order_tips` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `city_id` int(11) DEFAULT NULL,
  `content` varchar(255) DEFAULT NULL,
  `start_time` date DEFAULT NULL,
  `end_time` date DEFAULT NULL,
  `status` varchar(255) DEFAULT NULL,
  `worker_id` int(11) DEFAULT NULL,
  `ori_id` int(11) DEFAULT NULL,
  `is_deleted` int(11) DEFAULT '0',
  `created_at` datetime DEFAULT NULL,
  `updated_at` datetime DEFAULT NULL,
  `category_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8 ROW_FORMAT=DYNAMIC;

/*Table structure for table `outlet_grays` */

DROP TABLE IF EXISTS `outlet_grays`;

CREATE TABLE `outlet_grays` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `outlet_id` varchar(255) DEFAULT NULL,
  `title` varchar(255) DEFAULT NULL,
  `created_at` datetime DEFAULT NULL,
  `updated_at` datetime DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

/*Table structure for table `outlet_updates` */

DROP TABLE IF EXISTS `outlet_updates`;

CREATE TABLE `outlet_updates` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `version` varchar(255) DEFAULT NULL,
  `version_type` int(11) DEFAULT NULL,
  `zip_file_name` varchar(255) DEFAULT NULL,
  `zip_content_type` varchar(255) DEFAULT NULL,
  `zip_file_size` int(11) DEFAULT NULL,
  `zip_updated_at` datetime DEFAULT NULL,
  `is_new` tinyint(1) DEFAULT NULL,
  `zip_hash` varchar(255) DEFAULT NULL,
  `created_at` datetime DEFAULT NULL,
  `updated_at` datetime DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

/*Table structure for table `outlet_versions` */

DROP TABLE IF EXISTS `outlet_versions`;

CREATE TABLE `outlet_versions` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `outlet_id` varchar(255) DEFAULT NULL,
  `title` varchar(255) DEFAULT NULL,
  `version_type` int(11) DEFAULT NULL,
  `version` varchar(255) DEFAULT NULL,
  `city` varchar(255) DEFAULT NULL,
  `machine_code` varchar(255) DEFAULT NULL,
  `created_at` datetime DEFAULT NULL,
  `updated_at` datetime DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

/*Table structure for table `position_to_roles` */

DROP TABLE IF EXISTS `position_to_roles`;

CREATE TABLE `position_to_roles` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `position` varchar(255) DEFAULT NULL,
  `role_name` varchar(255) DEFAULT NULL,
  `role_key` varchar(255) DEFAULT NULL,
  `created_at` datetime DEFAULT NULL,
  `updated_at` datetime DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `index_position_to_roles_on_position` (`position`)
) ENGINE=InnoDB AUTO_INCREMENT=20 DEFAULT CHARSET=utf8 ROW_FORMAT=DYNAMIC;

/*Table structure for table `schema_migrations` */

DROP TABLE IF EXISTS `schema_migrations`;

CREATE TABLE `schema_migrations` (
  `version` varchar(255) NOT NULL,
  UNIQUE KEY `unique_schema_migrations` (`version`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 ROW_FORMAT=DYNAMIC;

/*Table structure for table `tips` */

DROP TABLE IF EXISTS `tips`;

CREATE TABLE `tips` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `title` varchar(255) DEFAULT NULL,
  `created_at` datetime DEFAULT NULL,
  `updated_at` datetime DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

/*Table structure for table `workers` */

DROP TABLE IF EXISTS `workers`;

CREATE TABLE `workers` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `sso_id` varchar(255) DEFAULT NULL,
  `name` varchar(255) DEFAULT NULL,
  `email` varchar(255) DEFAULT NULL,
  `is_admin` tinyint(1) DEFAULT '0',
  `created_at` datetime DEFAULT NULL,
  `updated_at` datetime DEFAULT NULL,
  `is_city_manager` tinyint(1) DEFAULT '0',
  `is_zongbu_manager` tinyint(1) DEFAULT '0',
  `is_shichang_zhuanyuan` tinyint(1) DEFAULT '0',
  `is_shichang_jingli` tinyint(1) DEFAULT '0',
  `is_yingxiao_manage` tinyint(1) DEFAULT '0',
  `is_yingxiao_zhuanyuan` tinyint(1) DEFAULT '0',
  `is_waibao` tinyint(1) DEFAULT NULL,
  `is_shichang` tinyint(1) DEFAULT NULL,
  `is_jiagongdian` tinyint(1) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `index_workers_on_sso_id` (`sso_id`)
) ENGINE=InnoDB AUTO_INCREMENT=17 DEFAULT CHARSET=utf8 ROW_FORMAT=DYNAMIC;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;
