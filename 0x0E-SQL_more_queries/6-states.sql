-- This script creates a database "hbtn_0d_usa" and table "states"
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
CREATE TABLE IF NOT EXISTS hbtn_0d_usa.states(
	id INT NOT UNIQUE AUTO_INCREMENT NOT NULL PRIMARY KEY,
	name VARCHAR(256) NOT NULL
);
