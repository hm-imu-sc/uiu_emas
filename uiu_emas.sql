-- phpMyAdmin SQL Dump
-- version 5.1.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Dec 02, 2021 at 03:10 PM
-- Server version: 10.4.19-MariaDB
-- PHP Version: 8.0.7

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `uiu_emas`
--

-- --------------------------------------------------------

--
-- Table structure for table `comments`
--

CREATE TABLE `comments` (
  `id` int(255) NOT NULL,
  `time_created` datetime NOT NULL DEFAULT current_timestamp(),
  `time_updated` datetime NOT NULL DEFAULT current_timestamp(),
  `trash` tinyint(1) NOT NULL DEFAULT 0,
  `status` tinyint(1) NOT NULL DEFAULT 0,
  `project_id` int(255) NOT NULL,
  `user_id` int(255) NOT NULL,
  `user_type` varchar(255) NOT NULL,
  `comment` text NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `prizes`
--

CREATE TABLE `prizes` (
  `id` int(255) NOT NULL,
  `time_created` datetime NOT NULL DEFAULT current_timestamp(),
  `time_updated` datetime NOT NULL DEFAULT current_timestamp(),
  `trash` tinyint(1) NOT NULL DEFAULT 0,
  `status` tinyint(1) NOT NULL DEFAULT 0,
  `project_id` int(255) NOT NULL,
  `student_id` varchar(255) NOT NULL,
  `prize` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `projects`
--

CREATE TABLE `projects` (
  `id` int(255) NOT NULL,
  `time_created` datetime NOT NULL DEFAULT current_timestamp(),
  `time_updated` datetime NOT NULL DEFAULT current_timestamp(),
  `trash` tinyint(1) NOT NULL DEFAULT 0,
  `status` tinyint(1) NOT NULL DEFAULT 0,
  `title` varchar(255) NOT NULL,
  `section_id` int(255) NOT NULL,
  `short_description` text NOT NULL,
  `intro_video` varchar(255) DEFAULT NULL,
  `report` varchar(255) DEFAULT NULL,
  `trimester` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `project_members`
--

CREATE TABLE `project_members` (
  `id` int(255) NOT NULL,
  `time_created` datetime NOT NULL DEFAULT current_timestamp(),
  `time_updated` datetime NOT NULL DEFAULT current_timestamp(),
  `trash` tinyint(1) NOT NULL DEFAULT 0,
  `status` tinyint(1) NOT NULL DEFAULT 0,
  `project_id` int(255) NOT NULL,
  `student_id` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `project_videos`
--

CREATE TABLE `project_videos` (
  `id` int(255) NOT NULL,
  `time_created` datetime NOT NULL DEFAULT current_timestamp(),
  `time_updated` datetime NOT NULL DEFAULT current_timestamp(),
  `trash` tinyint(1) NOT NULL DEFAULT 0,
  `status` tinyint(1) NOT NULL DEFAULT 0,
  `project_id` int(255) NOT NULL,
  `path` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `sections`
--

CREATE TABLE `sections` (
  `id` int(255) NOT NULL,
  `time_created` datetime NOT NULL DEFAULT current_timestamp(),
  `time_updated` datetime NOT NULL DEFAULT current_timestamp(),
  `trash` tinyint(1) NOT NULL DEFAULT 0,
  `status` tinyint(1) NOT NULL DEFAULT 0,
  `name` varchar(1) NOT NULL,
  `course_code` varchar(255) NOT NULL,
  `course_name` varchar(255) NOT NULL,
  `teacher_id` varchar(255) NOT NULL,
  `trimester` varchar(3) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `students`
--

CREATE TABLE `students` (
  `id` int(255) NOT NULL,
  `time_created` datetime NOT NULL DEFAULT current_timestamp(),
  `time_updated` datetime NOT NULL DEFAULT current_timestamp(),
  `trash` tinyint(1) NOT NULL DEFAULT 0,
  `status` tinyint(1) NOT NULL DEFAULT 0,
  `student_id` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `uiu_email` varchar(255) NOT NULL,
  `dob` date NOT NULL,
  `department` varchar(255) NOT NULL,
  `photo` varchar(255) NOT NULL,
  `password_hash` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `teachers`
--

CREATE TABLE `teachers` (
  `id` int(255) NOT NULL,
  `time_created` datetime NOT NULL DEFAULT current_timestamp(),
  `time_updated` datetime NOT NULL DEFAULT current_timestamp(),
  `trash` tinyint(1) NOT NULL DEFAULT 0,
  `status` tinyint(1) NOT NULL DEFAULT 0,
  `name` varchar(255) NOT NULL,
  `employee_id` varchar(255) NOT NULL,
  `uiu_email` varchar(255) NOT NULL,
  `dob` date NOT NULL,
  `department` varchar(255) NOT NULL,
  `photo` varchar(255) NOT NULL,
  `password_hash` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Indexes for dumped tables
--

--
-- Indexes for table `comments`
--
ALTER TABLE `comments`
  ADD PRIMARY KEY (`id`),
  ADD KEY `project_id_c` (`project_id`);

--
-- Indexes for table `prizes`
--
ALTER TABLE `prizes`
  ADD PRIMARY KEY (`id`),
  ADD KEY `project_id` (`project_id`),
  ADD KEY `student_id` (`student_id`);

--
-- Indexes for table `projects`
--
ALTER TABLE `projects`
  ADD PRIMARY KEY (`id`),
  ADD KEY `section_id` (`section_id`);

--
-- Indexes for table `project_members`
--
ALTER TABLE `project_members`
  ADD PRIMARY KEY (`id`),
  ADD KEY `project_id_m` (`project_id`),
  ADD KEY `student_id_m` (`student_id`);

--
-- Indexes for table `project_videos`
--
ALTER TABLE `project_videos`
  ADD PRIMARY KEY (`id`),
  ADD KEY `project_id_v` (`project_id`);

--
-- Indexes for table `sections`
--
ALTER TABLE `sections`
  ADD PRIMARY KEY (`id`),
  ADD KEY `teacher_id` (`teacher_id`);

--
-- Indexes for table `students`
--
ALTER TABLE `students`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `student_id` (`student_id`),
  ADD UNIQUE KEY `uiu_email` (`uiu_email`);

--
-- Indexes for table `teachers`
--
ALTER TABLE `teachers`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `employee_id` (`employee_id`),
  ADD UNIQUE KEY `uiu_email` (`uiu_email`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `comments`
--
ALTER TABLE `comments`
  MODIFY `id` int(255) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `prizes`
--
ALTER TABLE `prizes`
  MODIFY `id` int(255) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `projects`
--
ALTER TABLE `projects`
  MODIFY `id` int(255) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `project_members`
--
ALTER TABLE `project_members`
  MODIFY `id` int(255) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `sections`
--
ALTER TABLE `sections`
  MODIFY `id` int(255) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `students`
--
ALTER TABLE `students`
  MODIFY `id` int(255) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `teachers`
--
ALTER TABLE `teachers`
  MODIFY `id` int(255) NOT NULL AUTO_INCREMENT;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `comments`
--
ALTER TABLE `comments`
  ADD CONSTRAINT `project_id_c` FOREIGN KEY (`project_id`) REFERENCES `projects` (`id`);

--
-- Constraints for table `prizes`
--
ALTER TABLE `prizes`
  ADD CONSTRAINT `project_id` FOREIGN KEY (`project_id`) REFERENCES `projects` (`id`),
  ADD CONSTRAINT `student_id` FOREIGN KEY (`student_id`) REFERENCES `students` (`student_id`);

--
-- Constraints for table `projects`
--
ALTER TABLE `projects`
  ADD CONSTRAINT `section_id` FOREIGN KEY (`section_id`) REFERENCES `sections` (`id`);

--
-- Constraints for table `project_members`
--
ALTER TABLE `project_members`
  ADD CONSTRAINT `project_id_m` FOREIGN KEY (`project_id`) REFERENCES `projects` (`id`),
  ADD CONSTRAINT `student_id_m` FOREIGN KEY (`student_id`) REFERENCES `students` (`student_id`);

--
-- Constraints for table `project_videos`
--
ALTER TABLE `project_videos`
  ADD CONSTRAINT `project_id_v` FOREIGN KEY (`project_id`) REFERENCES `projects` (`id`);

--
-- Constraints for table `sections`
--
ALTER TABLE `sections`
  ADD CONSTRAINT `teacher_id` FOREIGN KEY (`teacher_id`) REFERENCES `teachers` (`employee_id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
