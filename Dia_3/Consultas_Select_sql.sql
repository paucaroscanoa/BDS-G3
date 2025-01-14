--SELECT
SELECT*from empleado;
SELECT nombre, pais from empleado;
SELECT*from empleado LIMIT 10;
SELECT*from empleado ORDER BY nombre;
SELECT*from empleado ORDER BY salario DESC;
SELECT*from empleado where pais='Peru';
SELECT*from empleado where salario>5000;
SELECT*from empleado where salario>5000 and pais='Peru';
