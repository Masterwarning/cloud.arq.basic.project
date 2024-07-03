CREATE TABLE Animal(
	id INT UNSIGNED NOT NULL AUTO_INCREMENT,
    user_id BIGINT UNSIGNED NOT NULL,
    name VARCHAR(128) NOT NULL,
    color VARCHAR(128) NOT NULL,
    birthday DATE NOT NULL,
    type ENUM('Gato', 'Perro', 'Ave', 'Roedor', 'Pez', 'Exotico', 'Otro') NOT NULL,
	size ENUM('Pequeño', 'Mediano', 'Grande') NOT NULL,
    weight INT NOT NULL,
    		PRIMARY KEY(id),
                CONSTRAINT FOREIGN KEY(user_id) REFERENCES User(id)
				ON DELETE CASCADE ON UPDATE CASCADE
)ENGINE InnoDB;