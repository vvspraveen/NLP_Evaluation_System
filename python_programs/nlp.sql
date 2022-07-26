-- phpMyAdmin SQL Dump
-- version 5.0.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Mar 30, 2020 at 11:43 AM
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
-- Database: `nlp`
--

-- --------------------------------------------------------

--
-- Table structure for table `admin`
--

CREATE TABLE `admin` (
  `username` varchar(255) NOT NULL,
  `password` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `admin`
--

INSERT INTO `admin` (`username`, `password`) VALUES
('admin', 'admin123');

-- --------------------------------------------------------

--
-- Table structure for table `staff_login`
--

CREATE TABLE `staff_login` (
  `username` varchar(255) NOT NULL,
  `password` varchar(255) NOT NULL,
  `branch` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `staff_login`
--

INSERT INTO `staff_login` (`username`, `password`, `branch`) VALUES
('', '', ''),
('', '', ''),
('', '', ''),
('vineeth', 'vinith007', 'cse');

-- --------------------------------------------------------

--
-- Table structure for table `student_register`
--

CREATE TABLE `student_register` (
  `student_name` varchar(255) DEFAULT NULL,
  `student_branch` varchar(255) DEFAULT NULL,
  `student_id` int(11) DEFAULT NULL,
  `student_email` varchar(255) DEFAULT NULL,
  `student_pn` int(11) DEFAULT NULL,
  `student_password` varchar(255) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COMMENT='STUDENT_REG_TABLE';

--
-- Dumping data for table `student_register`
--

INSERT INTO `student_register` (`student_name`, `student_branch`, `student_id`, `student_email`, `student_pn`, `student_password`) VALUES
('vinith CHINTHAKUNTA', 'cse', 2451, 'chinthakuntavineeth@gmail.com', 2147483647, '12345'),
('sri', 'cse', 123578, '', 0, ''),
('latha', 'eee', 12568, 'lath@gmail', 2147483647, 'l123'),
('niraj', 'cse', 898786576, 'niraj@mail', 877868098, 'niraj123'),
('ram', 'CSE', 987676098, 'ram@gmail', 987878767, 'ram123'),
('vineeth', 'cse', 2147483647, 'abc@mail.com', 989898988, '123456'),
('vineeth', 'cse', 2147483647, 'chinthakuntavineeth@gmail.com', 2147483647, '123456');
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
