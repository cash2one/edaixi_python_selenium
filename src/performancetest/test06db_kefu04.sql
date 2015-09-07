/*
SQLyog Ultimate v12.09 (64 bit)
MySQL - 5.5.43-0ubuntu0.14.04.1 : Database - kefu04
*********************************************************************
*/

/*!40101 SET NAMES utf8 */;

/*!40101 SET SQL_MODE=''*/;

/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;
CREATE DATABASE /*!32312 IF NOT EXISTS*/`kefu04` /*!40100 DEFAULT CHARACTER SET utf8 */;

USE `kefu04`;

/*Table structure for table `activities` */

DROP TABLE IF EXISTS `activities`;

CREATE TABLE `activities` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `key` varchar(255) DEFAULT NULL,
  `parameters` text,
  `worker_id` int(11) DEFAULT NULL,
  `customer_id` int(11) DEFAULT NULL,
  `trackable_id` int(11) DEFAULT NULL,
  `trackable_type` varchar(255) DEFAULT NULL,
  `created_at` datetime DEFAULT NULL,
  `updated_at` datetime DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `index_activities_on_trackable_type_and_trackable_id` (`trackable_type`,`trackable_id`),
  KEY `index_activities_on_worker_id` (`worker_id`),
  KEY `index_activities_on_customer_id` (`customer_id`)
) ENGINE=InnoDB AUTO_INCREMENT=474 DEFAULT CHARSET=utf8 ROW_FORMAT=DYNAMIC;

/*Table structure for table `common_replies` */

DROP TABLE IF EXISTS `common_replies`;

CREATE TABLE `common_replies` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `content` text,
  `created_at` datetime DEFAULT NULL,
  `updated_at` datetime DEFAULT NULL,
  `name` text,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=48 DEFAULT CHARSET=utf8 ROW_FORMAT=DYNAMIC;

/*Table structure for table `cs_job_votes` */

DROP TABLE IF EXISTS `cs_job_votes`;

CREATE TABLE `cs_job_votes` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `worker_id` int(11) DEFAULT NULL,
  `customer_id` int(11) DEFAULT NULL,
  `tag_id` int(11) DEFAULT NULL,
  `vote` int(11) DEFAULT NULL,
  `callbacker_id` int(11) DEFAULT NULL,
  `comment` text,
  `result_code` int(11) DEFAULT NULL,
  `created_at` datetime DEFAULT NULL,
  `updated_at` datetime DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `index_cs_job_votes_on_worker_id` (`worker_id`),
  KEY `index_cs_job_votes_on_customer_id` (`customer_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

/*Table structure for table `customers` */

DROP TABLE IF EXISTS `customers`;

CREATE TABLE `customers` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `php_id` int(11) DEFAULT NULL,
  `user_name` varchar(255) DEFAULT NULL,
  `state` int(11) DEFAULT '1',
  `worker_id` int(11) DEFAULT NULL,
  `phone` varchar(255) DEFAULT NULL,
  `weixin_token` varchar(255) DEFAULT NULL,
  `last_weixin_at` datetime DEFAULT NULL,
  `created_at` datetime DEFAULT NULL,
  `updated_at` datetime DEFAULT NULL,
  `remark_info` text,
  `last_feedback_at` datetime DEFAULT NULL,
  `last_ali_at` datetime DEFAULT NULL,
  `client_id` int(11) DEFAULT '0',
  `last_auto_reply_time` datetime DEFAULT NULL,
  `last_reply_at` datetime DEFAULT NULL,
  `last_callback_at` datetime DEFAULT NULL,
  `callback_status` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `index_customers_on_php_id` (`php_id`),
  KEY `index_customers_on_client_id` (`client_id`)
) ENGINE=InnoDB AUTO_INCREMENT=1239522 DEFAULT CHARSET=utf8 ROW_FORMAT=DYNAMIC;

/*Table structure for table `feedback_filters` */

DROP TABLE IF EXISTS `feedback_filters`;

CREATE TABLE `feedback_filters` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `filter_content` varchar(255) DEFAULT NULL,
  `from_state` int(11) DEFAULT '1',
  `to_state` int(11) DEFAULT '5',
  `created_at` datetime DEFAULT NULL,
  `updated_at` datetime DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `index_feedback_filters_on_to_state` (`to_state`),
  KEY `index_feedback_filters_on_from_state` (`from_state`)
) ENGINE=InnoDB AUTO_INCREMENT=130 DEFAULT CHARSET=utf8 ROW_FORMAT=DYNAMIC;

/*Table structure for table `feedbacks` */

DROP TABLE IF EXISTS `feedbacks`;

CREATE TABLE `feedbacks` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` varchar(255) COLLATE utf8_unicode_ci DEFAULT NULL,
  `phone` varchar(255) COLLATE utf8_unicode_ci DEFAULT NULL,
  `token` varchar(255) COLLATE utf8_unicode_ci DEFAULT NULL,
  `channel` varchar(255) COLLATE utf8_unicode_ci DEFAULT NULL,
  `message` text CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci,
  `status_code` int(11) DEFAULT '1',
  `worker_id` int(11) DEFAULT NULL,
  `replied_at` datetime DEFAULT NULL,
  `created_at` datetime DEFAULT NULL,
  `updated_at` datetime DEFAULT NULL,
  `type_code` int(11) DEFAULT '0',
  `reply_type` int(11) DEFAULT NULL,
  `message_type` int(11) DEFAULT '0',
  `user_name` varchar(255) COLLATE utf8_unicode_ci DEFAULT NULL,
  `customer_id` int(11) DEFAULT NULL,
  `tag_id` int(11) DEFAULT NULL,
  `client_id` int(11) DEFAULT '0',
  `handle_time` datetime DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `index_feedbacks_on_worker_id` (`worker_id`),
  KEY `index_feedbacks_on_user_id` (`user_id`),
  KEY `index_feedbacks_on_customer_id` (`customer_id`),
  KEY `index_feedbacks_on_status_code` (`status_code`),
  KEY `index_feedbacks_on_tag_id` (`tag_id`),
  KEY `index_feedbacks_on_client_id` (`client_id`)
) ENGINE=InnoDB AUTO_INCREMENT=71876 DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci ROW_FORMAT=DYNAMIC;

/*Table structure for table `order_comment_notes` */

DROP TABLE IF EXISTS `order_comment_notes`;

CREATE TABLE `order_comment_notes` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `order_comment_id` int(11) DEFAULT NULL,
  `note` text,
  `created_at` datetime DEFAULT NULL,
  `updated_at` datetime DEFAULT NULL,
  `worker_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=60 DEFAULT CHARSET=utf8 ROW_FORMAT=DYNAMIC;

/*Table structure for table `order_complaints` */

DROP TABLE IF EXISTS `order_complaints`;

CREATE TABLE `order_complaints` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `order_id` int(11) DEFAULT NULL,
  `order_sn` varchar(255) DEFAULT NULL,
  `fan_id` int(11) DEFAULT NULL,
  `user_name` varchar(255) DEFAULT NULL,
  `tel` varchar(255) DEFAULT NULL,
  `complaint` varchar(255) DEFAULT NULL,
  `status` int(11) DEFAULT NULL,
  `worker_id` int(11) DEFAULT NULL,
  `remark` varchar(255) DEFAULT NULL,
  `times` int(11) DEFAULT NULL,
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
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8 ROW_FORMAT=DYNAMIC;

/*Table structure for table `remarks` */

DROP TABLE IF EXISTS `remarks`;

CREATE TABLE `remarks` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `feedback_id` int(11) DEFAULT NULL,
  `worker_id` int(11) DEFAULT NULL,
  `content` text,
  `created_at` datetime DEFAULT NULL,
  `updated_at` datetime DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `index_remarks_on_worker_id` (`worker_id`),
  KEY `index_remarks_on_feedback_id` (`feedback_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 ROW_FORMAT=DYNAMIC;

/*Table structure for table `replies` */

DROP TABLE IF EXISTS `replies`;

CREATE TABLE `replies` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `content` text,
  `feedback_id` int(11) DEFAULT NULL,
  `customer_id` int(11) DEFAULT NULL,
  `worker_id` int(11) DEFAULT NULL,
  `reply_type` int(11) DEFAULT NULL,
  `created_at` datetime DEFAULT NULL,
  `updated_at` datetime DEFAULT NULL,
  `content_type` int(11) DEFAULT '0',
  `tag_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `index_replies_on_feedback_id` (`feedback_id`),
  KEY `index_replies_on_customer_id` (`customer_id`)
) ENGINE=InnoDB AUTO_INCREMENT=110152 DEFAULT CHARSET=utf8 ROW_FORMAT=DYNAMIC;

/*Table structure for table `rights` */

DROP TABLE IF EXISTS `rights`;

CREATE TABLE `rights` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` varchar(255) DEFAULT NULL,
  `phone` varchar(255) DEFAULT NULL,
  `token` varchar(255) DEFAULT NULL,
  `channel` varchar(255) DEFAULT NULL,
  `feedbackid` varchar(255) DEFAULT NULL,
  `transid` varchar(255) DEFAULT NULL,
  `reason` varchar(255) DEFAULT NULL,
  `solution` varchar(255) DEFAULT NULL,
  `extinfo` varchar(255) DEFAULT NULL,
  `feed_status` varchar(255) DEFAULT NULL,
  `status_code` int(11) DEFAULT NULL,
  `worker_id` int(11) DEFAULT NULL,
  `user_name` varchar(255) DEFAULT NULL,
  `customer_id` int(11) DEFAULT NULL,
  `created_at` datetime DEFAULT NULL,
  `updated_at` datetime DEFAULT NULL,
  `confirm_time` datetime DEFAULT NULL,
  `notes` varchar(255) DEFAULT NULL,
  `client_id` int(11) DEFAULT '0',
  PRIMARY KEY (`id`),
  KEY `index_rights_on_client_id` (`client_id`)
) ENGINE=InnoDB AUTO_INCREMENT=267 DEFAULT CHARSET=utf8 ROW_FORMAT=DYNAMIC;

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
) ENGINE=InnoDB AUTO_INCREMENT=105920 DEFAULT CHARSET=utf8 ROW_FORMAT=DYNAMIC;

/*Table structure for table `tags` */

DROP TABLE IF EXISTS `tags`;

CREATE TABLE `tags` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) DEFAULT NULL,
  `tag_model_name` varchar(255) DEFAULT NULL,
  `html_classes` varchar(255) DEFAULT NULL,
  `level` int(11) DEFAULT NULL,
  `parent_id` int(11) DEFAULT NULL,
  `order` int(11) DEFAULT NULL,
  `soft_deleted` tinyint(1) DEFAULT '0',
  `created_at` datetime DEFAULT NULL,
  `updated_at` datetime DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `index_tags_on_name` (`name`),
  KEY `index_tags_on_tag_model_name` (`tag_model_name`)
) ENGINE=InnoDB AUTO_INCREMENT=47 DEFAULT CHARSET=utf8 ROW_FORMAT=DYNAMIC;

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
  `is_kefu` tinyint(1) DEFAULT '0',
  `holly_login` varchar(255) DEFAULT NULL,
  `holly_password` varchar(255) DEFAULT NULL,
  `is_kefu_zhuguan` tinyint(1) DEFAULT '0',
  `is_zhichi` tinyint(1) DEFAULT '0',
  PRIMARY KEY (`id`),
  KEY `index_workers_on_sso_id` (`sso_id`)
) ENGINE=InnoDB AUTO_INCREMENT=55 DEFAULT CHARSET=utf8 ROW_FORMAT=DYNAMIC;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;
