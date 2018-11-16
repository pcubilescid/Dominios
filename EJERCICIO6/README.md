Programa que toma un fichero FASTA generado con el programa "Proteinas_1Organismo_Fasta.py" situado en la carpeta "Ejercicio5", ejecuta HMMscan, y guarda el resultado del programa y los dominios mas prometedores de cada proteina. 

El programa toma como parametros la base de datos de Pfam a usar, el fichero FASTA con las secuencias de proteinas a buscar, el fichero donde se debe guardar el resultado de ejecutar HMMscan, y el fichero donde se guardaran las correspondencias entre proteina y dominio.
 
Este ultimo fichero tiene  un formato tabular, con las siguientes columnas: 
Accession number de la proteina, identificador del dominio de Pfam, coordenada de inicio del dominio dentro de la secuencia de proteinas, coordenada de fin del dominio dentro de la secuencia de proteinas, y el domain e-value. 

Ejecucion (python3 Ejercicio6.py [database (Pfam)] [input.fa] [output.hmm] [output.txt])
