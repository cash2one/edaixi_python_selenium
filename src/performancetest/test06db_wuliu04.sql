/*
SQLyog Ultimate v12.09 (64 bit)
MySQL - 5.5.43-0ubuntu0.14.04.1 : Database - wuliu04
*********************************************************************
*/

/*!40101 SET NAMES utf8 */;

/*!40101 SET SQL_MODE=''*/;

/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;
CREATE DATABASE /*!32312 IF NOT EXISTS*/`wuliu04` /*!40100 DEFAULT CHARACTER SET utf8 */;

USE `wuliu04`;

/*Table structure for table `brands` */

DROP TABLE IF EXISTS `brands`;

CREATE TABLE `brands` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) DEFAULT NULL,
  `created_at` datetime DEFAULT NULL,
  `updated_at` datetime DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8;

/*Table structure for table `courier_profiles` */

DROP TABLE IF EXISTS `courier_profiles`;

CREATE TABLE `courier_profiles` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `courier_id` int(11) DEFAULT NULL,
  `user_token` varchar(255) DEFAULT NULL,
  `can_saoma` tinyint(1) DEFAULT '0',
  `can_maika` tinyint(1) DEFAULT '0',
  `can_jiedan` tinyint(1) DEFAULT '0',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=38 DEFAULT CHARSET=utf8 ROW_FORMAT=DYNAMIC;

/*Table structure for table `map_cities` */

DROP TABLE IF EXISTS `map_cities`;

CREATE TABLE `map_cities` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `created_at` datetime DEFAULT NULL,
  `updated_at` datetime DEFAULT NULL,
  `title` varchar(255) DEFAULT NULL,
  `api_city_id` int(11) DEFAULT NULL,
  `gaode_map_code` varchar(255) DEFAULT NULL,
  `center_lat` decimal(9,6) DEFAULT NULL,
  `center_lng` decimal(9,6) DEFAULT NULL,
  `search_radius` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=147 DEFAULT CHARSET=utf8 ROW_FORMAT=DYNAMIC;

/*Table structure for table `map_cities_workers` */

DROP TABLE IF EXISTS `map_cities_workers`;

CREATE TABLE `map_cities_workers` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `map_city_id` int(11) DEFAULT NULL,
  `worker_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 ROW_FORMAT=DYNAMIC;

/*Table structure for table `map_points` */

DROP TABLE IF EXISTS `map_points`;

CREATE TABLE `map_points` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `mars_lat` decimal(9,6) DEFAULT NULL,
  `mars_lng` decimal(9,6) DEFAULT NULL,
  `map_city_id` int(11) DEFAULT NULL,
  `created_at` datetime DEFAULT NULL,
  `updated_at` datetime DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `index_map_points_on_map_city_id` (`map_city_id`)
) ENGINE=InnoDB AUTO_INCREMENT=35097 DEFAULT CHARSET=utf8 ROW_FORMAT=DYNAMIC;

/*Table structure for table `map_points_polygons` */

DROP TABLE IF EXISTS `map_points_polygons`;

CREATE TABLE `map_points_polygons` (
  `map_polygon_id` int(11) DEFAULT NULL,
  `map_point_id` int(11) DEFAULT NULL,
  KEY `index_map_points_polygons_on_map_polygon_id` (`map_polygon_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 ROW_FORMAT=DYNAMIC;

/*Table structure for table `map_polygon_groups` */

DROP TABLE IF EXISTS `map_polygon_groups`;

CREATE TABLE `map_polygon_groups` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `title` varchar(255) DEFAULT NULL,
  `map_city_id` int(11) DEFAULT NULL,
  `color` varchar(255) DEFAULT NULL,
  `group_type` varchar(255) DEFAULT NULL,
  `created_at` datetime DEFAULT NULL,
  `updated_at` datetime DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `index_map_polygon_groups_on_map_city_id` (`map_city_id`),
  KEY `index_map_polygon_groups_on_title` (`title`)
) ENGINE=InnoDB AUTO_INCREMENT=2486 DEFAULT CHARSET=utf8 ROW_FORMAT=DYNAMIC;

/*Table structure for table `map_polygon_groups_polygons` */

DROP TABLE IF EXISTS `map_polygon_groups_polygons`;

CREATE TABLE `map_polygon_groups_polygons` (
  `map_polygon_group_id` int(11) DEFAULT NULL,
  `map_polygon_id` int(11) DEFAULT NULL,
  KEY `index_map_polygon_groups_polygons_on_map_polygon_group_id` (`map_polygon_group_id`),
  KEY `index_map_polygon_groups_polygons_on_map_polygon_id` (`map_polygon_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 ROW_FORMAT=DYNAMIC;

/*Table structure for table `map_polygons` */

DROP TABLE IF EXISTS `map_polygons`;

CREATE TABLE `map_polygons` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `title` varchar(255) DEFAULT NULL,
  `polygon_group_id` int(11) DEFAULT NULL,
  `map_city_id` int(11) DEFAULT NULL,
  `map_point_arr` text,
  `created_at` datetime DEFAULT NULL,
  `updated_at` datetime DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `index_map_polygons_on_map_city_id` (`map_city_id`),
  KEY `index_map_polygons_on_title` (`title`)
) ENGINE=InnoDB AUTO_INCREMENT=4485 DEFAULT CHARSET=utf8 ROW_FORMAT=DYNAMIC;

/*Table structure for table `schema_migrations` */

DROP TABLE IF EXISTS `schema_migrations`;

CREATE TABLE `schema_migrations` (
  `version` varchar(255) NOT NULL,
  UNIQUE KEY `unique_schema_migrations` (`version`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 ROW_FORMAT=DYNAMIC;

/*Table structure for table `sessions` */

DROP TABLE IF EXISTS `sessions`;

CREATE TABLE `sessions` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `session_id` varchar(255) NOT NULL,
  `data` text,
  `created_at` datetime DEFAULT NULL,
  `updated_at` datetime DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `index_sessions_on_session_id` (`session_id`),
  KEY `index_sessions_on_updated_at` (`updated_at`)
) ENGINE=InnoDB AUTO_INCREMENT=219028 DEFAULT CHARSET=utf8 ROW_FORMAT=DYNAMIC;

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
  `is_shouyidian` tinyint(1) DEFAULT '0',
  `store_id` int(11) DEFAULT NULL,
  `is_jiagongdian` tinyint(1) DEFAULT '0',
  `is_diaodu` tinyint(1) DEFAULT '0',
  `city_in_charge` varchar(255) DEFAULT NULL,
  `is_wangdian` tinyint(1) DEFAULT NULL,
  `is_wl_yunying` tinyint(1) DEFAULT NULL,
  `is_zb_yunying` tinyint(1) DEFAULT NULL,
  `is_wb_yunying` tinyint(1) DEFAULT NULL,
  `is_map_maker` tinyint(1) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `index_workers_on_sso_id` (`sso_id`)
) ENGINE=InnoDB AUTO_INCREMENT=295 DEFAULT CHARSET=utf8 ROW_FORMAT=DYNAMIC;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;
