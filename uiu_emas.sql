-- phpMyAdmin SQL Dump
-- version 5.1.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Jan 18, 2022 at 06:12 AM
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
-- Database: `uiu_emas_2`
--

-- --------------------------------------------------------

--
-- Table structure for table `booths`
--

CREATE TABLE `booths` (
  `id` int(255) NOT NULL,
  `time_created` datetime NOT NULL DEFAULT current_timestamp(),
  `time_updated` datetime NOT NULL DEFAULT current_timestamp(),
  `trash` tinyint(1) NOT NULL DEFAULT 0,
  `status` tinyint(1) NOT NULL DEFAULT 0,
  `club_id` varchar(255) NOT NULL,
  `intro_video` varchar(255) NOT NULL,
  `club_description` text NOT NULL,
  `recruiting` tinyint(1) NOT NULL DEFAULT 0
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `cff_comments`
--

CREATE TABLE `cff_comments` (
  `id` int(255) NOT NULL,
  `time_created` datetime NOT NULL DEFAULT current_timestamp(),
  `time_updated` datetime NOT NULL DEFAULT current_timestamp(),
  `trash` tinyint(1) NOT NULL DEFAULT 0,
  `status` tinyint(1) NOT NULL DEFAULT 0,
  `club_id` varchar(255) NOT NULL,
  `user_id` varchar(255) NOT NULL,
  `user_type` varchar(255) NOT NULL,
  `comment` text NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `cff_registrations`
--

CREATE TABLE `cff_registrations` (
  `id` int(255) NOT NULL,
  `time_created` datetime NOT NULL DEFAULT current_timestamp(),
  `time_updated` datetime NOT NULL DEFAULT current_timestamp(),
  `trash` tinyint(1) NOT NULL DEFAULT 0,
  `status` tinyint(1) NOT NULL DEFAULT 0,
  `student_id` varchar(255) NOT NULL,
  `club_id` varchar(255) NOT NULL,
  `t_shirt_size` varchar(255) NOT NULL,
  `approval` tinyint(1) NOT NULL DEFAULT 0,
  `year` year(4) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `cff_registrations`
--

INSERT INTO `cff_registrations` (`id`, `time_created`, `time_updated`, `trash`, `status`, `student_id`, `club_id`, `t_shirt_size`, `approval`, `year`) VALUES
(2, '2022-01-07 21:00:12', '2022-01-07 21:00:12', 0, 0, '011181076', '1', 'XL', 0, 0000),
(3, '2022-01-09 16:23:19', '2022-01-09 16:23:19', 0, 0, '011181076', '1', 'XL', 0, 0000);

-- --------------------------------------------------------

--
-- Table structure for table `clubs`
--

CREATE TABLE `clubs` (
  `id` int(255) NOT NULL,
  `time_created` datetime NOT NULL DEFAULT current_timestamp(),
  `time_updated` datetime NOT NULL DEFAULT current_timestamp(),
  `trash` tinyint(1) NOT NULL DEFAULT 0,
  `status` tinyint(1) NOT NULL DEFAULT 0,
  `name` varchar(255) NOT NULL,
  `club_id` varchar(255) NOT NULL,
  `email` varchar(255) NOT NULL,
  `creation_date` date NOT NULL,
  `department` varchar(255) NOT NULL,
  `logo_path` varchar(255) NOT NULL,
  `cff_registration_status` tinyint(1) NOT NULL DEFAULT 0,
  `password_hash` varchar(256) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `clubs`
--

INSERT INTO `clubs` (`id`, `time_created`, `time_updated`, `trash`, `status`, `name`, `club_id`, `email`, `creation_date`, `department`, `logo_path`, `cff_registration_status`, `password_hash`) VALUES
(1, '2022-01-07 20:29:35', '2022-01-07 20:29:35', 0, 0, 'UIU Computer Club', '1', 'uiuccl@cse.uiu.ac.bd', '0000-00-00', 'CSE', '', 0, ''),
(2, '2022-01-07 20:29:35', '2022-01-07 20:29:35', 0, 0, 'UIU App Forum', '2', 'uiuappforum@gmail.com', '0000-00-00', 'CSE', '', 0, ''),
(3, '2022-01-07 20:29:35', '2022-01-07 20:29:35', 0, 0, 'UIU Business Club', '3', 'uiubc@gmail.com', '0000-00-00', 'BBA', '', 0, ''),
(4, '2022-01-07 20:29:35', '2022-01-07 20:29:35', 0, 0, 'UIU Robotics Club', '4', 'uiurobotics@gmail.com', '0000-00-00', 'CSE', '', 0, ''),
(5, '2022-01-07 20:29:35', '2022-01-07 20:29:35', 0, 0, 'UIU Electrical and Electronics Club', '5', 'uiueec@gmail.com', '0000-00-00', 'EEE', '', 0, ''),
(6, '2022-01-09 16:22:39', '2022-01-09 16:22:39', 0, 1, 'UIU Marketing Forum', '6', 'uiumf@gmail.com', '0000-00-00', 'BBA', '', 1, '');

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
-- Table structure for table `events`
--

CREATE TABLE `events` (
  `id` int(255) NOT NULL,
  `time_created` datetime NOT NULL DEFAULT current_timestamp(),
  `time_updated` datetime NOT NULL DEFAULT current_timestamp(),
  `trash` tinyint(1) NOT NULL DEFAULT 0,
  `status` tinyint(1) NOT NULL DEFAULT 0,
  `club_id` varchar(255) NOT NULL,
  `title` varchar(255) NOT NULL,
  `cover_photo_path` varchar(255) NOT NULL,
  `description` text NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `feed_posts`
--

CREATE TABLE `feed_posts` (
  `id` int(255) NOT NULL,
  `time_created` datetime NOT NULL DEFAULT current_timestamp(),
  `time_updated` datetime NOT NULL DEFAULT current_timestamp(),
  `trash` tinyint(1) NOT NULL DEFAULT 0,
  `status` tinyint(1) NOT NULL DEFAULT 0,
  `club_id` varchar(255) NOT NULL,
  `image_path` varchar(255) NOT NULL,
  `caption` text NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `feed_posts`
--

INSERT INTO `feed_posts` (`id`, `time_created`, `time_updated`, `trash`, `status`, `club_id`, `image_path`, `caption`) VALUES
(1, '2022-01-12 21:03:35', '0000-00-00 00:00:00', 0, 0, '1', 'feed_posts_0_image_path.jpg', 'We provide free sleeping facilities for club members'),
(2, '2022-01-11 21:03:42', '0000-00-00 00:00:00', 0, 0, '4', 'feed_posts_2_image_path.jpg', 'Get registered today!!!'),
(3, '2022-01-10 21:03:44', '0000-00-00 00:00:00', 0, 0, '4', 'feed_posts_3_image_path.png', 'A new year, a new opportunity to be better.\n\nThe new year is a 365 pages new chapter. Let\'s start the chapter together.\n\nYes, you are guessing the right! UIU Robotics is arranging member recruitment for all the enthusiast people from UIU. There will be many more arrangements that will add new dimensions to your old year memories.\n\nLet\'s celebrate the old and new together. So, what else you are looking for! Join the UIU Robotics.\n\nRegistration Link: http://robotics.uiu.ac.bd/recruitment2022\n\nFor any information, contact us at any time.\n\nFacebook Event link: https://fb.me/e/1XrT6bq5o\nMail Us: robotics@uiu.ac.bd\n\nMiftahul Islam Mozumder,\nGeneral Secretary, UIU Robotics\nMobile: 01731628628\n\nM. Abdullah Khan\nPublic Relations Secretary, UIU Robotics\nMobile: 01521715781'),
(4, '2022-01-10 21:03:46', '0000-00-00 00:00:00', 0, 0, '2', 'feed_posts_4_image_path.jpg', 'Assalamualaikum Everyone !\r\nWe are happy to announce that after the success of â€œProgramming for beginners: seasons 1 to 4, we are again back with â€œProgramming for beginners season 5 (Fall 2021)â€. This is a training program that is organized every trimester by UIU APP Forum. It is open for all students of UIU. It will be a four class training program designed to teach the C programming language. After the whole training program, learners have the working knowledge to start programming, debugging and using the C programming language which will be beneficial for their skill development and academic courses. Once the training program has reached its completion, we will also arrange a programming contest and prize giving ceremony.\r\nInstructor:\r\nNiloy Kumar Kundu\r\nInstructor\r\nApp Forum\r\nUnited International University\r\nRegistration fee:\r\nNon App Forum member: 100 BDT\r\nApp Forum member: Free\r\nRegistration link: https://forms.gle/rak43RzQ8VJ14BEfA'),
(5, '2022-01-10 21:03:47', '0000-00-00 00:00:00', 0, 0, '1', 'feed_posts_5_image_path.jpg', 'We have already got the notice from the university that curriculums are going to be held online.\nWe have talked to the department, and we got the green light to hold our event tomorrow.\nBut we will highly appreciate you following the necessary precautions.'),
(6, '2022-01-11 21:10:21', '0000-00-00 00:00:00', 0, 0, '1', 'feed_posts_6_image_path.jpg', 'We are immensely delighted to inform you that our program \"Programmer Doctor\'s Chamber\" went exceptionally well through the participation of our beloved juniors. We can not thank you enough for your love and appreciation throughout the event.  \r\nApproximately, 60 of our beloved junior brothers and sisters took help from us. Your love and support help us to step forward.\r\nThanks, everyone for coming, and keep expecting more from us. Hopefully, we can help you more in the coming days. \r\nSpecial thanks to our Programming Wing & Executive Members.'),
(7, '2022-01-10 21:10:26', '0000-00-00 00:00:00', 0, 0, '4', 'feed_posts_7_image_path.png', 'UIU Cultural Club is inviting everyone from UIU family to enjoy the amazing 2 day long fest on 27th and 28th of November 2021 titled CLUB FORUM FEST- 2021. Our #UIURobotics family will be there in this gorgeous fest. You are cordially requested to visit the stall of UIU Robotics with your friends. Please ensure your participation as T-shirt, food coupon and other things will be provided through our stall. \r\nOut stall number: 06 (1st floor, near the ground stairs)\r\nJoin this festival along with your friends and make this event successful. We hope to see you all. If you have any questions or concerns please feel free to contact us. \r\nTo upload your profile picture frame, Please go to the link: https://twb.nz/uiucff\r\n-Upload your photo to attach the frame\r\n-Download and upload it to Facebook\r\n#UIUCCF #UIU_Robotics'),
(8, '2022-01-10 21:10:28', '0000-00-00 00:00:00', 0, 0, '2', 'feed_posts_8_image_path.jpg', 'Hero Presents \'UIU Club-Forum Fest 2021\'\r\n\r\nUIU Career Counseling Center & UIU Directorate of Student Affairs in association with UIU Cultural Club are going to organize \'UIU Club-Forum Fest 2021\''),
(9, '2022-01-10 21:10:29', '0000-00-00 00:00:00', 0, 0, '2', 'feed_posts_9_image_path.PNG', 'Come and Join us. Your life will look like this.'),
(10, '2022-01-10 21:10:30', '0000-00-00 00:00:00', 0, 0, '1', 'feed_posts_10_image_path.jpg', 'SUNSET BBQ'),
(11, '2022-01-10 21:10:31', '0000-00-00 00:00:00', 0, 0, '1', 'feed_posts_11_image_path.jpg', 'Are you a CS graduate and looking for deserving jobs? We are thrilled to inform you, UIU Computer Club alongside TechnTalents are going to organize an â€œICT job fair and career pathwayâ€ event at UIU. TechnTalents are working with a motivation to facilitate the right talents on the right job. The event will consist of several segments including an on spot interview and ICT career seminar. Those who aren\'t graduates will get the chance to connect with the community, get tips and tricks about career and can win prizes through playing quizzes.\n\nUIU Computer Club plays the role of a middleware to connect the industry with the students of UIU. We focus on guiding our junior brothers and sisters to become an asset for the industry through several seminars, workshops and events. This event can be a great way of kickstarting your career or choosing the right way for you.\n\nSo, what are you waiting for? Register yourself for the event.\n\nRegistration & Jobs Link: https://forms.gle/1vQaghiVUCddoxjT8\n\nEvent Page - https://fb.me/e/24yIKR5Hd '),
(12, '2022-01-11 13:38:20', '0000-00-00 00:00:00', 0, 0, '1', 'feed_posts_12_image_path.jpg', 'Just relax !!!'),
(13, '2022-01-11 13:52:27', '0000-00-00 00:00:00', 0, 0, '1', 'feed_posts_13_image_path.jpg', 'Hello folks!\r\nComputer Club will be organizing events on upcoming days. For securing organizing excellence, we need you to join our team. We\'re gleefully encouraging you to be a part of the UIU Computer Club as a volunteer.\r\n\r\nPlease fill-up the form ASAP.\r\nhttps://forms.gle/3RovNDsqszvPciFh6\r\n\r\n**Only the selected ones will be joining**'),
(14, '2022-01-11 13:53:11', '0000-00-00 00:00:00', 0, 0, '1', 'feed_posts_14_image_path.jpg', 'We know the MID exam is knocking at the door! We also know you, fellow CSE students, are anxious about the upcoming programming courses.\r\nNO WORRIES!!!\r\nTo ease your bright minds our Programming Wing Team, will be present in Computer Laboratory 12 on Tuesday and Wednesday (07/12/21 - 08/12/21) from 11:00 AM to 03:00 PM to help you out completely FREE OF COST.\r\nDon\'t hesitate to come by and get all the help you need from your beloved Computer Club. We are looking forward to see you.\r\nComputer Laboratory 12 ( 0532 )'),
(15, '2022-01-11 13:54:14', '0000-00-00 00:00:00', 0, 0, '2', 'feed_posts_15_image_path.jpg', 'Are you handling healthcare data? Want to know where and how to start with?\r\nCome join us. Learn healthcare data analysis with Python. Data Exploration, Visualization, Preparation, Prediction, Imputation. Two 90 minutes classes will give you sufficient idea to start visualizing, exploring healthcare data and making predictions.\r\nRegistration required by Sept 30. Register at: https://summit21.socialtech.global.'),
(16, '2022-01-11 15:34:07', '0000-00-00 00:00:00', 0, 0, '2', 'feed_posts_16_image_path.jpg', 'Programming for Beginners\r\nSeason 4\r\nAssalamualaikum Everyone!\r\nWe are very glad to announce that, we have successfully completed the 4th season of \"Programming for Beginners\". And, hopefully, this is just the beginning for all the people who have attended this workshop. The motive was to build your concept even better than before and encourage you to the path to your goal. We wanted to see your betterment and we are happy to see your efforts for that. All of you are appreciated who was there till the end. We have seen some good projects as the outcome. To appreciate the good projects and encourage the efforts given by you, we have come up with the name of the merit position holders of the Project Show.\r\nCongratulations to the prize winners and don\'t get disheartened who havenâ€™t got the prize. Wish you all the very best for the future!'),
(17, '2022-01-11 15:35:19', '0000-00-00 00:00:00', 0, 0, '4', 'feed_posts_17_image_path.jpg', '24 hours left! Hurry Up!\r\nDear competitive Programming Enthusiasts, \r\nHope you are doing well with problem-solving!\r\nIf you want to find the right way to start the competitive programming journey, \r\njoin Hashcoders: Virtual Competitive Programming adda with Mohammad Maruf Imtiaze. '),
(18, '2022-01-11 15:36:00', '0000-00-00 00:00:00', 0, 0, '4', 'feed_posts_18_image_path.jpg', 'Hello, graphic design enthusiasts!\r\nUIU Robotics is looking for some dedicated people to work as graphic designers. If you are flexible, committed, and have a keen eye for design, then this post is for you!\r\nRead the instructions below and fill up the form by scanning the QR code or visiting the link at the end of the post.\r\nInstructions:\r\n1. Provide your official UIU email address in the form and you will be contacted through email if selected.\r\n2. Upload 3 to 5 graphic designs which you have created in a Google Drive folder and set the visibility to \"Anyone with the link.\"\r\n3. Copy and paste that folder\'s link in the \"Portfolio Drive link\" field of the form. '),
(19, '2022-01-11 15:36:46', '0000-00-00 00:00:00', 0, 0, '1', 'feed_posts_19_image_path.png', '#UIUCPwaitinglist.\r\nGreat news for the participants of UIUCP. We are really excited to share opportunities with a few of our participants. These people are also selected for the CP Season 11. Congratulations.\r\nWe request all of the selected members to join the group within 5 PM, tomorrow. \r\nhere is the link,'),
(20, '2022-01-11 15:37:39', '0000-00-00 00:00:00', 0, 0, '4', 'feed_posts_20_image_path.png', 'Here\'s praying for your good health on the auspicious occasion of Durga Puja Maha Ashtami. Durga Ashtami, also known as Maha Ashtami, is one of the most special occasions of the Durga Puja Celebration. Happy Ashami! \r\n#durgapuja2021#uiu_robotics'),
(21, '2022-01-11 15:38:20', '0000-00-00 00:00:00', 0, 0, '1', 'feed_posts_21_image_path.jpg', '#UIUCPresult\r\nUIU Computer Club works with the vision to enhance the quality of programming in our students. Yesterday we organized an examination  to choose the finest blood of programming at UIU. Selected people will go through several grooming sessions and will be mentored by our trainers who have several years of programming contest experience.\r\nSo, Here is our result sheet. Selected members are requested to have an eye on our page for the future update.\r\nCongratulations to the selected members and don\'t lose hope for those who aren\'t selected this time.\r\n#1'),
(22, '2022-01-11 15:39:02', '0000-00-00 00:00:00', 0, 0, '2', 'feed_posts_22_image_path.png', 'Assalamualaikum,\r\nIn UIU APP FORUM we select instructors each trimester. \r\nThey instruct in workshops, help to solve problems of students and many more. It is one of the most respected position in UIU APP FORUM.\r\nAre you a Student of UIU? then be an instructor!! Apply in this form:\r\nhttps://docs.google.com/.../12lcUx4fJ8RHertehASa8Yn9.../edit\r\nAny student of UIU who is studying in CSE  can apply. If you get selected as an instructor, you will be given a free membership at UIU APP FORUM.'),
(23, '2022-01-11 15:39:49', '0000-00-00 00:00:00', 0, 0, '2', 'feed_posts_23_image_path.png', 'We wish you and your family a happy, healthy, and joyful Eid-Al-Adha Mubarak ðŸŒ™ðŸªðŸ‚ðŸ'),
(24, '2022-01-11 15:40:55', '0000-00-00 00:00:00', 0, 0, '1', 'feed_posts_24_image_path.jpg', '\"The Show Must Go On\"\r\nEven though we are going through a hectic situation but we still have to get the job done, to cope up with the real world.\r\nSo, lately, our beloved UIU Computer Club declared its new executive panel with such kind of courageous, energetic and passionate people.\r\n\"Alone we can do so little,together we can do so much.\" â€“ Helen Keller\r\nMay the sunshine pave the path of 1 and help all of us to build up a better future for all.\r\n#1\r\n#UIUComputerClub\r\n#WeAreWhatWeDo'),
(25, '2022-01-11 15:42:05', '0000-00-00 00:00:00', 0, 0, '4', 'feed_posts_25_image_path.jpg', 'A great teacher is one who knows their students, motivates them, and helps them evolve. You are definitely one of the greatest. We are lucky enough that we have had the opportunity to work with you and we are eagerly waiting to work with you and learn from you more in the future.\r\nWe wish you a very happy birthday dear Akib Zaman  sir.');

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

--
-- Dumping data for table `projects`
--

INSERT INTO `projects` (`id`, `time_created`, `time_updated`, `trash`, `status`, `title`, `section_id`, `short_description`, `intro_video`, `report`, `trimester`) VALUES
(1, '2021-12-05 20:27:24', '2021-12-05 20:27:24', 0, 1, 'uiu_emas', 3, 'Lorem ipsum dolor sit amet consectetur adipisicing elit. Minima sequi quos debitis in aliquam, dignissimos perferendis ab iure molestiae libero incidunt possimus ratione, inventore iste explicabo pariatur provident laborum suscipit voluptate accusamus? Nostrum, sit sapiente magnam repellat ab eaque doloribus facere nobis aspernatur officiis! Perspiciatis ipsum cum repellendus nobis totam.', 'projects-1-intro_video.mp4', 'projects-1-report.pdf', '213'),
(2, '2021-12-05 20:27:58', '2021-12-05 20:27:58', 0, 1, 'hostel_chai', 4, 'Lorem ipsum dolor sit amet consectetur adipisicing elit. Minima sequi quos debitis in aliquam, dignissimos perferendis ab iure molestiae libero incidunt possimus ratione, inventore iste explicabo pariatur provident laborum suscipit voluptate accusamus? Nostrum, sit sapiente magnam repellat ab eaque doloribus facere nobis aspernatur officiis! Perspiciatis ipsum cum repellendus nobis totam.', '', '', '213'),
(3, '2021-12-07 22:57:13', '2021-12-07 22:57:13', 0, 1, 'UIU kisu pari na', 6, 'Lorem ipsum dolor sit amet consectetur adipisicing elit. Minima sequi quos debitis in aliquam, dignissimos perferendis ab iure molestiae libero incidunt possimus ratione, inventore iste explicabo pariatur provident laborum suscipit voluptate accusamus? Nostrum, sit sapiente magnam repellat ab eaque doloribus facere nobis aspernatur officiis! Perspiciatis ipsum cum repellendus nobis totam.', '', '', '213'),
(4, '2021-12-07 23:02:53', '2021-12-07 23:02:53', 0, 1, 'UIU_naiko', 5, 'Lorem ipsum dolor sit amet consectetur adipisicing elit. Minima sequi quos debitis in aliquam, dignissimos perferendis ab iure molestiae libero incidunt possimus ratione, inventore iste explicabo pariatur provident laborum suscipit voluptate accusamus? Nostrum, sit sapiente magnam repellat ab eaque doloribus facere nobis aspernatur officiis! Perspiciatis ipsum cum repellendus nobis totam.', '', '', '213'),
(5, '2022-01-07 11:54:39', '2022-01-07 11:54:39', 0, 0, 'UIU_nayok', 2, 'Lorem ipsum dolor sit amet consectetur adipisicing elit. Minima sequi quos debitis in aliquam, dignissimos perferendis ab iure molestiae libero incidunt possimus ratione, inventore iste explicabo pariatur provident laborum suscipit voluptate accusamus? Nostrum, sit sapiente magnam repellat ab eaque doloribus facere nobis aspernatur officiis! Perspiciatis ipsum cum repellendus nobis totam.', '', '', '213'),
(8, '2022-01-07 16:53:52', '2022-01-07 16:53:52', 0, 1, 'UIU_AWESOME', 7, 'Lorem ipsum dolor sit amet consectetur adipisicing elit. Minima sequi quos debitis in aliquam, dignissimos perferendis ab iure molestiae libero incidunt possimus ratione, inventore iste explicabo pariatur provident laborum suscipit voluptate accusamus? Nostrum, sit sapiente magnam repellat ab eaque doloribus facere nobis aspernatur officiis! Perspiciatis ipsum cum repellendus nobis totam.', '', '', '212'),
(9, '2022-01-07 17:04:25', '2022-01-07 17:04:25', 0, 1, 'UIU_AWESOME2', 1, 'Lorem ipsum dolor sit amet consectetur adipisicing elit. Minima sequi quos debitis in aliquam, dignissimos perferendis ab iure molestiae libero incidunt possimus ratione, inventore iste explicabo pariatur provident laborum suscipit voluptate accusamus? Nostrum, sit sapiente magnam repellat ab eaque doloribus facere nobis aspernatur officiis! Perspiciatis ipsum cum repellendus nobis totam.', '', '', '212'),
(10, '2022-01-09 11:01:43', '2022-01-09 11:01:43', 0, 1, 'Animal Rescue System', 2, 'Lorem ipsum dolor sit amet consectetur adipisicing elit. Minima sequi quos debitis in aliquam, dignissimos perferendis ab iure molestiae libero incidunt possimus ratione, inventore iste explicabo pariatur provident laborum suscipit voluptate accusamus? Nostrum, sit sapiente magnam repellat ab eaque doloribus facere nobis aspernatur officiis! Perspiciatis ipsum cum repellendus nobis totam.', '', '', '212'),
(11, '2022-01-09 11:05:58', '2022-01-09 11:05:58', 0, 1, 'UIU_NINJAS', 1, 'Lorem ipsum dolor sit amet consectetur adipisicing elit. Minima sequi quos debitis in aliquam, dignissimos perferendis ab iure molestiae libero incidunt possimus ratione, inventore iste explicabo pariatur provident laborum suscipit voluptate accusamus? Nostrum, sit sapiente magnam repellat ab eaque doloribus facere nobis aspernatur officiis! Perspiciatis ipsum cum repellendus nobis totam.', '', '', '212'),
(12, '2022-01-09 11:06:42', '2022-01-09 11:06:42', 0, 1, 'UIU_ONE_LAST_TIME', 1, 'Lorem ipsum dolor sit amet consectetur adipisicing elit. Minima sequi quos debitis in aliquam, dignissimos perferendis ab iure molestiae libero incidunt possimus ratione, inventore iste explicabo pariatur provident laborum suscipit voluptate accusamus? Nostrum, sit sapiente magnam repellat ab eaque doloribus facere nobis aspernatur officiis! Perspiciatis ipsum cum repellendus nobis totam.', '', '', '212'),
(13, '2022-01-09 11:07:27', '2022-01-09 11:07:27', 0, 1, 'UIU_NINJAS_2', 6, 'Lorem ipsum dolor sit amet consectetur adipisicing elit. Minima sequi quos debitis in aliquam, dignissimos perferendis ab iure molestiae libero incidunt possimus ratione, inventore iste explicabo pariatur provident laborum suscipit voluptate accusamus? Nostrum, sit sapiente magnam repellat ab eaque doloribus facere nobis aspernatur officiis! Perspiciatis ipsum cum repellendus nobis totam.', '', '', '211'),
(14, '2022-01-09 11:08:24', '2022-01-09 11:08:24', 0, 1, 'UIU_ONE_LAST_TIME_2', 4, 'Lorem ipsum dolor sit amet consectetur adipisicing elit. Minima sequi quos debitis in aliquam, dignissimos perferendis ab iure molestiae libero incidunt possimus ratione, inventore iste explicabo pariatur provident laborum suscipit voluptate accusamus? Nostrum, sit sapiente magnam repellat ab eaque doloribus facere nobis aspernatur officiis! Perspiciatis ipsum cum repellendus nobis totam.', '', '', '211'),
(15, '2022-01-09 11:08:40', '2022-01-09 11:08:40', 0, 1, 'UIU_V1', 1, 'Lorem ipsum dolor sit amet consectetur adipisicing elit. Minima sequi quos debitis in aliquam, dignissimos perferendis ab iure molestiae libero incidunt possimus ratione, inventore iste explicabo pariatur provident laborum suscipit voluptate accusamus? Nostrum, sit sapiente magnam repellat ab eaque doloribus facere nobis aspernatur officiis! Perspiciatis ipsum cum repellendus nobis totam.', '', '', '211'),
(16, '2022-01-09 11:09:06', '2022-01-09 11:09:06', 0, 1, 'UIU_V3', 7, 'Lorem ipsum dolor sit amet consectetur adipisicing elit. Minima sequi quos debitis in aliquam, dignissimos perferendis ab iure molestiae libero incidunt possimus ratione, inventore iste explicabo pariatur provident laborum suscipit voluptate accusamus? Nostrum, sit sapiente magnam repellat ab eaque doloribus facere nobis aspernatur officiis! Perspiciatis ipsum cum repellendus nobis totam.', '', '', '211'),
(17, '2022-01-09 11:13:05', '2022-01-09 11:13:05', 0, 1, 'UIU_V6', 1, 'Lorem ipsum dolor sit amet consectetur adipisicing elit. Minima sequi quos debitis in aliquam, dignissimos perferendis ab iure molestiae libero incidunt possimus ratione, inventore iste explicabo pariatur provident laborum suscipit voluptate accusamus? Nostrum, sit sapiente magnam repellat ab eaque doloribus facere nobis aspernatur officiis! Perspiciatis ipsum cum repellendus nobis totam.', '', '', '211'),
(18, '2022-01-09 11:13:39', '2022-01-09 11:13:39', 0, 1, 'UIU_V7', 7, 'Lorem ipsum dolor sit amet consectetur adipisicing elit. Minima sequi quos debitis in aliquam, dignissimos perferendis ab iure molestiae libero incidunt possimus ratione, inventore iste explicabo pariatur provident laborum suscipit voluptate accusamus? Nostrum, sit sapiente magnam repellat ab eaque doloribus facere nobis aspernatur officiis! Perspiciatis ipsum cum repellendus nobis totam.', '', '', '211'),
(19, '2022-01-09 11:16:37', '2022-01-09 11:16:37', 0, 0, 'uiu_ninja10', 4, 'Lorem ipsum dolor sit amet consectetur adipisicing elit. Minima sequi quos debitis in aliquam, dignissimos perferendis ab iure molestiae libero incidunt possimus ratione, inventore iste explicabo pariatur provident laborum suscipit voluptate accusamus? Nostrum, sit sapiente magnam repellat ab eaque doloribus facere nobis aspernatur officiis! Perspiciatis ipsum cum repellendus nobis totam.', '', '', '213'),
(20, '2022-01-09 11:16:44', '2022-01-09 11:16:44', 0, 1, 'uiu_ninja12', 4, 'Lorem ipsum dolor sit amet consectetur adipisicing elit. Minima sequi quos debitis in aliquam, dignissimos perferendis ab iure molestiae libero incidunt possimus ratione, inventore iste explicabo pariatur provident laborum suscipit voluptate accusamus? Nostrum, sit sapiente magnam repellat ab eaque doloribus facere nobis aspernatur officiis! Perspiciatis ipsum cum repellendus nobis totam.', '', '', '212');

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

--
-- Dumping data for table `project_members`
--

INSERT INTO `project_members` (`id`, `time_created`, `time_updated`, `trash`, `status`, `project_id`, `student_id`) VALUES
(1, '2021-12-05 20:27:24', '2021-12-05 20:27:24', 0, 0, 1, '011181290'),
(2, '2021-12-05 20:27:24', '2021-12-05 20:27:24', 0, 0, 1, '011181076'),
(3, '2021-12-05 20:27:24', '2021-12-05 20:27:24', 0, 0, 1, '011181144'),
(4, '2021-12-05 20:27:58', '2021-12-05 20:27:58', 0, 0, 2, '011181290'),
(5, '2021-12-05 20:27:58', '2021-12-05 20:27:58', 0, 0, 2, '011181076'),
(6, '2021-12-07 22:57:13', '2021-12-07 22:57:13', 0, 0, 3, '011181076'),
(7, '2021-12-07 22:57:13', '2021-12-07 22:57:13', 0, 0, 3, '011181062'),
(8, '2021-12-07 23:02:53', '2021-12-07 23:02:53', 0, 0, 4, '011181076'),
(9, '2021-12-07 23:02:53', '2021-12-07 23:02:53', 0, 0, 4, '011181290'),
(10, '2021-12-07 23:02:53', '2021-12-07 23:02:53', 0, 0, 4, '011181123'),
(11, '2022-01-07 11:54:39', '2022-01-07 11:54:39', 0, 0, 5, '011181076'),
(12, '2022-01-07 11:54:39', '2022-01-07 11:54:39', 0, 0, 5, '011181254'),
(15, '2022-01-07 16:53:52', '2022-01-07 16:53:52', 0, 0, 8, '011181076'),
(16, '2022-01-07 16:53:52', '2022-01-07 16:53:52', 0, 0, 8, '011181123'),
(17, '2022-01-07 17:04:26', '2022-01-07 17:04:26', 0, 0, 9, '011181076'),
(18, '2022-01-07 17:04:26', '2022-01-07 17:04:26', 0, 0, 9, '011181123'),
(19, '2022-01-09 11:01:43', '2022-01-09 11:01:43', 0, 0, 10, '011181123'),
(20, '2022-01-09 11:01:44', '2022-01-09 11:01:44', 0, 0, 10, '011181076'),
(22, '2022-01-09 11:05:58', '2022-01-09 11:05:58', 0, 0, 11, '011181076'),
(23, '2022-01-09 11:05:58', '2022-01-09 11:05:58', 0, 0, 11, '011181254'),
(24, '2022-01-09 11:06:42', '2022-01-09 11:06:42', 0, 0, 12, '011181123'),
(25, '2022-01-09 11:07:27', '2022-01-09 11:07:27', 0, 0, 13, '011181123'),
(26, '2022-01-09 11:08:24', '2022-01-09 11:08:24', 0, 0, 14, '011181076'),
(27, '2022-01-09 11:08:40', '2022-01-09 11:08:40', 0, 0, 15, '011181123'),
(28, '2022-01-09 11:09:06', '2022-01-09 11:09:06', 0, 0, 16, '011181123'),
(29, '2022-01-09 11:09:06', '2022-01-09 11:09:06', 0, 0, 16, '011181254'),
(30, '2022-01-09 11:13:06', '2022-01-09 11:13:06', 0, 0, 17, '011181076'),
(31, '2022-01-09 11:13:06', '2022-01-09 11:13:06', 0, 0, 17, '011181123'),
(32, '2022-01-09 11:13:39', '2022-01-09 11:13:39', 0, 0, 18, '011181254'),
(33, '2022-01-09 11:13:39', '2022-01-09 11:13:39', 0, 0, 18, '011181290'),
(35, '2022-01-09 11:16:44', '2022-01-09 11:16:44', 0, 0, 19, '011181076'),
(37, '2022-01-09 13:54:39', '2022-01-09 13:54:39', 0, 0, 20, '011181123');

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

--
-- Dumping data for table `project_videos`
--

INSERT INTO `project_videos` (`id`, `time_created`, `time_updated`, `trash`, `status`, `project_id`, `path`) VALUES
(1, '2021-12-06 11:49:34', '2021-12-06 11:49:34', 0, 0, 1, 'video/app_general/1_demo_video0.mp4'),
(2, '2021-12-06 12:52:29', '2021-12-06 12:52:29', 0, 0, 1, 'video/app_general/1_demo_video0.mp4'),
(3, '2022-01-18 11:08:21', '2022-01-18 11:08:21', 0, 0, 1, 'project_videos-3-path.mp4');

-- --------------------------------------------------------

--
-- Table structure for table `recruits`
--

CREATE TABLE `recruits` (
  `id` int(255) NOT NULL,
  `time_created` datetime NOT NULL DEFAULT current_timestamp(),
  `time_updated` datetime NOT NULL DEFAULT current_timestamp(),
  `trash` tinyint(1) NOT NULL DEFAULT 0,
  `status` tinyint(1) NOT NULL DEFAULT 0,
  `student_id` varchar(255) NOT NULL,
  `club_id` varchar(255) NOT NULL
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

--
-- Dumping data for table `sections`
--

INSERT INTO `sections` (`id`, `time_created`, `time_updated`, `trash`, `status`, `name`, `course_code`, `course_name`, `teacher_id`, `trimester`) VALUES
(1, '2021-12-05 12:30:40', '2021-12-05 12:30:40', 0, 1, 'A', 'EEE_2123', 'Electronics', 'SS', '213'),
(2, '2021-12-05 12:32:40', '2021-12-05 12:32:40', 0, 1, 'A', 'CSE_3421', 'Software Engineering', 'SS', '213'),
(3, '2021-12-05 12:32:47', '2021-12-05 12:32:47', 0, 1, 'B', 'CSE_3421', 'Software Engineering', 'SS', '213'),
(4, '2021-12-05 12:32:54', '2021-12-05 12:32:54', 0, 1, 'C', 'CSE_3421', 'Software Engineering', 'SS', '213'),
(5, '2021-12-05 12:36:36', '2021-12-05 12:36:36', 0, 0, 'A', 'CSE_1115', 'Object Oriented Programming', 'SS', '213'),
(6, '2021-12-05 12:36:40', '2021-12-05 12:36:40', 0, 0, 'B', 'CSE_1115', 'Object Oriented Programming', 'SS', '213'),
(7, '2021-12-05 12:36:46', '2021-12-05 12:36:46', 0, 0, 'C', 'CSE_1115', 'Object Oriented Programming', 'SS', '213');

-- --------------------------------------------------------

--
-- Table structure for table `session_cache`
--

CREATE TABLE `session_cache` (
  `cache_key` varchar(255) NOT NULL,
  `value` longtext NOT NULL,
  `expires` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `session_cache`
--

INSERT INTO `session_cache` (`cache_key`, `value`, `expires`) VALUES
(':1:django.contrib.sessions.cache97zksmlj2pnxvxi4lzyohddseo5qglhn', 'gAWVHgAAAAAAAAB9lIwEdXNlcpR9lIwMbG9naW5fc3RhdHVzlIlzcy4=', '2022-01-31 17:15:16.000000'),
(':1:django.contrib.sessions.cacheabllvw2kjsauly4hk5mdizivt5yicotw', 'gAWVWwAAAAAAAAB9lCiMBHVzZXKUfZQojAxsb2dpbl9zdGF0dXOUiIwCaWSUjAkwMTExODEyOTCUjAZkb21haW6UjAdzdHVkZW50lHWMD19zZXNzaW9uX2V4cGlyeZRKgFEBAHUu', '2022-01-19 03:31:34.000000'),
(':1:django.contrib.sessions.cachee8a6d0m3csbaxe5zb49xtxysu0q2tq67', 'gAWVHgAAAAAAAAB9lIwEdXNlcpR9lIwMbG9naW5fc3RhdHVzlIlzcy4=', '2022-01-31 17:14:49.000000'),
(':1:django.contrib.sessions.cacheesg7ovgxxjmndjftzb741vof92udybxa', 'gAWVHgAAAAAAAAB9lIwEdXNlcpR9lIwMbG9naW5fc3RhdHVzlIlzcy4=', '2022-01-31 17:19:28.000000'),
(':1:django.contrib.sessions.cachegmoxy21oh0ok140y71ag35ian1cc3xif', 'gAWVNgAAAAAAAAB9lCiMD19zZXNzaW9uX2V4cGlyeZRKgFEBAIwEdXNlcpR9lIwMbG9naW5fc3RhdHVzlIlzdS4=', '2022-01-18 12:50:25.000000'),
(':1:django.contrib.sessions.cachepf3ln8i32z0na9mvy6zqcplobe86kqaj', 'gAWVNgAAAAAAAAB9lCiMD19zZXNzaW9uX2V4cGlyeZRKgFEBAIwEdXNlcpR9lIwMbG9naW5fc3RhdHVzlIlzdS4=', '2022-01-19 05:10:56.000000'),
(':1:django.contrib.sessions.cacheqxbntymvj2vresn607o7py83nysnudnc', 'gAWVDQAAAAAAAAB9lIwEdXNlcpR9lHMu', '2022-01-31 10:26:58.000000');

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
  `password_hash` varchar(256) NOT NULL,
  `phone_number` varchar(255) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `students`
--

INSERT INTO `students` (`id`, `time_created`, `time_updated`, `trash`, `status`, `student_id`, `name`, `uiu_email`, `dob`, `department`, `photo`, `password_hash`, `phone_number`) VALUES
(1, '2021-12-05 12:25:36', '2021-12-05 12:25:36', 0, 1, '011181076', 'Md. Tarek Hasan', 'mhasan181076@bscse.uiu.ac.bd', '1999-02-25', 'CSE', 'null', '5e884898da28047151d0e56f8dc6292773603d0d6aabbdd62a11ef721d1542d8', '01772888601'),
(2, '2021-12-05 12:27:01', '2021-12-05 12:27:01', 0, 1, '011181290', 'H. M. Mutasim Billah', 'hbillah181290@bscse.uiu.ac.bd', '2022-01-16', 'CSE', 'n', '5e884898da28047151d0e56f8dc6292773603d0d6aabbdd62a11ef721d1542d8', '01772666901'),
(3, '2021-12-05 12:27:55', '2021-12-05 12:27:55', 0, 1, '011181062', 'Mohammad Nazmush Shamael', 'mshamael181062@bscse.uiu.ac.bd', '2021-12-01', 'CSE', 'n', '5e884898da28047151d0e56f8dc6292773603d0d6aabbdd62a11ef721d1542d8', '01662555890'),
(4, '2021-12-05 12:28:45', '2021-12-05 12:28:45', 0, 1, '011181123', 'Sumayra Islam', 'sislam181123@bscse.uiu.ac.bd', '1999-12-21', 'CSE', 'n', '5e884898da28047151d0e56f8dc6292773603d0d6aabbdd62a11ef721d1542d8', '0166255556'),
(5, '2021-12-05 12:38:08', '2021-12-05 12:38:08', 0, 1, '011181254', 'Arifa Akter', 'aakter181254@bscse.uiu.ac.bd', '1999-08-25', 'CSE', 'n', '5e884898da28047151d0e56f8dc6292773603d0d6aabbdd62a11ef721d1542d8', '01772999623'),
(7, '2021-12-05 12:39:56', '2021-12-05 12:39:56', 0, 1, '011181144', 'Al Emran', 'mhossain181144@bscse.uiu.ac.bd', '1999-08-25', 'CSE', 'n', '5e884898da28047151d0e56f8dc6292773603d0d6aabbdd62a11ef721d1542d8', '01772999624');

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
  `password_hash` varchar(255) NOT NULL,
  `phone_number` varchar(255) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `teachers`
--

INSERT INTO `teachers` (`id`, `time_created`, `time_updated`, `trash`, `status`, `name`, `employee_id`, `uiu_email`, `dob`, `department`, `photo`, `password_hash`, `phone_number`) VALUES
(1, '2021-12-05 12:20:39', '2021-12-05 12:20:39', 0, 1, 'Md. Abir Hassan', 'MdAbH', 'ahassan@cse.uiu.ac.bd', '2022-01-23', 'CSE', 'n', '5e884898da28047151d0e56f8dc6292773603d0d6aabbdd62a11ef721d1542d8', '01738038712'),
(2, '2021-12-05 12:22:20', '2021-12-05 12:22:20', 0, 1, 'Md. Saidul Hoque Anik', 'SHqA', 'anik@cse.uiu.ac.bd', '2022-01-23', 'CSE', 'n', '5e884898da28047151d0e56f8dc6292773603d0d6aabbdd62a11ef721d1542d8', '01713130549'),
(3, '2021-12-05 12:23:54', '2021-12-05 12:23:54', 0, 1, 'Dr. Swakkhar Shatabda', 'SS', 'swakkhar@cse.uiu.ac.bd', '2022-01-30', 'CSE', 'n', '5e884898da28047151d0e56f8dc6292773603d0d6aabbdd62a11ef721d1542d8', '01552327508');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `booths`
--
ALTER TABLE `booths`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `club_id` (`club_id`);

--
-- Indexes for table `cff_comments`
--
ALTER TABLE `cff_comments`
  ADD PRIMARY KEY (`id`),
  ADD KEY `cff_comments_club_id` (`club_id`);

--
-- Indexes for table `cff_registrations`
--
ALTER TABLE `cff_registrations`
  ADD PRIMARY KEY (`id`),
  ADD KEY `cff_registrations_student_id` (`student_id`),
  ADD KEY `cff_registrations_club_id` (`club_id`);

--
-- Indexes for table `clubs`
--
ALTER TABLE `clubs`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `email` (`email`),
  ADD UNIQUE KEY `club_id` (`club_id`);

--
-- Indexes for table `comments`
--
ALTER TABLE `comments`
  ADD PRIMARY KEY (`id`),
  ADD KEY `project_id_c` (`project_id`);

--
-- Indexes for table `events`
--
ALTER TABLE `events`
  ADD PRIMARY KEY (`id`),
  ADD KEY `events_club_id` (`club_id`);

--
-- Indexes for table `feed_posts`
--
ALTER TABLE `feed_posts`
  ADD PRIMARY KEY (`id`),
  ADD KEY `feed_posts_id` (`club_id`);

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
-- Indexes for table `recruits`
--
ALTER TABLE `recruits`
  ADD PRIMARY KEY (`id`),
  ADD KEY `recruits_id` (`club_id`),
  ADD KEY `recruits_student_id` (`student_id`);

--
-- Indexes for table `sections`
--
ALTER TABLE `sections`
  ADD PRIMARY KEY (`id`),
  ADD KEY `teacher_id` (`teacher_id`);

--
-- Indexes for table `session_cache`
--
ALTER TABLE `session_cache`
  ADD PRIMARY KEY (`cache_key`),
  ADD KEY `session_cache_expires` (`expires`);

--
-- Indexes for table `students`
--
ALTER TABLE `students`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `student_id` (`student_id`),
  ADD UNIQUE KEY `uiu_email` (`uiu_email`),
  ADD UNIQUE KEY `phone_number` (`phone_number`);

--
-- Indexes for table `teachers`
--
ALTER TABLE `teachers`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `employee_id` (`employee_id`),
  ADD UNIQUE KEY `uiu_email` (`uiu_email`),
  ADD UNIQUE KEY `phone_number` (`phone_number`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `booths`
--
ALTER TABLE `booths`
  MODIFY `id` int(255) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `cff_comments`
--
ALTER TABLE `cff_comments`
  MODIFY `id` int(255) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `cff_registrations`
--
ALTER TABLE `cff_registrations`
  MODIFY `id` int(255) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT for table `clubs`
--
ALTER TABLE `clubs`
  MODIFY `id` int(255) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=7;

--
-- AUTO_INCREMENT for table `comments`
--
ALTER TABLE `comments`
  MODIFY `id` int(255) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `events`
--
ALTER TABLE `events`
  MODIFY `id` int(255) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `feed_posts`
--
ALTER TABLE `feed_posts`
  MODIFY `id` int(255) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=26;

--
-- AUTO_INCREMENT for table `prizes`
--
ALTER TABLE `prizes`
  MODIFY `id` int(255) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `projects`
--
ALTER TABLE `projects`
  MODIFY `id` int(255) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=22;

--
-- AUTO_INCREMENT for table `project_members`
--
ALTER TABLE `project_members`
  MODIFY `id` int(255) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=38;

--
-- AUTO_INCREMENT for table `project_videos`
--
ALTER TABLE `project_videos`
  MODIFY `id` int(255) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT for table `recruits`
--
ALTER TABLE `recruits`
  MODIFY `id` int(255) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `sections`
--
ALTER TABLE `sections`
  MODIFY `id` int(255) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=8;

--
-- AUTO_INCREMENT for table `students`
--
ALTER TABLE `students`
  MODIFY `id` int(255) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=8;

--
-- AUTO_INCREMENT for table `teachers`
--
ALTER TABLE `teachers`
  MODIFY `id` int(255) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `booths`
--
ALTER TABLE `booths`
  ADD CONSTRAINT `booths_club_id` FOREIGN KEY (`club_id`) REFERENCES `clubs` (`club_id`);

--
-- Constraints for table `cff_comments`
--
ALTER TABLE `cff_comments`
  ADD CONSTRAINT `cff_comments_club_id` FOREIGN KEY (`club_id`) REFERENCES `clubs` (`club_id`);

--
-- Constraints for table `cff_registrations`
--
ALTER TABLE `cff_registrations`
  ADD CONSTRAINT `cff_registrations_club_id` FOREIGN KEY (`club_id`) REFERENCES `clubs` (`club_id`),
  ADD CONSTRAINT `cff_registrations_student_id` FOREIGN KEY (`student_id`) REFERENCES `students` (`student_id`);

--
-- Constraints for table `comments`
--
ALTER TABLE `comments`
  ADD CONSTRAINT `project_id_c` FOREIGN KEY (`project_id`) REFERENCES `projects` (`id`);

--
-- Constraints for table `events`
--
ALTER TABLE `events`
  ADD CONSTRAINT `events_club_id` FOREIGN KEY (`club_id`) REFERENCES `clubs` (`club_id`);

--
-- Constraints for table `feed_posts`
--
ALTER TABLE `feed_posts`
  ADD CONSTRAINT `feed_posts_id` FOREIGN KEY (`club_id`) REFERENCES `clubs` (`club_id`);

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
-- Constraints for table `recruits`
--
ALTER TABLE `recruits`
  ADD CONSTRAINT `recruits_id` FOREIGN KEY (`club_id`) REFERENCES `clubs` (`club_id`),
  ADD CONSTRAINT `recruits_student_id` FOREIGN KEY (`student_id`) REFERENCES `students` (`student_id`);

--
-- Constraints for table `sections`
--
ALTER TABLE `sections`
  ADD CONSTRAINT `teacher_id` FOREIGN KEY (`teacher_id`) REFERENCES `teachers` (`employee_id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
