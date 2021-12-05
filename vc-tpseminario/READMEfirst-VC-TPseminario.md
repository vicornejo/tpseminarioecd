# Workshop de Big Data
Tomo de referencia el repositorio inicial para el TP final, por lo tanto para levantar el ambiente debe seguirse los mismos pasos que en clase y puede encontrarse el repositorio base de clase aqui:
[disponible en Github](https://github.com/MuttData/bigdata-workshop-es)

Voy a tomar los datos que voy a utilizar para mi proyecto de ECD2020

Consiste en hacer un analisis de los recorridos de medios de transporte durante
pandemia y luego de la misma.

Para esto, trabajo con Datasets del gobierno de la ciudad:

[Viaje en transporte publico] : URL disponible [https://data.buenosaires.gob.ar/dataset/sube/resource/b88f4c3d-325d-4397-93ff-c54657357092]
[Flujo vehicular] : URL disponible [https://data.buenosaires.gob.ar/dataset/flujo-vehicular-anillo-digital/resource/1df1e3f1-ab85-47b5-becc-39054d6761ee]

Trabajo de los datos para el TP:
 # Jupyter y Spark
 Trabaje con el primer dataset, reacomodando los datos ya que por ejemplo la fecha era un solo campo string con multiples datos y tuve que trabajarlo para separarlo en dia, mes, año. Para esto trabaje con sqlspark y tambien con pandas. Luego, realice algunos calculos para poder entender que cantidad de viajes se habian realizado entre 2020 y 2021 abierto por medios de transporte publico (tren, colectivo y subte). Por ultimo, trabaje con herramientas de visualizacion para poder graficar y terminar de comprender los datos. 
 Este script se puede encontrar en jupyter / notebook -> ["pyspark-vc.ipynb"]

 # Postgres y Superset
 Tuve algunas dificultades en alimentar las tablas a partir de otro script. Por lo tanto, para poder avanzar lo que hice fue crear una tabla desde una terminal, pero alimentarla de forma manual en funcion de los datos del dataset "dataset_flujo_vehicular.csv". Si bien no es lo ideal, me permitio poder entender como puede ejecutarse postgres desde una terminal de bash, y ademas luego esta misma tabla me permitio avanzar con la practica en superset. 
 Para poder generar la tabla y los datos, deje un instructivo para poder copiar y pegar las queries en otro archivo de lectura ["README-VC-TPseminario-SQL.md"]
 Una vez generada la tabla con los datos, accedi a superset desde localhost como en clase. Aqui me conecte al databes del workshop -> dataset la tabla creada "viajes". El paso a paso en imagenes lo deje en la carpeta ["VC-enimagenes"]
 
 # Batch
 Intente (aunque sin mucho exito) crear un generador de viajes diarios, en el archivo ["fakeVC_info_generator.py"] dentro del directorio: code -> python / us-stock-analysis -> src -> stream, tomando como semilla los valores promedio diarios de los meses agosto,septiembre y octubre de 2021. Tome como que a las 20 del dia se terminaba el conteo y comienza nuevamente a las 9am, principalmente para poder utilizar mayor cantidad de variaciones de codigo aplicado. No me permite integrarlo al worker1 de kafka. 
 Para ejecutarlo y generar los datos deberia introducir el comando:
 -  python src/stream/fakeVC_info_generator.py kafka:9092 viajes 2021-11-01T09:00:00Z

