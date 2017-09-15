/*
Navicat MySQL Data Transfer

Source Server         : localhost
Source Server Version : 50637
Source Host           : localhost:3306
Source Database       : city_distmsg

Target Server Type    : MYSQL
Target Server Version : 50637
File Encoding         : 65001

Date: 2017-09-13 22:27:03
*/

SET FOREIGN_KEY_CHECKS=0;

-- ----------------------------
-- Table structure for `citydist`
-- ----------------------------
DROP TABLE IF EXISTS `citydist`;
CREATE TABLE `citydist` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `start_city` varchar(20) DEFAULT NULL,
  `end_city` varchar(20) DEFAULT NULL,
  `start_lat` DECIMAL(20,4) DEFAULT NULL,
  `start_lon` DECIMAL(20,4) DEFAULT NULL,
  `end_lat` DECIMAL(20,4)DEFAULT NULL,
  `end_lon` DECIMAL(20,4)DEFAULT NULL,
  `dist_city` DECIMAL(20,4)DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of citydist
-- ----------------------------
