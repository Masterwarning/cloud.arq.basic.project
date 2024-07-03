CREATE TABLE User(
	id BIGINT UNSIGNED NOT NULL,
	name VARCHAR(128) NOT NULL,
	lastname VARCHAR(128) NOT NULL,
	email VARCHAR(128) NOT NULL,
	telephone BIGINT UNSIGNED NOT NULL,
	birthday DATE NOT NULL,
	gender ENUM('Femenino','Masculino','Omitido') NOT NULL,
	address VARCHAR(128),
		PRIMARY KEY(id),
		INDEX USING BTREE(email)	
)ENGINE InnoDB;