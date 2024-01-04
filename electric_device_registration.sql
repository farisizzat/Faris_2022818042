-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Jan 04, 2024 at 01:48 PM
-- Server version: 10.4.32-MariaDB
-- PHP Version: 8.2.12

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `electric_device_registration`
--

-- --------------------------------------------------------

--
-- Table structure for table `registration_information`
--

CREATE TABLE `registration_information` (
  `Student_name` text NOT NULL,
  `Student_id_number` int(10) NOT NULL,
  `Student_room_number` varchar(5) NOT NULL,
  `Student_college` text NOT NULL,
  `Student_gender` text NOT NULL,
  `Student_total_device` varchar(20) NOT NULL,
  `total_price` varchar(5) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `registration_information`
--

INSERT INTO `registration_information` (`Student_name`, `Student_id_number`, `Student_room_number`, `Student_college`, `Student_gender`, `Student_total_device`, `total_price`) VALUES
('MUHAMMAD HANIF AIMAN KAMARUZAMAN', 2022871792, 'A021', 'Malinja', 'Men', '3', ''),
('FARIS IZZAT', 2022818042, 'A012', 'Malinja', 'Men', '4', ''),
('MUHAMMAD AMMAR BIN KHAMISAN', 2022667383, 'A120', 'Malinja', 'Men', '10', '100'),
('hafizul zaheen', 2022661936, 'B318', 'Melati', 'Men', '8', '80'),
('', 0, '', '', '', '3', '30'),
('', 0, '', '', '', '2', '20'),
('', 0, '', '', '', '5', '50'),
('', 0, '', '', '', '7', '70'),
('MUHAMMAD HANIF AIMAN BIN KAMARUZAMAN ', 2022871792, 'A021', 'Malinja', 'Men', '2', '20'),
('MUHAMMAD FARIS IZZAT BIN TIRMIZI', 2022862749, '', 'Malinja', 'Men', '6', '60');
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
