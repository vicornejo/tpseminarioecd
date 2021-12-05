# TP Seminario - Indicaciones para generar la tabla en postgres

En una terminal corro los siguientes comandos:
1. Iniciar postgres con el comando:  ./control-env.sh psql
2. Luego, creo la tabla de viajes con sus campos con el siguiente script de SQL:
CREATE TABLE viajes (
 mes int,
 anio int,
 locacion varchar(12) not null,
 viajesdiarios int not null,
 sentido varchar(10),
 long decimal(9,6),
 lat decimal(9,6)
 );

3. Genero los datos para la tabla con un codigo SQL similar al siguiente. La query completa esta en un archivo .txt en la carpeta de dataset -> [queriesDataTabla.txt]. 

INSERT INTO viajes (mes, anio, locacion, viajesdiarios, sentido, long, lat) VALUES(3,2020, '48Q3CJ00+' ,729, 'Interna' ,-58.381519 , -34.588796);


4. Verifico en la terminal que se hayan cargado bien los datos con la siguiente query:

select * from viajes limit 15;

La salida se puede ver en la carpeta imagenesVC -> Postgres -> ["1. SQL- chequeo que se cargaron bien los datos"]

5. Trabajo con algunas queries para analizar los datos:

## cuantos registros tiene la tabla viajes? Como resultado, indica que hay  150514 registros (imagen 2)

select count(viajesdiarios) from viajes;

## Comparar abril 2020 y abril 2021. Se observa que baja la cantidad de viajes en el 2020 debido a la pandemia, y principalmente hay una baja de viajes dentro de CABA (imagen 2)
select anio, sum(viajesdiarios) as cantviajes, sentido from viajes where mes = 4 group by anio, sentido order by anio;

## mes y anio con menor cantidad de viajes?
select sum(viajesdiarios) as cantviajes, anio, mes from viajes group by anio, mes order by cantviajes asc limit 1;

Respuesta:
cantviajes | anio | mes 
------------+------+-----
    9129261 | 2020 |   4
(1 row)

## mes y anio con menor cantidad de viajes internos en caba?
select sum(viajesdiarios) as cantviajes, anio, mes from viajes where sentido = 'Interna' group by anio, mes order by cantviajes asc limit 1;

Respuesta:
 cantviajes | anio | mes 
------------+------+-----
    1280120 | 2021 |   8
(1 row)