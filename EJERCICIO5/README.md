Programa que permite grabar todas las secuencias de proteinas de un organismo en concreto en un fichero FASTA. 

El programa toma como parametros el identificador taxonomico de ese organismo, el fichero comprimido Uniprot, y un fichero de salida. 

La cabecera FASTA de cada secuencia de proteinas tiene, separado por puntos y comas los siguientes datos:
El accession number principal de la entrada, el identificador unico de la entrada, el identificador taxonomico del organismo, y la descripcion larga recomendada.

Ejecucion (python3 Proteinas_Nombre_NumPro.py [id_taxonomico(que quieres buscar)] [fichero_entrada.gz] [fichero_salida.txt])
