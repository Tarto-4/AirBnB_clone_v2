-- Check if the database exists, if not, create it
CREATE DATABASE IF NOT EXISTS `hbnb_test_db`;

-- Check if the user exists, if not, create it
CREATE USER IF NOT EXISTS 'hbnb_test'@'localhost' IDENTIFIED BY 'hbnb_test_pwd';

-- Grant privileges to the user
GRANT ALL PRIVILEGES ON `hbnb_test_db`.* TO 'hbnb_test'@'localhost';
GRANT SELECT ON `performance_schema`.* TO 'hbnb_test'@'localhost';

-- Flush privileges to apply changes immediately
FLUSH PRIVILEGES;
