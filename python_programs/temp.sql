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
-- Database: `temp`
--

-- --------------------------------------------------------

--
-- Table structure for table `math`
--

CREATE TABLE `math` (
  `employee_id` int(3) NOT NULL,
  `employee_sal` float NOT NULL,
  `employee_num` int(10) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COMMENT='employee_table';
-- Error reading data for table temp.math: #1064 - You have an error in your SQL syntax; check the manual that corresponds to your MariaDB server version for the right syntax to use near 'FROM `temp`.`math`' at line 1

-- --------------------------------------------------------

--
-- Table structure for table `roll_2147483647`
--

CREATE TABLE `roll_2147483647` (
  `sino` int(11) DEFAULT NULL,
  `questions` varchar(255) DEFAULT NULL,
  `original_answers` varchar(255) DEFAULT NULL,
  `written_answers` varchar(255) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `roll_2147483647`
--

INSERT INTO `roll_2147483647` (`sino`, `questions`, `original_answers`, `written_answers`) VALUES
(0, 'what is capital of zimbabwe?', 'what is capital of zimbabwe?', 'what is capital of zimbabwe?\r\n'),
(1, 'what is capital of India?', 'what is capital of India?', 'what is capital of India?'),
(2, 'what is capital of karnataka?', 'what is capital of karnataka?', 'what is capital of karnataka?\r\n'),
(3, 'what is capital of westbengal?', 'what is capital of westbengal?', 'what is capital of westbengal?\r\n'),
(4, 'what is capital of telangana? ', 'what is capital of telangana? ', 'what is capital of telangana?\r\n'),
(5, 'what is capital of somalia?', 'what is capital of somalia?', 'what is capital of somalia?\r\n'),
(6, 'what is capital of SouthAfrica?', 'what is capital of SouthAfrica?', 'what is capital of SouthAfrica?');

-- --------------------------------------------------------

--
-- Table structure for table `sample`
--

CREATE TABLE `sample` (
  `a` int(11) NOT NULL,
  `c` date NOT NULL,
  `d` decimal(10,0) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `sample`
--

INSERT INTO `sample` (`a`, `c`, `d`) VALUES
(1, '2026-09-10', '45'),
(2, '2014-09-07', '100'),
(2, '2014-09-07', '100'),
(2, '2014-09-07', '100'),
(3, '0000-00-00', '45'),
(3, '0000-00-00', '45'),
(4, '0000-00-00', '45'),
(9, '0000-00-00', '78');
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
