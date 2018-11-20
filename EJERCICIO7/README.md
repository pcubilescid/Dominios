Programa que indica las diferencias entre los dominios encontrados mediante hmmscan y los dominios anotados en UniProt. 

El programa toma como parametros el fichero FASTA de secuencias de proteina de uno de los organismos, el fichero comprimido de UniProt SW, el fichero tabular obtenido para ese mismo organismo en la ejecucion del programa creado en el "EJERCICIO6", y un fichero donde grabar los resultados de las diferencias. 

Este ultimo fichero tiene formato tabular: 
La primera columna es el identificador taxonomico del organismo al que pertenece la proteina; la siguiente el identificador de la proteina; la siguiente los identificadores de los dominios que aparecen tanto en UniProt como en la busqueda con HMMer en Pfam, separados por comas (y si no hubiese, un guion); en la siguiente los identificadores de los dominios que solo aparecen en UniProt, separados por comas (y si no hubiese, un guion); y en la ultima los identificadores de los dominios que solo aparecen en la busqueda con HMMer en Pfam, separados por comas (y si no hubiese, un guion).
