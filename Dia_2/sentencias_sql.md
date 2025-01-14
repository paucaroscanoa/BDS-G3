## División de SQL en sublenguajes
```Lenguaje de Consulta de Datos (DQL) - El Lenguaje de Consulta de Datos es el sublenguaje responsable de leer, o consultar, datos de una base de datos. En SQL, corresponde al SELECT

Lenguaje deManipulación de Datos (DML ) - El Lenguaje de Manipulación de Datos es el sublenguaje responsable de añadir, editar o borrar datos de una base de datos. En SQL, corresponde a los lenguajes INSERT, UPDATE, y DELETE

Lenguaje de Definición de Datos (DDL ) - El Lenguaje de Definición de Datos es el sublenguaje responsable de definir la forma en que se estructuran los datos en una base de datos. En SQL, esto corresponde a la manipulación de tablas a través de CREATE TABLE, ALTER TABLE, y DROP TABLE

Lenguaje de Control de Datos (DCL) - El Lenguaje de Control de Datos es el sublenguaje responsable de las tareas administrativas de control de la propia base de datos, especialmente la concesión y revocación de permisos de base de datos para los usuarios. En SQL, esto corresponde a los comandos GRANT, REVOKE, y DENY, entre otros.
```
## CREAR UNA TABLA
```
CREATE TABLE alumno(  
    id int NOT NULL PRIMARY KEY AUTO_INCREMENT,
    nro_documento VARCHAR(255) NOT NULL,
    nombre VARCHAR(255) NOT NULL,
    email VARCHAR(100)
);
----MODFICAR UNA TABLA----
ALTER TABLE alumno
ADD COLUMN nota INT DEFAULT 0;

----ELIMINAR UNA TABLA------
DROP TABLE alumno;
```
## SENTENCIAAS DM
```
--INSERTAR DATOS (INSERT)
insert into alumno(nro_documento,nombre)value('100','mario');

--INSERTAR VARIOS VALORES (SÓLO EN MYSQL)
insert into alumno(nro_documento, nombre, nota)
VALUES
('200','ana',15),
('300','juan',13),
('400','pedro',18),
('500','felipe',10),
('600','jorge',5);

--ACTUALIZAR DATOS (UPDATE)
UPDATE alumno SET email='CODIGO@GMAIL.COM';

--ACTUALIZAR CON WHERE
UPDATE alumno set email='cesar@gmial.com' WHERE id=1;

--ACTUALIZAR CON FUNCIONES
UPDATE alumno SET email=CONCAT(nombre,'@gmail.com') WHERE id!=1;

--ELIMINAR  DATOS (DELETE)
DELETE FROM alumno WHERE id >5;

--INSERTAR DATOS (INSERT)
insert into alumno(nro_documento,nombre)value('800','Juan');
UPDATE alumno SET email=CONCAT(nombre,'@gmail.com') WHERE id!=1;

--SELECCIONAR (SELECT)--
SELECT*FROM alumno;
SELECT nombre,nota from alumno;
SELECT nombre,email,nota  from alumno WHERE nota>15;
```