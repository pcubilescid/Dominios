Realizado y datos descargados 15/11/2018

Serie de programas que ayudan a comprobar, cuantos de los dominios Pfam mas relevantes encontrados en sus proteinas conocidas en UniProt SW coinciden con los dominios anotados.

Los organismos a buscar son el mono ardilla boliviano y el chimpace

Para facilitar la busqueda de estos organimos tenemos la siguiente informacion:

· Chimpanzee (Pan)

https://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?mode=Info&id=9596&lvl=3&p=has_linkout&p=blast_url&p=genome_blast&lin=f&keep=1&srchmode=1&unlock

- Taxonomy ID: 9596 (for references in articles please use NCBI:txid9596) Pan 
- Taxonomy ID: 9597 (for references in articles please use NCBI:txid9597) Pan paniscus
- Taxonomy ID: 9598 (for references in articles please use NCBI:txid9598) Pan troglodytes


· Black-capped squirrel monkey(Saimiri boliviensis)

https://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?mode=Info&id=39432&lvl=3&p=mapview&p=has_linkout&p=blast_url&p=genome_blast&lin=f&keep=1&srchmode=1&unlock

- Taxonomy ID: 39432 (for references in articles please use NCBI:txid39432)


Necesidades para el funcionamiento de los programas: 

· Uniprot

Ficheros comprimidos de Uniprot SwissProt
ftp://ftp.ebi.ac.uk/pub/databases/uniprot/current_release/knowledgebase/taxonomic_divisions/

para realizar estos problemas se ha descargado uniprot_sprot_mammals.dat.gz

· Pfam

Probado con la versión 32 de Pfam (ftp://ftp.ebi.ac.uk/pub/databases/Pfam/releases/Pfam32.0/) para ser usado con hmmscan ( descargar el fichero Pfam-A.hmm.gz ), descomprimido e indexado con hmmpress.

Recomendado crear una carpeta llamada database en la que guardar nuestra base de datos

comandos una vez descargado y descomprimido:

cat Pfam-A.hmm -> (nombre de tu base de datos)
hmmpress (nombre de tu base de datos)

· Python

- Version 3 de python
- librerias especificas, en requirements.txt 





