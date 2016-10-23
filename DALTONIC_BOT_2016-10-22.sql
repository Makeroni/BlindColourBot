# ************************************************************
# Sequel Pro SQL dump
# Version 4529
#
# http://www.sequelpro.com/
# https://github.com/sequelpro/sequelpro
#
# Host: raspilocal2 (MySQL 5.5.52-0+deb7u1)
# Database: DALTONIC_BOT
# Generation Time: 2016-10-22 12:15:00 +0000
# ************************************************************


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;


# Dump of table active_bot
# ------------------------------------------------------------

# CREATE DATABASE IF NOT EXISTS DALTONIC_BOT

DROP TABLE IF EXISTS `active_bot`;

CREATE TABLE `active_bot` (
  `chat_id` varchar(150) NOT NULL DEFAULT '',
  `enabled` tinyint(1) NOT NULL DEFAULT '1',
  `date` date DEFAULT NULL,
  `time` timestamp NULL DEFAULT NULL,
  PRIMARY KEY (`chat_id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

LOCK TABLES `active_bot` WRITE;
/*!40000 ALTER TABLE `active_bot` DISABLE KEYS */;


/*!40000 ALTER TABLE `active_bot` ENABLE KEYS */;
UNLOCK TABLES;


# Dump of table users_bot
# ------------------------------------------------------------

DROP TABLE IF EXISTS `users_bot`;

CREATE TABLE `users_bot` (
  `user_id` varchar(150) NOT NULL DEFAULT '',
  `daltonic_type` varchar(150) DEFAULT NULL,
  `date` date DEFAULT NULL,
  `time` timestamp NULL DEFAULT NULL,
  `name` varchar(150) DEFAULT NULL,
  `surname` varchar(150) DEFAULT NULL,
  PRIMARY KEY (`user_id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

LOCK TABLES `users_bot` WRITE;
/*!40000 ALTER TABLE `users_bot` DISABLE KEYS */;


/*!40000 ALTER TABLE `users_bot` ENABLE KEYS */;
UNLOCK TABLES;



/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;
/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
