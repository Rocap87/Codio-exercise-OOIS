CREATE DATABASE famous_scientists;
USE famous_scientists;
CREATE TABLE scientists ( 
id INT(1) NOT NULL auto_increment, 
name VARCHAR(255) NOT NULL, 
discovery TEXT NOT NULL,
year_of_birth INT(4) NOT NULL,
year_of_death INT(4) DEFAULT NULL,  
PRIMARY KEY (id) 
) AUTO_INCREMENT=1;

USE famous_scientists;
INSERT INTO scientists (name, discovery, year_of_birth, year_of_death) VALUES ("Galileo Galilei", "Modern observational astronomy", 1564, 1642);
