-- phpMyAdmin SQL Dump
-- version 5.0.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Mar 30, 2020 at 11:44 AM
-- Server version: 10.4.11-MariaDB
-- PHP Version: 7.4.1

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `questions`
--

-- --------------------------------------------------------

--
-- Table structure for table `anto`
--

CREATE TABLE `anto` (
  `sino` int(11) DEFAULT NULL,
  `questions` varchar(255) DEFAULT NULL,
  `answers` varchar(255) DEFAULT NULL,
  `level` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `anto`
--

INSERT INTO `anto` (`sino`, `questions`, `answers`, `level`) VALUES
(0, 'What is DBMS used for?', 'What is DBMS used for!!', 0),
(1, 'What is meant by a Database?', 'What is meant by a Database!!', 0),
(2, 'Why is the use of DBMS recommended?', 'Why is the use of DBMS recommended!!', 0),
(3, 'What is the purpose of normalization in DBMS?', 'What is the purpose of normalization in DBMS!!', 0),
(4, 'What are the different types of languages that are available in the DBMS?', 'What are the different types of languages that are available in the DBMS!!', 0),
(5, 'What is the purpose of SQL?', 'What is the purpose of SQL!!', 0),
(6, 'Explain the concepts of a Primary key and Foreign Key?', 'Explain the concepts of a Primary key and Foreign Key!!', 0),
(7, 'What are the main differences between Primary key and Unique Key?', 'What are the main differences between Primary key and Unique Key!!', 0),
(8, 'What is the concept of sub-query in terms of SQL?', 'What is the concept of sub-query in terms of SQL!!', 0);

-- --------------------------------------------------------

--
-- Table structure for table `dbms1`
--

CREATE TABLE `dbms1` (
  `sino` int(11) DEFAULT NULL,
  `questions` varchar(255) DEFAULT NULL,
  `level` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `dbms1`
--

INSERT INTO `dbms1` (`sino`, `questions`, `level`) VALUES
(0, 'What is DBMS used for', 1),
(1, 'What is meant by a Database', 1),
(2, ' Why is the use of DBMS recommended', 1),
(3, 'nothing', 1),
(4, 'What are the different types of languages that are available in the DBMS', 1),
(5, 'What is the purpose of SQL', 1),
(6, 'Explain the concepts of a Primary key and Foreign Key', 1),
(7, ' What are the main differences between Primary key and Unique Key', 1),
(8, 'What is the concept of sub-query in terms of SQL', 1),
(9, '', 1);

-- --------------------------------------------------------

--
-- Table structure for table `dbms2`
--

CREATE TABLE `dbms2` (
  `sino` int(11) DEFAULT NULL,
  `questions` varchar(255) DEFAULT NULL,
  `answers` varchar(255) DEFAULT NULL,
  `level` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `dbms3`
--

CREATE TABLE `dbms3` (
  `sino` int(11) DEFAULT NULL,
  `questions` varchar(255) DEFAULT NULL,
  `answers` varchar(255) DEFAULT NULL,
  `level` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `dbms3`
--

INSERT INTO `dbms3` (`sino`, `questions`, `answers`, `level`) VALUES
(0, 'What is DBMS used for', 'What is DBMS used for', NULL),
(1, 'What is meant by a Database', 'What is meant by a Database', NULL),
(2, ' Why is the use of DBMS recommended', ' Why is the use of DBMS recommended', NULL),
(3, ' What is the purpose of normalization in DBMS', ' What is the purpose of normalization in DBMS', NULL),
(4, 'What are the different types of languages that are available in the DBMS', 'What are the different types of languages that are available in the DBMS', NULL),
(5, 'What is the purpose of SQL', 'What is the purpose of SQL', NULL),
(6, 'Explain the concepts of a Primary key and Foreign Key', 'Explain the concepts of a Primary key and Foreign Key', NULL),
(7, ' What are the main differences between Primary key and Unique Key', ' What are the main differences between Primary key and Unique Key', NULL),
(8, 'What is the concept of sub-query in terms of SQL', 'What is the concept of sub-query in terms of SQL', NULL),
(9, '', '', NULL);

-- --------------------------------------------------------

--
-- Table structure for table `something`
--

CREATE TABLE `something` (
  `sino` int(11) DEFAULT NULL,
  `questions` varchar(255) DEFAULT NULL,
  `answers` varchar(255) DEFAULT NULL,
  `level` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `something0`
--

CREATE TABLE `something0` (
  `sino` int(11) DEFAULT NULL,
  `questions` varchar(255) DEFAULT NULL,
  `answers` varchar(255) DEFAULT NULL,
  `level` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `something1`
--

CREATE TABLE `something1` (
  `sino` int(11) DEFAULT NULL,
  `questions` varchar(255) DEFAULT NULL,
  `answers` varchar(255) DEFAULT NULL,
  `level` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `something2`
--

CREATE TABLE `something2` (
  `sino` int(11) DEFAULT NULL,
  `questions` varchar(255) DEFAULT NULL,
  `answers` varchar(255) DEFAULT NULL,
  `level` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `something3`
--

CREATE TABLE `something3` (
  `sino` int(11) DEFAULT NULL,
  `questions` varchar(255) DEFAULT NULL,
  `answers` varchar(255) DEFAULT NULL,
  `level` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `something4`
--

CREATE TABLE `something4` (
  `sino` int(11) DEFAULT NULL,
  `questions` varchar(255) DEFAULT NULL,
  `answers` varchar(255) DEFAULT NULL,
  `level` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `something4`
--

INSERT INTO `something4` (`sino`, `questions`, `answers`, `level`) VALUES
(0, 'what is capital of telangana? ', 'what is capital of telangana? ', 1),
(1, 'what is capital of westbengal?', 'what is capital of westbengal?', 1),
(2, 'what is capital of madras?', 'what is capital of madras?', 1),
(3, 'what is capital of karnataka?', 'what is capital of karnataka?', 1),
(4, 'what is capital of kochin?', 'what is capital of kochin?', 1),
(4, 'what is capital of kochin?', 'what is capital of kochin?', 1),
(6, 'what is capital of India?', 'what is capital of SouthAfrica?', 2),
(7, 'what is capital of SouthAfrica?', 'what is capital of England?', 2),
(8, 'what is capital of England?', 'what is capital of zimbabwe?', 2),
(8, 'what is capital of England?', 'what is capital of zimbabwe?', 2),
(10, 'what is capital of zimbabwe?', 'what is capital of Andamon and Nicobar?', 3);

-- --------------------------------------------------------

--
-- Table structure for table `something9`
--

CREATE TABLE `something9` (
  `sino` int(11) DEFAULT NULL,
  `questions` varchar(255) DEFAULT NULL,
  `answers` varchar(255) DEFAULT NULL,
  `level` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `something10`
--

CREATE TABLE `something10` (
  `sino` int(11) DEFAULT NULL,
  `questions` varchar(255) DEFAULT NULL,
  `answers` varchar(255) DEFAULT NULL,
  `level` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `somethingamo`
--

CREATE TABLE `somethingamo` (
  `sino` int(11) DEFAULT NULL,
  `questions` varchar(255) DEFAULT NULL,
  `answers` varchar(255) DEFAULT NULL,
  `level` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `somethingamo1`
--

CREATE TABLE `somethingamo1` (
  `sino` int(11) DEFAULT NULL,
  `questions` varchar(255) DEFAULT NULL,
  `answers` varchar(255) DEFAULT NULL,
  `level` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `somethingamo1`
--

INSERT INTO `somethingamo1` (`sino`, `questions`, `answers`, `level`) VALUES
(1, 'what is capital of telangana? ', NULL, 1),
(2, 'what is capital of westbengal?', NULL, 1),
(3, 'what is capital of madras?', NULL, 1),
(4, 'what is capital of karnataka?', NULL, 1),
(5, 'what is capital of kochin?', NULL, 1),
(6, 'what is capital of India?', NULL, 2),
(7, 'what is capital of SouthAfrica?', NULL, 2),
(8, 'what is capital of England?', NULL, 2),
(9, 'what is capital of zimbabwe?', NULL, 3),
(10, 'what is capital of somalia?', NULL, 3),
(11, 'what is capital of Andamon and Nicobar?', NULL, 3);

-- --------------------------------------------------------

--
-- Table structure for table `somethingamo2`
--

CREATE TABLE `somethingamo2` (
  `sino` int(11) DEFAULT NULL,
  `questions` varchar(255) DEFAULT NULL,
  `answers` varchar(255) DEFAULT NULL,
  `level` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `somethingamo2`
--

INSERT INTO `somethingamo2` (`sino`, `questions`, `answers`, `level`) VALUES
(1, 'what is capital of telangana? ', 'uploading..', 1),
(2, 'what is capital of westbengal?', 'uploading..', 1),
(3, 'what is capital of madras?', 'uploading..', 1),
(4, 'what is capital of karnataka?', 'uploading..', 1),
(5, 'what is capital of kochin?', 'uploading..', 1),
(6, 'what is capital of India?', 'uploading..', 2),
(7, 'what is capital of SouthAfrica?', 'uploading..', 2),
(8, 'what is capital of England?', 'uploading..', 2),
(9, 'what is capital of zimbabwe?', 'uploading..', 3),
(10, 'what is capital of somalia?', 'uploading..', 3),
(11, 'what is capital of Andamon and Nicobar?', 'uploading..', 3);

-- --------------------------------------------------------

--
-- Table structure for table `somethingamo3`
--

CREATE TABLE `somethingamo3` (
  `sino` int(11) DEFAULT NULL,
  `questions` varchar(255) DEFAULT NULL,
  `answers` varchar(255) DEFAULT NULL,
  `level` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `somethingamo3`
--

INSERT INTO `somethingamo3` (`sino`, `questions`, `answers`, `level`) VALUES
(1, 'what is capital of telangana? ', 'what is capital of telangana? ', 1),
(2, 'what is capital of westbengal?', 'what is capital of westbengal?', 1),
(3, 'what is capital of madras?', 'what is capital of madras?', 1),
(4, 'what is capital of karnataka?', 'what is capital of karnataka?', 1),
(5, 'what is capital of kochin?', 'what is capital of kochin?', 1),
(6, 'what is capital of India?', 'what is capital of India?', 2),
(7, 'what is capital of SouthAfrica?', 'what is capital of SouthAfrica?', 2),
(8, 'what is capital of England?', 'what is capital of England?', 2),
(9, 'what is capital of zimbabwe?', 'what is capital of zimbabwe?', 3),
(10, 'what is capital of somalia?', 'what is capital of somalia?', 3),
(11, 'what is capital of Andamon and Nicobar?', 'what is capital of Andamon and Nicobar?', 3);

-- --------------------------------------------------------

--
-- Table structure for table `somethingwork`
--

CREATE TABLE `somethingwork` (
  `sino` int(11) DEFAULT NULL,
  `questions` varchar(255) DEFAULT NULL,
  `answers` varchar(255) DEFAULT NULL,
  `level` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `somethingwork`
--

INSERT INTO `somethingwork` (`sino`, `questions`, `answers`, `level`) VALUES
(1, 'what is capital of telangana? ', 'what is capital of telangana? ', 1),
(2, 'what is capital of westbengal?', 'what is capital of westbengal?', 1),
(3, 'what is capital of madras?', 'what is capital of madras?', 1),
(4, 'what is capital of karnataka?', 'what is capital of karnataka?', 1),
(5, 'what is capital of kochin?', 'what is capital of kochin?', 1),
(5, 'what is capital of kochin?', 'what is capital of kochin?', 1),
(6, 'what is capital of India?', 'what is capital of SouthAfrica?', 2),
(7, 'what is capital of SouthAfrica?', 'what is capital of England?', 2),
(8, 'what is capital of England?', 'what is capital of zimbabwe?', 2),
(8, 'what is capital of England?', 'what is capital of zimbabwe?', 2),
(9, 'what is capital of zimbabwe?', 'what is capital of Andamon and Nicobar?', 3);

-- --------------------------------------------------------

--
-- Table structure for table `test123`
--

CREATE TABLE `test123` (
  `sino` int(11) DEFAULT NULL,
  `questions` varchar(255) DEFAULT NULL,
  `answers` varchar(255) DEFAULT NULL,
  `level` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `test123`
--

INSERT INTO `test123` (`sino`, `questions`, `answers`, `level`) VALUES
(1, 'what is capital of telangana? ', 'what is capital of telangana? ', 1),
(2, 'what is capital of westbengal?', 'what is capital of westbengal?', 1),
(3, 'what is capital of madras?', 'what is capital of madras?', 1),
(4, 'what is capital of karnataka?', 'what is capital of karnataka?', 1),
(5, 'what is capital of kochin?', 'what is capital of kochin?', 1),
(6, 'what is capital of India?', 'what is capital of India?', 2),
(7, 'what is capital of SouthAfrica?', 'what is capital of SouthAfrica?', 2),
(8, 'what is capital of England?', 'what is capital of England?', 2),
(9, 'what is capital of zimbabwe?', 'what is capital of zimbabwe?', 3),
(10, 'what is capital of somalia?', 'what is capital of somalia?', 3),
(11, 'what is capital of Andamon and Nicobar?', 'what is capital of Andamon and Nicobar?', 3);

-- --------------------------------------------------------

--
-- Table structure for table `xls`
--

CREATE TABLE `xls` (
  `hello` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
