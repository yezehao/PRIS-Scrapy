-- MySQL dump 10.13  Distrib 8.0.33, for Win64 (x86_64)
--
-- Host: localhost    Database: pris
-- ------------------------------------------------------
-- Server version	8.0.33

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `pris_age`
--

DROP TABLE IF EXISTS `pris_age`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `pris_age` (
  `age` varchar(20) DEFAULT NULL,
  `reactor number` int DEFAULT NULL,
  `Total Net Electrical Capacity [MW]` int DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `pris_age`
--

LOCK TABLES `pris_age` WRITE;
/*!40000 ALTER TABLE `pris_age` DISABLE KEYS */;
INSERT INTO `pris_age` VALUES ('0',4,3667),('1',6,7504),('2',6,5305),('3',5,5683),('4',6,5243),('5',9,10454),('6',4,3373),('7',10,9607),('8',10,9505),('9',5,4673),('10',4,4054),('11',3,3011),('12',6,3993),('13',5,3774),('14',1,202),('15',0,0),('16',3,1852),('17',2,1490),('18',2,1487),('19',4,3460),('20',2,1675),('21',6,5222),('22',2,1981),('23',6,3208),('24',4,2740),('25',4,3068),('26',3,3564),('27',4,4434),('28',4,3320),('29',4,3551),('30',6,6404),('31',5,3739),('32',4,3756),('33',8,9072),('34',9,8017),('35',10,9814),('36',20,20492),('37',21,20985),('38',30,30348),('39',28,25990),('40',15,12396),('41',12,10451),('42',18,16130),('43',18,14441),('44',5,4620),('45',8,7466),('46',5,3819),('47',9,7629),('48',8,5939),('49',12,8897),('50',9,6484),('51',6,4470),('52',4,2387),('53',3,2226),('54',3,1538);
/*!40000 ALTER TABLE `pris_age` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `pris_country`
--

DROP TABLE IF EXISTS `pris_country`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `pris_country` (
  `country` varchar(50) DEFAULT NULL,
  `reactor number in operation` int DEFAULT NULL,
  `reactor number suspended` int DEFAULT NULL,
  `reactor number under construction` int DEFAULT NULL,
  `reactor number permanent shutdown` int DEFAULT NULL,
  `Total Net Electrical Capacity [MW] in operation` int DEFAULT NULL,
  `Total Net Electrical Capacity [MW] suspended` int DEFAULT NULL,
  `Total Net Electrical Capacity [MW] under construction` int DEFAULT NULL,
  `Total Net Electrical Capacity [MW] permanent shutdown` int DEFAULT NULL,
  `2020-2022 EAF [%]` float DEFAULT NULL,
  `2020-2022 UCF [%]` float DEFAULT NULL,
  `2020-2022 UCL [%]` float DEFAULT NULL,
  `lifetime EAF [%] up to 2022` float DEFAULT NULL,
  `lifetime UCF [%] up to 2022` float DEFAULT NULL,
  `lifetime UCL [%] up to 2022` float DEFAULT NULL,
  `Nuclear Electricity Supplied [GW.h]` float DEFAULT NULL,
  `Nuclear Share [%]` float DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `pris_country`
--

LOCK TABLES `pris_country` WRITE;
/*!40000 ALTER TABLE `pris_country` DISABLE KEYS */;
INSERT INTO `pris_country` VALUES ('ARGENTINA',3,NULL,1,NULL,1641,NULL,25,NULL,64,64.4,20.8,74,8.5,8.5,7469.52,5.4),('ARMENIA',1,NULL,NULL,1,416,NULL,NULL,376,62.6,65.9,5,65.2,3.3,3.3,2630.85,31),('BELARUS',2,NULL,NULL,NULL,2220,NULL,NULL,NULL,50.3,50.3,36.3,50.3,36.3,36.3,4411.35,11.9),('BELGIUM',5,NULL,NULL,3,3928,NULL,NULL,2024,79.4,80.4,6.2,81.8,6.7,6.7,41744.4,46.4),('BRAZIL',2,NULL,1,NULL,1884,NULL,1340,NULL,82.4,82.5,4.9,76.3,7.8,7.8,13744.8,2.5),('BULGARIA',2,NULL,NULL,4,2006,NULL,NULL,1632,88.4,88.8,0.6,74.6,1.3,1.3,15784.1,32.6),('CANADA',19,NULL,NULL,6,13624,NULL,NULL,2143,72.2,72.6,2.6,76.5,10.4,10.4,81717.6,12.9),('CHINA',55,NULL,21,NULL,53181,NULL,21608,NULL,90.8,91.4,0.5,88.8,1.2,1.2,395354,5),('CZECH REPUBLIC',6,NULL,NULL,NULL,3934,NULL,NULL,NULL,83.6,84.3,2,80.4,3.6,3.6,29310.3,36.7),('FINLAND',5,NULL,NULL,NULL,4394,NULL,NULL,NULL,91.6,92.4,1.6,91.3,1.8,1.8,24242,35),('FRANCE',56,NULL,1,14,61370,NULL,1630,5549,62.4,67.6,15.2,74.9,8.9,8.9,282093,62.6),('HUNGARY',4,NULL,NULL,NULL,1916,NULL,NULL,NULL,89.3,90,2.5,86.4,2.7,2.7,14954.2,47),('INDIA',19,4,8,NULL,6290,595,6028,NULL,81.2,83.2,4.4,67.6,10.8,10.8,41972.4,3.1),('JAPAN',10,23,2,27,9486,22193,2653,17119,60.2,60.2,0.4,65.2,4,4,51907.5,6.1),('KOREA, REPUBLIC OF',25,NULL,3,2,24489,NULL,4020,1237,76.8,77.8,3,82.6,1.7,1.7,167514,30.4),('MEXICO',2,NULL,NULL,NULL,1552,NULL,NULL,NULL,80.7,82.9,8.3,81.4,7.2,7.2,10539.5,4.5),('NETHERLANDS',1,NULL,NULL,1,482,NULL,NULL,55,90.8,90.8,1.4,85.1,3.9,3.9,3930.56,3.3),('PAKISTAN',6,NULL,NULL,1,3262,NULL,NULL,90,87.1,87.9,4.4,69.9,10.8,10.8,22219.3,16.2),('ROMANIA',2,NULL,NULL,NULL,1300,NULL,NULL,NULL,91.1,92.1,1.4,91.2,2,2,10222,19.4),('RUSSIA',37,NULL,3,10,27727,NULL,2700,3957,83,83.7,1.7,74.6,3.8,3.8,209517,19.6),('SLOVAKIA',5,NULL,1,3,2308,NULL,440,909,90.1,91.9,0.7,81.1,1.6,1.6,14830.3,59.2),('SLOVENIA',1,NULL,NULL,NULL,688,NULL,NULL,NULL,92.2,92.9,0.7,86.5,1.5,1.5,5310.7,42.8),('SOUTH AFRICA',2,NULL,NULL,NULL,1854,NULL,NULL,NULL,69.5,75.4,10.1,73.5,6.7,6.7,10123.7,4.9),('SPAIN',7,NULL,NULL,3,7123,NULL,NULL,1067,89.3,90.6,2.1,85.1,3.9,3.9,56150.4,20.3),('SWEDEN',6,NULL,NULL,7,6937,NULL,NULL,4054,79.6,81.5,9.1,78.2,8.4,8.4,50018.2,29.4),('SWITZERLAND',4,NULL,NULL,2,2973,NULL,NULL,379,83,84.3,0.6,85.4,2.6,2.6,23179.6,36.4),('UKRAINE',15,NULL,2,4,13107,NULL,2070,3515,69,72.4,1.9,70.8,4,4,NULL,NULL),('UNITED ARAB EMIRATES',3,NULL,1,NULL,4011,NULL,1310,NULL,83.2,83.7,7.6,83.2,7.6,7.6,19300.4,6.8),('UNITED KINGDOM',9,NULL,2,36,5883,NULL,3260,7755,63.8,65.3,22.1,71.7,12.3,12.3,43604.8,14.2),('TAIWAN, CHINA',2,NULL,NULL,NULL,1874,NULL,NULL,NULL,86.4,87.1,0.3,84.2,2.4,2.4,NULL,NULL),('BANGLADESH',NULL,NULL,2,NULL,NULL,NULL,2160,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL),('EGYPT',NULL,NULL,3,NULL,NULL,NULL,3300,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL),('T脺RKIYE',NULL,NULL,4,NULL,NULL,NULL,4456,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL),('GERMANY',NULL,NULL,NULL,33,NULL,NULL,NULL,26235,91.8,92.8,1.3,83.1,5.1,5.1,31892.2,5.8),('ITALY',NULL,NULL,NULL,4,NULL,NULL,NULL,1423,NULL,NULL,NULL,45.8,7.1,7.1,NULL,NULL),('KAZAKHSTAN',NULL,NULL,NULL,1,NULL,NULL,NULL,52,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL),('LITHUANIA',NULL,NULL,NULL,2,NULL,NULL,NULL,2370,NULL,NULL,NULL,61.3,5.8,5.8,NULL,NULL),('IRAN, ISLAMIC REPUBLIC OF',1,NULL,1,NULL,915,NULL,974,NULL,77.4,78.2,2.7,73.6,6.5,6.5,6008.02,1.7),('UNITED STATES OF AMERICA',93,NULL,1,41,95835,NULL,1117,19976,92.8,92.8,1.3,83,5.2,5.2,772220,18.2);
/*!40000 ALTER TABLE `pris_country` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `pris_region`
--

DROP TABLE IF EXISTS `pris_region`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `pris_region` (
  `region` varchar(50) DEFAULT NULL,
  `reactor number in operation` int DEFAULT NULL,
  `reactor number suspended` int DEFAULT NULL,
  `reactor number under construction` int DEFAULT NULL,
  `reactor number permanent shutdown` int DEFAULT NULL,
  `Total Net Electrical Capacity [MW] in operation` int DEFAULT NULL,
  `Total Net Electrical Capacity [MW] suspended` int DEFAULT NULL,
  `Total Net Electrical Capacity [MW] under construction` int DEFAULT NULL,
  `Total Net Electrical Capacity [MW] permanent shutdown` int DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `pris_region`
--

LOCK TABLES `pris_region` WRITE;
/*!40000 ALTER TABLE `pris_region` DISABLE KEYS */;
INSERT INTO `pris_region` VALUES ('Africa',2,NULL,3,NULL,1854,NULL,3300,NULL),('America - Latin',7,NULL,2,NULL,5077,NULL,1365,NULL),('America - Northern',112,NULL,1,47,109459,NULL,1117,22119),('Asia - Far East',92,23,26,33,89030,22193,28281,21534),('Europe - Western',93,NULL,3,103,93090,NULL,4890,48541),('Asia - Middle East and South',29,4,12,1,14478,595,10472,90),('Europe - Central and Eastern',75,NULL,10,25,55622,NULL,9666,12811);
/*!40000 ALTER TABLE `pris_region` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `pris_trend`
--

DROP TABLE IF EXISTS `pris_trend`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `pris_trend` (
  `year` varchar(20) DEFAULT NULL,
  `reactor number operated` int DEFAULT NULL,
  `Total Net Electrical Capacity [GW]` float DEFAULT NULL,
  `Year-end Total Net Electrical Capacity [GW]` float DEFAULT NULL,
  `Year-end Operational Reactors` int DEFAULT NULL,
  `EAF [%]` float DEFAULT NULL,
  `UCF [%]` float DEFAULT NULL,
  `UCL [%]` float DEFAULT NULL,
  `LF [%]` float DEFAULT NULL,
  `Electricity Supplied [TW.h]` float DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `pris_trend`
--

LOCK TABLES `pris_trend` WRITE;
/*!40000 ALTER TABLE `pris_trend` DISABLE KEYS */;
INSERT INTO `pris_trend` VALUES ('2003',443,360.81,359.83,437,80.8,81.7,5.8,80,2504.78),('2004',443,366.05,364.54,437,83.2,84,4.6,82.4,2616.24),('2005',442,368.98,368.04,440,82.8,84,3.9,82.1,2626.34),('2006',442,371.73,369.49,434,82.9,83.9,4.3,82.1,2660.85),('2007',438,371.62,369.48,436,81.1,82.8,4.9,80.6,2608.18),('2008',436,369.74,368.27,434,80.6,81.5,5.3,80.2,2597.81),('2009',436,369.91,367.41,433,80.1,81.6,5.5,79.4,2558.06),('2010',438,372.12,370.93,436,81.7,82.7,5.7,81.3,2629.82),('2011',442,375.91,350.66,414,81.2,82.4,3.6,80.2,2517.98),('2012',419,356.32,350.94,412,77.4,78.5,4.6,76.7,2346.19),('2013',416,355.32,349.47,409,78.2,78.9,4.3,77.2,2358.86),('2014',414,354.56,353.96,413,80,80.6,3.2,78.6,2410.37),('2015',423,364.37,360.5,416,79.7,80.4,3.4,78.3,2441.34),('2016',426,370.23,368.19,422,79.6,81,4.7,77.7,2477.3),('2017',426,371.75,369.42,423,78.7,79.7,5.2,77.4,2502.82),('2018',432,379.74,374.11,424,79.8,80.8,3.9,79,2562.76),('2019',430,379.79,369.59,417,81.5,82.4,4.5,81,2657.16),('2020',422,375.27,369.8,414,80.5,82.4,4.8,79,2553.24),('2021',420,375.46,366.79,410,82.3,83.5,3.9,81.7,2653.34),('2022',416,374.26,370.99,411,80.6,81.7,5.6,80.1,2486.83);
/*!40000 ALTER TABLE `pris_trend` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `pris_type`
--

DROP TABLE IF EXISTS `pris_type`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `pris_type` (
  `type` varchar(20) DEFAULT NULL,
  `description` varchar(100) DEFAULT NULL,
  `reactor number in operation` int DEFAULT NULL,
  `reactor number suspended` int DEFAULT NULL,
  `reactor number under construction` int DEFAULT NULL,
  `reactor number permanent shutdown` int DEFAULT NULL,
  `Total Net Electrical Capacity [MW] in operation` int DEFAULT NULL,
  `Total Net Electrical Capacity [MW] suspended` int DEFAULT NULL,
  `Total Net Electrical Capacity [MW] under construction` int DEFAULT NULL,
  `Total Net Electrical Capacity [MW] permanent shutdown` int DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `pris_type`
--

LOCK TABLES `pris_type` WRITE;
/*!40000 ALTER TABLE `pris_type` DISABLE KEYS */;
INSERT INTO `pris_type` VALUES ('BWR','Boiling Light-Water Cooled and Moderated Reactor',41,19,2,53,43071,17859,2653,31655),('FBR','Fast Breeder Reactor',2,NULL,4,8,1380,NULL,2054,1951),('GCR','Gas Cooled, Graphite Moderated Reactor',8,NULL,NULL,44,4685,NULL,NULL,10272),('HTGR','High Temperature Gas Cooled Reactor',1,NULL,NULL,4,200,NULL,NULL,679),('LWGR','Light-Water Cooled, Graphite Moderated Reactor',11,NULL,NULL,13,7433,NULL,NULL,8924),('HWGCR','Heavy-Water Moderated, Gas Cooled Reactor',NULL,NULL,NULL,3,NULL,NULL,NULL,169),('SGHWR','Steam Generating Heavy-Water Reactor',NULL,NULL,NULL,1,NULL,NULL,NULL,92),('X','Other',NULL,NULL,NULL,2,NULL,NULL,NULL,87),('PHWR','Pressurized Heavy-Water Moderated and Cooled Reactor',46,2,3,10,24093,295,1890,2723),('PWR','Pressurized Light-Water Moderated and Cooled Reactor',301,6,48,69,287748,4634,52494,48145),('HWLWR','Heavy-Water Moderated, Boiling Light-Water Cooled Reactor',NULL,NULL,NULL,2,NULL,NULL,NULL,398);
/*!40000 ALTER TABLE `pris_type` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2023-07-17  3:56:39
