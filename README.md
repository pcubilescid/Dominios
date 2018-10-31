Serie de programas que ayudan a comprobar, cuantos de los dominios Pfam mas relevantes encontrados en sus proteinas conocidas en UniProt SW coinciden con los dominios anotados.

Los organismos a buscar son el mono ardilla boliviano y el chimpace

Probado con la versión 32 de Pfam (ftp://ftp.ebi.ac.uk/pub/databases/Pfam/releases/Pfam32.0/) para ser usado con hmmscan ( descargar el fichero Pfam-A.hmm.gz ), descomprimido e indexado con hmmpress.

· Chimpanzee (Pan)
https://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?mode=Info&id=9596&lvl=3&p=has_linkout&p=blast_url&p=genome_blast&lin=f&keep=1&srchmode=1&unlock
- Taxonomy ID: 9596 (for references in articles please use NCBI:txid9596) Pan 
- Taxonomy ID: 9597 (for references in articles please use NCBI:txid9597) Pan paniscus
- Taxonomy ID: 9598 (for references in articles please use NCBI:txid9598) Pan troglodytes

· Black-capped squirrel monkey(Saimiri boliviensis)
https://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?mode=Info&id=39432&lvl=3&p=mapview&p=has_linkout&p=blast_url&p=genome_blast&lin=f&keep=1&srchmode=1&unlock
- Taxonomy ID: 39432 (for references in articles please use NCBI:txid39432)

Ficheros comprimidos de Uniprot SwissProt
ftp://ftp.ebi.ac.uk/pub/databases/uniprot/current_release/knowledgebase/taxonomic_divisions/

IDtax_Nombre_NumPro.py --> 
Programa que toma como parametros un fichero comprimido de UniProt, y un fichero de salida. El fichero de salida debera estar en formato tabular, siendo las columnas el identificador taxonomico, el nombre del organismo, y el numero de proteinas para ese organismo que habia en el fichero comprimido. Con este programa podreis saber, inspeccionando su salida, si los ficheros descargados contienen secuencias de los organismos

Ejecucion (python3 IDtax_Nombre_NumPro.py [fichero_entrada.gz] [fichero_salida.txt])

Proteinas_Nombre_NumPro.py -->
Programa que permite grabar todas las secuencias de proteínas de un organismo en concreto en un fichero FASTA. El programa toma como parámetros el identificador taxonómico de ese organismo, el fichero comprimido Uniprot, y un fichero de salida. La cabecera FASTA de cada secuencia de proteínas tiene, separado por puntos y comas, el accession number principal de la entrada, el identificador único de la entrada, el identificador taxonómico del organismo, y la descripción larga recomendada.

Ejecucion (python3 Proteinas_Nombre_NumPro.py [id_taxonomico(que quieres buscar)] [fichero_entrada.gz] [fichero_salida.txt])
