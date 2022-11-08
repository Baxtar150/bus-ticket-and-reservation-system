-- phpMyAdmin SQL Dump
-- version 5.2.0
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Nov 08, 2022 at 02:08 PM
-- Server version: 10.4.24-MariaDB
-- PHP Version: 7.4.29

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `booking`
--

-- --------------------------------------------------------

--
-- Table structure for table `buses`
--

CREATE TABLE `buses` (
  `bus_id` varchar(10) NOT NULL,
  `bus_type` varchar(20) NOT NULL,
  `bus_color` varchar(20) NOT NULL,
  `bus_seat` varchar(10) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `commuter`
--

CREATE TABLE `commuter` (
  `bus_id` varchar(10) NOT NULL,
  `boarding` varchar(20) NOT NULL,
  `destination` varchar(20) NOT NULL,
  `bus_stop` varchar(20) NOT NULL,
  `passenger_no` int(2) NOT NULL,
  `Ticket_no` varchar(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `commuter`
--

INSERT INTO `commuter` (`bus_id`, `boarding`, `destination`, `bus_stop`, `passenger_no`, `Ticket_no`) VALUES
('A1001', 'Adamawa State', 'Adamawa State', 'Mubi', 2, '1000172jb'),
('A1003', 'Anambra State', 'Cross River State', 'Calabar', 2, '1004185se');

-- --------------------------------------------------------

--
-- Table structure for table `drivers`
--

CREATE TABLE `drivers` (
  `bus_id` varchar(10) NOT NULL,
  `driver_name` varchar(50) NOT NULL,
  `driver_phone` varchar(20) NOT NULL,
  `driver_route` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `users`
--

CREATE TABLE `users` (
  `Fullname` varchar(50) NOT NULL,
  `Email` varchar(100) NOT NULL,
  `Phone` varchar(20) NOT NULL,
  `Gender` varchar(10) NOT NULL,
  `Marital_status` varchar(20) NOT NULL,
  `DOB` date NOT NULL,
  `Password` text NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `users`
--

INSERT INTO `users` (`Fullname`, `Email`, `Phone`, `Gender`, `Marital_status`, `DOB`, `Password`) VALUES
('Muritala', 'koko@gmail.com', '08100000000', 'Male', 'Single', '2010-03-02', '12345'),
('qwert', 'qwert', 'qwert', 'Male', 'Single', '0000-00-00', '12345');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `buses`
--
ALTER TABLE `buses`
  ADD PRIMARY KEY (`bus_id`);

--
-- Indexes for table `commuter`
--
ALTER TABLE `commuter`
  ADD PRIMARY KEY (`bus_id`),
  ADD UNIQUE KEY `Ticket_no` (`Ticket_no`);

--
-- Indexes for table `drivers`
--
ALTER TABLE `drivers`
  ADD PRIMARY KEY (`bus_id`),
  ADD UNIQUE KEY `driver_phone` (`driver_phone`);

--
-- Indexes for table `users`
--
ALTER TABLE `users`
  ADD PRIMARY KEY (`Email`),
  ADD UNIQUE KEY `Phone` (`Phone`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
