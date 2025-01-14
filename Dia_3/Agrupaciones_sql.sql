-- FUNCIONES DE AGRUPACIÓN
--1. CONTAR
SELECT COUNT(*) FROM empleado;
SELECT COUNT(*) FROM empleado WHERE salario>5000;

--2. MAXIMO, MINIMO, PROMERIO
SELECT MAX(salario),MIN(salario),avg(salario) from empleado;

Select DISTINCT pais from empleado;

SELECT pais,COUNT(*) from empleado
GROUP BY pais
ORDER BY count(*) DESC;

--3. CREAR UNA CONSULTA QUE RETORNE EL SALARIO MAXIMO MINIMO Y PROMEDIO POR PAIS
--salario maximo minimo y promedio por pais
SELECT pais,MAX(salario),MIN(salario),avg(salario) from empleado
GROUP BY pais
ORDER BY count(*) DESC;

--Salario promedio por pais
SELECT pais,avg(salario) from empleado
GROUP BY pais
having avg(salario) > 4000;

-- 3. Subconsultas
SELECT avg(salario) from empleado;
select*from empleado
where salario>(select avg(salario) from empleado);

select pais,count(*),(select avg(salario) from empleado) as salario_promedio from empleado
where salario>(select avg(salario) from empleado)
GROUP BY pais ORDER BY count(*) DESC;