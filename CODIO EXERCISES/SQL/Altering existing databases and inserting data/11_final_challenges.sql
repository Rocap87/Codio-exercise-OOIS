CREATE DATABASE App;
USE App;
CREATE TABLE settings ( 
    user_id INT(7) NOT NULL,
    email_frequency TINYINT(2) UNSIGNED DEFAULT 15,
    layout VARCHAR(70) DEFAULT ‘vertical’,
    updated_at DATETIME DEFAULT NULL,
    PRIMARY KEY (email_frequency));


INSERT INTO App.settings VALUES (99, DEFAULT, "horizontal", "2015-09-15 04:01:04");

RENAME TABLE settings TO user_settings;
