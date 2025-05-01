CREATE TABLE empresa(  
    id int NOT NULL PRIMARY KEY AUTO_INCREMENT,
    ruc VARCHAR(20),
    razon_social VARCHAR(255)
);
CREATE TABLE ciudad(  
    id int NOT NULL PRIMARY KEY AUTO_INCREMENT,
    nombre VARCHAR(255) 
);
CREATE TABLE direccion(  
    id int NOT NULL PRIMARY KEY AUTO_INCREMENT,
    direccion VARCHAR(255),
    ciudad_id INT,
    empresa_id INT,
    Foreign Key (ciudad_id) REFERENCES ciudad(id),
    Foreign Key (empresa_id) REFERENCES empresa(id)
);

