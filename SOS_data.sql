-- MySQL dump 10.13  Distrib 8.0.35, for Linux (x86_64)
--
-- Host: localhost    Database: SOS_db_dev
-- ------------------------------------------------------
-- Server version	8.0.35-0ubuntu0.20.04.1

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
-- Table structure for table `categories`
--

DROP TABLE IF EXISTS `categories`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `categories` (
  `name` varchar(60) NOT NULL,
  `id` varchar(60) NOT NULL,
  `created_at` datetime NOT NULL,
  `updated_at` datetime NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `categories`
--

LOCK TABLES `categories` WRITE;
/*!40000 ALTER TABLE `categories` DISABLE KEYS */;
INSERT INTO `categories` VALUES ('video-editing','1b2e6ae5-19cf-43c2-905b-8ae241290bc0','2024-09-06 13:01:16','2024-09-06 17:34:27'),('gaming','59169001-d01c-44ed-9bcf-9737349a5d75','2024-09-06 13:01:16','2024-09-06 13:01:16'),('accounting','73326495-1722-4321-b1b6-3b1067127d5a','2024-09-06 13:01:16','2024-09-06 13:01:16'),('food','78138635-226d-4b13-9a3d-9201bb0823e0','2024-09-06 13:01:16','2024-09-06 13:01:16'),('marketing','7c436dc2-4ee6-428d-8426-e921619df358','2024-09-06 13:01:16','2024-09-06 13:01:16'),('education','8fba647d-5fb8-48de-bc1f-0688dad93327','2024-09-06 13:01:16','2024-09-06 13:01:16'),('programming','aae7bcb8-c100-4b0d-b520-ed9496579e4e','2024-09-06 13:01:16','2024-09-06 13:01:16'),('photo-editing','cbf69d2f-c7f7-4baa-ad7c-a2d9101d3b6f','2024-09-06 13:01:16','2024-09-06 17:35:26'),('health','ebe666fa-c0af-4605-8970-2f4dcb226b8c','2024-09-06 13:01:16','2024-09-06 13:01:16');
/*!40000 ALTER TABLE `categories` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `project_tools`
--

DROP TABLE IF EXISTS `project_tools`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `project_tools` (
  `project_id` varchar(60) NOT NULL,
  `tool_id` varchar(60) NOT NULL,
  `tool_version` varchar(60) DEFAULT NULL,
  PRIMARY KEY (`project_id`,`tool_id`),
  KEY `tool_id` (`tool_id`),
  CONSTRAINT `project_tools_ibfk_1` FOREIGN KEY (`project_id`) REFERENCES `projects` (`id`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `project_tools_ibfk_2` FOREIGN KEY (`tool_id`) REFERENCES `tools` (`id`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `project_tools`
--

LOCK TABLES `project_tools` WRITE;
/*!40000 ALTER TABLE `project_tools` DISABLE KEYS */;
INSERT INTO `project_tools` VALUES ('07f1fa56-3984-460b-ac6d-ff48ea46d227','5a2805d6-7b49-44fe-a7bb-25ad59fd3350',NULL),('07f1fa56-3984-460b-ac6d-ff48ea46d227','d5449a4a-0238-484b-8879-5963008996bb',NULL),('47331846-ed58-4407-8aae-2c13bcf954ee','21eefba7-7717-45d5-b175-eaf3f74e3f95',NULL),('47331846-ed58-4407-8aae-2c13bcf954ee','e65fe920-7ac4-4642-b3ac-8fd407ebb2ca',NULL),('6451c292-c452-4d88-8ec4-e1d9b9d6188a','36d01861-bf78-4e0e-a14b-8f1dd167c6dd',NULL),('6451c292-c452-4d88-8ec4-e1d9b9d6188a','d9cdeb50-bbab-484a-8d8e-13f8c421f51f',NULL),('722a6d51-33d0-43c7-bd0e-4dd6a9a6f1cb','36d01861-bf78-4e0e-a14b-8f1dd167c6dd',NULL),('722a6d51-33d0-43c7-bd0e-4dd6a9a6f1cb','d9cdeb50-bbab-484a-8d8e-13f8c421f51f',NULL);
/*!40000 ALTER TABLE `project_tools` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `projects`
--

DROP TABLE IF EXISTS `projects`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `projects` (
  `name` varchar(60) NOT NULL,
  `description` varchar(255) DEFAULT NULL,
  `video_url` varchar(255) DEFAULT NULL,
  `images` text,
  `category_id` varchar(60) NOT NULL,
  `user_id` varchar(60) NOT NULL,
  `id` varchar(60) NOT NULL,
  `created_at` datetime NOT NULL,
  `updated_at` datetime NOT NULL,
  PRIMARY KEY (`id`),
  KEY `category_id` (`category_id`),
  KEY `user_id` (`user_id`),
  CONSTRAINT `projects_ibfk_1` FOREIGN KEY (`category_id`) REFERENCES `categories` (`id`),
  CONSTRAINT `projects_ibfk_2` FOREIGN KEY (`user_id`) REFERENCES `users` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `projects`
--

LOCK TABLES `projects` WRITE;
/*!40000 ALTER TABLE `projects` DISABLE KEYS */;
INSERT INTO `projects` VALUES ('edumy','Edumy is where your learning journey in tech field starts you can learn, apply, notice your weaknesses and get rid of them',NULL,NULL,'8fba647d-5fb8-48de-bc1f-0688dad93327','11ff296e-cf0f-439b-9053-4a99bec90e18','07f1fa56-3984-460b-ac6d-ff48ea46d227','2024-09-06 15:34:51','2024-09-06 16:00:54'),('project-X','this project is all about using rest apis to get data from all over the world by using REST APIs and also show the resluts in a user friendly way',NULL,NULL,'aae7bcb8-c100-4b0d-b520-ed9496579e4e','11ff296e-cf0f-439b-9053-4a99bec90e18','47331846-ed58-4407-8aae-2c13bcf954ee','2024-09-06 15:21:36','2024-09-06 16:00:54'),('fedora','Fedora is an online app used to facilitate the process of ordering food from all favourite restaurants',NULL,NULL,'78138635-226d-4b13-9a3d-9201bb0823e0','367ead45-5cf0-4f64-9f0e-764c3b3ccbba','6451c292-c452-4d88-8ec4-e1d9b9d6188a','2024-09-06 15:21:36','2024-09-06 16:00:54'),('stormy','Stormy is an online platform for video editing it allows editors to unleash their best creativity ',NULL,NULL,'1b2e6ae5-19cf-43c2-905b-8ae241290bc0','dfde6636-f2df-43a6-9dfc-3cfae5ce32a6','722a6d51-33d0-43c7-bd0e-4dd6a9a6f1cb','2024-09-06 15:21:36','2024-09-06 15:21:36');
/*!40000 ALTER TABLE `projects` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `tools`
--

DROP TABLE IF EXISTS `tools`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `tools` (
  `name` varchar(128) NOT NULL,
  `id` varchar(60) NOT NULL,
  `created_at` datetime NOT NULL,
  `updated_at` datetime NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tools`
--

LOCK TABLES `tools` WRITE;
/*!40000 ALTER TABLE `tools` DISABLE KEYS */;
INSERT INTO `tools` VALUES ('REST APIs','0a18eefe-76f6-4aff-9a87-45d9a7ecf82d','2024-09-06 13:01:16','2024-09-06 13:01:16'),('dataDog','21eefba7-7717-45d5-b175-eaf3f74e3f95','2024-09-06 13:01:16','2024-09-06 13:01:16'),('docker','28657e8c-e8a8-4acc-b954-bf8e90956187','2024-09-06 13:01:16','2024-09-06 13:01:16'),('pyTorch','36d01861-bf78-4e0e-a14b-8f1dd167c6dd','2024-09-06 13:01:16','2024-09-06 13:01:16'),('sqlalchemy','5a2805d6-7b49-44fe-a7bb-25ad59fd3350','2024-09-06 13:01:16','2024-09-06 13:01:16'),('html','848f1c24-aaa8-4847-b8a0-b528fe3f7503','2024-09-06 13:01:16','2024-09-06 13:01:16'),('redis','949280a4-7821-4893-b121-3494e6623c01','2024-09-06 13:01:16','2024-09-06 13:01:16'),('Flask','d5449a4a-0238-484b-8879-5963008996bb','2024-09-06 13:01:16','2024-09-06 13:01:16'),('scikit-learn','d9cdeb50-bbab-484a-8d8e-13f8c421f51f','2024-09-06 13:01:16','2024-09-06 13:01:16'),('jinja','e65fe920-7ac4-4642-b3ac-8fd407ebb2ca','2024-09-06 13:01:16','2024-09-06 13:01:16'),('Nginx','f8386e4c-4196-40a0-bfcb-ede24e3c629b','2024-09-06 13:01:16','2024-09-06 13:01:16');
/*!40000 ALTER TABLE `tools` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `users`
--

DROP TABLE IF EXISTS `users`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `users` (
  `first_name` varchar(60) NOT NULL,
  `last_name` varchar(60) NOT NULL,
  `user_type` enum('developer','client','employer') NOT NULL,
  `username` varchar(60) NOT NULL,
  `password` varchar(128) NOT NULL,
  `email` varchar(128) NOT NULL,
  `id` varchar(60) NOT NULL,
  `created_at` datetime NOT NULL,
  `updated_at` datetime NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`),
  UNIQUE KEY `email` (`email`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `users`
--

LOCK TABLES `users` WRITE;
/*!40000 ALTER TABLE `users` DISABLE KEYS */;
INSERT INTO `users` VALUES ('Abdelmoneim','Maher','developer','abdo-maher','123','abdo@gmail.com','11ff296e-cf0f-439b-9053-4a99bec90e18','2024-09-06 13:01:16','2024-09-06 13:01:16'),('Ahmed','Shrief','developer','shefo','456','shefo@gmail.com','367ead45-5cf0-4f64-9f0e-764c3b3ccbba','2024-09-06 13:01:16','2024-09-06 13:01:16'),('Ahmed','maher','developer','ahmed-zayed','h34','almaher@gmail.com','7c9208cb-d5b0-42bc-8179-4923b98830a9','2024-09-06 13:01:16','2024-09-06 13:01:16'),('Abdullahi','Tukur','developer','abdullahi-tukur','789','abdullahi@yahoo.com','dfde6636-f2df-43a6-9dfc-3cfae5ce32a6','2024-09-06 13:01:16','2024-09-06 13:01:16');
/*!40000 ALTER TABLE `users` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2024-09-11 15:56:12
