-- Check if the database exists, if not, create it
CREATE DATABASE IF NOT EXISTS `hbnb_dev_db`;

-- Check if the user exists, if not, create it
CREATE USER IF NOT EXISTS 'hbnb_dev'@'localhost' IDENTIFIED BY 'hbnb_dev_pwd';

-- Grant privileges to the user
GRANT ALL PRIVILEGES ON `hbnb_dev_db`.* TO 'hbnb_dev'@'localhost';
GRANT SELECT ON `performance_schema`.* TO 'hbnb_dev'@'localhost';

-- Flush privileges to apply changes immediately
FLUSH PRIVILEGES;
