/*
Navicat MySQL Data Transfer

Source Server         : localhost
Source Server Version : 50637
Source Host           : localhost:3306
Source Database       : city_distmsg

Target Server Type    : MYSQL
Target Server Version : 50637
File Encoding         : 65001

Date: 2017-09-14 00:11:22
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
  `start_lat` decimal(20,4) DEFAULT NULL,
  `start_lon` decimal(20,4) DEFAULT NULL,
  `end_lat` decimal(20,4) DEFAULT NULL,
  `end_lon` decimal(20,4) DEFAULT NULL,
  `dist_city` decimal(20,4) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of citydist
-- ----------------------------
INSERT INTO `citydist` VALUES ('1', 'Beijing', 'Tianjin', '39.8592', '116.4551', '39.0618', '117.2351', '111.0952');
INSERT INTO `citydist` VALUES ('2', 'Beijing', 'Jinan', '39.8592', '116.4551', '36.5979', '117.1472', '367.0369');
INSERT INTO `citydist` VALUES ('3', 'Tianjin', 'Jinan', '39.0618', '117.2351', '36.5979', '117.1472', '273.5922');
INSERT INTO `citydist` VALUES ('4', 'Tianjin', 'Shijiazhuang', '39.0618', '117.2351', '38.0048', '114.5215', '264.0881');
INSERT INTO `citydist` VALUES ('5', 'Jinan', 'Shijiazhuang', '36.5979', '117.1472', '38.0048', '114.5215', '280.2929');
INSERT INTO `citydist` VALUES ('6', 'Shijiazhuang', 'Beijing', '38.0048', '114.5215', '39.8592', '116.4551', '265.4787');
